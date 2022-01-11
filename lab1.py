# Домашнее задание 1, вариант 4
inputList = list()


def inputStream():
    while True:
        data = input()
        if data == "":
            break
        inputList.append(data)
    return inputList


def count():
    resultMap = dict()
    setOfList = set(inputList)
    for i in setOfList:
        resultMap[i] = inputList.count(i)
    return sorted(resultMap)


inputStream()
print(count())
