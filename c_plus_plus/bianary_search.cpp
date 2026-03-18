#include <iostream>
#include <algorithm>
using namespace std;

int binary_search(int target, int arr[], int len){
    int l = 0, r = len - 1;

    while(l <= r){
        int m = (l + r) / 2;

        if(arr[m] > target){
            r = m - 1;
        }
        else if(arr[m] < target){
            l = m + 1;
        }
        else{
            return m;
        }
    }
    return -1;
}

int main(){
    int n, target;
    cin >> n >> target;

    int* arr = new int[n];

    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }

    sort(arr, arr + n);

    int res = binary_search(target, arr, n);
    cout << res;

    delete[] arr;
}
