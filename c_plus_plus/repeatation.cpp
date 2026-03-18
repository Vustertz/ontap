#include <iostream>
using namespace std;

int main(){
    string s;
    cin >> s;

    int ans = 1;
    int cur = 1;

    for(int i = 0; i < s.length(); i++){
        if(s[i] == s[i+1]){
            cur++;
        }else{
            cur = 1;
        }

        if(cur > ans){
            ans = cur;
        }
    }

    cout << ans;
}
