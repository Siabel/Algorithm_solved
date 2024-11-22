#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false); 
  cin.tie(NULL); cout.tie(NULL);

  int n, c, coor, res;
  cin >> n >> c;
  vector<int> vec;

  for(int i = 0; i < n; i++){
    cin >> coor;
    vec.push_back(coor);
  }

  sort(vec.begin(), vec.end());

  int start = 1;
  int end = vec[n - 1] - vec[0] + 1;

  while(start <= end){
    int mid = (start + end) / 2;
    int cnt = 1;
    int idx = vec[0];

    for(int i = 0; i < n; i++){
      if(idx + mid <= vec[i]){
        idx = vec[i];
        cnt++;
      }
    }

    if(cnt < c)
      end = mid - 1;
    else{
      res = mid;
      start = mid + 1;
    }
  }

  cout << res;
  return 0;
}