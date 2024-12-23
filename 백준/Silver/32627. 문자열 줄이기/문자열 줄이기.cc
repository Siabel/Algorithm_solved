#include <iostream>
using namespace std;

int n, m, cnt[26] = {}, usecnt[26] = {};
string s, res;

void init(){
  ios_base::sync_with_stdio(false); 
  cin.tie(NULL); cout.tie(NULL);

  cin >> n >> m;
  cin >> s;

  for(const char &c : s){
    cnt[c - 'a']++;
  }
}

void solve(){
  for (int i = 0; i < 26; i++) {
    if (cnt[i] > m) {
      usecnt[i] = m;
      break;
    } 
    else {
      usecnt[i] = cnt[i];
      m -= cnt[i];
    }
  }

  for (const char &c : s) {
    if(usecnt[c - 'a']-- > 0) {
      continue;
    }

    res += c;
  }
}

int main() {
  init();
  solve();

  cout << res << "\n";
  return 0;
}