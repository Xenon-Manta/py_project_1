# Tools Project
Python project.


Environment (for consistency):
Python 3.7.x (I'm running 3.7.2)
Pip3 Package Manager (we can move to something more sophisticated soon) version 19.0.2 or newer (pip3 install --upgrade pip3)

Tools Currently in this Repo:
port_scan.py
  - Simple socket scan that pulls down the banner and dumps it to the terminal

ftp_bf.py
  - FTP login utility that attempts to brute force a login, first checking anonymous logins and then transitions to a     password file supplied as an argument
  
input_validation.py
  - Starting point of a script that is designed to be run in front of other tools to validate and sanitize inputs before passing arguments on to other tools (Work In Progress). This is an automation support script.
  
ELK_install.sh
  - Installs Elasticsearch and Logstash onto a Raspberry Pi for a mobile, fast, temporary logging platform.
