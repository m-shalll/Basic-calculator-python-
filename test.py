def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def devision(x,y):
    return x/y
while(1):
    flag=input("Enter your operation:")
    if(flag.upper()=="AC"):
        print("***Done***")
        break
    elif(flag not in["*","/","-","+"]):
        print("Wrong input please enter one of those options: * / + -")
        continue
    else:
        x=int(input("Enter your first number="))
        y=int(input("Enter your second number="))
        if(flag=="*"):
            result=multiply(x,y)
        elif(flag=="/"):
            result=devision(x,y)
        elif(flag=="-"):
            result=subtract(x,y)
        else:
            result=add(x,y)
        print(f"Your result={result}")