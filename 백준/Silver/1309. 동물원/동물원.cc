#include <iostream>
#define MAX 100001
using namespace std;

int n;
int dp[MAX] = {1, 3};

void solve(){
  for(int i = 2; i <= n; i++)
    dp[i] = (dp[i - 1] * 2 + dp[i - 2]) % 9901;
}

int main() {
  ios_base::sync_with_stdio(false); 
  cin.tie(NULL); cout.tie(NULL);

  cin >> n;

  solve();

  cout << dp[n] % 9901;
  return 0;
}