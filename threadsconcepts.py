import threading
import time

def print_numbers():
    for i in range(5):
        print("Number:",i)
        time.sleep(1)
    
def printLetters():
    for c in "ABCDE":
        print("letter:",c)
        time.sleep(1)

t1 = threading.Thread(target =print_numbers )
t2 = threading.Thread(target =printLetters )

t1.start()
t2.start()

t1.join()
t2.join()

print("Both threads fineshed")