#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  
  priority_queue<int, vector<int>> q;
  
  int n;
  cin >> n;

  for(int i = 0; i < n; i++){
    int x;
    cin >> x;
    if(x == 0){
      if(q.empty())
        cout << '0';
      else{
        int a = q.top();
        cout << a;
        q.pop();        
      }
      cout << "\n";
    }
    else{
      q.push(x);
    }

  }
  return 0;
}