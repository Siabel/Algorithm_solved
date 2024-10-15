#include <iostream>
using namespace std;

int main()
{
    int a1, a2, a3;
    int b1, b2;
    
    cin >> a1 >> a2 >> a3 >> b1 >> b2;
    int min_a = 2000;
    int min_b = 2000;
    
    if(a1 < min_a)
        min_a = a1;
    if(a2 < min_a)
        min_a = a2;
    if(a3 < min_a)
        min_a = a3;
    if(b1 < min_b)
        min_b = b1;
    if(b2 < min_b)
        min_b = b2;
    
    cout << min_a + min_b - 50;
}