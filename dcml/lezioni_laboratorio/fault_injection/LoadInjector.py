import multiprocessing
import os.path
import random
import subprocess
import tempfile
import threading
import time
from multiprocessing import Pool, cpu_count
from urllib.request import urlopen

# SUPPORT METHODS


def current_ms():
    """
    Reports the current time in milliseconds
    :return: long int
    """
    return round(time.time() * 1000)


def url_reader(sites_urls: list, url_index: int = 0, duration_ms: int = 1000):
    """
    Function to continuously read data from remote urls
    :param duration_ms: duration of the task in ms
    :param sites_urls: list of trings representing URLs
    :param url_index: index of the site to be queried
    """
    start_time = current_ms()
    while True:
        url_index = (url_index + 1) % len(sites_urls)
        try:
            with urlopen(sites_urls[url_index]) as f:
                my_str = f.read()
        except:
            my_str = "error"
        if current_ms() - start_time > duration_ms:
            break
        else:
            time.sleep(0.0001)


def stress_cpu(x: int = 1234):
    """
    Function to be used to stress the CPU. Computes x^2
    :param x: the number to compute x^2 of
    :return: None
    """
    while True:
        x * x


# ABSTRACT CLASS FOR INJECTIONS


class LoadInjector:
    """
    Abstract class for Injecting Errors in the System
    Should you want to implement your own injector, just extend/override this class
    """

    def __init__(self, tag: str = "", duration_ms: float = 1000):
        """
        Constructor
        """
        self.valid = True
        self.tag = tag
        self.duration_ms = duration_ms
        self.inj_thread = None
        self.completed_flag = True
        self.injected_interval = []
        self.init()

    def is_valid(self) -> bool:
        return self.valid

    def init(self):
        """
        Override needed only if the injector needs some pre-setup to be run. Default is an empty method
        :return:
        """
        pass

    def inject_body(self):
        """
        Abstract method to be overridden
        """
        pass

    def inject(self):
        """
        Caller of the body of the injection mechanism, which will be executed in a separate thread
        """
        self.inj_thread = threading.Thread(target=self.inject_body, args=())
        self.inj_thread.start()

    def is_injector_running(self):
        """
        True if the injector has finished working (end of the 'injection_body' function)
        """
        return not self.completed_flag

    def force_close(self):
        """
        Tries to force-close the injector
        """
        pass

    def get_injections(self) -> list:
        """
        Returns start-end times of injections exercised with this method
        """
        return self.injected_interval

    def get_name(self) -> str:
        """
        Abstract method to be overridden, provides a string description of the injector
        """
        return "[" + self.tag + "]Injector" + "(d" + str(self.duration_ms) + ")"

    @classmethod
    def fromJSON(cls, job):
        """
        This function allows to create an instance of an injector from a json description of the injector
        :param job: the JSON description of the injector
        :return: the injector object (subclass of LoadInjector)
        """
        if job is not None:
            if "type" in job:
                if job["type"] in {
                    "Memory",
                    "RAM",
                    "MemoryUsage",
                    "Mem",
                    "MemoryStress",
                }:
                    return MemoryStressInjection.fromJSON(job)
                if job["type"] in {"Disk", "SSD", "DiskMemoryUsage", "DiskStress"}:
                    return DiskStressInjection.fromJSON(job)
                if job["type"] in {"CPU", "Proc", "CPUUsage", "CPUStress"}:
                    return CPUStressInjection.fromJSON(job)
                if job["type"] in {"Deadlock", "Dl", "Dead"}:
                    return DeadlockInjection.fromJSON(job)
                if job["type"] in {
                    "HTTP",
                    "HTTPRead",
                    "NetRead",
                    "WebRead",
                    "SiteRead",
                }:
                    return HTTPReadInjection.fromJSON(job)
                if job["type"] in {"StopProcess", "Process"}:
                    return ProcessHangInjection.fromJSON(job)
        return None


# SUBCLASSES OF THE LOADINJECTOR CLASS


class SpinInjection(LoadInjector):
    """
    SpinLoop Error. Simple injection that runs a thread stuck in an endless loop
    """

    def __init__(self, tag: str = "", duration_ms: float = 1000):
        """
        Constructor
        """
        LoadInjector.__init__(self, tag, duration_ms)
        self.force_stop = False

    def inject_body(self):
        """
        Abstract method to be overridden
        """
        self.completed_flag = False
        start_time = current_ms()
        while True:
            if current_ms() - start_time > self.duration_ms or self.force_stop:
                break

        self.injected_interval.append({"start": start_time, "end": current_ms()})
        self.completed_flag = True
        self.force_stop = False

    def force_close(self):
        """
        Try to force-close the injector
        """
        self.force_stop = True

    def get_name(self) -> str:
        """
        Abstract method to be overridden
        """
        return "[" + self.tag + "]SpinInjection" + "(d" + str(self.duration_ms) + ")"


class DiskStressInjection(LoadInjector):
    """
    DiskStress Error
    """

    def __init__(
        self,
        tag: str = "",
        duration_ms: float = 1000,
        n_workers: int = 10,
        n_blocks: int = 10,
        rw_folder: str = "./",
    ):
        """
        Constructor
        """
        self.n_workers = n_workers
        self.n_blocks = n_blocks
        self.rw_folder = rw_folder
        self.poold = None
        LoadInjector.__init__(self, tag, duration_ms)

    def inject_body(self):
        """
        Abstract method to be overridden
        """
        self.completed_flag = False
        start_time = current_ms()
        self.poold = []
        poold_pool = Pool(self.n_workers)
        poold_pool.map_async(self.stress_disk, range(self.n_workers))
        self.poold.append(poold_pool)
        time.sleep((self.duration_ms - (current_ms() - start_time)) / 1000.0)
        if self.poold is not None:
            for pool_disk in self.poold:
                pool_disk.terminate()
        self.injected_interval.append({"start": start_time, "end": current_ms()})
        self.completed_flag = True

    def force_close(self):
        """
        Try to force-close the injector
        """
        if self.poold is not None:
            for pool_disk in self.poold:
                pool_disk.terminate()
        self.completed_flag = True

    def stress_disk(self, worker_id: int) -> None:
        block_to_write = "x" * 1048576
        while True:
            filehandle = tempfile.TemporaryFile(dir=self.rw_folder)
            for _ in range(self.n_blocks):
                filehandle.write(block_to_write.encode())
            filehandle.seek(0)
            for _ in range(self.n_blocks):
                content = filehandle.read(1048576)
                del content
            filehandle.close()
            del filehandle

    def get_name(self) -> str:
        """
        Abstract method to be overridden
        """
        return (
            "["
            + self.tag
            + "]DiskStressInjection"
            + "(d"
            + str(self.duration_ms)
            + "-nw"
            + str(self.n_workers)
            + ")"
        )

    @classmethod
    def fromJSON(cls, job):
        return DiskStressInjection(
            tag=(job["tag"] if "tag" in job else ""),
            duration_ms=(job["duration_ms"] if "duration_ms" in job else 1000),
            n_workers=(job["n_workers"] if "n_workers" in job else 10),
            n_blocks=(job["n_blocks"] if "n_blocks" in job else 10),
        )


class CPUStressInjection(LoadInjector):
    """
    CPUStress Error, executes many parallel threads that compute a very simple arithmetic operation
    without storing results anywhere
    """

    def __init__(self, tag: str = "", duration_ms: float = 1000):
        """
        Constructor
        """
        self.poolc = None
        LoadInjector.__init__(self, tag, duration_ms)

    def inject_body(self):
        """
        Abstract method to be overridden
        """
        self.completed_flag = False
        start_time = current_ms()
        self.poolc = Pool(cpu_count())
        self.poolc.map_async(stress_cpu, range(cpu_count()))
        time.sleep((self.duration_ms - (current_ms() - start_time)) / 1000.0)
        if self.poolc is not None:
            self.poolc.terminate()
        self.injected_interval.append({"start": start_time, "end": current_ms()})
        self.completed_flag = True

    def force_close(self):
        """
        Try to force-close the injector
        """
        if self.poolc is not None:
            self.poolc.terminate()
        self.completed_flag = True

    def get_name(self) -> str:
        """
        Abstract method to be overridden
        """
        return (
            "[" + self.tag + "]CPUStressInjection" + "(d" + str(self.duration_ms) + ")"
        )

    @classmethod
    def fromJSON(cls, job):
        return CPUStressInjection(
            tag=(job["tag"] if "tag" in job else ""),
            duration_ms=(job["duration_ms"] if "duration_ms" in job else 1000),
        )


class MemoryStressInjection(LoadInjector):
    """
    Loops and adds data to an array simulating memory usage
    """

    def __init__(
        self, tag: str = "", duration_ms: float = 1000, items_for_loop: int = 1234567
    ):
        """
        Constructor
        """
        LoadInjector.__init__(self, tag, duration_ms)
        self.items_for_loop = items_for_loop
        self.force_stop = False

    def inject_body(self):
        """
        Abstract method to be overridden
        """
        self.completed_flag = False
        start_time = current_ms()
        my_list = []
        while True:
            my_list.append([999 for i in range(0, self.items_for_loop)])
            if current_ms() - start_time > self.duration_ms or self.force_stop:
                break
            else:
                time.sleep(0.001)

        self.injected_interval.append({"start": start_time, "end": current_ms()})
        self.completed_flag = True
        self.force_stop = False

    def force_close(self):
        """
        Try to force-close the injector
        """
        self.force_stop = True

    def get_name(self) -> str:
        """
        Abstract method to be overridden
        """
        return (
            "["
            + self.tag
            + "]MemoryStressInjection(d"
            + str(self.duration_ms)
            + "-i"
            + str(self.items_for_loop)
            + ")"
        )

    @classmethod
    def fromJSON(cls, job):
        return MemoryStressInjection(
            tag=(job["tag"] if "tag" in job else ""),
            duration_ms=(job["duration_ms"] if "duration_ms" in job else 1000),
            items_for_loop=(
                job["items_for_loop"] if "items_for_loop" in job else 1234567
            ),
        )


class DeadlockInjection(LoadInjector):
    """
    Creates deadlocks through reverse acquisitions of locks
    """

    def __init__(
        self,
        tag: str = "",
        duration_ms: float = 1000,
        n_threads: int = 2,
        n_locks: int = 1,
    ):
        """
        Constructor
        """
        self.n_threads = n_threads
        self.n_locks = n_locks
        self.force_stop = False
        LoadInjector.__init__(self, tag, duration_ms)

    def inject_body(self):
        """
        Abstract method to be overridden
        """
        self.completed_flag = False
        start_time = current_ms()
        deadlocks = [
            DeadlockInjection.DeadlockGroup(n_threads=self.n_threads)
            for i in range(0, self.n_locks)
        ]
        for dl in deadlocks:
            dl.run()
        while True:
            # The 20 is because I am expecting to need some ms to terminate all processes
            if current_ms() - start_time - 20 > self.duration_ms or self.force_stop:
                break
        for dl in deadlocks:
            dl.stop()
        deadlocks = None
        self.injected_interval.append({"start": start_time, "end": current_ms()})
        self.completed_flag = True
        self.force_stop = False

    def force_close(self):
        """
        Try to force-close the injector
        """
        self.force_stop = True

    def get_name(self) -> str:
        """
        Abstract method to be overridden
        """
        return (
            "["
            + self.tag
            + "]DeadlockInjection"
            + "(d"
            + str(self.duration_ms)
            + "-t"
            + str(self.n_threads)
            + "-l"
            + str(self.n_locks)
            + ")"
        )

    class DeadlockGroup:
        """
        Service class that groups processes needed to create deadlock
        """

        def __init__(self, n_threads: int = 2):
            if n_threads < 2:
                n_threads = 2
            self.n_threads = n_threads
            self.l1 = multiprocessing.Lock()
            self.l2 = multiprocessing.Lock()
            self.threads = []

        def run(self):
            """
            Runs threads and creates deadlock around the two locks
            :return:
            """
            self.threads = []
            self.threads.append(
                multiprocessing.Process(
                    target=self.f1,
                    args=[
                        "t1",
                    ],
                )
            )
            self.threads.append(
                multiprocessing.Process(
                    target=self.f2,
                    args=[
                        "t2",
                    ],
                )
            )
            for i in range(0, self.n_threads - 2):
                self.threads.append(
                    multiprocessing.Process(
                        target=self.f_other,
                        args=[
                            "t_other",
                        ],
                    )
                )
            for thr in self.threads:
                thr.start()

        def stop(self):
            """
            Stops deadlocking threads
            :return:
            """
            for thr in self.threads:
                thr.terminate()
            self.threads = []

        def f1(self, name):
            with self.l1:
                time.sleep(0.01)
                with self.l2:
                    time.sleep(0.001)

        def f2(self, name):
            with self.l2:
                time.sleep(0.01)
                with self.l1:
                    time.sleep(0.01)

        def f_other(self, name):
            with self.l2:
                time.sleep(0.01)

    @classmethod
    def fromJSON(cls, job):
        return DeadlockInjection(
            tag=(job["tag"] if "tag" in job else ""),
            duration_ms=(job["duration_ms"] if "duration_ms" in job else 1000),
            n_threads=(job["n_threads"] if "n_threads" in job else 2),
            n_locks=(job["n_locks"] if "n_locks" in job else 1),
        )


class HTTPReadInjection(LoadInjector):
    """
    Reads data from HTTP urls
    """

    def __init__(
        self,
        tag: str = "",
        duration_ms: float = 1000,
        parallel_reads: int = 1,
        sites_urls: list = ["www.google.com"],
        sites_csv: str = "",
    ):
        """
        Constructor
        """
        self.parallel_reads = parallel_reads
        self.sites_urls = sites_urls
        if sites_csv is not "" and os.path.exists(sites_csv):
            try:
                with open(sites_csv, "r") as fil:
                    self.sites_urls = ["http://" + line.rstrip("\n") for line in fil]
            except:
                print("Sites file is not readable")
        self.http_readers = None
        LoadInjector.__init__(self, tag, duration_ms)

    def inject_body(self):
        """
        Abstract method to be overridden
        """
        self.completed_flag = False
        start_time = current_ms()
        self.http_readers = [
            multiprocessing.Process(
                target=url_reader,
                args=(
                    self.sites_urls,
                    random.randint(0, len(self.sites_urls) - 1),
                    self.duration_ms,
                ),
            )
            for _ in range(0, self.parallel_reads)
        ]
        for http_reader in self.http_readers:
            http_reader.start()
        time.sleep((self.duration_ms - current_ms() + start_time) / 1000.0)
        for http_reader in self.http_readers:
            http_reader.terminate()
        self.injected_interval.append({"start": start_time, "end": current_ms()})
        self.completed_flag = True

    def force_close(self):
        """
        Try to force-close the injector
        """
        if self.http_readers is not None:
            for http_reader in self.http_readers:
                http_reader.terminate()
        self.completed_flag = True

    def get_name(self) -> str:
        """
        Abstract method to be overridden
        """
        return (
            "["
            + self.tag
            + "]HTTPReadInjection(d"
            + str(self.duration_ms)
            + "-r"
            + str(self.parallel_reads)
            + ")"
        )

    @classmethod
    def fromJSON(cls, job):
        return HTTPReadInjection(
            tag=(job["tag"] if "tag" in job else ""),
            duration_ms=(job["duration_ms"] if "duration_ms" in job else 1000),
            parallel_reads=(job["parallel_reads"] if "parallel_reads" in job else 1),
            sites_urls=(
                job["sites_urls"] if "sites_urls" in job else ["www.google.com"]
            ),
            sites_csv=(job["sites_csv"] if "sites_csv" in job else ""),
        )


class ProcessHangInjection(LoadInjector):
    """
    Pauses a process for a timeframe
    """

    def __init__(
        self, tag: str = "", duration_ms: float = 1000, process_name: str = "arancino"
    ):
        """
        Constructor
        """
        LoadInjector.__init__(self, tag, duration_ms)
        if self.exists_process(process_name):
            self.process_name = process_name
        else:
            self.process_name = None
            print("[Error] Could not find service %s" % process_name)
            self.valid = False
        self.force_stop = False

    def exists_process(self, pname):
        if pname is not None:
            try:
                cmd_out = subprocess.check_output(["pgrep", pname])
                cmd_out = cmd_out.decode("utf-8")
                return cmd_out is not None and len(cmd_out) > 0
            except:
                return False
        else:
            return False

    def inject_body(self):
        """
        Abstract method to be overridden
        """
        self.completed_flag = False
        if self.process_name is not None:
            start_time = current_ms()
            try:
                subprocess.check_output(["pkill", "-STOP", self.process_name])
                while True:
                    if current_ms() - start_time >= self.duration_ms or self.force_stop:
                        break
                subprocess.check_output(["pkill", "-CONT", self.process_name])
                self.injected_interval.append(
                    {"start": start_time, "end": current_ms()}
                )
            except:
                subprocess.check_output(["pkill", "-CONT", self.process_name])
                while True:
                    if current_ms() - start_time >= self.duration_ms:
                        break
        else:
            time.sleep(self.duration_ms / 1000.0)
        self.completed_flag = True
        self.force_stop = False

    def force_close(self):
        """
        Try to force-close the injector
        """
        self.force_stop = True

    def get_name(self) -> str:
        """
        Abstract method to be overridden
        """
        return (
            "["
            + self.tag
            + "]ProcessHangInjection"
            + "(d"
            + str(self.duration_ms)
            + "-n"
            + str(self.process_name)
            + ")"
        )

    @classmethod
    def fromJSON(cls, job):
        return ProcessHangInjection(
            tag=(job["tag"] if "tag" in job else ""),
            duration_ms=(job["duration_ms"] if "duration_ms" in job else 1000),
            process_name=(job["process_name"] if "process_name" in job else "arancino"),
        )
