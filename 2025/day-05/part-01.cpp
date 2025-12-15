#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

int main() {
    ifstream fin;
    fin.open("input.txt");
    vector<pair<long long, char>> plane;
    int count = 0;
    string interval;

    while (getline(fin, interval) && !interval.empty()) {
        stringstream ss(interval);
        long long num1, num2;
        char del;
        ss >> num1 >> del >> num2;

        plane.push_back({num1, 'A'});
        plane.push_back({num2, 'C'});
    }

    string idString;
    while (getline(fin, idString)) {
        long long id = stol(idString);
        plane.push_back({id, 'B'});
    }

    sort(plane.begin(), plane.end());

    int turn = 0;
    for (auto& pair : plane) {
        if (pair.second == 'A') {
            turn++;
        } else if (pair.second == 'C') {
            turn--;
        } else if (pair.second == 'B' && turn > 0) {
            count++;
        }
    }
    cout << count;

    return 0;
}