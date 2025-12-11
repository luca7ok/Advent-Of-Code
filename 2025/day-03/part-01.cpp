#include <fstream>
#include <iostream>

using namespace std;

int main() {
    ifstream fin;
    fin.open("input.txt");

    string bank;
    int sum = 0;

    while (getline(fin, bank)) {
        int battery1 = 0;
        int battery2 = 0;
        for (int i = 0; i < bank.size(); i++) {
            int num = bank[i] - '0';
            if (battery1 < num) {
                if (i == bank.size() - 1) {
                    battery2 = num;
                } else {
                    battery1 = num;
                    battery2 = bank[i + 1] - '0';
                }

            } else if (battery1 == num) {
                battery2 = max(battery2, num);
            } else if (battery2 < num) {
                battery2 = num;
            }
        }
        sum += battery1 * 10 + battery2;
    }
    cout << sum;
    return 0;
}