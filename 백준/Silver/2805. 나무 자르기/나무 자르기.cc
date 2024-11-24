#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false); 
  cin.tie(NULL); cout.tie(NULL);

  int n, h, m;
  vector<int> tree;

  cin >> n >> m;

  for(int i = 0; i < n; i++){
    cin >> h;
    tree.push_back(h);
  }

  sort(tree.begin(), tree.end());

  long long start = 0;
  long long end = *max_element(tree.begin(), tree.end());
  int res = 0;

  while(start <= end){
    long long cnt = 0;
    int mid = (start + end) / 2;

    for(int i = 0; i < n; i++) {
      if(tree[i] - mid > 0) 
        cnt += tree[i] - mid;
      }
      
      if(cnt >= m){
        res = mid;
        start = mid + 1;
      } 
      else{
        end = mid - 1;
      }
  }

  cout << res;
  return 0;
}