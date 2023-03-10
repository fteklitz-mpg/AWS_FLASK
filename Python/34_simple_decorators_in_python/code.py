# user = {"username": "Jose", "access_level": "guest"}
# user = {"username": "Jose", "access_level": "admin"}

def get_admin_password():
    return "1234"

# def secure_get_admin():
#     if user["access_level"] == "admin":
#         return "1234"

def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}."
        
    return secure_function
    
    
get_admin_password = make_secure(get_admin_password)
user = {"username": "Jose", "access_level": "admin"}   
print(get_admin_password())


