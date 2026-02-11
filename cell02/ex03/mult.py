def main(): 
    first_num = int(input("Enter the first number: \n")) 
    second_num = int(input("Enter the second number: \n")) 
    x = first_num * second_num 
    print(first_num, "x", second_num, "=", x) 
    if x < 0: 
        print("This number is negative.") 
    elif x > 0: 
        print("This number is positive.") 
    else: 
        print("This number is both positive and negative.") 
        
main()
##Enter the first number: 
##42
##Enter the second number: 
##42
##42 x 42 = 1764
##This number is positive.
##Enter the first number: 
##78
##Enter the second number: 
##-1
##78 x -1 = -78
##This number is negative.