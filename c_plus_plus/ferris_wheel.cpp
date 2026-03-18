#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int n,a,l,r,ans;
    cin >> n >> a;
    r = n - 1,l = 0,ans = 0;

    int* arr = new int[n];
    for(int i = 0;i < n;i++){
        cin >> arr[i];
    }

    sort(arr,arr + n);

    while(l <= r){
        if(arr[l] + arr[r] <= a){
            l += 1;
        }
        r -= 1;
        ans += 1;
    }

    cout << ans;
}
