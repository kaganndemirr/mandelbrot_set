#include <unistd.h>
#include <sys/wait.h>
#include <iostream>
#include <complex>
#include <chrono>
#include <fstream>


auto escapeTimeAlgorithm(std::complex<double> c, auto maxIter){
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

	std::ofstream pixelFile("x, y, color.txt");

    int width = 128;
    int height = 128;
    int x1 = -2.0;
    int x2 = 2.0;
    int y1 = -2.0;
    int y2 = 2.0;

    int max_iter = 1000000;

    for(int x = 0; x < width; x++){
        double zx = x * (x2 - x1) / width + x1;
        for(int y = 0; y < height; y++){
            double zy = y * (y2 - y1) / height + y1;
            auto color = escapeTimeAlgorithm(std::complex(zx, zy), max_iter);
            pixelFile << std::to_string(x) + " " + std::to_string(y) + " " + std::to_string(color) + "\n";
        }
    }

    pixelFile.close();

    std::chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
    std::cout << "Elapsed Time = " << std::chrono::duration_cast<std::chrono::seconds>(end - begin).count() << "s.\n";

    return 0;

}

