import delivery

def sign_upAccount():
    user = {}
    
    user["name"] = input("Enter your name: ")
    user["password"] = input("Enter your password: ")
    
    confirm_password = input("Enter your confirm password: ")
    if user["password"] != confirm_password:
           return "Passwords do not match"
        
    
    user["phone_number"] = input("Enter your phone number: ")
    
    obj = delivery.mongodatabase()
    obj.save_user(user)

    print("User signed up successfully!")
    


    