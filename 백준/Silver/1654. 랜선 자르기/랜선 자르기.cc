#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
  ios_base::sync_with_stdio(0); 
  cin.tie(NULL); cout.tie(NULL);

  int k, n, cnt;
  int max_len = -1;
  cin >> k >> n;

  vector<int> vec(k);
  for(int i = 0 ; i < k ; i++){
    cin >> vec[i];
    max_len = max(max_len, vec[i]);
  }

  long long start = 1;
  long long end = max_len;
  long long mid = (start + end) / 2;

  while(start <= end){
    cnt = 0;

    for(int i = 0 ; i < k ; i++){
      cnt += vec[i] / mid;
    }

    if(cnt >= n){
      start = mid + 1;
    }
    else{
      end = mid - 1;
    }
    mid = (start + end) / 2;

  }

  cout << mid;

  return 0;
}