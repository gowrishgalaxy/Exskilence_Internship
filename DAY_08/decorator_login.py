def login(decorated):
    def wrapper(user, password):
        if user == "admin" and password == "1234":
            print("Login successful")
            decorated(user, password)
        else:
            print("Login failed")
    return wrapper

@login
def login_page(user, password):
    print("welcome to the dashboard")

login_page("admin", "1234")
login_page("someone", "bad")
