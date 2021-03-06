# sample.py
import cProfile
import sys
from multiprocessing import Process

def write_heavy_data(number):
    big_number = 100000
    with open("result2/dummy%d.txt" % number, "w") as fw:
        for j in xrange(big_number):
            print number
            fw.write("line %d\n" % j)

def main_for_io(cpu_number):
    if cpu_number == 1:
        write_heavy_data()
    if cpu_number > 1:
        process_list = []
        for var in range(0, cpu_number):
            process_list.append(Process(target=write_heavy_data,  args=(var,)))
        for process in process_list:
            process.start()

        for process in process_list:
            process.join()

if __name__ == "__main__":
    cProfile.run("main_for_io(int(sys.argv[1]))")
