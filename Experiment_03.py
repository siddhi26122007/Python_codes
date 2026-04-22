def char_type(ch):
    a=ord(ch)
    if a==32:
        print("enter a character")
    elif 48<=a<=57:
        print("its a digit")
    elif 65<=a<=90:
        print("uppercase")
    elif 97<=a<=122:
        print("lowercase")
    else:
        print("special symbol")
def main():
    while(1):
        ch=input("enter the character")
        if len(ch)!=1:
            print("error")
        else:
            char_type(ch)
main()
             

