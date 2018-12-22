from sklearn.cluster import KMeans
from clustering_viz.clustering.core.IClusteringAlgorithm import *
from sklearn import datasets



class KMeansAlgorithm ( IClusteringAlgorithm ) :

	def __init__( self, data, params ) :
		super( KMeansAlgorithm, self ).__init__( data, params )
		self.params = params
		# define some specific kmeans algorithm properties ...
		# like objects from sklearn, etc.	




	def _runAlgorithm( self ) :
		kmean = KMeans(n_clusters= self.params['kmeans'])
		kmean.fit(self.m_data)
		self.m_resultLabels = kmean.labels_
		pass

#test = KMeansAlgorithm([1,2,3], {'a':'b'})
#print(test._runAlgorithm())
