def makeSet(file):
    """Pull the items from the puzzle input and put in a set"""
    values = []
    f = open(file)
    lines = f.readlines()
    f.close()
    print(lines)
    for line in lines:
        values.append(int(line.strip()))
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
def find3Values(values):
    """Returns the product of three values in set that add to 2020"""
    for i in range(len(values)):
        for j in range(i+1,len(values)):
            if 2020 - (values[i] + values[j]) in values:
                return values[i] * values[j] * (2020 - values[i] - values[j])


def test():
    testset = {1721, 979, 266, 299, 675, 1456}
    for val in testset:
        print(val)
    return findValue(testset)
if __name__ == "__main__":
    values = makeSet("input")
    option = input("2 or 3")
    if option == "2":
        product = findValue(values)
    elif option == "3":
        product = find3Values(values)
    # product = test()
    if product != None:
        print("Value:", product)
    else:
        print("Value not found")
