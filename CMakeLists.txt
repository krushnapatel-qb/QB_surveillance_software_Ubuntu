cmake_minimum_required(VERSION 3.0)
project(qb)

# Define installation directory and executable name
set(EXECUTABLE_NAME "qb")
set(EXECUTABLE_PATH "/home/tipl-qb/Desktop/SS_21Nov/dist/qb")

set(INSTALL_DIR "/opt/qb_files")

#set(DESKTOP_FILE_NAME "${EXECUTABLE_NAME}.desktop")
set(SERVICE_FILE_NAME "${EXECUTABLE_NAME}.service")
set(SHELL_FILE_NAME "${EXECUTABLE_NAME}.service")

# Install the executable
install(FILES "${EXECUTABLE_PATH}"
        DESTINATION "${INSTALL_DIR}"
        PERMISSIONS OWNER_EXECUTE OWNER_READ OWNER_WRITE GROUP_EXECUTE GROUP_READ GROUP_WRITE WORLD_EXECUTE WORLD_READ)
        #PERMISSIONS OWNER_EXECUTE OWNER_READ GROUP_EXECUTE GROUP_READ WORLD_EXECUTE WORLD_READ)

# Install the icon file
#install(FILES "/home/tipl-qb/Desktop/SS_21Nov/qb_logo.png"
#        DESTINATION "${INSTALL_DIR}"
#        PERMISSIONS OWNER_EXECUTE OWNER_READ OWNER_WRITE GROUP_EXECUTE GROUP_READ GROUP_WRITE WORLD_EXECUTE WORLD_READ)

# Create and install the .desktop file
#configure_file(
#    "${CMAKE_SOURCE_DIR}/${DESKTOP_FILE_NAME}.in"
#    "${CMAKE_BINARY_DIR}/${DESKTOP_FILE_NAME}"
#    @ONLY)
#
#install(FILES "${CMAKE_BINARY_DIR}/${DESKTOP_FILE_NAME}"
#        DESTINATION "/usr/share/applications"
#        PERMISSIONS OWNER_EXECUTE OWNER_READ OWNER_WRITE GROUP_EXECUTE GROUP_READ GROUP_WRITE WORLD_EXECUTE WORLD_READ)

# Create and install the .service file
configure_file(
    "${CMAKE_SOURCE_DIR}/${SERVICE_FILE_NAME}.in"
    "${CMAKE_BINARY_DIR}/${SERVICE_FILE_NAME}"
    @ONLY)

install(FILES "${CMAKE_BINARY_DIR}/${SERVICE_FILE_NAME}"
        DESTINATION "/etc/systemd/system"
        PERMISSIONS OWNER_EXECUTE OWNER_READ OWNER_WRITE GROUP_EXECUTE GROUP_READ GROUP_WRITE WORLD_EXECUTE WORLD_READ)

# Create and install the install_service.sh file
configure_file(
    "${CMAKE_SOURCE_DIR}/${SHELL_FILE_NAME}"
    @ONLY)

install(FILES "${CMAKE_BINARY_DIR}/${SHELL_FILE_NAME}"
        DESTINATION "${INSTALL_DIR}"
        PERMISSIONS OWNER_EXECUTE OWNER_READ OWNER_WRITE GROUP_EXECUTE GROUP_READ GROUP_WRITE WORLD_EXECUTE WORLD_READ)

#update-desktop-database ~/.local/share/applications/

# Set package details
set(CPACK_PACKAGE_NAME "qb")
set(CPACK_PACKAGE_VERSION "1.0.0")
set(CPACK_PACKAGE_CONTACT "krushna@quantumbot.co.in")
set(CPACK_GENERATOR "DEB")

# Set post-installation script
set(CPACK_DEBIAN_PACKAGE_CONTROL_EXTRA "${CMAKE_SOURCE_DIR}/preinst;${CMAKE_SOURCE_DIR}/postinst;${CMAKE_SOURCE_DIR}/postrm")

# Include CPack for packaging
include(CPack)