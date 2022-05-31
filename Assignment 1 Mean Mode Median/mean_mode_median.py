import statistics
from collections import Counter


def sampleMean(sampleList):
    try:
        sampleList.sort()
    except Exception as e:
        return ("Invalid Data")
    else:
        return sum(sampleList)/len(sampleList)


def sampleMedian(sampleList):
    sampleList.sort()
    listLength = len(sampleList)
    if listLength % 2 != 0:
        return sampleList[listLength//2]
    else:
        return (sampleList[(listLength//2)]+sampleList[(listLength//2)-1])/2


def sampleMode(sampleList):
    sampleList.sort()
    occuranceList = Counter(sampleList)
    listMode = [k for k, v in dict(occuranceList).items(
    ) if v == max(list(occuranceList.values()))]
    if(len(listMode) == len(sampleList)):
        return sampleList[0]
    else:
        return listMode[0]


if __name__ == "__main__":
    sampleList = [11, 627, 83, 94, 45, 1, 987]
    print(f"The random list is {sampleList}")
    print(f"mean is {sampleMean(sampleList)}")
    print(f"Mode is {sampleMode(sampleList)}")
    print(f"Median is {sampleMedian(sampleList)}")
    print(
        f"Mean,Mode,Median is {statistics.mean(sampleList)}  {statistics.mode(sampleList)}  {statistics.median(sampleList)}")
