#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

int calculateMinutes(const string& start, const string& end) {
  int sh, sm, eh, em;
  sscanf(start.c_str(), "%d:%d", &sh, &sm);
  sscanf(end.c_str(), "%d:%d", &eh, &em);
  return (eh * 60 + em) - (sh * 60 + sm);
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int N, M;
  cin >> N >> M;

  map<string, vector<pair<int, int>>> youtuber;
  int weeksCount = M / 7;

  for (int i = 0; i < N; i++) {
    string name, start, end;
    int day;
    cin >> name >> day >> start >> end;

    int week = (day - 1) / 7;
    int minutes = calculateMinutes(start, end);

    if (youtuber[name].size() <= week) {
      youtuber[name].resize(weeksCount, {0, 0});
    }
    youtuber[name][week].first++;
    youtuber[name][week].second += minutes;
  }

  vector<string> youtuberValid;

  for (const auto& [name, weeks] : youtuber) {
    if ((int)weeks.size() != weeksCount) continue;
    bool isValid = true;

    for (const auto& [count, totalTime] : weeks) {
      if (count < 5 || totalTime < 60 * 60) {
        isValid = false;
        break;
      }
    }

    if (isValid) {
      youtuberValid.push_back(name);
    }
  }

  if (youtuberValid.empty()) {
    cout << -1 << "\n";
  } else {
    sort(youtuberValid.begin(), youtuberValid.end());
    for (const string& youtuber : youtuberValid) {
      cout << youtuber << "\n";
    }
  }

  return 0;
}
