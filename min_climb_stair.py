from python_library import array_input

stair = array_input()
cost = 0
n = len(stair)
if stair[0] + 1 < stair[1]:
    start = 0
else:
    start = 1
for i in range(start,n):
    if stair