import sys

def main():
    if len(sys.argv) == 2:
        print(sys.argv[1].upper())
    else:
        print("none")

main()
#python upcase_it.py
#python upcase_it.py initiation
#python upcase_it.py "This exercise is quite easy!"
