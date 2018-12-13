from sklearn.metrics import silhouette_score
from math import pow
from collections import defaultdict
import numpy as np


def distance(x, y):
	s = 0
	n = len(x)
	for i in range(n-1):
		s = s + pow((x[i] -y[i]), 2)

	return pow(s, 1/n)


def centroid(s):
	n = len(s)
	c = 0
	for i in s:
		c = c+i
	c = c/n 
	return c


def silhouette_metric(data, label):                                                                 
	return silhouette_score( data, label , metric='euclidean', sample_size=None, random_state=None )


def Sum_Squared_Within(data, label):
	data2 = np.array(data)
	n = len(data2)
	set_label = set(label)
	frequency =  defaultdict(list)
	for i in range(n):
		frequency[ label[i] ].append( data2[i] )
	#print(frequency) 
	dict_cluster = {}
	for key, value in frequency.items():
		dict_cluster[key] = value
	#print(dict_cluster)

	dict_cent = {}
	for i in dict_cluster.keys():
		c = 0
		for j in dict_cluster[i]:
			c = c+j
		c = c/len(dict_cluster[i]) 
		dict_cent[i] = c
	#print(dict_cent)

	sse = 0
	for i in dict_cluster.keys():
		for j in dict_cluster[i]:
			sse = sse + distance(dict_cent[i], j)
	return sse



def Sum_Squared_Between(data, label):
	data2 = np.array(data)
	n = len(data2)
	set_label = set(label)
	frequency =  defaultdict(list)
	for i in range(n):
		frequency[ label[i] ].append( data2[i] )
	dict_cluster = {}
	for key, value in frequency.items():
		dict_cluster[key] = value
	dict_cent = {}
	for i in dict_cluster.keys():
		c = 0
		for j in dict_cluster[i]:
			c = c+j
		c = c/len(dict_cluster[i]) 
		dict_cent[i] = c

	x_med = 0
	for i in range(n):
		x_med = x_med + data2[i]
	x_med = x_med/n

	ssb = 0
	for i in dict_cluster.keys():
		ssb = ssb + len(dict_cluster[i])*(distance(dict_cent[i], x_med)**2)

	return ssb
