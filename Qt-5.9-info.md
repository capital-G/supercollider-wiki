The Qt 5.9 PR is known to be compatible with Qt 5.7. The current Ubuntu repositories as of May 2018 are still stuck in 5.5, but there are third-party PPA's that allow installation of new versions on Ubuntu Trusty (14.04) and Xenial (16.04). Here are the xenial instructions:

    sudo apt-add-repository ppa:beineri/opt-qt571-xenial
    sudo apt update
    sudo apt install qt57base qt57location qt57declarative qt57tools qt57webengine qt57webchannel qt57xmlpatterns qt57svg
    cmake -DCMAKE_PREFIX_PATH=/opt/qt57 ..

Check the CMakeCache.txt file in the build directory and look for lines like the below. If any of the paths start with `/usr/lib/x86_64-linux-gnu`, change them to `/opt/qt57/lib`. I think this may be a bug in our CMake system.

    //No help, variable specified on the command line.
    QT_BIN_PATH:UNINITIALIZED=/opt/qt57

    //The directory containing a CMake configuration file for Qt5Concurrent.
    Qt5Concurrent_DIR:PATH=/opt/qt57/lib/cmake/Qt5Concurrent

    //The directory containing a CMake configuration file for Qt5Core.
    Qt5Core_DIR:PATH=/opt/qt57/lib/cmake/Qt5Core

    //The directory containing a CMake configuration file for Qt5Gui.
    Qt5Gui_DIR:PATH=/opt/qt57/lib/cmake/Qt5Gui

    //The directory containing a CMake configuration file for Qt5LinguistTools.
    Qt5LinguistTools_DIR:PATH=/opt/qt57/lib/cmake/Qt5LinguistTools

    //The directory containing a CMake configuration file for Qt5Network.
    Qt5Network_DIR:PATH=/opt/qt57/lib/cmake/Qt5Network

    //The directory containing a CMake configuration file for Qt5OpenGL.
    Qt5OpenGL_DIR:PATH=/opt/qt57/lib/cmake/Qt5OpenGL

    //The directory containing a CMake configuration file for Qt5Positioning.
    Qt5Positioning_DIR:PATH=/opt/qt57/lib/cmake/Qt5Positioning

    //The directory containing a CMake configuration file for Qt5PrintSupport.
    Qt5PrintSupport_DIR:PATH=/opt/qt57/lib/cmake/Qt5PrintSupport

    //The directory containing a CMake configuration file for Qt5Qml.
    Qt5Qml_DIR:PATH=/opt/qt57/lib/cmake/Qt5Qml

    //The directory containing a CMake configuration file for Qt5Quick.
    Qt5Quick_DIR:PATH=/opt/qt57/lib/cmake/Qt5Quick

    //The directory containing a CMake configuration file for Qt5Sql.
    Qt5Sql_DIR:PATH=/opt/qt57/lib/cmake/Qt5Sql

    //The directory containing a CMake configuration file for Qt5Svg.
    Qt5Svg_DIR:PATH=/opt/qt57/lib/cmake/Qt5Svg

    //The directory containing a CMake configuration file for Qt5WebChannel.
    Qt5WebChannel_DIR:PATH=/opt/qt57/lib/cmake/Qt5WebChannel

    //The directory containing a CMake configuration file for Qt5WebEngineCore.
    Qt5WebEngineCore_DIR:PATH=/opt/qt57/lib/cmake/Qt5WebEngineCore

    //The directory containing a CMake configuration file for Qt5WebEngineWidgets.
    Qt5WebEngineWidgets_DIR:PATH=/opt/qt57/lib/cmake/Qt5WebEngineWidgets

    //The directory containing a CMake configuration file for Qt5WebEngine.
    Qt5WebEngine_DIR:PATH=/opt/qt57/lib/cmake/Qt5WebEngine

    //The directory containing a CMake configuration file for Qt5Widgets.
    Qt5Widgets_DIR:PATH=/opt/qt57/lib/cmake/Qt5Widgets