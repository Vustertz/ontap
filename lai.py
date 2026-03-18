saving = int(input())
time = int(input())
interest = float(input())
print(saving, time, interest)
s = 0
for i in range(time):
    s = s * interest + saving
    if(i%12 == 11):
        print(f"year {i//12 + 1}")
    print(s)