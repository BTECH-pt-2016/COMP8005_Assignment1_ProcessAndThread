# sample.py
import cProfile
import sys
from multiprocessing import Process

def write_heavy_data(number, Fibnumber):
    print Fibnumber
    j = fibR(Fibnumber)
    with open("result2/dummy%d.txt" % number, "w") as fw:
        fw.write("fibbonacci is %d\n" % j)


def fibR(n):
    if n==1 or n==2:
        return 1
    return fibR(n-1)+fibR(n-2)

def main_for_io(cpu_number,Fibnumber):
    if cpu_number == 1:
        write_heavy_data()
    if cpu_number > 1:
        process_list = []
        for var in range(0, cpu_number):
            process_list.append(Process(target=write_heavy_data,  args=(var,Fibnumber,)))
        for process in process_list:
            process.start()

        for process in process_list:
            process.join()

if __name__ == "__main__":
    cProfile.run("main_for_io(int(sys.argv[1]),int(sys.argv[2]))")
