#include <fstream>
#include <iostream>
#include <thread>

// ReSharper disable once CppDFAConstantFunctionResult
int main(const int argc, char *argv[])
{
    if (argc > 1) {
        if (argv[1] == "help") {
            std::cout << "HELP INFORMATION HERE, PRESS ANY KEY TO CONTINUE" << std::endl;
            std::getc(stdin);
            return 0;
        }
    }
    std::cout << "Hello, World!" << std::endl;
    std::ofstream MyFile("eplusout.txt");
    MyFile << "E+ Output";
    MyFile.close();
    const int MAX_N = static_cast<int>(std::thread::hardware_concurrency());
    std::cout << "Found this for MAX_N: " << MAX_N << std::endl;
    return 0;
}
