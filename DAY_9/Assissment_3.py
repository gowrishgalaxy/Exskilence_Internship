"""
Task 3 (Decorator) – Simple Problem Statement
Permission Checker

Problem:
Create a decorator to allow only admin users to access a function.

Requirements:
1. Create a decorator named admin_only.
2. If username is "admin", allow function execution.
3. Otherwise, print "Access Denied".
4. Apply the decorator to dashboard().
5. Test with admin and non-admin users.
"""


def admin_only(func):
    def wrapper(username):
        if username == "admin":
            func(username)
        else:
            print("Access Denied")
    return wrapper


@admin_only
def dashboard(username):
    print("Welcome to Admin Dashboard")


# Test cases
dashboard("admin")
dashboard("user")
