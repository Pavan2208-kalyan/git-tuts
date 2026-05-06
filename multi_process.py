# MultiProcessing Module

import multiprocessing

def print_cube(n):
    print("Cube of a number is {}".format(n**3))


def print_square(n):
    print("Sqaure of a number is {}".format(n**2))
    
# if __name__== "__main__":
#     p1=multiprocessing.Process(target=print_cube,args=(10,))
#     p2=multiprocessing.Process(target=print_square,args=(10,))
#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()
#     print("Both processes are done")

## MultiThreading

# import time
# from threading import Thread
# from threading import Lock


# num = 0
# num_lock=Lock()

# def count(n):
#     global num
#     for _ in range(n):
#         with num_lock:
#             num +=1

# import_threading=100

# t1= Thread(target=count,args=(import_threading,))
# t2=Thread(target=count,args=(import_threading,))

# start=time.time()

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# end=time.time()

# print("Time taken is ",end-start)


# from threading import Thread
# from threading import Lock
# import time

# num_lock=Lock()
# num=0

# def count_of_n(n):
#     global num

#     for _ in range(n):
#         with num_lock:
#             num+=1

# thread_count =1000000

# p1=Thread(target=count_of_n,args=(thread_count,))
# p2=Thread(target=count_of_n,args=(thread_count,))
# start_time=time.time()
# p1.start()
# p2.start()
# p1.join()
# p2.join()
# end_time=time.time()

# print("After exr",end_time-start_time)



