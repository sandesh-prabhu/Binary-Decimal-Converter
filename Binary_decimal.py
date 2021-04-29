def btd(b):
    t,d,i=0,0,0
    while b!=0:
        t=b%10
        d=d+t*(2**i)
        b=b//10
        i+=1
    print(d)
def dtb(num):
    if num>=1:
        dtb(num//2)
    print(num%2,end="")
while 1:
    print("")
    print("MENU")
    print("1->Binary to Decimal")
    print("2->Decimal to Binary")
    print("3->Exit")
    c=int(input("Enter your choice:"))
    if c==1:
        n=input("Binary:")
        btd(int(n))
    elif c==2:
        n=input("Decimal:")
        dtb(int(n))
    elif c==3:
        break;;;;;
    else:
        print("Invalid Input")
