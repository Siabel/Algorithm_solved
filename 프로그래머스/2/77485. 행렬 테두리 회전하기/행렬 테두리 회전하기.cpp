#include <string>
#include <vector>

using namespace std;

int map[110][110];

int Min(int A, int B) { return A < B ? A : B; }


int Turning(int x, int y, int xx, int yy)
{
  int min_num;
  int start = map[x][y];
  min_num = start;
  for (int i = x; i < xx; i++)
  {
    min_num = Min(min_num, map[i][y]);
    map[i][y] = map[i + 1][y];
  }
  for (int i = y; i < yy; i++)
  {
    min_num = Min(min_num, map[xx][i]);
    map[xx][i] = map[xx][i + 1];
  }
  for (int i = xx; i > x; i--)
  {
    min_num = Min(min_num, map[i][yy]);
    map[i][yy] = map[i - 1][yy];
  }
  for (int i = yy; i > y; i--)
  {
    min_num = Min(min_num, map[x][i]);
    map[x][i] = map[x][i - 1];
  }
  map[x][y + 1] = start;
  return min_num;
}

vector<int> solution(int rows, int columns, vector<vector<int>> queries) 
{
  vector<int> ans;
  int Num = 1;

  for (int i = 0; i < rows; i++)
  {
    for (int j = 0; j < columns; j++)
    {
      map[i][j] = Num++;
    }
  }
  
  for (int i = 0; i < queries.size(); i++)
  {
    int x = queries[i][0]; x--;
    int y = queries[i][1]; y--;
    int xx = queries[i][2]; xx--;
    int yy = queries[i][3]; yy--;

    ans.push_back(Turning(x, y, xx, yy));
  }

  return ans;
}