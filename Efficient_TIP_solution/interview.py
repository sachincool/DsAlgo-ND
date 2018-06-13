def getCharCount(s):
	charCount_s = {}
	for char in s:
		if char not in charCount_s:
			charCount_s[char] = 1
		else:
			charCount_s[char] += 1
	return charCount_s

def anagramTest(s, t):
	if type(s) != str or type(t) != str or len(s) == 0 or len(s) != len(t):
		#print('False: input error')
		return False
	else:
		charCount_s = getCharCount(s)
		charCount_t = getCharCount(t)
		if charCount_s == charCount_t:
			print('True: '+s+" is an anagram of "+t)
			return True
		return False

## QUESTION1: given 2 strings s and t, is some anagram of t a substring of s?
def question1(s, t):
	#check that s and t are strings, and s is longer than t
	if type(s) != str or type(t) != str or len(s) < len(t):
		print('False: Improperly formated input')
		return False
	else:
		#check if t contains letters not found in s
		for char in t:
			if char not in s:
				print('False: t contains letters not in s')
				return False
		#for each len(t) long substring of s, run anagram test
		for i in range(0, len(s)):
			if anagramTest(t, s[i:i+len(t)]):
				print("True: "+s[i:i+len(t)]+" is an anagram of "+t)
				return True
		print("False, no anagrams found")
		#if all anagram tests fail, return false
		return False

def testQ1():
	print("Q1 Test1: expected outcome True")
	question1("udacity", "ad")
	print("Q1 Test2: expected outcome False")
	question1("udacity", "aj")
	print("Q1 Test3: expected outcome False")
	question1("udacity", 2)
#s = s[ beginning : beginning + LENGTH]
testQ1()

def isPalindrome(s):
	return s[::-1] == s

### QUESTION2: give a string s, what is the longest panindromic substring (lps) of s?
def question2(s):
	lps = ""
	#check if s is a string
	if type(s) != str:
		print("Error: non-string input")
		return "Error: non-string input"
	elif len(s)<2:
		print("True: input length is 1 or 0")
		return s
	else:
		length = len(s)
		substrings = []
		for x in range(0, length):
			for y in range(x, length):
				if isPalindrome(s[x:y + 1]) and len(s[x:y + 1]) > len(lps):
					lps = s[x:y + 1]
		print("lps is "+lps)
		return lps

def testQ2():
	print("Q2 test 1, should print 'lps is racecar'")
	question2("driver racecarsdsadasgfdhgfsdsadsfgfdgjhgkguliuseweadsdadfghf")
	print("Q2 test 2, should print 'lps is dad'")
	question2("dad173123")
	print("Q2 test 3, should print 'Error: non-string input'")
	question2(1)

testQ2()
## QUESTION 3: Find minimum spanning tree of a graph

### isGraph function takes in a dictionary and determines whether it fits the format of a graph adjacency list as defined in the udacity assignment. Should return true for the above test graph.
def isGraph(g):
	if type(g) != dict:
		#print("input is not dict")
		return False
	else:
		for key in g:
			if type(key) is not int:
				return False
			if isinstance(type(g[key]), list):
				return False
			else:
				for i in range(0, len(g[key])):
					if type(g[key][i]) is not tuple:
						return False
	return True

##a nice, reasonably complex graph to test with. Source http://www.geeksforgeeks.org/greedy-algorithms-set-2-kruskals-minimum-spanning-tree-mst/
graph1 = {
    0:[(1,4),(7,8)],
    1:[(2,8),(0,4),(7,11)],
    2:[(1,8),(3,7),(5,4),(8,2)],
    3:[(2,7),(5,14),(4,9)],
    4:[(3,9),(5,10)],
    5:[(4,10),(3,14),(2,4),(6,2)],
    6:[(8,6),(5,2),(7,1)],
    7:[(6,1),(8,7),(1,11),(0,8)],
    8:[(7,7),(6,6),(2,2)]
}

graph1MST = {
    0:[(1,4),(7,8)],
    1:[(0,4)],
    2:[(3,7),(5,4),(8,2)],
    3:[(2,7),(4,9)],
    4:[(3,9)],
    5:[(2,4),(6,2)],
    6:[(5,2),(7,1)],
    7:[(6,1),(0,8)],
    8:[(2,2)]
}

graph2 = {1: [(2, 2)],
 1: [(1, 2), (3, 5)], 
 3: [(2, 5)]}

graph2MST = {1: [(2, 2)],
 1: [(1, 2), (3, 5)], 
 3: [(2, 5)]}

# Question3: Find minimum spanning tree for undirected weighted graph
# Solution inspired by (nothing copied from) GeneDer's solution on Github https://github.com/GeneDer/Technical-Interview/blob/master/Solutions.py
def question3(g):
	#check that the input is a properly formatted graph adjacency tree
	if not isGraph(g):
		print("The input graph is not properly formatted")
		return False
	#get node set
	nodes = g.keys()
	#get edge set
	edges = set()
	for x in nodes:
		for y in g[x]:
			if x > y[0]:
				edges.add((y[1], y[0], x))
			elif x < y[0]:
				edges.add((y[1], x, y[0]))
	# sort edges
	edges = sorted(list(edges))
	# loop through edges and store only those which do not create cycles with disjoin set/union find algorithm
	mst_edges = []
	x = 0
	nodes = list(nodes)
	for node in nodes:
		nodes[x] = set([node])
		x += 1
	for x in edges:
		# get indices of both nodes
		for y in range(0, len(nodes)):
			if x[1] in nodes[y]:
				x1 = y
			if x[2] in nodes[y]:
				x2 = y
		# Store union in the smaller index and pop the larger. Append edge to mst_edges
		if x1 < x2:
			nodes[x1] = set.union(nodes[x1], nodes[x2])
			nodes.pop(x2)
			mst_edges.append(x)
		if x1 > x2:
			nodes[x2] = set.union(nodes[x1], nodes[x2])
			nodes.pop(x1)
			mst_edges.append(x)
		# break loop when all nodes are in one graph
		if len(nodes) == 1:
			break
	#  put mst in proper format
	mst = {}
	for x in mst_edges:
		if x[1] in mst:
			mst[x[1]].append((x[2], x[0]))
		else:
			mst[x[1]] = [(x[2], x[0])]
		if x[2] in mst:
			mst[x[2]].append((x[1], x[0]))
		else:
			mst[x[2]] = [(x[1], x[0])]
	return mst

def testQ3():
	##Test case 1, input graph with cycles
	for key in list(graph1.keys()):
		for edge in question3(graph1)[key]:
			if edge not in graph1MST[key]:
				print("Q3 Test1 (Graph with cycles): fail")
		else:
			print("Q3 Test 1 (Graph with cycles): pass")
	##Test case 2, input graph with no cycles
	for key in list(graph2.keys()):
		for edge in question3(graph2)[key]:
			if edge not in graph2MST[key]:
				print("Q3 Test2 (Graph without cycles): fail")
		else:
			print("Q3 Test2 (Graph without cycles): pass")
	##Test case 3, non graph input
	if not question3(0):
		print("Q3 Test3 (non-graph input): Pass")
	else:
		print("Q3 Test3 (non-graph input): Fail")
testQ3()
#question3(graph)

############ Question 4 #####################
# Find least common ancestor (LCA) of two nodes in a binary search tree
def findChildren(n):
	children = []
	x = 0
	for each in n:
		if each == 1:
			children.append(x)
		x +=1 
	return children
print("findChildren: "+str(findChildren([0,0,1,1])))

def findRight(n):
	children = findChildren(n)
	return children[-1]

def findLeft(n):
	children = findChildren(n)
	return children[0]

print("Find Right: "+ str(findRight([0,0,1,1])))
print("Find Left: "+ str(findLeft([0,0,1,1])))

def question4(m, r, n1, n2):
	nodeIndex = r
	root = m[nodeIndex]
	# make sure n1 and n2 are integers
	if type(n1) != int:
		return "n1 not int"
	if type(n2) != int:
		return "n2 not int"
	#Traverse tree starting at root
	current_node = root
	print("Node: "+str(current_node))
	while findLeft(current_node) != None or findRight(current_node) != None: 
		try:
			# if the current node is greater than both n1 and n2, go left
			if nodeIndex > n1 and nodeIndex > n2:
				nodeIndex = findLeft(current_node)
				current_node = m[nodeIndex]
			# if the current node is less than both n1 and n2, go left
			elif nodeIndex < n1 and nodeIndex < n2:
				nodeIndex = findRight(current_node)
				current_node = m[nodeIndex]
			# If the current node is between n1 and n2, the current node is the lca
			else:
				return nodeIndex
		except:
			break
	return nodeIndex
####Chain together node objects to construct a tree for test purposes

def test4():
	print("Q4 Test 1: LCA is root (should return 3)"+"\n"+str(question4([[0, 1, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[1, 0, 0, 0, 1],
		[0, 0, 0, 0, 0]],
		3,
		1,
		4)))

	print("Q4 Test 2: LCA is left of root (should return 2) "+"\n"+str(question4([
		[0,0,0,0,0,0],
		[1,0,0,0,0,0],
		[0,1,0,1,0,0],
		[0,0,0,0,0,0],
		[0,0,1,0,0,1],
		[0,0,0,0,0,0]],
		4,
		1,
		3)))

	print("Q4 Test 3: LCA is right of root (should return 4): "+"\n"+str(question4([
		[0,0,0,0,0,0],
		[1,0,0,0,0,0],
		[0,0,0,0,0,0],
		[0,1,0,0,1,0],
		[0,0,1,0,0,1],
		[0,0,0,0,0,0]
		],
		3,
		4,
		5)))

test4()

#####################Question 5######################
# Find element in a singly linked list which is m elements from the end.
class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None

#### String together a linked list: ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

n1 = Node("one")
n2 = Node("two")
n3 = Node("three")
n4 = Node("four")
n5 = Node("five")
n6 = Node("six")
n7 = Node("seven")
n8 = Node("eight")
n9 = Node("nine")
n10 = Node("ten")

n1.next = n2
n2.next = n3
n3.next= n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n9
n9.next = n10

def findLength(n):
	x = 1
	currentNode = n
	while currentNode.next != None:
		currentNode = currentNode.next
		x += 1
	return x

print(str(findLength(n1)))

def question5(n, m):
	if type(n) != Node:
		return "n is not a node object"
	if type(m) != int:
		return "m is not int"
	lengthList = findLength(n)
	currentNode = n
	x = 0
	while x < lengthList - m - 1:		
		currentNode = currentNode.next
		x += 1
	return currentNode.value

def testQ5():
	print("Q5 test1: m=6: expected outcome: 'four'")
	print(str(question5(n1, 6)))
	print("Q5 test2: m=0: outcome: 'ten'")
	print(str(question5(n1, 0)))
	print("Q5 test 3, n is not node. expected outcome: 'n is not a node object'")
	print(str(question5(1, 1)))
	print("Q5 test 4, m is not int. expected outcome: 'm is not int'")
	print(str(question5(n1, "1")))

testQ5()
