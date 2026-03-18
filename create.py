import random
import zipfile

# 1️⃣ Tham số
n = 10**6
k = random.randint(1, 1000)
c = (random.randint(1, 10**6) for _ in range(n))  # generator tiết kiệm RAM

# 2️⃣ Tạo file TUYETCHIEU.INP
inp_file = "TUYETCHIEU.INP"
with open(inp_file, "w") as f:
    f.write(f"{n} {k}\n")
    chunk_size = 10000
    buffer = []
    for idx, num in enumerate(c, 1):
        buffer.append(str(num))
        if idx % chunk_size == 0:
            f.write(" ".join(buffer) + "\n")
            buffer = []
    if buffer:
        f.write(" ".join(buffer) + "\n")

# 3️⃣ Tạo file ZIP
zip_file = "TUYETCHIEU.zip"
with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(inp_file, arcname=inp_file)

print(f"Đã tạo xong file ZIP '{zip_file}' chứa '{inp_file}' với n={n}, k={k}")
