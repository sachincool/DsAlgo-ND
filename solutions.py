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

def Question3(G):
    """Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list structured like this:"""



















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
"""
