#include <cmath>
#include <cstring>
#include <fstream>
#include <iostream>
#include <sstream>
#include <unordered_set>

using namespace std;

ifstream fin;

int digitCount(long long num) {
    int count = 0;
    while (num) {
        num /= 10;
        count++;
    }
    return count;
}

long long myPow(long long a, long long b) {
    long long nr = 1;
    while (b) {
        if (b % 2 == 1) {
            nr = (nr * a);
        }
        a = (a * a);
        b >>= 1;
    }
    return nr;
}

int main() {
    fin.open("input.txt");
    long long sum = 0;
    long long mini = 0;
    long long maxi = 0;
    string ranges;
    string range;
    unordered_set<long long> validSet;

    getline(fin, ranges);
    stringstream ss(ranges);

    while (getline(ss, range, ',')) {
        stringstream ss2(range);
        long long firstID, lastID;
        char del;
        ss2 >> firstID >> del >> lastID;

        int maxDigits = digitCount(lastID);
        for (int length = 1; length <= maxDigits / 2; length++) {
            long long mask = myPow(10, length) + 1;
            long long mini = max(myPow(10, length - 1), (firstID + mask - 1) / mask);
            long long maxi = min(myPow(10, length) - 1, lastID / mask);
            for (long long int pattern = mini; pattern <= maxi; pattern++) {
                validSet.insert(pattern * mask);
            }
        }
    }
    for (long long num : validSet) {
        sum += num;
    }
    cout << sum;
}