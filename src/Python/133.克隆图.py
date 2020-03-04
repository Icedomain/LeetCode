#
# @lc app=leetcode.cn id=133 lang=python3
#
# [133] 克隆图
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        '''
        # BFS       
        queue = [node]
        copy_node = Node(node.val)
        visited = {node: copy_node}
        while queue:
            node = queue.pop(0)
            for i in node.neighbors:
                if i in visited:
                    visited[node].neighbors.append(visited[i])
                else:
                    copy_node_ne = Node(i.val)
                    visited[node].neighbors.append(copy_node_ne)
                    visited[i] = copy_node_ne
                    queue.append(i)
                    
        return copy_node
        '''
        # DFS     
        stack = [node]
        copy_node = Node(node.val)
        visited = {node: copy_node}
        while stack:
            node = stack.pop()
            for i in node.neighbors:
                if i in visited:
                    visited[node].neighbors.append(visited[i])
                else:
                    copy_node_ne = Node(i.val)
                    visited[node].neighbors.append(copy_node_ne)
                    visited[i] = copy_node_ne
                    stack.append(i)
                    
        return copy_node
        
