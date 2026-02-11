
import sys

def main():
    if len(sys.argv) == 1:
        print("none")
        return

    for p in sys.argv[1:]:
        if not p.endswith("ism"):
            print(p + "ism")

main()

# python append_it.py

# python append_it.py "parallel" "egoism" "human"
