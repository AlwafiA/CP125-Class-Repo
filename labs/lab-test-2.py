#ALWAFI ABDULGADER ALAMIN
#MC2515202741

"""
PROBLEM DESCRIPTION:
Create a program that accepts 5 integer input values from the user and is stored in a
list. The program will perform the following task:
1. Print all the numbers that has been entered in ascending order
2. Calculate and find the sum of all the entered numbers
3. Find and print the largest number
"""
#get and sort list
def get_list(nu):
    listt = []
    listt.append(nu)
    
    while len(listt) < 5:
        first = int(input("Enter number: "))
        listt.append(first)
        print(listt)


    print(f"Numbers in ascending order: {sorted(listt)}")
    print(f"Sum of all numbers: {sum(listt)}")
    print(f"Largest number: {max(listt)}")
    return listt


call = get_list(int(input("Enter number: ")))

"""
rin - code
def info_num(mo):
    result = []
    for i in range(5):
        num = int(input)
        result.append(num)
    print(sorted(result))
    print(sum(result))
    print(max(result))

info_num()"""
    