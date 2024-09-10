#include <iostream>
using namespace std;

int main()
{
  int arr[5];
  int sum, ans;
  sum = ans = 0;

  for(int i = 0; i < 5; i++)
  {
    cin >> arr[i];
    sum += (arr[i] * arr[i]);
  }
  
  ans = sum % 10;

  cout << ans;

  return 0;
}