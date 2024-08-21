cmake_minimum_required(VERSION 3.29)
project(RegressionsOnGHA)

set(CMAKE_CXX_STANDARD 20)

add_executable(RegressionsOnGHA main.cpp)

enable_testing()

# make some directories like E+ would
file(MAKE_DIRECTORY "${PROJECT_BINARY_DIR}/testfiles")  # build/testfiles
file(MAKE_DIRECTORY "${PROJECT_BINARY_DIR}/testfiles/1ZoneUncontrolled")  # build/testfiles
file(MAKE_DIRECTORY "${PROJECT_BINARY_DIR}/testfiles/5ZoneAirCooled")  # build/testfiles

add_test(
        NAME TestRegressionsOnGHA1
        COMMAND RegressionsOnGHA
        WORKING_DIRECTORY "${PROJECT_BINARY_DIR}/testfiles/1ZoneUncontrolled"
)
add_test(
        NAME TestRegressionsOnGHA2
        COMMAND RegressionsOnGHA
        WORKING_DIRECTORY "${PROJECT_BINARY_DIR}/testfiles/5ZoneAirCooled"
)
