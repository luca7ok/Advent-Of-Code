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

        dial = direction == 'L' ? (dial - distance) % 100 : (dial + distance) % 100;

        if (dial == 0) {
            count++;
        }
    }
    std::cout << count;
}