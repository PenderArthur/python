#!/usr/bin/python3
# -*- coding:utf-8 -*-

class Node(object):
	def __init__(self,value):
		#初始化节点
		self.value = value
		self.left = 0
		self.right= 0
class Tree(object):
	def __init__(self):
		self.root = 0
	def find(self,value):
		#按照值查找
		n = self.root
		if(root ==0):
			return 0
		while(n !=0):
			if(n.value == value):
				return n
			elif(n.value <value):
				n = n.right
			else:
				n = n.left
		return 0
	def insert(self,value):
		if(self.root == 0):
			self.root = Node(value)
			return
		#新增时要考虑是否有重复值，重复值当做大于
		n = self.root
		nP = 0
		while(n!=0):
			nP = n
			if(n.value >value):
				#这样子 else里面可能的就是 n.value<=value了
				n = n.left
			else:
				n = n.right
		n= Node(value)
		if(nP.value >value):
			nP.left = n
		else:
			nP.right = n
	def delete(self,value):
		#删除时要考虑三种情况，当然也要考虑重复值
		#1删除叶子节点 简单
		#2删除存在一个左孩子或者右孩子
		#3删除存在左右孩子的
		#4看了github上别人写的，你的错了一点了 https://github.com/wangzheng0822/algo/blob/master/python/24_tree/binary_search_tree.py
		n = self.root
		nParent = 0
		nPlist = []
		nList = []
		

		while(n!=0):
			
			if(n.value < value):
				nParent = n
				n = n.right
			elif(n.value>value):
				nParent = n
				n = n.left
			else:
				#print(nParent.value)
				nList.append(n)
				nPlist.append(nParent)
				nParent = n
				n = n.right
				
		if(len(nList) == 0):
			return 
		for i in range(len(nList)-1,-1,-1):
			n = nList[i]
			nParent = nPlist[i]
			#print(i)
			#print(n.value)
			#print(nParent.value)
			if(n.left != 0 and n.right != 0):
				#存在左右孩子
				minN = n.right
				while(minN.left != 0):
					minN = minN.left
				n.value = minN.value
				minN = 0
			else:
				child = 0
				if(n.left != 0):
					child = n.left
				elif(n.right != 0):
					child = n.right
				if(nParent == 0):
					self.root = child
				elif(nParent.left == n):
					nParent.left = child
				elif(nParent.right == n):
					nParent.right = child
def sout(n):
	if(n == 0):
		return 
	else:
		sout(n.left)
		print(n.value)
		sout(n.right)
tree = Tree()
tree.insert(5)
tree.insert(1)
tree.insert(2)
tree.insert(1)
tree.delete(1)
sout(tree.root)
