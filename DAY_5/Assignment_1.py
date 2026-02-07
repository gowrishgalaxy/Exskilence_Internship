"""
Task:
1. Create one object of InstagramAccount
2. Add at least 2 private reels
3. Add at least 2 archived reels
4. Display private reels as follower and non-follower
5. Display archived reels using correct and wrong password
"""

class InstagramAccount:
    def __init__(self, username, archive_password):
        self.username = username
        self.__private_reels = []
        self.__archived_reels = []
        self.__archive_password = archive_password

    # Add reels
    def add_private_reel(self, reel):
        self.__private_reels.append(reel)

    def add_archived_reel(self, reel):
        self.__archived_reels.append(reel)

    # Display private reels
    def display_private_reels(self, is_follower):
        if is_follower:
            print("Private Reels:")
            for reel in self.__private_reels:
                print("-", reel)
        else:
            print("Private reels are visible only to followers")

    # Display archived reels
    def display_archived_reels(self, password):
        if password == self.__archive_password:
            print("Archived Reels:")
            for reel in self.__archived_reels:
                print("-", reel)
        else:
            print("Wrong password. Cannot access archived reels")


# Create object
account = InstagramAccount("john_doe", "insta123")

# Add private reels
account.add_private_reel("Gym workout reel")
account.add_private_reel("Family trip reel")

# Add archived reels
account.add_archived_reel("Old college reel")
account.add_archived_reel("First post reel")

# Display private reels
print("\nAs follower:")
account.display_private_reels(is_follower=True)

print("\nAs non-follower:")
account.display_private_reels(is_follower=False)

# Display archived reels
print("\nWith correct password:")
account.display_archived_reels("insta123")

print("\nWith wrong password:")
account.display_archived_reels("wrongpass")
