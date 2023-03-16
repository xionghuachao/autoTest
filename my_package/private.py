class Phone:
    #私有成员变量
    __current=5
    #私有方法
    def __keep(self):
        print("单核模式定义")
    def ss(self):
        if self.__current>2 :
            print("满足")
phone=Phone()
phone.ss()

