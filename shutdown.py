# Python Script To Turn Off Your Computer

 # Python Library To Import 

import os 

# Function For Shutdown

def shutdown():
   
   # Gives Choice Whether To Shut Down Or Not 

   response = (input("Do you want to shutdown your computer (y/n)?:"))
   if response == 'n':
        print("You don't want to shutdown your computer! Please proceed with your day!")
   elif response == 'y':
        
# Command for shutting down Mac (this is an AppleScript that does the same job)

        os.system("osascript -e 'tell application \"System Events\" to shut down'")

# Calling For Function

shutdown()