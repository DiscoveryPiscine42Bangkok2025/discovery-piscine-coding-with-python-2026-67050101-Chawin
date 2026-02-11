import sys

def main():
    if len(sys.argv) != 2:
        print("none")
        return

    param = sys.argv[1]
    user_input = input("What was the parameter? ")

    if user_input == param:
        print("Good job!")
    else:
        print("Nope, sorry...")

main()
#output example:
# cd ex10
# python parameter_matching.py
# python parameter_matching.py "Hello"
