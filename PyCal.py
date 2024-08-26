def welcome_message():
    print("*** WELCOME !!! This is PyCal World *** ")


def calculate_sum():
    numbers = input("Enter numbers separated by spaces: ")
    string_lst = numbers.split()
    int_lst = [int(num) for num in string_lst]
    total = sum(int_lst)
    print("Summation of Given Numbers: ", total)


def calculate_sub():
    print("First Number - Second Number")
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    print("The Result of Substraction is: ", a - b)


def calculate_mul():
    numbers = input("Enter numbers separated by spaces: ")
    string_lst = numbers.split()
    int_lst = [int(num) for num in string_lst]
    mul = 1
    for i in range(len(int_lst)):
        mul = mul * int_lst[i]
    print("The Multiplication Result is: ", mul)


def calculate_div():
    print("First Number/Second Number")
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    div = float(a / b)
    print("The Division Result is: ", div)


def menu():
    print("Here are the Operations You Can Operate : ")
    print("Press the Numbers")
    print("1. For Summation ")
    print("2. For Substraction ")
    print("3. For Multiplication ")
    print("4. For Division ")
    print("5. For Stop ")


welcome_message()

while True:
    menu()
    n = int(input("Enter a Valid Number : "))
    if n == 1:
        calculate_sum()

    elif n == 2:
        calculate_sub()

    elif n == 3:
        calculate_mul()

    elif n == 4:
        calculate_div()

    elif n == 5:
        print("Thanks For Using PyCal")
        break

    # else:
    #     print("Enter a Valid Digit")
