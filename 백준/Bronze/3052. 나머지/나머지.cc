#include <iostream>
using namespace std;

int main() {
	int arr[42] = {};
	int num;
	int cnt = 0;
    
	for (int i = 0; i < 10; ++i)
	{
		cin >> num;
		++arr[num % 42];
	}

    for (int i = 0; i < 42; ++i) 
        if (arr[i] > 0) 
            ++cnt;
    
	cout << cnt;
}