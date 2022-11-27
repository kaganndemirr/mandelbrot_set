#include <unistd.h>
#include <sys/wait.h>
#include <iostream>
#include <complex>
#include <chrono>

#define FORK_NUMBER 64

auto escapeTimeAlgorithm(std::complex<double> c) {
    int maxIter = 1000000;
    std::complex<double> z(0, 0);
    for(int i = 0; i < maxIter; i++){
        z = pow(z, 2) + c;
        if (norm(z) > 2){
            return i;
        }
    }
    return 0;
}

int main()
{
    std::chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();

    int width = 128;
    int height = 128;
    int x1 = -2.0;
    int x2 = 2.0;
    int y1 = -2.0;
    int y2 = 2.0;

    pid_t shutDownArray[FORK_NUMBER];
    int pID;

    for(int processNumber = 0; processNumber < FORK_NUMBER; processNumber++){
        pID = fork();
        if (pID == -1){
            std::cout << "Error with creating process\n";
            return 2;
        }
        else if (pID == 0){
            std::string information;

            for(int x = processNumber * (width / FORK_NUMBER); x < (processNumber + 1) * (width / FORK_NUMBER); x++){
                auto zx = x * (x2 - x1) / width + x1;
                for(int y = 0; y < height; y++){
                    auto zy = y * (y2 - y1) / height + y1;
                    auto color = escapeTimeAlgorithm(std::complex(static_cast<double>(zx), static_cast<double>(zy)));
                    information += std::to_string(x) + " " + std::to_string(y) + " " + std::to_string(color) + "\n";
                }
            }

            exit(EXIT_SUCCESS);
        }
        else{
            shutDownArray[processNumber] = pID;
        }

    }

    if (pID > 0){

        for(auto & i : shutDownArray){
            waitpid(i, nullptr, 0);
        }

        std::chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
        std::cout << "Elapsed Time = " << std::chrono::duration_cast<std::chrono::seconds>(end - begin).count() << "s.\n";

    }

    return 0;

}
