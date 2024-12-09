#include <iostream>
#include <vector>

using namespace std;


int main(){
  ios::sync_with_stdio(false);
  cin.tie(0); cout.tie(0);

  int n;
  vector<int> v, res;

  cin >> n;
  v.resize(n), res.resize(n);
  for(int i = 0; i < n; i++)
    cin >> v[i];
    
  for(int i = 0; i < n; i++){
    int j = 0;
    while(v[i] != 0){
      if(res[j] == 0){
        v[i]--;
      }
      j++;
    }
    while(res[j] != 0){
      j++;
    }
    res[j] = i + 1;
  }

  for(int i = 0; i < n; i++)
    cout << res[i] << " ";

  return 0;
}