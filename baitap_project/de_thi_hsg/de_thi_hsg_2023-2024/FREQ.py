def main():
    # Mở file FREQ.INP và đọc dữ liệu
    with open('FREQ.INP', 'r') as f:
        n = int(f.readline())  # Đọc số lượng phần tử
        arr = list(map(int, f.readline().split()))  # Đọc dãy số

    # Tạo từ điển để đếm tần suất xuất hiện của các số
    freq = {}

    for num in arr:
        if num in freq:
            freq[num] += 1  # Tăng tần suất nếu số đã xuất hiện
        else:
            freq[num] = 1  # Khởi tạo tần suất là 1 nếu số chưa xuất hiện

    # Tìm số có tần suất lớn nhất, nếu có nhiều số có tần suất như nhau, chọn số lớn nhất
    max_freq = -1
    max_num = -1
    for num, count in freq.items():
        if count > max_freq or (count == max_freq and num > max_num):
            max_freq = count
            max_num = num

    # Lưu kết quả vào FREQ.OUT
    with open('FREQ.OUT', 'w') as f_out:
        f_out.write(f"{max_num} {max_freq}\n")

# Gọi hàm main để chạy chương trình
main()
