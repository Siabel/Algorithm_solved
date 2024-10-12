#include <iostream>
using namespace std;

int main() {
    cout << fixed;

	int n;
	int score[1001] = {};
	
    double res = 0;
    int max = 0;
	
    cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> score[i];
		if (score[i] > max)
			max = score[i];
		res += score[i];
	}
	
    res = (res / max * 100) / n;

	cout.precision(3);
    
	cout << res << endl;
}