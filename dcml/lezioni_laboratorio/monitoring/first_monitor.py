from time import sleep
import psutil as pst
import csv


def read_cpu_usage():
    cpu_t = pst.cpu_times()
    usr_sp_cputime = cpu_t[0]
    idle_time = cpu_t.idle
    cpu_dict = {"idle_time": cpu_t.idle, "usr_time": cpu_t.user}
    cpu_dict["interrupt_time"] = cpu_t.irq
    return cpu_dict


def write_dict_to_csv(filename, dict, first_time=False):
    if first_time:
        f = open(filename, "w")
    f = open(filename, "a")
    w = csv.DictWriter(f, dict.keys())
    if first_time:
        w.writeheader()
    w.writerow(dict)
    f.close()


if __name__ == "__main__":
    first_time = True

    while True:
        cpu_t = read_cpu_usage()
        # print("User time:" + str(u_t))
        # print(f"Idle time: {i_t}")
        # print("cpu_times are: %s", cpu_t)
        write_dict_to_csv("cpu_usage.csv", cpu_t, first_time)
        first_time = False
        sleep(1)
