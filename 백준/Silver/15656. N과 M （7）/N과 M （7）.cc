#include <iostream>
#include <algorithm>
#define MAX 9
using namespace std;

int n, m;
int arr[MAX];
int save[MAX];
bool visited[MAX] = {};

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
  }
  else{
    for(int i = 0; i < n; i++){
      visited[i] = true;
      arr[idx] = save[i];
      solve(idx + 1);
      visited[i] = false;
    }
  }
}

int main() {
  init();
  solve(0);

  return 0;
}