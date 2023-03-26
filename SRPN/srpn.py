# This is your SRPN file. Make your changes here.
# to provide array for data storage , stack = []

stack = []
random = [1714636915, 1681692777, 846930886, 1804289383, 521595368, 35005211, 1303455736, 304089172, 1540383426, 1365180540, 1967513926, 2044897763, 1102520059, 783368690, 1350490027, 1025202362, 1189641421, 596516649, 1649760492, 719885386, 424238335, 1957747793, 1714636915, 1681692777, 846930886, 1804289383]
# Returning only numbers#
def isnum(n):
    try:
        int(n)
        return True
    except:
        return False

# Setting maximum and minimum range for the calculator#
def max_min(x):
    if int(x) > 2147483647:
        x = 2147483647
    elif int(x) < -2147483648:
        x = -2147483648
    return int(x)


def process_command(command):
# splitting string into a list where each word/number is a list item #
    horiz = command.split()
    for x in range(len(horiz)):
        if isnum(horiz[x]):
            command = int(horiz[x])
        else:
            command = horiz[x]

# "Stack underflow" is printed when the length of the list is shorter than 2 numerical elements #

# Proceed with addition of last and 2nd last element of the list when the command shows "+" operator #

    if command == "+":
        if len(stack) < 2:
            print("Stack underflow.")
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            res = int(num2) + int(num1)
            stack.append(max_min(res))

# Proceed with multiplication of last and 2nd last element of the list when the command shows "*" operator #
    elif command == "*":
        if len(stack) < 2:
            print("Stack underflow.")
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            res = int(num2) * int(num1)
            stack.append(max_min(res))

# Proceed with substraction of last and 2nd last element of the list when the command shows "-" operator #
    elif command == "-":
        if len(stack) < 2:
            print("Stack underflow.")
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            res = int(num2) - int(num1)
            stack.append(max_min(res))

# Proceed with division of last and 2nd last element of the list when the command shows "/" operator #
    elif command == "/":
        if int(stack[-1]) == 0:
            print("Divide by 0.")
        elif  len(stack) < 2:
            print("Stack underflow.")
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            res = int(int(num2) / int(num1))
            stack.append(max_min(res))

# Proceed with remainder of last and 2nd last element of the list when the command shows "%" operator #       
    elif command == "%":
        if len(stack) < 2:
            print("Stack underflow.")
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            res = int(int(num2) % int(num1))  
            stack.append(max_min(res))

# Proceed with exponential of last and 2nd last element of the list when the command shows "^" operator # 
    elif command == "^":
        if int(stack[-1]) < 0: 
            print("Negative power.")
        elif len(stack) < 2:
            print("Stack underflow.")
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            res = int(int(num2) ** int(num1))
            stack.append(max_min(res))

# displaying numerical numbers in the list when command shows "d" #
    elif command == "d":
        for x in stack:
            print (x)
  
# random numbers when command shows "r" #
    elif command == "r":
        stack.append(int(random.pop()))
# return "Stack overflow" if the length is more than 22 #
        if len(stack) > 22:
            print("Stack overflow.")
# maximum length of numerical elements the calculator could take is 22, "stack overflow" is shown if the length is more than 22 #
    elif len(stack) > 22:
        print("Stack overflow.")

# return last enter into the start#
    elif command == "=":
        print(stack[-1])

# only number is added into the list #
    elif isnum(command):
        stack.append(max_min(command))

    
#This is the entry point for the program.
#Do not edit the below
if __name__ == "__main__": 
    while True:
        try:
            cmd = input()
            if process_command(cmd):
                print(str(stack))
        except:
            exit()
