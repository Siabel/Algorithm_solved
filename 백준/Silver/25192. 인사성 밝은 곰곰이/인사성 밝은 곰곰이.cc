#include <iostream>
#include <set>
using namespace std;

int main()
{
	int n, cnt = 0;
	cin >> n;
	set<string> m;
	string str;

	while (n--)
	{
		cin >> str;

		if (str == "ENTER")
		{
			cnt += m.size();
			m.clear();
			continue;
		}
		
		m.insert(str);
	}

	cnt += m.size();

	cout << cnt;
}