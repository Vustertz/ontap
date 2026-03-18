#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int n,temp,ans;
    cin >> n;

    pair<int,int> arr[n * 2];
    temp = 0,ans = 0;

    for(int i = 0;i < n*2;i+= 2){
        cin >> arr[i].first;
        arr[i].second = 1;
        cin >> arr[i + 1].first;
        arr[i + 1].second = -1;
    }

    sort(arr,arr + n*2);

    for(int i = 0;i < n * 2;i++){
        temp += arr[i].second;
        if(temp > ans){
            ans = temp;
        }
    }
    cout << ans;
}
