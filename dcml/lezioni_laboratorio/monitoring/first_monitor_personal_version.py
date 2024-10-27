from time import sleep
import psutil as pst
import csv


def read_cpu_usage():
    cpu_t = pst.cpu_times()
    cpu_dict = {"idle_time": cpu_t.idle, "usr_time": cpu_t.user}
    cpu_dict["interrupt_time"] = cpu_t.irq
    return cpu_dict


def read_disks():
    disk = pst.disk_usage("/")
    disk_dict = {
        "total": disk.total,
        "used": disk.used,
        "free": disk.free,
    }
    return disk_dict


# Function to return info on the disk in gigabytes
def read_disks_gb():
    disk = pst.disk_usage("/")
    disk_dict = {
        "total": disk.total / (2**30),
        "used": disk.used / (2**30),
        "free": disk.free / (2**30),
    }
    return disk_dict


def read_memory_gb():
    mem = pst.virtual_memory()
    mem_dict = {
        "total": mem.total / (2**30),
        "available": mem.available / (2**30),
        "used": mem.used / (2**30),
        "free": mem.free / (2**30),
    }
    return mem_dict


def write_dict_to_csv(filename, dict, first_time=False):
    if first_time:
        f = open(filename, "w")
    else:
        f = open(filename, "a")
    w = csv.DictWriter(f, dict.keys())
    if first_time:
        w.writeheader()
    w.writerow(dict)
    f.close()


if __name__ == "__main__":
    first_time = True

    while True:
        # print("User time:" + str(u_t))
        # print(f"Idle time: {i_t}")
        # print("cpu_times are: %s", cpu_t)
        write_dict_to_csv("cpu_usage.csv", read_cpu_usage(), first_time)
        write_dict_to_csv("disk_usage.csv", read_disks_gb(), first_time)
        write_dict_to_csv("memory_usage.csv", read_memory_gb(), first_time)
        first_time = False
        sleep(1)
