"""
For the given code:
1. Add comments as a list of strings.
2. Add creator_name and location attributes.
3. Add display methods for comments, creator name, and location.
4. Ensure comments are stored as a list of strings.
"""

class Instagram:
    def __init__(self, title, description, creator_name, location):
        self.title = title
        self.description = description
        self.creator_name = creator_name
        self.location = location
        self.likes = 0
        self.comments = []

    def display_title(self):
        print("Title:", self.title)

    def display_description(self):
        print("Description:", self.description)

    def display_creator_name(self):
        print("Creator Name:", self.creator_name)

    def display_location(self):
        print("Location:", self.location)

    def display_likes(self):
        print("Likes:", self.likes)

    def add_like(self):
        self.likes += 1

    def add_comment(self, comment):
        self.comments.append(comment)

    def display_comments(self):
        if len(self.comments) == 0:
            print("No comments yet")
        else:
            print("Comments:")
            for c in self.comments:
                print("-", c)


# Object creation
reel1 = Instagram(
    "Travel Vlog",
    "Exploring mountains",
    "Arjun",
    "Manali"
)

# Method calls
reel1.display_title()
reel1.display_description()
reel1.display_creator_name()
reel1.display_location()

reel1.add_like()
reel1.display_likes()

reel1.add_comment("Amazing video")
reel1.add_comment("Beautiful place")
reel1.display_comments()
