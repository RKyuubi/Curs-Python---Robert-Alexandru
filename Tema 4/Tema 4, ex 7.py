string_name = ("command = ‘platform: Solaris; version: 2.5; username: mcristi; all rights reserved to …’")
#list_created= string_name.split(";")

inceput_username = string_name.find("username:")

inceput_username += len("username:") #
sfarsit_username = string_name.find(";",inceput_username)

username = string_name[inceput_username:sfarsit_username].strip()
print (username)


