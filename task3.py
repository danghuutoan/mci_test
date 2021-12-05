import sys


def _BracketCombinations(num, current_string, ouput, open, close):
    if len(current_string) == num * 2:
        ouput.append(current_string)
        return ouput

    if open < num:
        _BracketCombinations(num, current_string + "(", ouput, open + 1, close)

    if close < open:
        _BracketCombinations(num, current_string + ")", ouput, open, close + 1)


def BracketCombinations(num):
    output = []
    _BracketCombinations(num, "", output, 0, 0)
    return output


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("please enter row num")
        exit(1)
    input = int(sys.argv[1])
    print(BracketCombinations(input))
