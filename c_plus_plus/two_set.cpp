#include <iostream>
using namespace std;

int main(){
    long long n;
    cin >> n;

    long long total = n*(n+1)/2;

    if(total % 2 != 0){
        cout << "NO";
        return 0;
    }

    cout << "YES" << endl;

    long long sum = total/2;

    long long arr1[n], arr2[n];
    long long t = 0, j = 0;

    for(int i = n; i >= 1; i--){
        if(sum >= i){
            arr1[t++] = i;
            sum -= i;
        }else{
            arr2[j++] = i;
        }
    }

    cout << t << endl;
    for(int i = 0; i < t; i++){
        cout << arr1[i] << " ";
    }

    cout << endl << j << endl;

    for(int i = 0; i < j; i++){
        cout << arr2[i] << " ";
    }
}
