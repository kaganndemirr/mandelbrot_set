#include <iostream>
#include <complex>
#include <chrono>
#include <fstream>


auto escapeTimeAlgorithm(std::complex<double> c) {
    std::complex<double> z(0, 0);
    for(int i = 0; i < 10000; i++){
        z = std::pow(z, 2) + c;
        if (std::abs(z) > 2){
            return i;
        }
    }
    return 0;
}

int main()
{

	std::ofstream pixelFile("x, y, color.txt");

    int width = 1280;
    int height = 1280;
    double x1 = -2.0;
    double x2 = 2.0;
    double y1 = -2.0;
    double y2 = 2.0;

    for(int x = 0; x < width; x++){
        double zx = x * (x2 - x1) / width + x1;
        for(int y = 0; y < height; y++){
            double zy = y * (y2 - y1) / height + y1;
            auto color = escapeTimeAlgorithm(std::complex(zx, zy));
            pixelFile << std::to_string(x) + " " + std::to_string(y) + " " + std::to_string(color) + "\n";
        }
    }

    pixelFile.close();

    return 0;

}

