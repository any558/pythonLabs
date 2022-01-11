from unittest.mock import patch


def testInput():
    r = []
    x = input()
    while x:
        r.append(x)
        x = input()

    resultMap = dict()
    setOfList = set(r)
    for i in setOfList:
        resultMap[i] = r.count(i)

    return sorted(resultMap.items(), key=lambda item: item[0])


def test_f():
    with patch('builtins.input', side_effect=['2', '2', '2', '3', '3', '4', '5', '5', '']):
        testResult = testInput()
        assert testResult == [('2', 3), ('3', 2), ('4', 1), ('5', 2)]


test_f()
