def pass_controller(password):
    if len(password) < 8:
        return False
    
    else:
        return True 

print(pass_controller("Hello"))