import sys

def main():
    if len(sys.argv) != 2:
        print("none")
        return

    text = sys.argv[1]
    count_z = text.count("z")

    if count_z == 0:
        print("none")
    else:
        print("z" * count_z)

main()
# python string_are_arrays.py
# python string_are_arrays.py "The character z is not found in this string"
# python string_are_arrays.py "The character z is found in this string"
# python string_are_arrays.py "Zaz visits the zoo with Zazie"