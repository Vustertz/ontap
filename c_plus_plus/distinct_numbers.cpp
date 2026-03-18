#include <iostream>
#include <map>
using namespace std;

int main(){
    int n;
    cin >> n;
    long long* arr = new long long[n];
    map<int,int> dict;

    for(int i = 0;i < n;i++){
        cin >> arr[i];
        dict[arr[i]] += 1;
    }

    cout << dict.size();

}
