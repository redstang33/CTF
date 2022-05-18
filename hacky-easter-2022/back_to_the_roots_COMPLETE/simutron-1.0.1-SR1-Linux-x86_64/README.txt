###Simutron (Electronic Circuit Simulator).
______________________________________________________________________

It's developed in C++ using QTCreator IDE and currently can be built
with Qt5 framework only.

Main focus is made on providing simple environment for debugging
firmware for AVR microprocessors and Arduino boards.

Simutron internally uses a simulation core library - libsimavr
supplied by simavr project: a lean, mean and hackable AVR simulator,
  see https://github.com/buserror/simavr
Simutron supports every processor model, supported by underlying libsimavr version.
Look for additional information on the simutron wiki page:
	https://sourceforge.net/p/simutron/wiki/Home/

______________________________________________________________________
______________________________________________________________________

###COMPILING:

______________________________________________________________________

####Linux:

#####Prerequisites:
Install libelf package from your linux repo, e.g.
sudo apt-get install libelf-dev

Install QT5 development packages:
sudo apt-get install qtbase5-dev

Firstly, you need to download and build libsimavr:
---------------------------------------------------

Go to https://github.com/buserror/simavr, download a simavr-master.zip and unpack it
  - or do
git clone https://github.com/buserror/simavr.git simavr-master

Go to simavr-master folder:
cd simavr-master

Make simavr:
make build-simavr

And install it:
sudo make install DESTDIR=your_installation_root

IMPORTANT: if your_installation_root is in your local directory, e.g. /home/yourname/simavr,
to be able compile and run simutron
you will have to set the following variables in ypur environment:
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/yourname/simavr/lib
export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/home/yourname/simavr/lib/pkgconfig
If your_installation_root is a common path ( /usr or /usr/local ),
everething should work without environment changes.

Also the dependencies folder already contains a copy 
of simavr v1.4 sources with all required patches applied.
Subsequent simavr releases should render it obsolete,
so ensure to update it from https://github.com/buserror/simavr
if necessary.


Compiling Simutron:
---------------------------------
IMPORTANT: Ensure your qmake program pertains to Qt5 development environment (Qt4 builds are not supported any more):
qmake --version
 -- or on some distros:
qmake-qt5 --version
Something like "Using Qt version 5.7.1 in /usr/lib64" should be reported.

You can use build-unix script in the project's top dir, or
follow this manual build procedure:

Go to Simutron source root folder, i.e. where src, bin, lib & plugins subfolders reside 
and run qmake to generate makefiles:

qmake
 -- or on some distros:
qmake-qt5

make

You should see simutron executable file in the bin folder.
If you run it now, no plugin components will be available yet.


Compiling plugins:
Look for plugins in the plugins folder.
Go to plugins/<plugin name> folder and run compile script there, e.g.:

cd plugins/full_adder
./compile

Repeat these steps for other plugins.

Now lib directory should contain a bunch of .so files.

After build, no installation step required.
Just go to the bin subfolder and run simutron or start-simutron.

For evaluation you can load one of supplied .simu project files.

______________________________________________________________________

####Windows:

WARNING: Don't use spaces in any installation and source folder path.

To build from sources you will nead to install the following compilers and tools:

- Latest Qt development framework bundled with MinGW - see there: https://www.qt.io/download-open-source
	for instance http://download.qt.io/official_releases/qt/5.7/5.7.0/qt-opensource-windows-x86-mingw530-5.7.0.exe
	NOTE: ensure to select MinGW during installation as it is turned off by default
- Msys-1.0, look there: http://www.mingw.org/wiki/MSYS and there: https://wiki.qt.io/MinGW-64-bit
- cmake (https://cmake.org/download)
- WinAVR, look there: https://sourceforge.net/projects/winavr

Also the following source packages required:
- dlfcn-win32
- libelf-0.8.13
For convenience you can download simutron-Win-dep.zip archive
and unpack it over the root of source tree.

Also the dependencies folder already contains a copy 
of simavr v1.4 sources with all required patches applied.
Subsequent simavr releases should render it obsolete,
so ensure to update it from https://github.com/buserror/simavr
if necessary.


Go to the simutron source root folder and open build-mingw.bat file with text editor.
Look for additional build instructions in comments inside build-mingw.bat,
alter necessary variables according your tools and libraries installation path,
then run build-mingw.bat to build simavr & simutron.

________________________________________________________________________________
________________________________________________________________________________


###INSTALLATION:

####Prerequisites:
______________________________________________________________________
#####Linux:
___________________
Simutron requires Qt5 redistributable, libelf and libsimavr shared libraries to run.
Also it uses cutecom and gtkwave external applications.
So, depending on your OS:
Ubuntu: sudo apt-get install qt5-default cutecom gtkwave libelf
Fedora 25: dnf install qt5-qtbase cutecom gtkwave elfutils-libelf
ALTLinux: apt-get install libqt5-core libqt5-gui libqt5-xml libqt5-widgets cutecom gtkwave libelf

libsimavr.so is bundled with the simutron binary release in the lib folder.
___________________
#####Windows:
___________________
For AVR MCU UART to host serial port connection functionality
	-please install com0com Null-modem emulator,
		*for x64 recommended https://sourceforge.net/projects/com0com/files/com0com/2.2.2.0/com0com-2.2.2.0-x64-fre-signed.zip/download
		*for x86 recommended https://sourceforge.net/projects/com0com/files/latest/download?source=files
	-This is not required for Simutron build process, only for run.
	-Simutron links UART0 port of simulated MCU to the host virtual serial port with name \\.\CNCA0.
	-This \\.\CNCA0 name can be specified in most terminal programs instead of COM port.
	-Additionally, you can create alias (like e.g. COM5:) for \\.\CNCA0 device using com0com setup program.
Other necessary libraries are shipped with the simutron binary release.

####Install simutron:
______________________________________________________________________
Unpack simutron binary distribution archive, go to bin folder,
or, if you built it from source, go to bin folder inside source tree,
and run simutron (on Windows),
or start-simutron (on Linux).
Note (Linux): the start-simutron script in the bin folder set LD_LIBRARY_PATH environment variable
to access libsimavr.so in lib folder.

________________________________________________________________________________
________________________________________________________________________________

###USING Simutron:


Circuit Simulator:

    Right-click:      context menu: open, save, etc.

    Drag-drop components from left-pane->Components
    to the circuit and create connectors by clicking on pins.
    
    Click+move components.
    Right-click on components: component context menu.
    Select single components and see/edit properties in left-pane->Properties tab
    
    Shift+click_on_empty: scroll circuit.
    Mouse_wheel:          zoom in/out.
    
    click_on_wire:        create node and init new wire.
    ctrl+click_on_wire:   move wire 

There are several ready-made example simulation projects shipped with simutron.
Look for files with .simu extention under bin and examples folders.
Simulation starts right after you open a simu file: no additional intervention required.
Look for additional information on the simutron wiki page:
	https://sourceforge.net/p/simutron/wiki/Home/

________________________________________________________________________________


