from operator import index
import threading
import time

def background_task(data):

    print("Thread {0}: starting doing in background".format(data))
    index = 0

    while True:
        file = open('log.txt', 'w')
        index += 1 
        file.write("Thread {0}: Simulation: {1}\n".format(data, index))
        file.close()
        time.sleep(2)

if __name__ == "__main__":

    thread_infin = threading.Thread(target=background_task, args=("Task-1",))   
    thread_infin.start()

    print("Thread are still running!")