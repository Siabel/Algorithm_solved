#include<iostream>
using namespace std;

int main() {
  int n;
  cin >> n;
  
  if (n == 0){
    cout << 1;
    return 0;
  }
  
    long long temp = 1;
  
  for (int i = 1; i <= n; ++i) 
    temp *= i;
  
  cout << temp;
}