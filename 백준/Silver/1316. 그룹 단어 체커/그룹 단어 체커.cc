#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>
using namespace std;

int n, cnt = 0;
string word;


void init(){
  ios::sync_with_stdio(false);
  cin.tie(0); cout.tie(0);

  cin >> n;

}

void check(string Word){
  vector<char> v;
  int len = Word.length();
  for(int i = 0; i <= len - 1; i++){
    if(Word[i] != Word[i + 1]){
      if(find(v.begin(), v.end(), Word[i]) != v.end())
        return;
      else
        v.push_back(Word[i]);
    }
  }

  cnt++;
}

int main(){
  init();

  for(int i = 0; i < n; i++){
    cin >> word;
    check(word);
  }

  cout << cnt;
}