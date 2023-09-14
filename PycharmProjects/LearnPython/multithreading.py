from threading import Thread,Barrier
import time
barrier=Barrier(4)
def fun(text,sl):

    def start(text,sl):
        print(f"Test starts : {text}")
        time.sleep(sl)

    def passed(text,sl):
        print(f"Test passed : {text}")
        barrier.wait()
        time.sleep(sl)

    def end(text,sl):
        print(f"Test ends : {text}")
        time.sleep(sl)

    start(text,sl)
    passed(text,sl)
    end(text,sl)

t1 = Thread(target=fun,args=("Thread 1",2,))
t2 = Thread(target=fun,args=("Thread 2",3,))
t3 = Thread(target=fun,args=("Thread 3",4,))
t4 = Thread(target=fun,args=("Thread 4",1,))

thread_list=[t1,t2,t3,t4]

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()
