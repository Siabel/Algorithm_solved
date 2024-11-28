#include <iostream>
using namespace std;

int board[19][19];
int dx[4] = {1, 0, 1, -1};
int dy[4] = {0, 1, 1, 1};

void init() {
  ios_base::sync_with_stdio(false); 
  cin.tie(NULL); cout.tie(NULL);

  for (int i = 0; i < 19; i++) {
    for (int j = 0; j < 19; j++) {
      cin >> board[i][j];
    }
  }
}

bool check(int x, int y, int player, int& startX, int& startY) {
  for (int d = 0; d < 4; d++) {
    int cnt = 1;
    int nx = x + dx[d], ny = y + dy[d];
    int sx = x, sy = y;

    while (nx >= 0 && ny >= 0 && nx < 19 && ny < 19 && board[nx][ny] == player) {
      cnt++;
      nx += dx[d];
      ny += dy[d];
    }

    nx = x - dx[d], ny = y - dy[d];
    while (nx >= 0 && ny >= 0 && nx < 19 && ny < 19 && board[nx][ny] == player) {
      sx = nx;
      sy = ny;
      cnt++;
      nx -= dx[d];
      ny -= dy[d];
    }

    if (cnt == 5) {
      startX = sx;
      startY = sy;
      return true;
    }
  }
  return false;
}

void dfs() {
  for (int i = 0; i < 19; i++) {
    for (int j = 0; j < 19; j++) {
      if (board[i][j] != 0) {
        int startX = 0, startY = 0;
        if (check(i, j, board[i][j], startX, startY)) {
          cout << board[i][j] << "\n" << startX + 1 << " " << startY + 1;
          return;
        }
      }
    }
  }
  cout << 0 << endl;
}

int main() {
  init();
  dfs();
  return 0;
}
