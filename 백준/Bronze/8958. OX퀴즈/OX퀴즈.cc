#include <iostream>
using namespace std;

int main() {
	int t;
	string s;
	int score;
	int cnt;

	cin >> t;

	for (int i = 0; i < t; i++) {
		cin >> s;
		
		score = 0;
		cnt = 1;

		for (int i = 0; i < s.length(); i++) 
        {
			if (s[i] == 'O') 
                score += cnt++;
			else if (s[i] == 'X') 
                cnt = 1;
		}
		cout << score << endl;
	}
	return 0;
}