cmake_minimum_required(VERSION 3.17)
project(mongoose)

add_library(mongoose mongoose/mongoose.c)
include_directories(mongoose/)

