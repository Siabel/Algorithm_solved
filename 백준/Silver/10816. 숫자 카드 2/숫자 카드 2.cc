#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL); cout.tie(NULL);

  vector<int> vec;
  int n, m, num, find_num;
  cin >> n;

  for(int i = 0; i < n; i++){
    cin >> num;
    vec.push_back(num);
  }

  sort(vec.begin(), vec.end());
  cin >> m;

  for(int i = 0; i < m; i++){
    cin >> find_num;
    
    cout << upper_bound(vec.begin(),vec.end(), find_num) - lower_bound(vec.begin(), vec.end(), find_num)<< " ";
  }
  return 0;
}