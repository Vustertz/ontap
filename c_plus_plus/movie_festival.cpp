#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int n,ans = 0,curr_end = 0;
    cin >> n;

    pair<int,int> arr[n];

    for(int i = 0;i < n;i++){
        cin >> arr[i].second >> arr[i].first;
    }

    sort(arr,arr + n);

    for(int i = 0;i < n;i++){
        if(curr_end <= arr[i].second){
            curr_end = arr[i].first;
            ans += 1;
        }
    }

    cout << ans;
}
