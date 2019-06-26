from sklearn.cluster import SpectralClustering
from clustering_viz.clustering.core.IClusteringAlgorithm import *
from sklearn import datasets



class SpectralAlgorithm( IClusteringAlgorithm ) :
	def __init__(self, data, params) :
		super(SpectralAlgorithm, self).__init__(data, params)
		self.params = params

	def _runAlgorithm( self) :
		spectral = SpectralClustering(n_clusters = self.params['spectral']  )
		spectral.fit(self.m_data)
		self.m_resultLabels = spectral.labels_
		pass

