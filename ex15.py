from sys import argv
script,user_name = argv
prompt='> '
print("Hi ", user_name, "I m the", script," script.")
print("Do you like me ", user_name,"?")
likes = input(prompt)
print("Where do you live ", user_name," ?")
lives = input(prompt)
print("What kind of computer do you have ?")
computer = input(prompt)
print("Alright,so you said ", likes," about liking me.You live in", lives," Not sure that is " , computer," Nice.")


