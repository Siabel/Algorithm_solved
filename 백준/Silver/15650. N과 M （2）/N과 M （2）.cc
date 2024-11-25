#include <iostream>
#define MAX 9
using namespace std;

int n, m;
int arr[MAX];
int visited[MAX] = {};

void init(){
  ios_base::sync_with_stdio(false); 
  cin.tie(NULL); cout.tie(NULL);

  cin >> n >> m;
}

void solve(int num, int idx){
  if(idx == m){
    for(int i = 0; i < m; i++){
      cout << arr[i] << ' '; 
    }
    cout << "\n";
  }
  else{
    for(int i = num; i <= n; i++){
      if(!visited[i]){
        visited[i] = true;
        arr[idx] = i;
        solve(i + 1, idx + 1);
        visited[i] = false;
      }
    }
  }
}

int main() {
  init();
  solve(1, 0);

  return 0;
}