#include <iostream>
#include <algorithm>
using namespace std;

int n;
int x;
int arr[100001];

void init(){
  ios_base::sync_with_stdio(false); 
  cin.tie(NULL); cout.tie(NULL);
  
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	cin >> x;
	sort(arr, arr + n);
}

void solve(){	
	int start = 0;
	int end = n - 1;
	int res = 0;
	while (start < end) {
		if(arr[start] + arr[end] == x){
			res++;
			end--;
		} 
    else if(arr[start] + arr[end] > x){
			end--;
		} 
    else{
			start++;
		}
	}
	
	cout << res;
}

int main() {
  init();
  solve();
  return 0;
}