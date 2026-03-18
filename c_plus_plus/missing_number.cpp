#include <iostream>
using namespace std;

int main(){
    long long n;
    cin >> n;

    long long* arr = new long long[n];
    long long ans = 0;

    for(int i = 0; i < n - 1; i++){
        cin >> arr[i];
    }

    long long a = n * (n + 1) / 2;

    for(int i = 0; i < n - 1; i++){
        ans += arr[i];
    }

    cout << (a - ans);

    delete[] arr;
}
