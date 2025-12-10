#include <cmath>
#include <cstring>
#include <fstream>
#include <iostream>
#include <sstream>

using namespace std;

std::ifstream fin;

int main() {
    fin.open("input.txt");
    long long sum = 0;
    long long mini = 0;
    long long maxi = 0;
    string ranges;
    string range;

    getline(fin, ranges);
    stringstream ss(ranges);

    while (getline(ss, range, ',')) {
        stringstream ss2(range);
        long long firstID, lastID;
        char del;
        ss2 >> firstID >> del >> lastID;

        for (int length = 2; length <= 18; length += 2) {
            long long minHalf = pow(10, length / 2 - 1);
            long long maxHalf = pow(10, length / 2) - 1;
            long long multiplier = pow(10, length / 2) + 1;

            for (long long half = minHalf; half <= maxHalf; half++) {
                long long num = half * multiplier;
                if (num >= firstID && num <= lastID) {
                    sum += num;
                }
            }
        }
    }
    cout << sum;
}