#include <iostream>
#include <queue>
#include <vector>

using namespace std;

struct cmp
{
  bool operator()(int a, int b){
    if(abs(a) == abs(b))
      return a > b;
    return abs(a) > abs(b);
  }
};

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int n, x;
  cin >> n;
  priority_queue<int, vector<int>, cmp> pq;

  for(int i = 0; i < n; i++){
    cin >> x;
    if(x == 0){
      if(pq.empty())
        cout << 0;
      else{
        cout << pq.top();
        pq.pop();
      }
      cout << "\n";
    }
    else
      pq.push(x);
  }
  return 0;
}