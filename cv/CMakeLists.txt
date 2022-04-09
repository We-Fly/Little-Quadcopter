cmake_minimum_required(VERSION 3.10)

project(opencv_demo)

add_executable(write_text src/main.cpp)

set(OPENCV_INCLUDE_DIR /usr/include/opencv4)
set(OPENCV_LIB_DIR /usr/lib/)

message(STATUS "OpenCV library path: ${OPENCV_LIB_DIR}")

# set include directory
target_include_directories(write_text PUBLIC "${OPENCV_INCLUDE_DIR}")

# set library directory
target_link_directories(write_text PUBLIC "${OPENCV_LIB_DIR}")

# link specific object files we need
target_link_libraries(write_text opencv_imgcodecs opencv_core opencv_imgproc)