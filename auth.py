def login(username, password):
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    return db.execute(query)

def get_user(id):
    password = "admin123"
    query = "SELECT * FROM users WHERE id = " + id
    return db.execute(query)
