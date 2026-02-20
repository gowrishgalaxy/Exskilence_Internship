"""
Task:
1. Create one object of InstagramAccount
2. Add at least 2 private reels
3. Add at least 2 archived reels
4. Display private reels as follower and non-follower
5. Display archived reels using correct and wrong password
"""
class InstagramAccount:
    def __init__(self, user, password):
        self.user=user
        self._password=password
        self.__PrivateReel=[]
        self.__ArchivedReel=[]

    def add_private_reel(self, P_reel):
        self.__PrivateReel.append(P_reel)

    def add_archived_reel(self, A_reel):
        self.__ArchivedReel.append(A_reel)

    def show_private_reel(self, is_fallower):
        if is_fallower == ("fallow" or "fallowed"):
            print("User is fallowed")
            for i in  self.__PrivateReel:
                print("-", i)
        else:
            print("User is unfallowed")

    def show_archive_reel(self, password):
        if password == self._password:
            print("Correct password")
            for i in self.__ArchivedReel:
                print("-", i)
        else:
            print("Wrong password")



user = InstagramAccount("Arjun", "Arjun@123")

user.add_private_reel("PrivateReel_1")
user.add_private_reel("PrivateReel_2")

user.add_archived_reel("ArchiveReel_1")
user.add_archived_reel("ArchiveReel_2")

user.show_private_reel("fallow")
user.show_archive_reel("Arjun@123")

print()

user.show_private_reel("unfallow")
user.show_archive_reel("Arjun@111")
        