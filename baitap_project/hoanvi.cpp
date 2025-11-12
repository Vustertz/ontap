#include <bits/stdc++.h>
using namespace std;

void hoan_vi(vector<int> &arr, int i) {
    // Nếu đã đến phần tử cuối cùng, in ra dãy
    if (i == arr.size() - 1) {
        for (int x : arr) cout << x << " ";
        cout << endl;
        return;
    }

    // Duyệt qua các phần tử từ i đến hết
    for (int j = i; j < arr.size(); j++) {
        swap(arr[i], arr[j]);          // Hoán đổi
        hoan_vi(arr, i + 1);           // Đệ quy
        swap(arr[i], arr[j]);          // Hoàn tác (quay lui)
    }
}

int main() {
    int n;
    cout << "Nhap so luong phan tu: ";
    cin >> n;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cout << "Nhap phan tu thu " << i + 1 << ": ";
        cin >> arr[i];
    }

    cout << "\nTat ca cac hoan vi la:\n";
    hoan_vi(arr, 0);

    return 0;
}
