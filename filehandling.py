#1. a) Creating file with timestamp

#importing datetime module
from datetime import datetime

#creating a variable wchich holds current time
current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

#converting the date and time into string
str_current_datetime = str(current_datetime)

#creating file name with extension
file_name = str_current_datetime+".txt"
file = open(file_name, 'w')

print("File created : ", file.name)
file.close()

#1 b) The file content should have the content of current timestamp

#opening the file to write in it
f = open(file.name, "w")
f.write(current_datetime)
f.close()


#2 Write another function to read a text file. the function will take the name of the text file and the display the content of the file in the console
#reading the content inside the created file
f = open("hello.txt", "r")
print(f.read())
