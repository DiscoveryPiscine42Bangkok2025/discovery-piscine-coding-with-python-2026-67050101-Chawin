import sys

def main():
    if len(sys.argv) == 2:
        print(sys.argv[1].lower())
    else:
        print("none")

main()

# python downcase_it.py
# python downcase_it.py "LUCIOLE"
# python downcase_it.py "This Exercise Is Quite Easy!" 
# this exercise is quite easy!