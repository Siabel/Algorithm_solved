#include <iostream>
#define MAX_VAL 101
#include <stack>

using namespace std;

int n, m;
int farm[MAX_VAL][MAX_VAL];
int visited[MAX_VAL][MAX_VAL];
int dx[] = {0, -1, -1, -1, 0, 1, 1, 1};
int dy[] = {-1, -1, 0, 1, 1, 1, 0, -1};

bool is_top(int r, int c)
{
  int now_height = farm[r][c];
  stack<pair<int, int>> stack;
  bool flag = true;

  pair<int, int> tmp;

  stack.push(make_pair(r, c));

  while (!stack.empty()) {
    tmp.first = stack.top().first;
    tmp.second = stack.top().second;
    stack.pop();

    for (int i=0; i<8; i++){
      int nr = tmp.first + dx[i];
      int nc = tmp.second + dy[i];
      if (0 <= nr && nr < n && 0 <= nc && nc < m){
        if (!visited[nr][nc] && farm[nr][nc] == now_height) {
          stack.push(make_pair(nr, nc));
          visited[nr][nc] = 1;
        }
        else if (farm[nr][nc] > now_height)
        {
          flag = false;
        }
        
      }
    }
  }
  return flag;
}

int main()
{
  ios_base::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);

  cin >> n >> m;

  for (int i=0; i<n; i++) {
    for(int j=0; j<m; j++) {
      cin >> farm[i][j];
      visited[i][j] = 0;
    }
  }
  
  int cnt = 0;

  for (int i=0; i<n; i++){
    for (int j=0; j<m; j++){
      if (!visited[i][j] && is_top(i, j)){
        cnt ++;
      }
    }
  }

  cout << cnt << endl;

  return 0;
}