#include <iostream>
#include <queue>
#define MAX 201
using namespace std;

int n, a, b, c, d;
int board[MAX][MAX] = {};
bool visited[MAX][MAX];
queue<pair<int, int>> q;
int dx[] = {-2,-2,0,0,2,2};
int dy[] = {-1,1,-2,2,-1,1};

void BFS(int x, int y) {
  visited[x][y] = true;
  q.push(make_pair(x, y));

  while (!q.empty()) {
    x = q.front().first;
    y = q.front().second;
    q.pop();

    for (int i = 0; i < 6; i++) {
      int nx = x + dx[i];
      int ny = y + dy[i];

      if (ny < 0 || nx < 0 || ny > n || nx > n)
        continue;
      if (!visited[nx][ny]) {
        visited[nx][ny] = true;
        board[nx][ny] = board[x][y] + 1;
        q.push(make_pair(nx, ny));
      }
    }
  }
}
 
int main() {
  cin >> n >> a >> b >> c >> d;

  BFS(a, b);
  
  if (board[c][d] == 0)
    cout << -1;
  else
    cout << board[c][d];
}