About this example project:
__________________________________

This is a full source of Code::Blocks project demonstrating
an AVR firmware with menu system for standard 16x4 LCD.
This project uses slightly modified (for conformance with newer avr-gcc) version 
of Roberto Brunialti's MENWIZ avr menu library.
Look original version there: https://github.com/brunialti/MENWIZ.git.


Configuring compiler, libraries and Code::Blocks IDE
______________________________________________________

Requires Arduino IDE/SDK 1.6.12 for compiler and libraries - download it
and unpack into your home folder.
In Code::Blocks IDE under Settings/Compiler make copy of "GNU AVR GCC Compiler" item
and name it "Debug Arduino 1.6.12 GNU AVR GCC Compiler",
then go to "Toolchain executables" tab and set "Compiler's installation directory"
to <your home dir>/arduino-1.6.12/hardware/tools/avr .
Add the folowing lines into "Additional Paths":
	<your home dir>/arduino-1.6.12/hardware/tools/avr/libexec/gcc/avr/4.9.2
	<your home dir>/arduino-1.6.12/hardware/tools/avr/libexec/gcc/avr/4.9.2/plugin
	<your home dir>/arduino-1.6.12/hardware/tools/avr/libexec/gcc/avr/4.9.2/install-tools
	<your home dir>/arduino-1.6.12/hardware/tools/avr/avr/bin
Also on the "Search directories" tab remove any directories listed under "Compiler" and "Linker".
Also on the "Other settings" tab press "Advanced options.." and ensure that
"command line macro" under "Link object files to executable" and "Link object files to console executable"
doesn't contain any -s -Os -O0 .. -O3 options.
Also on the "Compiler Flags" tab uncheck corresponding option flags.

You need to configure avr-gdb yet - look for more instructions here:
https://sourceforge.net/p/simutron/wiki/About%20avr-gdb/

After that you Code::Blocks IDE is ready to build debuggable AVR firmware image
and run it under debugger with help of simavr/simutron.


Adjust project settings
__________________________________

Open LCD20x4Test.cbp project in Code::Blocks IDE, go to Project/"Build options.."
On the "Custom variables" tab of top LCD20x4Test item set ARDUINO_DIR value to <your home dir>/arduino-1.6.12 .
Verify compilation of Debug target.


Start debugging session
________________________
Open LCD20x4Test.simu file in simutron IDE, verify firmware in action.
Press "Gdb" button on the processor symbol to activate GDB host.
Go to Code::Blocks IDE, set breakpoints in source files where desired,
e.g. inside the "void act()" function in LCD20x4Test.cpp file.
Press Debug/Continue button or F8. Debugger will break immediately
in some arbitrary place. Press F8 again.
Go to simutron IDE, using up, down and confirm buttons in the simulation,
navigate to "WRITE TO SERIAL" submenu and activate it's action.
Debugger will break on your breakpoint. Notice the processor symbol
in simulation will change to dark-gray at the same time to indicate the
pause due to breakpoint.
Set another breakpoint inside msc() function, press F8 again. After
some period, a breakpoint at msc() function will be triggered. You can evaluate
variables, set more breakpoints, step through the code, etc.
