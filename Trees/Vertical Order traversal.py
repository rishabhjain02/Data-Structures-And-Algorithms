"""

Vertical Order traversal
Problem Description

Given a binary tree, return a 2-D array with vertical order traversal of it. Go through the example and image for more details.

Image Link: https://i.imgur.com/MazRrBA.jpeg

NOTE: If 2 Tree Nodes shares the same vertical level then the one with lesser depth will come first.



Problem Constraints
1 <= number of nodes <= 10^5



Input Format
First and only arument is a pointer to the root node of binary tree, A.



Output Format
Return a 2D array denoting the vertical order traversal of tree as shown.



Example Input
Input 1:

      6
    /   \
   3     7
  / \     \
 2   5     9
Input 2:

      1
    /   \
   3     7
  /       \
 2         9


Example Output
Output 1:

 [
    [2],
    [3],
    [6, 5],
    [7],
    [9]
 ]
Output 2:

 [
    [2],
    [3],
    [1],
    [7],
    [9]
 ]


Example Explanation
Explanation 1:

 First row represent the verical line 1 and so on.

"""

# Definition for a  binary tree node
# class TreeNode:
# 	def __init__(self, x):
# 		self.val = x
# 		self.left = None
# 		self.right = None

from collections import defaultdict, deque

def vertical_order(root, hash_map):
    min_dist = 0
	max_dist = 0
	# For storing horizontal distance of each node w.r.t. root node
	hd_map = defaultdict(int)
	queue = deque()
	
	# Horizontal distance of root node is 0
	hd_map[root] = 0
	hash_map[0] = [root.val]
	queue.append(root)
	    
	while len(queue) > 0:
	    node = queue.popleft()
	        
	    if node.left != None:
	        left_child = node.left
	        queue.append(left_child)
	        hd_map[left_child] = hd_map[node] - 1
	        hr_dist = hd_map[left_child]
	        min_dist = min(min_dist, hr_dist)
	        hash_map[hr_dist].append(left_child.val)
	            
	    if node.right != None:
	        right_child = node.right
	        queue.append(right_child)
	        hd_map[right_child] = hd_map[node] + 1
	        hr_dist = hd_map[right_child]
	        max_dist = max(max_dist, hr_dist)
	        hash_map[hr_dist].append(right_child.val)
    
    return min_dist, max_dist
    

class Solution:
	# @param A : root node of tree
	# @return a list of list of integers
	def verticalOrderTraversal(self, A):
	    if A == None:
	        return []
	        
	    ans = []
	    # For storing same distance node together 
	    # e.g. 1: [n1, n2, n3] i.e. n1, n2 and n3 nodes have 1 distance w.r.t. root
	    hash_map = defaultdict(list)
	    
	    min_dist, max_dist = vertical_order(A, hash_map)
	    
	    for i in range(min_dist, max_dist+1):
	        ans.append(hash_map[i])
	        
	    return ans

        
        