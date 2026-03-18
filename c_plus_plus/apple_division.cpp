#include <iostream>
#include <cmath>
using namespace std;

long long n,min_dif,total;
long long arr[20];

void dfs(int i,long long sum1){
    if(i == n){
        long long sum2 = total - sum1;
        long long dif = abs(sum1 - sum2);
        if(dif < min_dif){
            min_dif = dif;
        }
        return;
    }

    dfs(i + 1,sum1 + arr[i]);
    dfs(i + 1,sum1);
}

int main(){
    cin >> n;
    for(int i = 0;i < n;i++){
        cin >> arr[i];
        total += arr[i];
    }
    min_dif = total;

    dfs(0,0);
    cout << min_dif;

}
