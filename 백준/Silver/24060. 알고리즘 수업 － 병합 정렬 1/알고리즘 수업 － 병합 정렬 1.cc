#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
int A[500001] = {};
int res[500001] = {};
int n, k;
int cnt = 0;

void init(){
  ios_base::sync_with_stdio(false); 
  cin.tie(NULL); cout.tie(NULL);

  cin >> n >> k;
  
  for (int i = 0; i < n; i++)
    cin >> A[i];
}

void merge(int p, int q, int r)
{
  int left = p, right = q + 1, temp = 0;
  while (left <= q && right <= r)
  {
    if (A[left] <= A[right])
    {
      res[temp++] = A[left++];
    }
    else
    {
      res[temp++] = A[right++];
    }
  }
  while (left <= q)
  {
    res[temp++] = A[left++];
  }
  while (right <= r)
  {
    res[temp++] = A[right++];
  }

  left = p;
  temp = 0;
  while (left <= r)
  {
    A[left++] = res[temp++];
    cnt++;
    if (cnt == k)
    {
      cout << A[left - 1];
      return;
    }
  }
}

void merge_sort(int p, int r)
{
  if (p < r)
  {
    int q = floor((p + r) / 2);
    merge_sort(p, q);
    merge_sort(q + 1, r);
    merge(p, q, r);
  }
}

int main()
{
  init();

  merge_sort(0, n - 1);
  if (cnt < k)
    cout << "-1";
}