from sklearn.metrics import silhouette_score
from math import pow
from collections import defaultdict
import numpy as np
from scipy.spatial import distance as distance2
import math


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
	print("metrics.....")   
	s = silhouette_score( data, label , metric='euclidean', sample_size=None, random_state=None )
	print("silueta")
	print(s)
	if s<0: return 0.05                                                          
	return s# silhouette_score( data, label , metric='euclidean', sample_size=None, random_state=None )


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


	dict_cent = {}
	for i in dict_cluster.keys():
		c = 0
		for j in dict_cluster[i]:
			c = c+j
		c = c/len(dict_cluster[i]) 
		dict_cent[i] = c
	#print(dict_cent)

	sse = 0
	norm = []
	for i in dict_cluster.keys():
		sse = 0
		for j in dict_cluster[i]:
			sse = sse + distance(dict_cent[i], j)
			
		norm.append(sse)
	array_norm = []
	#print("testing error SOM")
	#print(len(norm))
	#print(len(dict_cluster.keys()))
	for i in dict_cluster.keys():
		array_norm.append( (norm[i]-min(norm))/(max(norm)-min(norm))   )
	return 1 - sum(array_norm)/len(array_norm)
	#return sse

'''
somelist =  [1,12,2,53,23,6,17] 
max_value = max(somelist)
min_value = min(somelist)
avg_value = sum(somelist)/len(somelist)
'''

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
	norm = []
	for i in dict_cluster.keys():
		ssb = 0
		ssb = ssb + len(dict_cluster[i])*(distance(dict_cent[i], x_med)**2)
		norm.append(ssb)
	array_norm = []
	#print(max(norm))
	#print(min(norm))
	for i in dict_cluster.keys():
		array_norm.append( (norm[i]-min(norm))/(max(norm)-min(norm))   )
	return sum(array_norm)/len(array_norm)
	#return ssb




def root_mean_square(data, label):
	"""
	The Root-Mean-Square Standard Deviation (RMSSTD), the root mean square
	standard deviation of all variables within each cluster. A measure of
	connectedness.
	"""
	#self.description = "The Root-Mean-Square Standard Deviation (RMSSTD), a measure of connectedness"
	data = np.array(data)
	numCluster=max(label)+1
	attributes=len(data[0])
	denominator=attributes*(len(data)-numCluster)
	normSum=0
	#iterate through all the clusters
	for i in range(numCluster):
		indices=[t for t, x in enumerate( label ) if x == i]
		clusterMember=data[indices,:]
		#compute the center of the cluster
		clusterCenter=np.mean(clusterMember,0)
		#compute the square error for every member in the cluster
		for member in clusterMember:
			normSum=normSum+distance2.euclidean(member, clusterCenter)
	validation = math.sqrt(normSum/denominator)
	return validation




def r_squared(data, label):
	"""
	R-squared, a statistical measure of how close the data is to a fitted regression line.
	A measure of compactness.
	"""
	#self.description = "R-squared, a measure of compactness"
	#compute the center of the dataset
	data = np.array(data)
	dataCenter=np.mean(data,0)
	numCluster=max(label)+1
	normClusterSum=0
	normDatasetSum=0
	#iterate through all the clusters
	for i in range(numCluster):
		indices=[t for t, x in enumerate(label) if x == i]

		clusterMember=data[indices,:]
		#compute the center of the cluster
		clusterCenter=np.mean(clusterMember,0)
		#compute the norm for every member in the cluster with cluster center and dataset center
		for member in clusterMember:
			normClusterSum=normClusterSum+distance2.euclidean(member, clusterCenter)
			normDatasetSum=normDatasetSum+distance2.euclidean(member, dataCenter)
	#compute the fitness
	validation = (normDatasetSum-normClusterSum)/normDatasetSum
	return validation





def Baker_Hubert_Gamma(data, label):
	"""
	Baker-Hubert Gamma Index: A measure of compactness, based on similarity between points in a cluster, compared to similarity
	with points in other clusters
	"""
	#self.description = 'Gamma Index: a measure of compactness'
	splus=0
	sminus=0
	pairDis=distance2.pdist(data)
	numPair=len(pairDis)
	temp=np.zeros((len(label),2))
	temp[:,0]=label
	vecB=distance2.pdist(temp)
	#iterate through all the pairwise comparisons
	for i in range(numPair-1):
		for j in range(i+1,numPair):
			if vecB[i]>0 and vecB[j]==0:
				#heter points smaller than homo points
				if pairDis[i]<pairDis[j]:
					splus=splus+1
				#heter points larger than homo points
				if pairDis[i]>vecB[j]:
					sminus=sminus+1
			if vecB[i]==0 and vecB[j]>0:
				#heter points smaller than homo points
				if pairDis[j]<pairDis[i]:
					splus=splus+1
				#heter points larger than homo points
				if pairDis[j]>vecB[i]:
					sminus=sminus+1
	#compute the fitness
	validation = (splus-sminus)/(splus+sminus)
	return validation


def Banfeld_Raferty(self):
		""" Banfeld-Raferty index is the weighted sum of the logarithms of the traces of the variance-covariance matrix of each cluster"""
		self.description = 'Weighted sum of the logarithms of the traces of the variance-covariance matrix of each cluster'
		sumTotal=0
		numCluster=max(self.classLabel)+1
		#iterate through all the clusters
		for i in range(numCluster):
			sumDis=0
			indices=[t for t, x in enumerate(self.classLabel) if x == i]
			clusterMember=self.dataMatrix[indices,:]
			#compute the center of the cluster
			clusterCenter=np.mean(clusterMember,0)
			#iterate through all the members
			for member in clusterMember:
				sumDis=sumDis+math.pow(distance.euclidean(member, clusterCenter),2)
			if sumDis/len(indices) <= 0:
				warnings.warn('Cannot calculate Banfeld_Raferty, due to an undefined value', UserWarning)
			else:
				sumTotal=sumTotal+len(indices)*math.log(sumDis/len(indices))
		#return the fitness
				self.validation = sumTotal
		return self.validation
