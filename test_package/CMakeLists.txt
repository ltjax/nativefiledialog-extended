cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(nfd_example nfd_example.cpp)
target_link_libraries(nfd_example ${CONAN_LIBS})
