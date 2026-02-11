import sys

def main():
    if len(sys.argv) == 1:
        print("none")
        return

    params = sys.argv[1:]
    print(f"parameters: {len(params)}")

    for p in params:
        print(f"{p}: {len(p)}")

main()

# python count_it.py "Game" "of" "Thrones"
# parameters: 3
# Game: 4
# of: 2
# Thrones: 7
