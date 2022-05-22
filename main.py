import re  # to split a lot of chars
from statistics import median  # to find the median


def q1():
    a = str(input("Please enter hex number: "))  # get the number
    try:  # check if it is valid hex num
        print(int(a, 16))  # print the number as dec

    except:  # (else)
        print("invalid hex number")  # print if it's invalid hex number


def q2():
    a = str(input("Please enter a string"))  # get the input
    hex_lst = re.split('g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z', a.lower())  # make a list of the hex nums
    n = sum([int(x, 16) for x in hex_lst])  # find the sun
    print(n)  # print sum as dec
    print(bin(n)[2::])  # print sum as bim
    print(oct(n)[2::])  # print sum as oct


def q3():
    lst = []  # the list of the input
    a = str(input("Please enter a num"))  # get the first input
    while a.isnumeric():  # check if the input is ended
        lst.append(float(a))  # add the num to the input list
        a = str(input("Please enter a num"))  # get the next
    print("The avg is: ", sum(lst) / len(lst))  # Print the avg
    print("The med is: ", median(lst))  # Print the median


#q1()
#q2()
#q3()