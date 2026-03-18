#include <iostream>
using namespace std;

void sum(int i, int k, int n, int sub[], int arr[]){
    if(i == n){
        for(int j = 0; j < k; j++){
            cout << sub[j] << " ";
        }
        cout << endl;
        return;
    }

    sub[k] = arr[i];
    sum(i + 1, k + 1, n, sub, arr);

    sum(i + 1, k, n, sub, arr);
}

int main(){
    int n;
    cin >> n;

    int* arr = new int[n];
    int* sub = new int[n];

    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }

    sum(0, 0, n, sub, arr);

    delete[] arr;
    delete[] sub;
}
