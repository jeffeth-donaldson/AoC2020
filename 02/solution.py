def getInput(file):
    f = open(file)
    lines = f.readlines()
    f.close()
    return lines

def validatePassword(rule,password):
    """Checks validity of password against supplied rule
    X-Y a: where X is the minimum occurances of a, and Y is the maximum"""
    min = ""
    max = ""
    target = ""
    foundMin = False
    for i in range(len(rule)):
        if not foundMin:
            if rule[i] == "-":
                foundMin = True
            else:
                min += rule[i]
        else:
            if rule[i] == " ":
                target = rule[i+1]
                break
            else:
                max += rule[i]
    count = 0
    while target in password:
        count += 1
        password = password.replace(target, '',1)
    if count >= int(min) and count <= int(max):
        return True
    else:
        return False

def validCount(passwords):
    """Returns the amount of valid passwords in a list"""
    valid = 0
    for password in passwords:
        rulepass = password.split(":")
        if validatePassword(rulepass[0],rulepass[1]):
            valid += 1
    return valid

if __name__ == "__main__":
    lines = getInput("input")
    count = validCount(lines)
    print(count)
