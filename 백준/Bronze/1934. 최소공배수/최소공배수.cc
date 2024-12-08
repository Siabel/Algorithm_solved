#include <iostream>
using namespace std;

int solve(int A, int B) {
	int r = A % B;
	if (r == 0) {
		return B;
	}
	else {
		return solve(B, r);
	}
}

int main() {
	int t;
	int a, b;
	int lcd;

	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> a >> b;

		lcd = (a * b) / (solve(a, b));
		cout << lcd << "\n";
	}

	return 0;
}