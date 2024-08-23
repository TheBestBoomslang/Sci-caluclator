import math 
print("Calc(it's just slang for calculator) type EXIT to exit NOTE: some operators only use first number ex(sqrt and square)")
calcwhile = True
while(calcwhile):
    n1 =int(input("Input your first number: \n"))
    n2 =int(input("Input your second number: \n"))
    op = input("Input your operator (examples:* / + - sqrt square sin cos tan  nlog e) \n")
    match op:
        case "e":
            print(math.exp(n1))
        case "nlog":
            if(n1<=0):
                print("pick a postive non zero number")
            else:
                print(math.log10(n1))
        case "tan":
           print(math.tan(n1))
        case "sin":
           print(math.sin(n1))
        case "cos":
           print(math.cos(n1))
        case "sqrt":
           print(math.sqrt(n1))
        case "square":
            if(n1<0):
                print("pick a postive number")
            else:
                print(n1*n1)
        case "*":
            print(n1*n2)
        case "/":
            if(n2 == 0):
                print("error cannot divide by zero")
            else:
                print(n1/n2)
        case "+":
            print(n1+n2)
        case "-":
            print(n1-n2)
        case _:  
            print("error not a valid operator starting the calc(short for calculator I am just using slang) over")
    exit = input("Type EXIT to exit or press ENTER to continue: ")
    if(exit == "EXIT"):
        break
    else:
        pass
