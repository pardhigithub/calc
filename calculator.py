def sum(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def mod(x,y):
    return x%y

operator = input("select an operalor(+,-,*,/,%): ")

while True:
    if operator in ('+','-','*','/','%'):
        try:
            n1 = float(input("enter first number: "))
            n2 = float(input("enter second number: "))
        except ValueError:
            continue
    
        if operator=='+':
            print(sum(n1,n2))
            break
        elif operator=='-':
            print(sub(n1,n2))
            break
        elif operator=='*':
            print(mul(n1,n2))
            break
        elif operator=='/':
            print(div(n1,n2))
            break
        elif operator=='%':
            print(mod(n1,n2))
            break

    else:
        print("invalid sign")
        break