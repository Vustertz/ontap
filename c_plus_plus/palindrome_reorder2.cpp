#include <iostream>
using namespace std;

int main(){

    string s;
    cin >> s;

    int freq[26] = {0};

    for(char c : s){
        freq[c - 'A']++;
    }

    int odd = 0;
    int key = -1;

    for(int i = 0; i < 26; i++){
        if(freq[i] % 2){
            odd++;
            key = i;
        }
    }

    if(odd > 1){
        cout << "NO SOLUTION";
        return 0;
    }

    string left = "", mid = "";

    if(key != -1){
        mid.append(freq[key], char(key + 'A'));
        freq[key] = 0;
    }

    for(int i = 0; i < 26; i++){
        for(int j = 0; j < freq[i] / 2; j++){
            left += char(i + 'A');
        }
    }

    string right = "";

    for(int i = left.length()-1; i >= 0; i--){
        right += left[i];
    }

    cout << left << mid << right;
}
