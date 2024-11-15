#include <iostream>
using namespace std;
#define MAX 101

int paper[MAX][MAX] = {};

int main() {
  int n, r, c;
  int cnt = 0;
  cin >> n;

  for(int t = 0; t < n; t++){
    cin >> r >> c;

    for(int i = r; i < r + 10; i++){
      for(int j = c; j < c + 10; j++){
        paper[i][j] = 1;
      }
    }
  }

  for(int i = 0; i < MAX; i++){
    for(int j = 0; j < MAX; j++){
      if(paper[i][j])
        cnt++;
    }
  }

  cout << cnt;

  return 0;
}