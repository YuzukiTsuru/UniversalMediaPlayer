cmake_minimum_required(VERSION 3.17)
project(UniversalMediaPlayer)

set(CMAKE_CXX_STANDARD 17)

set(CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/CMake)

message("-- Find File")

if (APPLE)
        message(WARNING "macOS is not currently supported. If run it in macOS, You'll get:\n"
                "\tcaopengllayer vout display error: No drawable-nsobject found!\n"
                "but development and testing are allowed."
                " If you want to develop with macOS, Please add VLC plugin to the environment variables before using: "
                "\n\tVLC_PLUGIN_PATH=/Applications/VLC.app/Contents/MacOS/plugins")
endif ()

find_package(LIBVLC REQUIRED)
file(GLOB SRCPP src/*.cpp)

include_directories(
        lib/libvlcpp/
        ${LIBVLC_INCLUDE_DIR}
        )

add_executable(UniversalMediaPlayer ${SRCPP})
target_link_libraries(UniversalMediaPlayer ${LIBVLC_LIBRARY})