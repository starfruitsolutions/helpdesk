# helpdesk
custom helpdesk tray
To build:
Compile the python to EXEs using pyinstaller
Edit the installer script for inno setup to point to your compiled resources
remove "skipifsilent" to run after a silent install
Compile using inno setup to create installer
A silent install can be executed with /VERYSILENT /NOCANCEL
