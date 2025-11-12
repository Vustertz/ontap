def bang_cuu_chuong():
    try:
        n = int(input())
        if n <= 0:
            print("hay nhap so lon hon 0")
            return
        with open("output.txt","w",encoding="utf-8") as f:
            for i in range(1, n + 1):
                f.write(f"bang cuu chuong {i}: " + "\n")
                for j in range(1, n + 1):
                    f.write(f"{i} * {j} = {i*j}" + "\n")
    except ValueError:
        print("hay nhap 1 so nguyen vao")
bang_cuu_chuong()
                



