#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  vector<int> vec;  
  int n, m, num;
  cin >> n;

  for(int i = 0; i < n; i++){
    cin >> num;
    vec.push_back(num);
  }

  sort(vec.begin(), vec.end());

  cin >> m;
  for(int i = 0; i < m; i++){
    cin >> num;

    bool find = binary_search(vec.begin(), vec.end(), num);
    cout << find << "\n";
  }
  return 0;
}