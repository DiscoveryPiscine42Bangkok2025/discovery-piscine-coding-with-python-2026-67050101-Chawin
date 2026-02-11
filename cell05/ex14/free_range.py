import sys

def main():
    if len(sys.argv) != 3:
        print("none")
        return

    x = [i for i in range(int(sys.argv[1]),  int(sys.argv[2]) + 1)]
    print(x)
main()

# python free_range.py 10 14