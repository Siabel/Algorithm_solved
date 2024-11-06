#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

// 메모리 초과
// int main(){
//   int n, x;
//   cin >> n;
//   vector<int> vec;

//   for(int i = 0; i < n; i++){
//     cin >> x;
//     vec.push_back(x);
//   }

//   sort(vec.begin(), vec.end());

//   for(int i = 0; i < n; i++){
//     cout << vec[i] << "\n";
//   }
  
//   return 0;
// }

// 메모리 초과
// int main(){
//   ios_base::sync_with_stdio(false);
//   cin.tie(NULL);
//   cout.tie(NULL);

//   int n, x;
//   priority_queue<int, vector<int>, greater<int>> q;
//   cin >> n;

//   for(int i = 0; i < n; i++){
//     cin >> x;
//     q.push(x);
//   }

//   while (!q.empty()) {
//     cout << q.top() << "\n";
//     q.pop();
//   }
// }

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int n, num;
  int arr[10001] = {};
  cin >> n;

  for(int i = 0; i < n; i++){
    cin >> num;
    arr[num]++;
  }

  for(int i = 0; i < 10001; i++){
    for(int j = 0; j < arr[i]; j++){
      cout << i << "\n";
    }
  }

  return 0;
}