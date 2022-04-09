cmake_minimum_required(VERSION 3.10)

project(opencv_demo)

MESSAGE(STATUS "operation system is ${CMAKE_SYSTEM}")
 
IF (CMAKE_SYSTEM_NAME MATCHES "Linux")
	MESSAGE(STATUS "current platform: Linux ")
    set(OPENCV_INCLUDE_DIR /usr/include/opencv4)
    set(OPENCV_LIB_DIR /usr/lib/)
ELSEIF (CMAKE_SYSTEM_NAME MATCHES "Windows")
	MESSAGE(STATUS "current platform: Windows")
    set(OPENCV_INCLUDE_DIR C:\\opencv\\opencv-build\\install\\include\\opencv2)
    set(OPENCV_LIB_DIR C:\\opencv\\opencv-build\\install\\x64\\mingw\\lib)
#ELSEIF (CMAKE_SYSTEM_NAME MATCHES "FreeBSD")
#	MESSAGE(STATUS "current platform: FreeBSD")
ELSE ()
	MESSAGE(STATUS "not supported platform: ${CMAKE_SYSTEM_NAME}")
ENDIF (CMAKE_SYSTEM_NAME MATCHES "Linux")

MESSAGE(STATUS "###################################")
message(STATUS "OpenCV include path: ${OPENCV_INCLUDE_DIR}")
message(STATUS "OpenCV library path: ${OPENCV_LIB_DIR}")
add_executable(write_text src/main.cpp)

# set include directory
target_include_directories(write_text PUBLIC "${OPENCV_INCLUDE_DIR}")

# set library directory
target_link_directories(write_text PUBLIC "${OPENCV_LIB_DIR}")

# link specific object files we need
target_link_libraries(write_text opencv_imgcodecs opencv_core opencv_imgproc)
