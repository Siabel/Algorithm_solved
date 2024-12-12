#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n, m, r;
int cnt = 0;
vector<int> visited;
vector<vector<int>> graph;

void init(){
  ios_base::sync_with_stdio(false); 
  cin.tie(0);

  cin >> n >> m >> r;
  graph.resize(n + 1);
}

void dfs(int start) {
  if(visited[start]) {
		return;
	}

  visited[start] = ++cnt;

  for (int next : graph[start]) {
    if (!visited[next]) {
      dfs(next);
    }
  }
}

int main() {
  init();
  
  for (int i = 0; i < m; ++i) {
    int u, v;
    cin >> u >> v;
    graph[u].push_back(v);
    graph[v].push_back(u);
  }

  for (int i = 0; i < n + 1; ++i) {
    sort(graph[i].begin(), graph[i].end());
  }

  visited.resize(n + 1, 0);

  dfs(r);

  for(int i = 1; i <= n; i++){
    cout << visited[i] << "\n";
  }

  return 0;
}