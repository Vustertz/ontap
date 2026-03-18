#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int m,n,k,l,r,ans;
    l = 0,r = 0,ans = 0;
    cin >> m >> n >> k;

    long long* apartment = new long long[m];
    long long* appliant = new long long[n];

    for(int i = 0;i < m;i++){
        cin >> apartment[i];
    }

    for(int i = 0;i < n;i++){
        cin >> appliant[i];
    }

    sort(apartment, apartment + m);
    sort(appliant, appliant + n);

    while(l < m && r < n){
        if(appliant[r] > apartment[l] + k){
            l += 1;
            continue;
        }else if(appliant[r] < apartment[l] - k){
            r += 1;
            continue;
        }
        ans += 1;
        l += 1;
        r += 1;
    }

    cout << ans;
}
