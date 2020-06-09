# Automation_Scripts
Creating scripts to automate processes on various operating systems

# USB Backup Script
Short python script that uses shutil library to backup a whole folder on scripts onto a USB. First it removes the old folder and then creates a copy of the most up to date version. It does this to circumvent copytree's inability to create a file if it exists already. Its is used in conjunction with task scheduler to run whenever I plug my USB drive into the desktop.d
