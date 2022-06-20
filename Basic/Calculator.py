logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiplay(a,b):
    return a*b

def divide(a,b):
    return a/b

operations={
    "+":add,
    "-":sub,
    "*":multiplay,
    "/":divide
}

def calculator():
    print(logo)
    num1=float((input("What is the first number?: ")))

    for i in operations:
        print(i)

    should_continue=True

    while should_continue:
        symbol=input("pick up an operation : ")
        num2=float((input("What is the next  number?: ")))
        calculation_function=operations[symbol]
        answer=calculation_function(num1,num2)
        
        print(f"{num1} {symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue with {answer}, or type 'n' to start new claculation: ") == "y" :
            num1=answer
            should_continue=True
        else:
            should_continue=False
            calculator()

calculator()

