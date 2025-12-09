#include <cmath>
#include <cstring>
#include <fstream>
#include <iostream>

std::ifstream fin;

int main() {
    fin.open("input.txt");

    int dial = 50;
    std::string rotation;
    int count = 0;

    while (std::getline(fin, rotation)) {
        char direction = rotation[0];
        rotation.erase(0, 1);
        int distance = std::stoi(rotation);

        count += distance / 100;
        distance %= 100;

        if (direction == 'L') {
            if (dial - distance <= 0 && dial != 0) {
                count++;
            }
            dial = (dial - distance + 100) % 100;
        } else {
            if (dial + distance >= 100) {
                count++;
            }
            dial = (dial + distance) % 100;
        }
    }
    std::cout << count;
}