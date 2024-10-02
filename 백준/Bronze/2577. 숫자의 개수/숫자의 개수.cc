#include <iostream>
using namespace std;

int main()
{
  int a, b, c, res;
  cin >> a >> b >> c;

  res = a * b * c;

  int num[10] = {0};

  while(res > 0)
  {
    num[res % 10]++;
    res /= 10;
  }

  for(int i = 0; i < 10; i++)
  {
    cout << num[i] << endl;
  }
      
    return 0;
}