from task3 import BracketCombinations


def testCase1():
    expected = ["()"]
    actual = BracketCombinations(1)
    assert len(expected) == len(actual)
    for x in expected:
        assert x in actual


def testCase2():
    expected = [""]
    actual = BracketCombinations(0)
    assert len(expected) == len(actual)
    for x in expected:
        assert x in actual


def testCase3():
    expected = ["()()()", "()(())", "(())()", "((()))", "(()())"]
    actual = BracketCombinations(3)
    assert len(expected) == len(actual)
    for x in expected:
        assert x in actual

