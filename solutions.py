#! /usr/bin/python

def Question1(s,t):
    """Given two strings s and t, determine whether some anagram of t is a substring of s. For example: if s = "udacity" and t = "ad", then the function returns True. Your function definition should look like: question1(s, t) and return a boolean True or False."""

    if len(s)==0 or len(t)==0:
        return False
    s_len=len(s)
    t_len=len(t)
    t_sort=sorted(t)
    for start in range(s_len-t_len+1):
        if t_sort == sorted(s[start:start+t_len]):
            return True
    return False


def Question2(a):
    """Given a string a, find the longest palindromic substring contained in a. Your function definition should look like question2(a), and return a string."""
    if len(a) == 0:
        return "No String found"
    s='$*'+'*'.join(a)+'*#'
    p=[0]*len(s)
    mirr,C,R,maxLPSIndex,maxLPS=0,0,0,0,0  #mirror #centerPositio #centerRightPosition
    for i in range(1,len(s)-1):
        mirr= 2 * C - i
        if R > i:
            p[i]=min(R - i,p[mirr])
        while s[i+(p[i]+1)] == s[i - (p[i]+1)]:
            p[i]+=1
        if i + p[i] > R:
            C = i
            R = i+p[i]
        if p[i] > maxLPS:
            maxLPS=p[i]
            maxLPSIndex=i
    return "Input String :{} \n Longest Palindromic SubString {}".format(a,s[maxLPSIndex - p[maxLPSIndex]:maxLPSIndex + 1 +p[maxLPSIndex]].replace('*',''))

import collections

parent=dict()
rank=dict()

def make_set(vertex):
    parent[vertex]=vertex
    rank[vertex]=0


def find_set(vertex):
    if parent[vertex] != vertex:
        parent[vertex]= find_set(parent[vertex])
    return parent[vertex]


def union(vertex1,vertex2):
    parent1=find_set(vertex1)
    parent2=find_set(vertex2)
    if parent1 != parent2:
        if rank[parent1] > rank[parent2]:
            parent[parent2]=parent1
        elif rank[parent1] < rank[parent2]:
            parent[parent1]=parent2
        else:
            parent[parent2]=parent1
            rank[parent1] +=1


def get_edges(adj):
    edge_list=[]
    for vertex,edges in adj.iteritems():
        for edge in edges:
            if vertex < edge[0]:
                edge_list.append((edge[1],vertex,edge[0]))
    return edge_list


def Question3(G):
    """Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list structured like this:"""
    if not bool(G) :
        return "Wrong Graph input"
    for vertex in  G.keys():
        make_set(vertex)
    edges=get_edges(G)
    MST=set()
    edges.sort()
    for weight,vertex1,vertex2 in edges:
        if find_set(vertex1) != find_set(vertex2):
            union(vertex1,vertex2)
            MST.add((weight,vertex1,vertex2))
    adj=collections.defaultdict(list)
    for edge in MST:
        weight=edge[0]
        vertex1=edge[1]
        vertex2=edge[2]
        adj[vertex1].append((vertex2,weight))
    return dict(adj)

Graph1={'A': [('B', 2)],
         'B': [('A', 2), ('C', 5)],
          'C': [('B', 5)]}
Graph2={}
Graph3={'A':[('B',6),('C',8),('D',8)],
        'B':[('C',7),('D',9)],
        'C':[('D',4),('A',8),('B',7)],
        'D':[('B',9),('C',4),('A',8)]}
Graph4={'A': [('B', 2), ('C', 5)],
        'B': [('A', 2), ('C', 4)],
        'C': [('A', 5), ('B', 4)]}

class Element(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST(object):
    def __init__(self,root):
        self.root=Element(root)
    def insert(self,new_val):
        self.insert_helper(self.root,new_val)

    def insert_helper(self,current,new_val):
        if current.data<new_val:
            if current.right:
                self.insert_helper(current.right,new_val)
            else:
                current.right=Element(new_val)

        else:
            if current.left:
                self.insert_helper(current.left,new_val)
            else:
                current.left=Element(new_val)

def lca(root,n1,n2):
    if root is None:
        return None
    if root.data > max(n1,n2):
        return lca(root.left,n1,n2)
    elif root.data < min(n1,n2):
        return lca(root.right,n1,n2)
    else: return root.data

def Question4(T,r,n1,n2):
    """
    Find the least common ancestor between two nodes on a binary search tree. The least common ancestor is the farthest node from the root that is an ancestor of both nodes. For example, the root is a common ancestor of all nodes on the tree, but if both nodes are descendents of the root's left child, then that left child might be the lowest common ancestor. You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties. The function definition should look like question4(T, r, n1, n2), where T is the tree represented as a matrix, where the index of the list is equal to the integer stored in that node and a 1 represents a child node, r is a non-negative integer representing the root, and n1 and n2 are non-negative integers representing the two nodes in no particular order. For example, one test case might be
    """
    if not T:
        return None
    bst=BST(r)
    for row in reversed(range(len(T))):
        for node in range(len(T[row])):
            if T[row][node] == 1:
                bst.insert(node)
    return lca(bst.root,n1,n2)

T=[[0, 1, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[1, 0, 0, 0, 1],[0, 0, 0, 0, 0]]
T2=[
[0,0,0,0],
[1,0,0,0],
[0,1,0,1],
[0,0,0,0]]
T3=[]
T4=[[0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0]]

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList(object):
    def __init__(self,head=None):
        self.head=head
    def append(self,new_element):
        current=self.head
        if self.head:
            while current.next:
                current=current.next
            current.next=Node(new_element)
        else: self.head=Node(new_element)

def Question5(ll,m):
    if type(m) is not int or m <=0:
        return "wrong value of m"
    pointer1=ll
    pointer2=ll
    count=1
    while count < m:
        pointer1=pointer1.next
        count+=1
    while pointer1.next:
        pointer1=pointer1.next
        pointer2=pointer2.next
    return pointer2.data

ll= LinkedList(Node("0"))
ll.append("1")
ll.append("2")
ll.append("3")
ll.append("4")
ll.append("5")
ll.append("6")
ll.append(7)

# Driver code
print Question1("abdc","abd")
# True
print Question1(""," ad")
# False
print Question1(""," ")
# False
print "============================="
print Question2("abababa")
# LongestPalindromicSubstring "abababa"
print Question2("abacdfgdcaba")
# LongestPalindromicSubstring "aba"
print Question2("")
# LongestPalindromicSubstring "No String found"
print Question2("abcdefgh")
# LongestPalindromicSubstring "a"

print "============================="
print Question3(Graph1)
# {'A': [('B', 2)], 'C': [('B', 5)], 'B': [('C', 5), ('A', 2)]}
print Question3(Graph2)
# Wrong Graph input
print Question3(Graph3)
# {'A': [('B', 6)], 'C': [('D', 4)], 'B': [('C', 7)]}
print Question3(Graph4)
# {'A': [('B', 2)], 'B': [('C', 4)]}

print "============================="
print Question4(T,3,1,4)
# 3
print Question4(T2,2,1,0)
# 1
print Question4(T3,1,1,1)
# None
print Question4(T4,3,1,2)
# 1

print "============================="
print Question5(ll.head,2) #print 6
print Question5(ll.head,-1) # print "wrong value of m"
print Question5(ll.head,8) # print 0
