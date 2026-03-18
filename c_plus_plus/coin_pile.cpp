#include <iostream>
using namespace std;

int main(){
    int n,a,b;
     cin >> n;

     for(int i = 0;i < n;i++){
        cin >> a >> b;
        if((a + b)%3 == 0 && max(a,b) <= min(a,b)*2){
            cout << "YES" << endl;
        }else{
            cout << "NO" << endl;
        }
     }
}
