# sample.py
import cProfile
import sys
from threading import Thread
import math
import time

def write_heavy_data(var, number, numberMin, numberMax):
    #divisibleNumbers = []

    start_time = time.time()
    with open("result/dummy%d.txt" % var, "w") as fw:
        for j in xrange(numberMin,numberMax):
            if(number % j == 0):
                fw.write("can be divided by %d\n" % j)
                print j
                #divisibleNumbers.add(j)
            else:
                fw.write("cannot be divided by %d\n" % j)
        end_time = time.time()
        length = end_time - start_time
        fw.write("thread started at %d\n" %start_time)
        fw.write("thread ended at %d\n" %end_time)
        fw.write("thread took %d\n" %length)
    #return divisibleNumbers



def main(cpu, dividient):
    start_time = time.time()
    if cpu == 1:
        write_heavy_data()
    if cpu > 1:
        thread_list = []
        numberMin = 0
        numberMax = 1
        numbersParThread = math.floor( dividient / cpu )
        remainder = dividient % cpu
        for cpu_id in range(0, cpu):
            if(numberMin == 0):
                numberMin += 1
            else:
                numberMin = numberMax
            if(cpu_id < remainder):
                numberMax += numbersParThread + 1
            else:
                numberMax += numbersParThread
            thread_list.append(Thread(target=write_heavy_data,  args=(cpu_id,dividient,int(numberMin),int(numberMax))))
        for thread in thread_list:
            thread.start()
        for thread in thread_list:
            thread.join()
    end_time = time.time()
    print end_time - start_time


if __name__ == "__main__":
    cProfile.run("main(int(sys.argv[1]),long(sys.argv[2]))")
