/**
 * @file main.cpp
 * @author CodyGua (cody23333@gmail.com)
 * @brief 将一个图片上添加测试文字
 * @version 0.1
 * @date 2022-04-09
 * 
 */

#include <opencv2/opencv.hpp>
#include <iostream>
using namespace std;
using namespace cv;
int main() {

    cv::Mat img = cv::imread("wind-turbine.jpg", cv::IMREAD_COLOR);
    cv::putText(img, "Test text", cv::Point(100, 100), cv::FONT_ITALIC, 2.0, cv::Scalar(0, 0, 255), 2);
    cv::imwrite("text_img.jpg", img);
    cout<<"ok"<<endl;

    return 0;
}
