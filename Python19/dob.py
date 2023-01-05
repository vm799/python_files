# write a program that enables you to extract data from a text file  DOB.txt
#  Read the data stored
# print out data into 2 sections name and birthdate

contents_names = " " #intialising string to put data  into
contents_dob = " "

with open("DOB.txt", "r+") as f: # open the file
    for line in f:  #looping through each line of text
        contents_names += (" ".join((line.split())[0:2])) + "\n" #split each line into strings and select name and surname indices and add to the variable content_names
        contents_dob += (" ".join((line.split())[2:5])) + "\n" #same for birthdate data     

# bolded titles- Name and Birthdate as requested in question (referenced website below)
# .lstrip() to remove leading whitespace
print(f"""
      
\033[1mName\033[0m  
{contents_names.lstrip()} 

\033[1mBirthdate\033[0m 
{contents_dob.lstrip()}

""")

#f.close()  # ensuring file is closed not needed now as refactored 'with open (file, r+)

# struggled to open the file needed help here https://stackoverflow.com/questions/55191397/vscode-read-file-from-current-folder-where-py-file-is
#  help with printing 2 data lists from one file https://stackoverflow.com/questions/29117913/dividing-a-text-file-into-2-lists-using-python
# help with spacing https://sabe.io/blog/python-print-line-break#:~:text=The%20easiest%20way%20to%20use,be%20on%20a%20new%20line.
# knowing how to bold text https://appdividend.com/2022/07/27/how-to-print-bold-python-text/