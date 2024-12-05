#include <iostream>
using namespace std;

int cnt;
int n;
string temp;

void init(){
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  
  cin >> n;
}

int recursion(string &s, int l, int r){ 
  ::cnt++;
  if(l >= r) return 1;
  else if(s[l] != s[r]) return 0;
  else return recursion(s, l+1, r-1);
}

int isPalindrome(string &s){ 
  return recursion(s, 0, s.length() - 1);
}

int main(){
  init();
  
  while (n--) {
    ::cnt = 0;
    cin >> temp;
    cout << isPalindrome(temp) << " " << ::cnt << '\n';
  }
}