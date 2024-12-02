#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int n, l, r, num;
vector<int> v;
bool check = true;

void init(){
  ios::sync_with_stdio(false);
  cin.tie(0); cout.tie(0);
  
  cin >> n >> l >> r;
  for(int i = 0; i < n; i++){
    cin >> num;
    v.push_back(num);
  }
}

void sequence_check(){
  sort(v.begin() + l - 1 , v.begin() + r);

  for(int i = 0; i < n - 1; i++){
    if(v[i] > v[i + 1]){
      check = false;
      break;
    }
  }
}

int main(){
  init();
  sequence_check();

  if(check)
    cout << "1";
  else
    cout << "0";
}