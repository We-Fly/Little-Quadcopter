#include "opencv2/opencv.hpp"
#include <iostream>
using namespace std;
using namespace cv;
int main() {

    cv::Mat img = cv::imread("wind-turbine.jpg", cv::IMREAD_COLOR);
    cv::putText(img, "Test text", cv::Point(100, 100), cv::FONT_ITALIC, 2.0,
                cv::Scalar(0, 0, 255), 2);
    cv::imwrite("text_img.jpg", img);

    return 0;
}
