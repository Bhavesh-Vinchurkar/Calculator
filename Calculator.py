def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

parent_while=True
while parent_while:
    a=float(input("What's the first number? : "))  
    while_calc=True
    stored_result=0
    while while_calc:
        print('+')
        print('-')
        print('*')
        print('/')
        operation=input("Pick an operation : ")
        c=float(input("What's the next number? : "))

        if operation=='+':
            stored_result=add(a,c)
            print(stored_result)

        elif operation=='-':
            stored_result=subtract(a,c)
            print(stored_result)

        elif operation=='*':
            stored_result=multiply(a,c)
            print(stored_result)

        elif operation=='/':
            stored_result=divide(a,c)
            print(stored_result)

        next_op=input(f"Type 'y' to continue calculating with {stored_result}, type 'n' to start a new calculation, or type 'exit' to end the program : ").lower()
        if next_op=='n':
            while_calc=False
        elif next_op=='exit':
            parent_while=False
            while_calc=False
        else:
            a=stored_result
