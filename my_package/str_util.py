def str_reverse(s) :
    return s[::-1]
def substr(s,x,y) :

    str1=s[x:y:1]
    return str1
if __name__ == '__main__':
    print(str_reverse("123"))
    print(substr("黑马程序员",1,3))