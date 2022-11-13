def addition(x,y):
    print(x+y)
def substraction(x,y):
    print(x-y)
def multiply(x,y):
    print(x*y)
def divide(x,y):
    print(x/y)
def square(x):
    print(x*x)

print("A. addition")
print("B substraction")
print("C multiply")
print("D divide")
print("S square")
print("Q exit")
while True:
    choice= input("input your choice 🚀"+"\n")

    if choice == "A" or choice=="a":
        print("addition"+"\n")
        a = int(input("input first number"))
        b = int(input("input second number"))
        addition(a,b)
    elif choice =="B" or choice=="b":
        print("substraction"+"\n")
        a = int(input("input first number"))
        b = int(input("input second number"))
        substraction(a,b)
    elif choice == "C" or choice == "c":
        print("multiply"+"\n")
        a = int(input("input first number"))
        b = int(input("input second number"))
        multiply(a,b)
    elif choice == "D" or choice == "d":
        print("Divide"+"\n")
        a = int(input("input first number"))
        b = int(input("input second number"))
        divide(a,b)
    elif choice == "S" or choice == "s":
        print("squre"+"\n")
        a = int(input("input the number to be squared"))
        sqroot(a)


    elif choice == "Q" or choice == "q":
        print("program ended"+"\n")
        break
