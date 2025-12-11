#include <fstream>
#include <iostream>
#include <stack>

using namespace std;

int main() {
    ifstream fin;
    fin.open("input.txt");

    string bank;
    long long sum = 0;

    while (getline(fin, bank)) {
        stack<int> stack;
        for (int i = 0; i < bank.size(); i++) {
            int num = bank[i] - '0';
            while (!stack.empty() && num > stack.top() &&
                   stack.size() - 1 + bank.size() - i >= 12) {
                stack.pop();
            }
            if (stack.size() < 12) {
                stack.push(num);
            }
        }
        long long num = 0;
        long long multipier = 1;
        while (!stack.empty()) {
            num = stack.top() * multipier + num;
            multipier *= 10;
            stack.pop();
        }
        sum += num;
    }
    cout << sum;
    return 0;
}