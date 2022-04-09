cmake_minimum_required(VERSION 3.0.0)

SET(PROJECT_NAME opencv_demo)
project(${PROJECT_NAME})
#include(CTest)
#enable_testing()

MESSAGE(STATUS "operation system is ${CMAKE_SYSTEM}")

IF (CMAKE_SYSTEM_NAME MATCHES "Linux")
	MESSAGE(STATUS "current platform: Linux ")
    find_package( OpenCV REQUIRED )
    include_directories(${OpenCV_INCLUDE_DIRS})
    set(OPENCV_INCLUDE_DIR /usr/include/opencv4)
    set(OPENCV_LIB_DIR /usr/lib/)
ELSEIF (CMAKE_SYSTEM_NAME MATCHES "Windows")
	MESSAGE(STATUS "current platform: Windows")
    set(OpenCV_DIR C:/opencv/OpenCV-MinGW-Build-OpenCV-4.5.5-x64)
    find_package(OpenCV REQUIRED)
    include_directories(${OpenCV_INCLUDE_DIRS})
    #find_package( OpenCV REQUIRED )
    #include_directories( ${OpenCV_INCLUDE_DIRS} )
    #link_directories(${OpenCV_LIB})
    #set(OPENCV_INCLUDE_DIR ${OpenCV_DIR}include)
    #set(OPENCV_LIB_DIR ${OpenCV_DIR}x64/mingw/lib)
#ELSEIF (CMAKE_SYSTEM_NAME MATCHES "FreeBSD")
#	MESSAGE(STATUS "current platform: FreeBSD")
ELSE ()
	MESSAGE(STATUS "not supported platform: ${CMAKE_SYSTEM_NAME}")
ENDIF (CMAKE_SYSTEM_NAME MATCHES "Linux")

message(STATUS "###################################")
message(STATUS "Project: ${PROJECT_NAME}")
message(STATUS "    OpenCV include path: ${OPENCV_INCLUDE_DIR}")
message(STATUS "    OpenCV library path: ${OPENCV_LIB_DIR}")
message(STATUS "    src file: ${DIR_SRCS}")
message(STATUS "###################################")

aux_source_directory(src DIR_SRCS)

add_executable(${PROJECT_NAME} ${DIR_SRCS})

TARGET_LINK_LIBRARIES(${PROJECT_NAME} ${OpenCV_LIBS})
#set(CMAKE_CXX_STANDARD 11)

# set include directory
#target_include_directories(${PROJECT_NAME} PUBLIC "${OPENCV_INCLUDE_DIR}")

# set library directory
#target_link_directories(${PROJECT_NAME} PUBLIC "${OPENCV_LIB_DIR}")

# link specific object files we need
#target_link_libraries(${PROJECT_NAME} ${OpenCV_LIBS})
#${OpenCV_LIBS} opencv_imgcodecs opencv_core opencv_imgproc
#target_link_libraries( ${PROJECT_NAME} ${OpenCV_LIBS} )

#set(CPACK_PROJECT_NAME ${PROJECT_NAME})
#set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
#include(CPack)