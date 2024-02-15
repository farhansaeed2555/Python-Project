# Sample data - replace this with your actual social media data 
comments_data = [
    {"user": "user1", "comment": "Great post!", "likes": 100},
    {"user": "user2", "comment": "Interesting!", "likes": 70},
    # Add more comments here
]

# list to stor likes data 
likes_data = [5, 8, 12, 3, 7]   # Replace with your actual likes data

# Iterate through comment using a loop
for comment in comments_data:
    print(f"User: {comment['user']}")
    print(f"Comment: {comment['comment']}")
    print(f"Likes: {comment['likes']}")
    print("---")

# Iterate through likes using a loop
total_likes = 0
for like in likes_data:
    total_likes += like

print(f"Total Likes: {total_likes}")

# Dictionaries to store user information and activity
user_info = {
    "user1": {"name": "Farhan Saeed", "followers": 1000},
    "user2": {"name": "Saad Razzaq", "followers": 1500},
    # Add more user information here
}

# Access user information and activity using dictionaries
for user, info in user_info.items():
    print(f"User: {user}")
    print(f"Name: {info['name']}")
    print(f"Followers: {info['followers']}")
    # Add more user information if needed
    print("---")