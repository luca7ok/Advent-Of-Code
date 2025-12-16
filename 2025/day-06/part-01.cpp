#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

int main() {
    ifstream fin;
    fin.open("input.txt");

    string line;
    vector<vector<long long>> problems;
    vector<char> operands;
    long long sum = 0;

    while (getline(fin, line)) {
        stringstream ss(line);
        if (line[0] == '*' || line[0] == '+') {
            char oper;

            while (ss >> oper) {
                operands.push_back(oper);
            }

        } else {
            vector<long long> row;
            long long number;

            while (ss >> number) {
                row.push_back(number);
            }
            problems.push_back(row);
        }
    }

    for (int j = 0; j < problems[0].size(); j++) {
        long long worksheet = problems[0][j];
        for (int i = 1; i < problems.size(); i++) {
            worksheet =
                (operands[j] == '*') ? worksheet * problems[i][j] : worksheet + problems[i][j];
        }
        sum += worksheet;
    }
    cout << sum;

    return 0;
}