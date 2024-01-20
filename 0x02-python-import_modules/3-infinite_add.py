#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total = 0
    for s in range(len(sys.argv) - 1):
        total += int(sys.argv[s + 1])
        print("{}".format(total))
