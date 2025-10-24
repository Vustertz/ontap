def bang_cuu_chuong():
    n = int(input())
    with open("output.txt","w",encoding="utf-8") as f:
        for i in range(1, n + 1):
            f.write(f"bang cuu chuong {i}: " + "\n")
            for j in range(1, n + 1):
                f.write(f"{i} * {j} = {i*j}" + "\n")
bang_cuu_chuong()
                



