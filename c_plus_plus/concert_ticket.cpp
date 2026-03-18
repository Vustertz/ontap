#include <iostream>
#include <algorithm>
using namespace std;

const int MAXN = 200005;

int parent[MAXN];
int tickets[MAXN];

int find(int x){
    if(x < 0){
        return -1;
    }
    if(parent[x] == x){
        return x;
    }
    return parent[x] = find(parent[x]);
}

int main(){
    int n, m;
    cin >> n >> m;

    for(int i = 0; i < n; i++){
        cin >> tickets[i];
    }

    sort(tickets, tickets + n);

    for(int i = 0; i < n; i++){
        parent[i] = i;
    }

    while(m--){
        int x;
        cin >> x;

        int pos = upper_bound(tickets, tickets + n, x) - tickets - 1;

        int available = find(pos);

        if(available < 0){
            cout << -1 << "\n";
        }else{
            cout << tickets[available] << "\n";
            parent[available] = find(available - 1);
        }
    }
}
