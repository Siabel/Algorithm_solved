#include <iostream>
#include <queue>
#define MAX 1001
using namespace std;

int n, w, l;
int truck[MAX];
queue<int> bridge;
int sum = 0;
int cnt = 0;

void init(){
  ios::sync_with_stdio(false);
  cin.tie(0), cout.tie(0);

  cin >> n >> w >> l;

  for(int i = 0; i < n; i++){
    cin >> truck[i];
  }
}

void solve(){
  for(int i = 0; i < n; i++){
    while(true){
      if(bridge.size() == w){
        sum -= bridge.front();
        bridge.pop();
      }
      if(truck[i] + sum <= l)
        break;
      else{
        bridge.push(0);
        cnt++;
      }
    }
    bridge.push(truck[i]);
    sum += truck[i];
    cnt++;
  }
}

int main(){
  init();
  solve();

  cout << cnt + w;
  return 0;
}