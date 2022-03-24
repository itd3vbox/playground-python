import threading
import time

def background_task(data):
    print("Thread {0}: starting".format(data))

    for index in range(10):
        print("Thread {0}: Simulation: {1}".format(data, index))
        time.sleep(2)

    print("Thread {0}: finishing".format(data))

if __name__ == "__main__":

    thread_1 = threading.Thread(target=background_task, args=("Task-1",))   
    thread_1.start()
    print("Wait for the thread to finish")

    thread_2 = threading.Thread(target=background_task, args=("Task-2",))   
    thread_2.start()
    print("Wait for the thread to finish")