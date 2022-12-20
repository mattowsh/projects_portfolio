Libraries:
- tkinter: a Python library for creating GUI applications

Methods:
- Tk():
- geometry():
- mainloop():
- Text():
- grid():
- delete():
- insert():
- Button():
- iconphoto():
- minsize and maxsize
- configure
- label



GUI
- concept: graphical user interface

errors in development:
<b>_tkinter.TclError: no display name and no $DISPLAY environment variable</b>
you are trying to run a program that uses a graphical user interface (GUI) on a computer that does not have a graphical display, or when the program is not being run in an environment that is able to display graphics.

the Tkinter library is unable to find a display to use for rendering the graphical elements of the program.

<b>Solution:</b>
in my case, I use a WSL (Windows Subsystem for Linux). to run GUI applications, you will need to install an X server on your Windows machine and configure WSL to use it. An X server is a program that provides the graphical display and input capabilities needed to run GUI applications.

X server in this project: VcXsrv (https://sourceforge.net/projects/vcxsrv/)
config:
- check the WSL IP value:
a) from console (windows): ipconfig command
b) from wsl directly: cat /etc/resolv.conf
to set the display variable: 
export DISPLAY=<wsl_ip>:<vcxsrv_value(like 0.0)>


comments:
- why use 'global calculation'?:



by https://www.youtube.com/watch?v=NzSCNjn4_RI&ab_channel=NeuralNine