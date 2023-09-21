# lab8.py
# Celvis

# Import                                                                     
import sys

def main():
    # variable
    total = 0

    # Loop through the comamnd line arguments made
    for arg in sys.argv[1:]:
        try:
            num = int(arg)
            total += num
        except ValueError:
            pass

    # Output
    print("The result is", total)

if __name__ == "__main__":
    main()

