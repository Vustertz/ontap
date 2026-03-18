def prime():
    def prime_check(i):
        if i < 2:
            return False
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                return False
        return True
    
    with open('PRIME.INP', 'r') as f:
        n = f.readline()
    check = 0

    for i in n:
        if i.isdigit():
            if prime_check(int(i)):
                check += int(i)
    with open('PRIME.OUT','w') as f:
        f.write(str(check))

prime()
        




