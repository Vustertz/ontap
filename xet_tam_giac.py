def is_triangle():
    with open('xet_tam_giac.inp','r') as f:
        [a, b, c] = list(map(float, f.readline().split()))
    eps = 1e-10
    with open('xet_tam_giac.out','w') as f:
        if not (a + b > c and a + c > b and b + c > a):
            f.write("Khong phai tam giac")
            return
        if abs(a - b) < eps and abs(b - c) < eps:
            f.write("Tam giac deu")
            return
        if ((abs(a*a + b*b - c*c) < eps and abs(a - b) < eps) or (abs(a*a + c*c - b*b) < eps and abs(a - c) < eps) or (abs(b*b + c*c - a*a) < eps and abs(b - c) < eps)):
            f.write("Tam giac vuong can")
            return
        if abs(a - b) < eps or abs(a - c) < eps or abs(b - c) < eps:
            f.write("Tam giac can")
            return
        if (abs(a*a + b*b - c*c) < eps or abs(a*a + c*c - b*b) < eps or abs(b*b + c*c - a*a) < eps):
            f.write("Tam giac vuong")
            return
        f.write("Tam giac thuong")

is_triangle()
