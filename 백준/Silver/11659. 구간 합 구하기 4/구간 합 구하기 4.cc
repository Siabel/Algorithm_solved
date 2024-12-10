#include <iostream>
#define MAX 100001

using namespace std;

int n, m;
int arr[MAX];

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  cin >> n >> m;

  for(int i = 0; i < n; i++)
    cin >> arr[i];
  
  for(int i = 1; i <= n; i++)
    arr[i] += arr[i-1];

  for(int i=0;i<m;i++) {
    int x, y;
    cin >> x >> y;

    cout << arr[y - 1] - arr[x - 2] << "\n";
  }
}