#include <iostream>
#include <algorithm>
using namespace std;

string s;
int n;
bool used[8] = {false};
string res[40320];
int idx = 0;

void backtrack(string path){

    if(path.length() == n){
        res[idx++] = path;
        return;
    }

    for(int i = 0; i < n; i++){

        if(used[i]){
            continue;
        }

        if(i > 0 && s[i] == s[i-1] && !used[i-1]){
            continue;
        }

        used[i] = true;
        path += s[i];

        backtrack(path);

        path.pop_back();
        used[i] = false;
    }
}

int main(){

    cin >> s;

    sort(s.begin(), s.end());

    n = s.length();

    backtrack("");

    cout << idx << endl;

    for(int i = 0; i < idx; i++){
        cout << res[i] << endl;
    }
}
