from datetime import datetime
from part_A_task_1 import Post


class Node:
    """A node in the binary search tree for storing posts"""

    def __init__(self, post):
        self.post = post  # The social media post object
        self.left = None  # Pointer to the left child node
        self.right = None  # Pointer to the right child node


class BinarySearchTree:
    """A binary search tree to manage posts based on datetime"""

    def __init__(self):
        self.root = None  # Root of the binary search tree

    def insert(self, post, node=None):
        # If the root node is empty, make the new post the root
        if self.root is None:
            self.root = Node(post)
            return
        # Start from the root node if no specific node is provided
        if node is None:
            node = self.root
        # Recursive insertion
        if post.datetime < node.post.datetime:
            if node.left is None:
                node.left = Node(post)  # checking if the new post time is less than the current node's time and if the left node is empty. If yes, insert it to its left
            else:     # if the left node is not empty,
                self.insert(post, node.left)    # Recursively insert into the left subtree
        else:
            if node.right is None:        # Place the new post in the right subtree if it's later or equal to the current node
                node.right = Node(post)
            else:
                self.insert(post, node.right)  # Recursively insert into the right subtree

    def find_range(self, start_str, end_str, node=None, results=None):
        """Returns all posts within the specified datetime range"""
        # Initialize results list and start from the root node if first call.
        if results is None:
            results = []
        if node is None:
            node = self.root   # Start from the root node if no specific node is provided
            if node is None:
                return results  # Return empty list if the tree is empty.

        # defining the start datetime and end datetime
        start_datetime = datetime.strptime(start_str, "%Y-%m-%d %H:%M:%S")
        end_datetime = datetime.strptime(end_str, "%Y-%m-%d %H:%M:%S")

        # finding the posts in the specified datetime range
        if start_datetime <= node.post.datetime <= end_datetime:
            if node.left:  # If there is a left child, traverse into it to check earlier posts
                self.find_range(start_str, end_str, node.left, results)
            results.append(node.post)  # Add the current node's post if it falls within the range
            if node.right:  # If there is a right child, traverse into it to check later posts
                self.find_range(start_str, end_str, node.right, results)

        elif node.post.datetime < start_datetime:
            if node.right:  # Only traverse into the right child if the current node's datetime is less than the start datetime
                self.find_range(start_str, end_str, node.right, results)
        else:
            if node.left:  # Only traverse into the left child if the current node's datetime is greater than the end datetime
                self.find_range(start_str, end_str, node.left, results)
        return results  # Return the list of posts that were found within the range


# Test Cases
if __name__ == "__main__":
    post_manager = BinarySearchTree()

    # Inserting posts
    post_manager.insert(Post("2024-04-15 09:00:00", "Good morning everyone", "User10"))
    post_manager.insert(Post("2024-04-15 10:00:00", "This is Dubai Mall", "User255"))
    post_manager.insert(Post("2024-04-15 11:00:00", "It is raining", "User3"))
    post_manager.insert(Post("2024-04-16 15:00:00", "Good afternoon", "User10"))

   # Test case 1
    found_posts = post_manager.find_range("2024-04-15 09:00:00", "2024-04-15 11:30:00")
    print("Test Case 1: Posts on April 15, 2024 from 9:00 AM to 11:30 AM")
    for post in found_posts:
        print(f"Datetime: {post.datetime}, Post Content: {post.post_content}, Posted by: {post.creator}")

    # Test case 2
    found_posts = post_manager.find_range("2024-04-14 08:00:00", "2024-04-14 10:00:00")
    print("\nTest Case 2: Posts on April 14, 2024 from 8:00 AM to 10:00 AM")
    print("Expected: No posts found.")
    print(f"Actual: {'No posts found.' if not found_posts else 'Posts found!'}")

    # Test case 3
    found_posts = post_manager.find_range("2024-04-15 08:00:00", "2024-04-16 16:00:00")
    print("\nTest Case 3: Posts from April 15 (8 AM) to April 16 (4 PM), 2024")
    for post in found_posts:
        print(f"Datetime: {post.datetime}, Post Content: {post.post_content}, Posted by: {post.creator}")

