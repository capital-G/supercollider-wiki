The Qt 5.9 PR is known to be compatible with Qt 5.7. The current Ubuntu repositories as of May 2018 are still stuck in 5.5, but there are third-party PPA's that allow installation of new versions on Ubuntu Trusty (14.04) and Xenial (16.04). Here are the xenial instructions:

    sudo apt-add-repository ppa:beineri/opt-qt571-xenial
    sudo apt update
    sudo apt install qt57base qt57location qt57declarative qt57tools qt57webengine qt57webchannel qt57xmlpatterns qt57svg
    cmake -DCMAKE_PREFIX_PATH=/opt/qt57 ..