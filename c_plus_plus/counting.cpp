#include <iostream>
#include <map>
using namespace std;

int main(){
    map<int,int> dictionary;

    int n,a;
    cin >> n;

    int* arr = new int[n];

    for(int i = 0; i < n; i++){
        cin >> a;
        dictionary[a] += 1;
    }

    for(auto j : dictionary){
        cout << j.first << " " << j.second << endl;
    }

    delete[] arr;
}
