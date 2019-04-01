from sklearn.cluster import KMeans
from clustering_viz.clustering.core.IClusteringAlgorithm import *
from clustering_viz.clustering.core.linear_algebra import squared_distance, vector_mean, distance

from sklearn import datasets
import random as random



class KMeansAlgorithm2 ( IClusteringAlgorithm ) :

	def __init__( self, data, params ) :
		super( KMeansAlgorithm2, self ).__init__( data, params )
		self.params = params
		self.means = None
		# define some specific kmeans algorithm properties ...
		# like objects from sklearn, etc.	



	def classify(self, input):
		"""return the index of the cluster closest to the input"""
		return min(range(self.params['kmeans']), key=lambda i: squared_distance(input, self.means[i]))



	def _runAlgorithm( self ) :
		#random.seed(0)
		self.means = random.sample(list(self.m_data), self.params['kmeans'])
		assignments = None

		while True:
			# Find new assignments
			new_assignments = list(map(self.classify, self.m_data))

			# If no assignments have changed, we're done.
			if assignments == new_assignments:
				self.m_resultLabels = assignments
				return 

			# Otherwise keep the new assignments,
			assignments = new_assignments

			for i in range(self.params['kmeans']):
				i_points = [p for p, a in zip(self.m_data, assignments) if a == i]
				# avoid divide-by-zero if i_points is empty
				if i_points:
					self.means[i] = vector_mean(i_points)
