#include <vector>
#include <algorithm>

std::vector<int> solution(int n, long long left, long long right) {
    std::vector<int> answer;
    
    for (long long i = left; i <= right; ++i) {
        int row = i / n;
        int col = i % n;
        answer.push_back(std::max(row, col) + 1);
    }
    
    return answer;
}