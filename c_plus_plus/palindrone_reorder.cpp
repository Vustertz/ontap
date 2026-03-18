#include <iostream>
#include <map>
using namespace std;

int main(){
    string s;
    char keyval = 0;
    int time = 0;
    map<char,int> dictionary;

    cin >> s;

    for(auto i:s){
        dictionary[i] += 1;
    }

    for(auto i:dictionary){
        if(i.second % 2 == 1){
            keyval = i.first;
            time += 1;
        }
    }

    if(time > 1){
        cout << "NO SOLUTION";
    }else{
        string res,mid = "";
        if(keyval){
            for(int i = 0; i < dictionary[keyval]; i++){
                mid += keyval;
            }
            dictionary[keyval] = 0;
        }

        string left = "",right = "";
        for(auto i:dictionary){
            for(int j = 0; j < (i.second / 2);j++){
                left += i.first;
            }
        }

        for(int i = left.length() - 1;i >= 0;i--){
            right += left[i];
        }

        cout << left << mid << right;

    }
}
