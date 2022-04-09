cmake_minimum_required(VERSION 3.13)

project(opencv_demo)

MESSAGE(STATUS "operation system is ${CMAKE_SYSTEM}")

IF (CMAKE_SYSTEM_NAME MATCHES "Linux")
	MESSAGE(STATUS "current platform: Linux ")
    find_package( OpenCV REQUIRED )
    #set(OPENCV_INCLUDE_DIR /usr/include/opencv4)
    #set(OPENCV_LIB_DIR /usr/lib/)
ELSEIF (CMAKE_SYSTEM_NAME MATCHES "Windows")
	MESSAGE(STATUS "current platform: Windows")
    set(OpenCV_DIR C:/opencv/OpenCV-MinGW-Build-OpenCV-4.5.5-x64/)
    find_package( OpenCV REQUIRED )
    #include_directories( ${OpenCV_INCLUDE_DIRS} )
    set(OPENCV_INCLUDE_DIR ${OpenCV_DIR}include)
    set(OPENCV_LIB_DIR ${OpenCV_DIR}x64/mingw/bin)
#ELSEIF (CMAKE_SYSTEM_NAME MATCHES "FreeBSD")
#	MESSAGE(STATUS "current platform: FreeBSD")
ELSE ()
	MESSAGE(STATUS "not supported platform: ${CMAKE_SYSTEM_NAME}")
ENDIF (CMAKE_SYSTEM_NAME MATCHES "Linux")

MESSAGE(STATUS "###################################")
message(STATUS "OpenCV include path: ${OPENCV_INCLUDE_DIR}")
message(STATUS "OpenCV library path: ${OPENCV_LIB_DIR}")
add_executable(write_text src/main.cpp)
set(CMAKE_CXX_STANDARD 11)

# set include directory
target_include_directories(write_text PUBLIC "${OPENCV_INCLUDE_DIR}")

# set library directory
target_link_directories(write_text PUBLIC "${OPENCV_LIB_DIR}")

# link specific object files we need
target_link_libraries(write_text ${OpenCV_LIBS})
#${OpenCV_LIBS} opencv_imgcodecs opencv_core opencv_imgproc
