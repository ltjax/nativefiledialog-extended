cmake_minimum_required(VERSION 3.2)
project(nativefiledialog-extended)

set(nfd_PLATFORM Undefined)
if(WIN32)
  set(nfd_PLATFORM PLATFORM_WIN32)
elseif(APPLE)
  set(nfd_PLATFORM PLATFORM_MACOS)
elseif(UNIX AND NOT APPLE)
  set(nfd_PLATFORM PLATFORM_LINUX)
endif()

set(CMAKE_CXX_STANDARD 11)

message("nfd Platform: ${nfd_PLATFORM}")

add_subdirectory(src)
add_subdirectory(test)
