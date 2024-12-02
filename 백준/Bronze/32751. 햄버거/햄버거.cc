#include <iostream>
using namespace std;

int n;
int arr[4];
char ingredient[100001] = {};
bool taste = true;

void init(){
  ios::sync_with_stdio(false);
  cin.tie(0);

  cin >> n;
  for(int i = 0; i < 4; i++)
    cin >> arr[i];

  for(int i = 0; i < n; i++)
    cin >> ingredient[i];
}

void delicious(){
  for(int i = 0; i < n; i++){
    if(ingredient[0] != 'a' || ingredient[n - 1] != 'a'){
      taste = false;
      break;
    }
    
    if(ingredient[i] == ingredient[i + 1]){
      taste = false;
      break;
    }

    if(ingredient[i] == 'a')
      arr[0]--;
    else if(ingredient[i] == 'b')
      arr[1]--;
    else if(ingredient[i] == 'c')
      arr[2]--;
    else
      arr[3]--;
  }

  for(int i = 0; i < 4; i++){
    if(arr[i] < 0)
      taste = false;
  }
}

int main(){
  init();
  delicious();

  if(taste)
    cout << "Yes";
  else
    cout << "No";

  return 0;
}