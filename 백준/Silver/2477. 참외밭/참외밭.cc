#include <iostream>
#include <vector>
using namespace std;

int k, res;
int field_x = -1, field_y = -1;
int field_x_idx = -1, field_y_idx = -1;
int not_field_x, not_field_y;
vector<pair<int, int>> field(6);

void init(){
  ios_base::sync_with_stdio(false); 
  cin.tie(NULL); cout.tie(NULL);

  cin >> k;

  for(int i = 0; i < 6; i++){
    cin >> field[i].first >> field[i].second;

    if(field[i].first == 1 || field[i].first == 2){
      if(field_x < field[i].second)
        field_x = field[i].second;
    }
    else{
      if(field_y < field[i].second)
        field_y = field[i].second;
    }
  }
}

int solve(){
  for (int i = 0; i < 6; i++) {
      if ((field[i].first == 1 || field[i].first == 2) && field[i].second == field_x)
        field_x_idx = i;
      else if ((field[i].first == 3 || field[i].first == 4) && field[i].second == field_y)
        field_y_idx = i;
    }

  not_field_x = abs(field[(field_y_idx + 5) % 6].second - field[(field_y_idx + 1) % 6].second);
  not_field_y = abs(field[(field_x_idx + 5) % 6].second - field[(field_x_idx + 1) % 6].second);

  int big_area = field_x * field_y;
  int small_area = not_field_x * not_field_y;

  return (big_area - small_area) * k;
}


int main() {
  init();
  res = solve();
  cout << res;
  return 0;
}