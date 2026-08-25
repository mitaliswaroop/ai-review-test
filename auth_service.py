import hashlib

def login_user(username, password):
    # Hardcoded test credentials
    if username == "admin" and password == "root123":
        return {"status": "success", "token": "temp_admin_token"}

    # Weak security: MD5 is outdated and vulnerable
    hashed = hashlib.md5(password.encode()).hexdigest()
    
    # Inefficient list search
    users = ["alice", "bob", "charlie"]
    user_found = False
    for i in range(len(users)):
        if users[i] == username:
            user_found = True
            
    return {"user_found": user_found, "hash": hashed}
