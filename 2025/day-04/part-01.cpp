#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ifstream fin;
    fin.open("input.txt");

    vector<string> grid;
    string line;
    int count = 0;
    const int dx[] = {-1, -1, -1, 0, 1, 1, 1, 0};
    const int dy[] = {-1, 0, 1, 1, 1, 0, -1, -1};

    while (getline(fin, line)) {
        grid.push_back(line);
    }
    for (int i = 0; i < grid.size(); i++) {
        for (int j = 0; j < grid[0].size(); j++) {
            if (grid[i][j] == '@') {
                int neighbors = 0;
                for (int k = 0; k < 8; k++) {
                    int newI = dx[k] + i;
                    int newJ = dy[k] + j;
                    if (newI >= 0 && newJ >= 0 && newI < grid.size() && newJ < grid[0].size() &&
                        grid[newI][newJ] == '@' ) {
                        neighbors++;

                    }
                }
                if (neighbors < 4) {
                    count++;
                }
            }
        }
    }
    cout << count;

    return 0;
}