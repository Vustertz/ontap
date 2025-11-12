def prime():
    def prime_check(i):
        if i < 2:
            return False
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                return False
        return True
    
    with open('PRIME.INP', 'r') as f:
        n = int(f.readline().strip())  
        ar = list(map(int, f.readline().split()))  
    check = []

    for i in range(n): 
        if prime_check(ar[i]):  
            if i == n - 1: 
                check.append(ar[i - 1])  
            else:
                check.append(ar[i + 1])  
    with open('PRIME.OUT', 'w') as f:
        f.write(' '.join(map(str, check))) 
prime()
