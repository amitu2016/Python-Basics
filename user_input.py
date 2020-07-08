user_input = input("Enter Your Name: ")
message = "Hello %s" % user_input      ## First Way
message = f"Hello {user_input}"         ## Second Way


print(message)