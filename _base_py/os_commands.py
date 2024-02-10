# importing os module 
import os
  
# Add a new environment variable 
os.environ['GeeksForGeeks'] = 'www.geeksforgeeks.org'
  
# Get the value of
# Added environment variable 
print("GeeksForGeeks:", os.environ['GeeksForGeeks'])