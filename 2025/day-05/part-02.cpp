#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

int main() {
    ifstream fin;
    fin.open("input.txt");
    vector<pair<long long, int>> plane;
    long long count = 0;
    string interval;

    while (getline(fin, interval) && !interval.empty()) {
        stringstream ss(interval);
        long long num1, num2;
        char del;
        ss >> num1 >> del >> num2;

        plane.push_back({num1, 1});
        plane.push_back({num2 + 1, -1});
    }

    sort(plane.begin(), plane.end());

    int active = 0;
    for (int i = 0; i < plane.size(); i++) {
        if (active > 0) {
            count += plane[i].first - plane[i - 1].first;
        }
        active += plane[i].second;
    }
    cout << count;

    return 0;
}