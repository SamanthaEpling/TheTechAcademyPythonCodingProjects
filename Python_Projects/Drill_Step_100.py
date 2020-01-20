# author: Samantha Epling
# January 19, 2020
# The Tech Academy, Python Course, Step 100, Drill

import os

fPath = 'C:\\Users\\Student\\Desktop\\GitHub\\TheTechAcademyPythonCodingProjects\\Python_Projects'
# for the purposes of demonstration, I am including my made up list
# of files in a directory I created
print(os.listdir(fPath))
# the actual drill assignment:
for file_name in os.listdir(fPath):
    if file_name.endswith(".txt"):        
        txtfile = file_name
        abPath = os.path.join(fPath, txtfile)
        print(abPath)
        print(os.path.getmtime(abPath))



