#include <iostream>
using namespace std;

int main() {
	int t;
	int h, w, n;
	int res;
	cin >> t;

	for (int i = 0; i < t; i++) {
		cin >> h >> w >> n;

		if (n % h == 0) {
			res = h * 100 + (n / h);
		}
		else {
			res = (n % h) * 100 + (n / h) + 1;
		}
		cout << res << endl;
	}
}