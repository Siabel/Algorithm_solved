#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <cstring>

using namespace std;

int n;
int volume = 2;
int cnt = 0, res = 0;
int x, y;
int board[21][21];
int visited[21][21] = {};

int dx[4] = {0, -1, 0, 1};
int dy[4] = {1, 0, -1, 0};

struct Fish{
  int x;
  int y;
  int value;
};

vector<Fish> v;

bool cmp(const Fish& a, const Fish& b) {
  if (a.value == b.value) {
    if (a.x == b.x) {
      return a.y < b.y;
    }
    return a.x < b.x;
  }
  return a.value < b.value;
}

void init(){
  ios_base::sync_with_stdio(false); 
  cin.tie(NULL); cout.tie(NULL);
  
  cin >> n;

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      cin >> board[i][j];
      
      if (board[i][j] == 9) {
        x = i;
        y = j;
        board[i][j] = 0;
      }
    }
  }
}

bool check(int x, int y){
  if(x < 0 || y < 0 || x >= n || y >= n || visited[x][y] || board[x][y] > volume)
    return true;
  return false;
}

int bfs(int a, int b){
  v.clear();
  memset(visited, 0, sizeof(visited));


  queue<pair<int, int>> q;
  visited[a][b] = 0;
  q.push({a, b});

  while(!q.empty()){
    auto cur = q.front();
    q.pop();

    for(int i = 0; i < 4; i++){
      int nx = dx[i] + cur.first;
      int ny = dy[i] + cur.second;

      if(check(nx, ny))
        continue;
      
      if(board[nx][ny] > 0 && board[nx][ny] < volume){
        Fish fish;
        fish.x = nx;
        fish.y = ny;
        fish.value = visited[cur.first][cur.second] + 1;
        v.push_back(fish);
      }

      q.push({nx, ny});
      visited[nx][ny] = visited[cur.first][cur.second] + 1;
    }
  }

  if (!v.empty()) {
    sort(v.begin(), v.end(), cmp);
    auto n = v[0];

    x = n.x;
    y = n.y;
    res += n.value;
    cnt++;
    board[x][y] = 0;
    
    if (cnt == volume) {
      cnt = 0;
      volume++;
    }
    return 1;
  }
  else {
    return 0;
  }
}

int main() {
  init();
  
  while(true){
    int temp = bfs(x, y);
    if(temp == 0)
      break;
  }

  cout << res;
}