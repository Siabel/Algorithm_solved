#include <iostream>
using namespace std;

int main()
{
  while(true){
    int a, b, c;
    cin >> a >> b >> c;

    if(a == 0 && b == 0 && c == 0)
      break;
    
    a *= a;
    b *= b;
    c *= c;

    if(a + b == c || b + c == a || a + c == b)
      cout << "right" << endl;
    else
      cout << "wrong" << endl;
  }
  return 0;
}