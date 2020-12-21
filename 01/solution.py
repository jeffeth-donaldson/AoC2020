def makeSet(file):
    """Pull the items from the puzzle input and put in a set"""
    values = set()
    f = open(file)
    lines = f.readlines()
    f.close()
    print(lines)
    for line in lines:
        values.add(int(line.strip()))
    return values

def findValue(values):
    """Returns product of pair of values in set that add to 2020"""
    print(values)
    for value in values:
        print("Testing:",value)
        if 2020 - value in values:
            return value * (2020 - value)
        else:
            print(2020 - value, "not in set")

def test():
    testset = {1721, 979, 266, 299, 675, 1456}
    for val in testset:
        print(val)
    return findValue(testset)
if __name__ == "__main__":
    values = makeSet("input")
    product = findValue(values)
    # product = test()
    if product != None:
        print("Value:", product)
    else:
        print("Value not found")
