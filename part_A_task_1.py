from datetime import datetime

class Post:
    """A class to represent a social media post"""
    def __init__(self, date_time, post, creator):
        # Initializing attributes of a post
        self.datetime = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")  # Time and Date of posting
        self.post_content = post  # The content of the post
        self.creator = creator  # The creator of the post (the user)

class HashTable:
    """A class to represent the hash table that will store the posts"""
    def __init__(self, size=200):
        self.size = size  # The size of the hash table (default is 200)
        # Initialize the hash table with empty lists for chaining
        # Chaining is a way to handle collision
        self.table = [[] for i in range(size)]

    def simple_hash(self, datetime_obj):
        """A simple function for hashing posts in the table"""
        key = datetime_obj.strftime("%Y%m%d")
        hash_value = 0
        for char in key:
            # Calculate the hash by summing the ASCII values of the characters in the date string
            hash_value += ord(char)
        return hash_value % self.size  # Use modulo to ensure the hash index fits within the table size

    def insert(self, datetime_obj, value):
        """This function inserts the posts in the hash table"""
        # Calculate the hash index for the given datetime object
        index = self.simple_hash(datetime_obj)
        # Store the post in the appropriate slot based on the index
        self.table[index].append((datetime_obj, value))

    def find(self, datetime_str):
        """This function returns the posts based on its datetime"""
        # Convert the datetime string to a datetime object
        datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
        # Find the correct slot using the hash function
        index = self.simple_hash(datetime_obj)
        bucket = self.table[index]  # Access the bucket
        results = []  # List to store the found posts
        for dt, post in bucket:
            # Check if the datetime object matches
            if dt == datetime_obj:
                results.append(post)  # Append the post to the results list
        # Return the results or a message indicating no posts were found
        return results if results else "No posts found."

class PostHandling:
    """A class to manage posts using a hash table for storage"""
    def __init__(self):
        # Initialize a HashTable to store posts
        self.posts_table = HashTable()

    def add_post(self, post):
        # Insert a new post into the hash table
        self.posts_table.insert(post.datetime, post)

    def find_post_by_datetime(self, datetime_str):
        # Retrieve posts by datetime
        result = self.posts_table.find(datetime_str)
        if result == "No posts found.":
            print(result)
        else:
            # Print details of all posts found
            num_posts = len(result)
            print(f"Number of posts found at {datetime_str}: {num_posts}\n")
            for i, post in enumerate(result, start=1):
                print(f"Post {i}:")
                print(f"Datetime: {post.datetime}\nPost: {post.post_content}\nUser: {post.creator}\n")



post_1 = Post("2024-04-15 09:00:00", "Good morning everyone", "User10")
post_2 = Post("2024-04-15 10:00:00", "Post content", "User255")
post_3 = Post("2024-04-15 10:00:00", "Another post at the same time!", "User3")
# Test Cases
if __name__ == "__main__":
    handler = PostHandling()
    handler.add_post(post_1)
    handler.add_post(post_2)
    handler.add_post(post_3)

    print("Test Case 1: ")
    handler.find_post_by_datetime("2024-04-15 10:00:00")

    print("Test Case 2: ")
    handler.find_post_by_datetime("2024-04-16 12:00:00")

