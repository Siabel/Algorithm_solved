#include <iostream>
using namespace std;

int h, m;

int main() 
{
    cin >> h >> m;

    m -= 45;
    if(m < 0) 
    {
        m += 60;
        h -= 1;
        
        if(h < 0) {
            h += 24;
        }
    }
    cout << h << " " << m;
}