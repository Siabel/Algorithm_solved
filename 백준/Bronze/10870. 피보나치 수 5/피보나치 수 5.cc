#include <iostream>
using namespace std;

int n;

void init(){
  ios::sync_with_stdio(false);
  cin.tie(0); cout.tie(0);

  cin >> n;
}
int solve(int n) {
	if (n == 0) {
		return 0;
	}
	else if (n == 1) {
		return 1;
	}
	else {
		return solve(n - 1) + solve(n - 2);
	}
}

int main() {
	init();

	cout << solve(n) << "\n";
}