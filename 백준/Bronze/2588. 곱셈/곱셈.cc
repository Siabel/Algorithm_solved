#include <iostream>
#include <string>

using namespace std;

int main() {
  int a, b;
  cin >> b >> a;

  cout << b * (a % 10) << "\n" << b * ((a % 100 - a % 10) / 10) << "\n" << b * (a / 100) << "\n" << a * b;

  return 0;
}