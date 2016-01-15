# sample.py
import cProfile
import sys
from threading import Thread

def write_heavy_data(number):
    big_number = 100000
    #file_number = 10
    #for i in xrange(file_number):
    with open("result/dummy%d.txt" % number, "w") as fw:
        for j in xrange(big_number):
            fw.write("line %d\n" % j)

def spin_for_a_while(number):
    i = 0
    while i < number:
        i += 1


def main_for_io(cpu_number):
    big_number = 10000000
    if cpu_number == 1:
        spin_for_a_while(big_number)
        write_heavy_data()
    if cpu_number > 1:
		thread_list = []
		for var in range(0, 10):
			thread_list.append(Thread(target=write_heavy_data,  args=(var,)))
		'''
		thread_for_cpu = Thread(target=spin_for_a_while, args=(big_number,))
        thread_for_io = Thread(target=write_heavy_data)
        thread_list = [thread_for_cpu, thread_for_cpu]
        thread_for_cpu.start()
        thread_for_io.start()
		'''
		for thread in thread_list:
			thread.start()
        	thread.join()

if __name__ == "__main__":
    cProfile.run("main_for_io(int(sys.argv[1]))")