Original author: Brian Heim (brianlheim@gmail.com)

This batch script will build both dynamic and static versions of `libsndfile`. It compiles `libFLAC`, `libogg`, and `libvorbis` from source, and links them statically into `libsndfile`. Note that for `libFLAC`, you need NASM (the [Netwide Assembler](http://www.nasm.us/)) installed to compile. This script adds it to your `PATH` if it isn't there already.

Required software: VS 2017, NASM, git, cmake.

```batch
:: Brian Heim, 2018-01-08
:: Script for building libsndfile on Windows using VS 2017 with FLAC/Ogg/Vorbis support
:: See the readmes of the respective projects for other relevant instructions

:: the SDK version is necessary (for me anyway) to get the right version of the SDK.
:: otherwise it defaults to 8.1, which isn’t on my machine
set SDK_VERSION=10.0.16299.0
:: You may not need this if you've got them in your path already, or maybe the paths are different.
set DEVENV_EXE="C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\Common7\IDE\devenv"
set MSBUILD_EXE="C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\MSBuild\15.0\Bin\MSBuild"
set MSBUILD_CONFIG=/p:Configuration=Release  /p:WindowsTargetPlatformVersion=%SDK_VERSION%

:: install nasm, if you don't have it. This is needed to build FLAC
:: curl http://www.nasm.us/pub/nasm/releasebuilds/2.13/win64/nasm-2.13-installer-x64.exe -o nasm.exe nasm.exe
:: (go through install process, don’t know flag to install silently)
set PATH=C:\Program Files\NASM;%PATH%
:: rm nasm.exe

:: download sources
git clone --depth=1 https://github.com/xiph/flac
git clone --depth=1 https://github.com/erikd/libsndfile
git clone --depth=1 https://github.com/xiph/ogg
git clone --depth=1 https://github.com/xiph/vorbis

:: build ogg static libs
cd ogg\win32\VS2015
start libogg_static.sln
%DEVENV_EXE% libogg_static.sln /upgrade
:: At this point the IDE might open and the command may hang at the end. Just close it
:: (click Ignore) and press any key to continue.
%MSBUILD_EXE% libogg_static.sln %MSBUILD_CONFIG%
cd ..\..\..

:: build flac static libs (with ogg)
cp ogg\win32\VS2015\Win32\Release\libogg_static.lib flac\objs\release\lib
cp -r ogg\include\ogg flac\include
cd flac\src\libFLAC
%DEVENV_EXE% libFLAC_static.vcxproj /upgrade
%MSBUILD_EXE% libFLAC_static.vcxproj %MSBUILD_CONFIG%
cd ..\..
cp src\libFLAC\objs\Release\lib\libFLAC_static.lib objs\Release\lib
cd ..

:: build vorbis static libs
cd vorbis
mkdir build && cd build
cmake -G"Visual Studio 15 2017" -DOGG_INCLUDE_DIRS=..\..\ogg\include -DCMAKE_C_FLAGS="/wd4244" ^
    -DOGG_LIBRARIES=..\..\ogg\win32\VS2015\Win32\Release\libogg_static.lib ..
cmake --build . --config Release
cd ..\..

:: build libsndfile with FLAC
cd libsndfile
mkdir build && cd build

set FLAC_CONFIG=-DFLAC_INCLUDE_DIR=..\..\flac\include ^
    -DFLAC_LIBRARY=..\..\flac\objs\release\lib\libFLAC_static.lib
set OGG_CONFIG=-DOGG_INCLUDE_DIR=..\..\ogg\include ^
    -DOGG_LIBRARY=..\..\ogg\win32\VS2015\Win32\Release\libogg_static.lib
set VORBIS_CONFIG=-DVORBIS_INCLUDE_DIR=..\..\vorbis\include ^
    -DVORBIS_LIBRARY=..\..\vorbis\build\lib\Release\vorbis.lib ^
    -DVORBISFILE_LIBRARY=..\..\vorbis\build\lib\Release\vorbisfile.lib ^
    -DVORBISENC_LIBRARY=..\..\vorbis\build\lib\Release\vorbisenc.lib
set EXTERNAL_LIBS_CONFIG=%FLAC_CONFIG% %OGG_CONFIG% %VORBIS_CONFIG%

:: this is so ridiculous
cmake -G"Visual Studio 15 2017" -DENABLE_STATIC_RUNTIME=ON -DBUILD_TESTING=OFF ^
    -DENABLE_PACKAGE_CONFIG=OFF -DDISABLE_EXTERNAL_LIBS=OFF -DBUILD_SHARED_LIBS=OFF ^
    %EXTERNAL_LIBS_CONFIG% -DCMAKE_SHARED_LINKER_FLAGS="/NODEFAULTLIB:MSVCRT /ignore:4049 /LTCG" ^
    -DCMAKE_STATIC_LINKER_FLAGS="/NODEFAULTLIB:MSVCRT /ignore:4049 /LTCG" ^
    -DCMAKE_C_FLAGS="/wd4244" ..

:: the first linker flag was necessary for me.
:: /ignore:4049 and /wd4244 stop warning spam
:: /LTCG, according to an info post, speeds up linking

cmake --build . --target sndfile-shared --config Release
cmake --build . --target sndfile-static --config Release
cd ..\..

echo "The dll and lib files are in libsndfile\build\Release\"
```