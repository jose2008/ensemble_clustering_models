#from sklearn.mixture import GMM
from clustering_viz.clustering.core.IClusteringAlgorithm import *
from sklearn import mixture






class GmmAlgorithm( IClusteringAlgorithm ) :
	def __init__(self, data, params) :
		super(GmmAlgorithm, self).__init__(data, params)
		self.params = params


	def _runAlgorithm( self ) :
		#gmm = GMM(n_components = self.params['gmm'])
		gmm = mixture.GaussianMixture(n_components = self.params['gmm'])
		gmm.fit(self.m_data)
		self.m_resultLabels = gmm.predict(self.m_data)