#include <iostream>
#include <vector>

using namespace std;

// 에라토스테네스의 체
vector<bool> is_prime_num(int a) {
  vector<bool> arr(a + 1, true);
  arr[0] = false;
  arr[1] = false;

  for (int i = 2; i * i <= a; i++) {
    if (arr[i]) {
      for (int j = i * i; j <= a; j += i) {
        arr[j] = false;
        }
    }
  }
  return arr;
}

int main() {
  int n;
  int cnt = 0;
  vector<bool> primes = is_prime_num(1001);

  cin >> n;

  for (int i = 0; i < n; i++) {
    int num;
    cin >> num;

    if (primes[num]) {
      cnt++;
    }
  }

  cout  << cnt;

  return 0;
}