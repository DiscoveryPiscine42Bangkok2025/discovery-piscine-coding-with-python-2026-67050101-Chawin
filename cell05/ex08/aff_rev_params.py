import sys

def main():
    if len(sys.argv) <= 2:
        print("none")
    else:
        for param in reversed(sys.argv[1:]):
            print(param)

main()
# cd ex08
# python aff_rev_params.py
# python aff_rev_params.py "coucou"
# python aff_rev_params.py "Python" "piscine" "hello"
