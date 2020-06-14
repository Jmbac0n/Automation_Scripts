import os, shutil

def main():

    desktop_src = 'C:/Users/Jake/AppData/Local/Programs/Python/Python38/MyScripts'
    laptop_src = 'C:/Users/user/AppData/Local/Programs/Python/Python38/MyScripts'
    usb_src = 'D:/MyScripts'

    print("""\
        *** Script Backup Utility ***
        
        Please select an option:

        1. Desktop to USB       2. USB to Desktop
        3. Laptop to USB        4. USB to Laptop
        """)

    user_input = input()

    def remove_old_backup(Destination):
        shutil.rmtree(Destination)

    def create_backup(Source, Destination):

        shutil.copytree(Source, Destination)

    def Desktop_to_USB():
        remove_old_backup(usb_src)
        create_backup(desktop_src, usb_src)

    def USB_to_Desktop():
        remove_old_backup(desktop_src)
        create_backup(usb_src, desktop_src)

    def Laptop_to_USB():
        remove_old_backup(usb_src)
        create_backup(laptop_src, usb_src)
    
    def USB_to_Laptop():
        remove_old_backup(laptop_src)
        create_backup(usb_src, laptop_src)

    success_message = ("Backup Sucessful")

    if user_input == ("1"):
        Desktop_to_USB()
        print(success_message)
    elif user_input == ("2"):
        USB_to_Desktop()
        print(success_message)
    elif user_input == ("3"):
        Laptop_to_USB()
        print(success_message)
    elif user_input == ("4"):
        USB_to_Laptop()
        print(success_message)
    else:
        print("Invalid Option")
        main()

main()

#TODO

