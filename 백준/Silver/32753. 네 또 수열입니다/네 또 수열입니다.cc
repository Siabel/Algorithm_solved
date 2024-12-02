#include <iostream>
#include <vector>
using namespace std;

int n, k;

void init(){
  ios::sync_with_stdio(false);
  cin.tie(0); cout.tie(0);

  cin >> n >> k;
}

void solve(){
  if(n == 1){
    for(int i = 0; i < k; i++)
      cout << "1 ";
  }
  else if(n == 2 && k == 1)
    cout << "1 2";
  else
    cout << "-1";
}

int main(){
  init();
  solve();
}