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

"""
print Question1("abdc","abd")
# True
print Question1(""," ad")
# False
print Question1(""," ")
# False


print Question2("abababa")
# LongestPalindromicSubstring "abababa"
print Question2("abacdfgdcaba")
# LongestPalindromicSubstring "aba"
print Question2("")
# LongestPalindromicSubstring "No String found"
print Question2("abcdefgh")
# LongestPalindromicSubstring "a"

print Question3(Graph1)
# {'A': [('B', 2)], 'C': [('B', 5)], 'B': [('C', 5), ('A', 2)]}
print Question3(Graph2)
# Wrong Graph input
print Question3(Graph3)
# {'A': [('B', 6)], 'C': [('D', 4)], 'B': [('C', 7)]}
print Question3(Graph4)
# {'A': [('B', 2)], 'B': [('C', 4)]}
"""
