#include <iostream>
using namespace std;
 
int main()
{
    int cnt;    
    int min = 1000001;
    int max = -1000001;
    
    cin >> cnt;
    int arr[cnt];
    
    for(int i = 0; i < cnt; i++ )
    {
        cin >> arr[i];
        if( max < arr[i] ) max = arr[i];
        if( min > arr[i] ) min = arr[i];
    }
    
	cout << min << ' ' << max;
 
	return 0;
}