import sys


def task1(n):
    for i in range(n):
        str = "* " * (i + 1)
        print(str)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("please enter row num")
        exit(1)
    n = int(sys.argv[1])
    task1(n)
