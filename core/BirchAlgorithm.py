from sklearn.cluster import Birch
from clustering_viz.clustering.core.IClusteringAlgorithm import *
from sklearn import datasets



class BirchAlgorithm ( IClusteringAlgorithm ) :

	def __init__( self, data , params ) :
		super( BirchAlgorithm, self ).__init__( data, params )
		self.params = params
		# define some specific kmeans algorithm properties ...
		# like objects from sklearn, etc.

	

	def _runAlgorithm( self ) :
		birch = Birch(branching_factor=50, n_clusters=self.params['birch'], threshold=0.5)
		birch.fit(self.m_data)
		self.m_resultLabels = birch.labels_
		pass