#get respone from user
#save that response to a variable
#open your file for writing
#write response to file
#make sure file is closed

user_response = input("hello what is you favorite ride at Disney Land? ")
with open("response.txt", "w") as file:
    file.write(user_response)
