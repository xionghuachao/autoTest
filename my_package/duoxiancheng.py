import time
import threading
def sing():
    while True :
        print("我在唱歌")
        time.sleep(1)
def dance(msg):
    while True :
        print(msg)
        time.sleep(1)
if __name__ == '__main__':
    sing=threading.Thread(target=sing)
    dance = threading.Thread(target=dance,args=("我要跳舞",))
    sing.start()
    dance.start()