from sklearn.cluster import MiniBatchKMeans
from clustering_viz.clustering.core.IClusteringAlgorithm import *
from sklearn import datasets



class MiniBatchKMeansAlgorithm ( IClusteringAlgorithm ) :

	def __init__( self, data, params ) :
		super( MiniBatchKMeansAlgorithm, self ).__init__( data, params )
		self.params = params
		# define some specific kmeans algorithm properties ...
		# like objects from sklearn, etc.	




	def _runAlgorithm( self ) :

		Agglomerative = MiniBatchKMeans(n_clusters= self.params['MiniBatchKMeansClustering']).fit(self.m_data)
		#core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
		#core_samples_mask[db.core_sample_indices_] = True
		#labels = db.labels_



		self.m_resultLabels = Agglomerative.labels_
		pass