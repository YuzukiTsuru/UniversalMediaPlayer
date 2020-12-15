cmake_minimum_required(VERSION 3.17)
project(UniversalMediaPlayer)

set(CMAKE_CXX_STANDARD 17)


file(GLOB SRCPP src/*.cpp)
add_executable(UniversalMediaPlayer ${SRCPP})