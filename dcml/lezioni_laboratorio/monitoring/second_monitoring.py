import csv
from datetime import datetime
from time import sleep
import psutil
import time

# Library for getting indicators -> https://psutil.readthedocs.io/en/latest/
import pyshark as pyshark


def current_milli_time():
    """
    This function returns the current time in milliseconds
    :return:
    """
    return round(time.time() * 1000)


def read_data():
    """
    This function reads data from the system
    :return: a dictionary
    """
    data_dict = {
        "time": current_milli_time(),
        "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    cpu_probe(data_dict)
    vm_probe(data_dict)
    return data_dict


def cpu_probe(data_dict):
    """
    This function reads CPU data from the system and uses it to update a dict
    """
    cpu_t = psutil.cpu_times()
    data_dict["idle_time"] = cpu_t.idle
    data_dict["usr_time"] = cpu_t.user
    data_dict["interrupt_time"] = cpu_t.irq


def vm_probe(data_dict):
    """
    This function reads VM data from the system and uses it to update a dict
    """
    vm_data = psutil.virtual_memory()
    data_dict["mem_total"] = vm_data.total
    data_dict["mem_available"] = vm_data.available
    data_dict["mem_percent"] = vm_data.percent


def pyshark_parse(data_dict, pk_capture):
    """
    This function parses PyShark data into the existing dict. For the moment it gets only 3 indicators
    Note: for PyShark to work you have to install wireshark+tshark in your system.
    """
    n_packets = 0
    is_tcp = 0
    byte_size = 0
    for packet in pk_capture._packets:
        n_packets += 1
        byte_size += int(packet.captured_length)
        is_tcp += 1 if packet.transport_layer == "TCP" else 0
    data_dict["n_packets"] = n_packets
    data_dict["tcp_packets"] = is_tcp
    data_dict["packet_size"] = byte_size


def write_dict_to_csv(filename, dict_item, is_first_time):
    """
    This function writes a dictionary as a row of a CSV file
    :param filename:
    :param dict_item:
    :param is_first_time:
    :return:
    """
    if is_first_time:
        f = open(filename, "w", newline="")
    else:
        f = open(filename, "a", newline="")
    w = csv.DictWriter(f, dict_item.keys())
    if is_first_time:
        w.writeheader()
    w.writerow(dict_item)
    f.close()


if __name__ == "__main__":
    """
    Main of the monitor
    """
    is_first_time = True
    while True:
        # Monitors PSUtil data
        monit_data = read_data()
        # Monitor with PyShark for the remaining loop time (replaces sleep)
        capture = pyshark.LiveCapture(interface="wlan0")
        capture.sniff(timeout=1)
        capture.close()
        # Add PyShark data to dict
        pyshark_parse(monit_data, capture)
        print(monit_data)
        write_dict_to_csv("my_first_dataset.csv", monit_data, is_first_time)
        is_first_time = False
