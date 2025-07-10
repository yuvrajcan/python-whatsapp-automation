import pywhatkit
phone = input("Enter the phone number: ")
image_path = ('download.jpeg')
pywhatkit.sendwhats_image(phone, image_path, "xyz")