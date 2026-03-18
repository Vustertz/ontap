with open('input.txt','r') as f:
    k = int(f.readline())

i = (k+2)//2
round(i)
print(i*(i-1)//2 + (k-i) +1)