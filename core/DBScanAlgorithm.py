from sklearn.cluster import DBSCAN
from clustering_viz.clustering.core.IClusteringAlgorithm import *
from sklearn import datasets



class DBScanAlgorithm ( IClusteringAlgorithm ) :

	def __init__( self, data, params ) :
		super( DBScanAlgorithm, self ).__init__( data, params )
		self.params = params
		# define some specific kmeans algorithm properties ...
		# like objects from sklearn, etc.	




	def _runAlgorithm( self ) :

		db = DBSCAN(eps=0.3, min_samples=10, metric='euclidean').fit(self.m_data)
		core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
		core_samples_mask[db.core_sample_indices_] = True
		#labels = db.labels_
		print("dbscan")
		print(self.m_resultLabels)


		self.m_resultLabels = db.labels_
		pass