#include <iostream>
#include <algorithm>
#define MAX 9
using namespace std;

int n, m;
int arr[MAX];
int save[MAX];

void init(){
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL); cout.tie(NULL);

    cin >> n >> m;
    for(int i = 0; i < n; i++){
        cin >> save[i];
    }
    sort(save, save + n);
}

void solve(int idx){
  if(idx == m){
        for(int i = 0; i < m; i++){
            cout << arr[i] << ' '; 
        }
        cout << "\n";
        return;
  }

  int last = 0;
  for(int i = 0; i < n; i++){
    if(save[i] != last){
        arr[idx] = save[i];
        last = save[i];
        solve(idx + 1);
    }
  }
}

int main() {
  init();
  solve(0);
  return 0;
}