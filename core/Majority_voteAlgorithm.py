from clustering_viz.clustering.core.IClusteringAlgorithm import *
from sklearn import datasets


class Majority_voteAlgorithm ( IClusteringAlgorithm ) :

	def __init__( self, data, params ) :
		super( Majority_voteAlgorithm, self ).__init__( data, params )
		self.params = params
		# define some specific kmeans algorithm properties ...
		# like objects from sklearn, etc.	




	def _runAlgorithm( self ) :
		#kmean = KMeans(n_clusters= self.params['kmeans'])
		#kmean.fit(self.m_data)
		self.m_resultLabels = self.params['Majority_voteAlgorithm']
		pass