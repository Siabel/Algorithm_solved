#include <iostream>
using namespace std;
 
int main(){
    int n;
    cin >> n;
 
    if(n == 1){
        for(int i = 2; i < 9; i++){
            cin >> n;
            if(i != n){
                cout << "mixed";
                break;
            }
            if(n == 8) 
                cout << "ascending";
        }
    } else if(n == 8){
        for(int i = 7; i > 0; i--){
            cin >> n;
            if(i != n){
                cout << "mixed";
                break;
            }
            if(n == 1) 
                cout << "descending";
        }
    } else cout << "mixed";
    return 0;
}