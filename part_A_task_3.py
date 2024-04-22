import heapq #imports module
from part_A_task_1 import Post, post_1, post_2, post_3

class Sm_priortize_views: #creating class
  """Class represents social media top views"""

  # contrusctor
  def __init__(self):
    self.topviews_posts=[] # empty list to store posts with views

  # methods
  def add_post(self,post,views): # method to push the data of the post into the list
      heapq.heappush(self.topviews_posts,(views,post.post_content,post.creator))

  # retrieves posts with the most views
  def sort_most_views_post(self,n): # method to retireve post with the most views
    if self.topviews_posts != []: #checks if the list is empty
      return heapq.nlargest(n,self.topviews_posts) #returns a post with the most views
    else:
      return "Empty, please add a post" # returns Empty if the list is empty


# Test Case 1: Empty post
priority_queue = Sm_priortize_views()
print(priority_queue.sort_most_views_post(1))

# Test Case 2: Single Post with top view
priority_queue.add_post(post_1, 1000)
priority_queue.add_post(post_2, 500)
priority_queue.add_post(post_3, 1500)
print(priority_queue.sort_most_views_post(1))

# Test Case 3: Multiple Posts with the top views
print(priority_queue.sort_most_views_post(3))