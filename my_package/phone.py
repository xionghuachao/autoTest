class Phone:
    __is_5g=False

    def __check_5g(self):
        if self.__is_5g :
            print("5G开启")
        elif self.__is_5g==False :
            print("5G关闭，使用4G")
    def call_by(self):
           self.__check_5g()
           print("通话中")
#Phone(False).call_by()
class Phone1(Phone):
    face_id="10001"
    def call_by5(self):

        print("2022")
ph=Phone1()
ph.call_by5()
ph.call_by()
#演示多继承
class Nfc:
    nfc_type="第五代"
    produce="hm"
    def read_card(self):
        print("nfc读卡")
    def write_card(self):
        print("nfc写卡")
class Reote :

    rc_type="红外"

    def control(self):
        print("红外开启了")

class Reme(Nfc,Reote) :
    def se(self):
      print(super().produce)
reme=Reme()

reme.read_card()
reme.read_card()
reme.se()

reme.control()
#在子类中调用父类属性super().produce或者phone.produce





