def tongchuso(string):
    n = 0
    for i in string:
        n += int(i)
    return n

string = str(input())
print(tongchuso(string))
