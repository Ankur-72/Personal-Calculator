print("Hi! I am your personal calculator.")
print("Please type '1' for addition")
print("Please type '2' for subtraction")
print("Please type '3' for multiplication")
print("Please type '4' for division")
select = int(input())

if select == 1:
    print("Please provide the two numbers to add")
    a = int(input())
    b = int(input())
    
    def addition(a,b):
        return a+b
        
    x = addition(a,b)
    print(x)

if select == 2:
    print("Please provide the two numbers to subtraction")
    a = int(input())
    b = int(input())
    
    def subtraction(a,b):
        return a-b
        
    x = subtraction(a,b)
    print(x)

if select == 3:
    print("Please provide the two numbers to multiplication")
    a = int(input())
    b = int(input())
    
    def multiplication(a,b):
        return a*b
        
    x = multiplication(a,b)
    print(x)

if select == 4:
    print("Please provide the two numbers to division")
    a = int(input())
    b = int(input())
    
    def division(a,b):
        return a/b
        
    x = division(a,b)
    print(x)
