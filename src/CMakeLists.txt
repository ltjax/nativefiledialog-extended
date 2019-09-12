set(TARGET_NAME nfd)

set(HEADER_FILES
  include/nfd/nfd.h
  include/nfd/nfd.hpp)

if(nfd_PLATFORM STREQUAL PLATFORM_WIN32)
  set(SOURCE_FILES nfd_win.cpp)
endif()

if(nfd_PLATFORM STREQUAL PLATFORM_LINUX)
  find_package(PkgConfig REQUIRED)
  pkg_check_modules(GTK3 REQUIRED gtk+-3.0)
  message("Using GTK version: ${GTK3_VERSION}")
  set(SOURCE_FILES nfd_gtk.cpp)
endif()

if(nfd_PLATFORM STREQUAL PLATFORM_MACOS)
  find_library(APPKIT_LIBRARY AppKit)
  set(SOURCE_FILES nfd_cocoa.m)
endif()

# Define the library
add_library(${TARGET_NAME} STATIC
  ${SOURCE_FILES} ${HEADER_FILES})

# Allow includes from include/
target_include_directories(${TARGET_NAME}
  PUBLIC include/)

if(nfd_PLATFORM STREQUAL PLATFORM_LINUX)
  target_include_directories(${TARGET_NAME}
    PRIVATE ${GTK3_INCLUDE_DIRS})
  target_link_libraries(${TARGET_NAME}
    PRIVATE ${GTK3_LIBRARIES})
endif()


if(nfd_PLATFORM STREQUAL PLATFORM_MACOS)
  target_link_libraries(${TARGET_NAME}
    PRIVATE ${APPKIT_LIBRARY})
endif()

# Install rules
install(FILES ${HEADER_FILES} DESTINATION include/nfd)
install(TARGETS ${TARGET_NAME} ARCHIVE DESTINATION lib)
