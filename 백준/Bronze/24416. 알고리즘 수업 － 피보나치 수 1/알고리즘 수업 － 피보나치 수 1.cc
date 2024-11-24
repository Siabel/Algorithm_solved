#include <algorithm>
#include <iostream>

using namespace std;
int arr[41];

int main() {
	int n; 
    cin >> n;

    arr[1] = arr[2] = 1;
	for (int i = 3; i < 41; ++i) 
        arr[i] = arr[i - 1] + arr[i - 2];

	cout << arr[n] << " " << n - 2;

    return 0;
}