#include <iostream>
#include <fstream>
using namespace std;

void quicksort(int arr[], int l, int r){
    int i = l;
    int j = r;
    int pivot = arr[(l + r) / 2];

    while(i <= j){
        while(arr[i] < pivot) i++;
        while(arr[j] > pivot) j--;

        if(i <= j){
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            i++;
            j--;
        }
    }

    if(l < j) quicksort(arr, l, j);
    if(i < r) quicksort(arr, i, r);
}

int main(){
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    int n;
    int j = 0;
    fin >> n;
    int arr[100000];

    while(fin>>arr[j]){
        j ++;
    }

    quicksort(arr, 0, n-1);

    for(int i = 0;i < n;i++){
        fout << arr[i] << " ";
    }
}
