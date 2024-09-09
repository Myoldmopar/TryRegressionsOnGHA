cmake_minimum_required(VERSION 3.28)
project(RegressionsOnGHA)

set(CMAKE_CXX_STANDARD 20)

add_executable(RegressionsOnGHA main.cpp)

enable_testing()

# make some directories like E+ would
file(MAKE_DIRECTORY "${PROJECT_BINARY_DIR}/testfiles")  # build/testfiles
file(MAKE_DIRECTORY "${PROJECT_BINARY_DIR}/testfiles/1ZoneUncontrolled")  # build/testfiles
file(MAKE_DIRECTORY "${PROJECT_BINARY_DIR}/testfiles/5ZoneAirCooled")  # build/testfiles

if (WIN32)
add_test(
        NAME TestRegressionsOnGHA0
        COMMAND "Hellllo"
        WORKING_DIRECTORY "${PROJECT_BINARY_DIR}/testfiles/1ZoneUncontrolled"
)
endif()
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

install(TARGETS RegressionsOnGHA RUNTIME DESTINATION bin)

include(CPack)

# Define a custom command to create the shortcut
if (WIN32)
    add_custom_command(
            OUTPUT ${CMAKE_INSTALL_PREFIX}/RegressionsOnGHA_Shortcut.lnk
            COMMAND powershell.exe -ExecutionPolicy Bypass -File ${CMAKE_SOURCE_DIR}/create_shortcut.ps1
            -TargetPath "${CMAKE_INSTALL_PREFIX}/bin/RegressionsOnGHA.exe"
            -ShortcutPath "${CMAKE_INSTALL_PREFIX}/RegressionsOnGHA_Shortcut.lnk"
            -Arguments "help"
            COMMENT "Creating Windows shortcut for hello.exe"
    )
    # Add a custom target that depends on the shortcut
    add_custom_target(create_shortcut ALL DEPENDS ${CMAKE_INSTALL_PREFIX}/RegressionsOnGHA_Shortcut.lnk)
    # Install the shortcut
    install(FILES ${CMAKE_INSTALL_PREFIX}/RegressionsOnGHA_Shortcut.lnk DESTINATION .)
else ()
    add_custom_command(
            OUTPUT ${CMAKE_INSTALL_PREFIX}/RegressionsOnGHA_Shortcut.desktop
            COMMAND ${CMAKE_COMMAND} -E echo "[Desktop Entry]\n" > ${CMAKE_INSTALL_PREFIX}/RegressionsOnGHA_Shortcut.desktop
            COMMAND ${CMAKE_COMMAND} -E echo "Version=1.0\n" >> ${CMAKE_INSTALL_PREFIX}/RegressionsOnGHA_Shortcut.desktop
            COMMAND ${CMAKE_COMMAND} -E echo "Name=Run With Help\n" >> ${CMAKE_INSTALL_PREFIX}/RegressionsOnGHA_Shortcut.desktop
            COMMAND ${CMAKE_COMMAND} -E echo "Exec=${CMAKE_INSTALL_PREFIX}/bin/RegressionsOnGHA help\n" >> ${CMAKE_INSTALL_PREFIX}/RegressionsOnGHA_Shortcut.desktop
            COMMAND ${CMAKE_COMMAND} -E echo "Icon=application-default-icon\n" >> ${CMAKE_INSTALL_PREFIX}/RegressionsOnGHA_Shortcut.desktop
            COMMAND ${CMAKE_COMMAND} -E echo "Terminal=true\n" >> ${CMAKE_INSTALL_PREFIX}/RegressionsOnGHA_Shortcut.desktop
            COMMAND ${CMAKE_COMMAND} -E echo "Type=Application\n" >> ${CMAKE_INSTALL_PREFIX}/RegressionsOnGHA_Shortcut.desktop
            VERBATIM
            COMMENT "Creating .desktop file for hello in ${CMAKE_INSTALL_PREFIX}"
    )
    # Add a custom target that depends on the shortcut
    add_custom_target(create_shortcut ALL DEPENDS ${CMAKE_INSTALL_PREFIX}/RegressionsOnGHA_Shortcut.desktop)
    # Install the shortcut
    install(FILES ${CMAKE_INSTALL_PREFIX}/RegressionsOnGHA_Shortcut.desktop DESTINATION .)
endif ()
