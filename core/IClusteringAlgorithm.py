#CCI #: 00221513745718003027
import numpy as np
from sklearn.metrics import silhouette_score
#from clusteringMetric import *
from sklearn.decomposition import PCA as sklearnPCA
from sklearn.preprocessing import StandardScaler
import numpy as np
from clustering_viz.clustering.core.clusteringMetric import *



class IClusteringAlgorithm ( object ) :


	def __init__( self, data, params ) :
		super( IClusteringAlgorithm, self ).__init__()

		# numpy array with the dataset
		self.m_data = data
		# metrics results as a dictionary
		self.m_resultMetrics = {  }
		# labels return after applying clustering
		self.m_resultLabels = []
		# clustering algorithm params
		self.m_params = params


	def _runAlgorithm( self ) :
		raise NotImplementedError( 'ERROR> virtual method' )


	def _computeMetrics( self ) :
		# define here all common metrics

		# aqui ya tenemos los labels    
		# entonces ya podemos calcular :

		# metric 1: siloutte coefficient
		# self.m_resultMetrics['silouette'] = sklearn.computesiloutte(self.m_data,self.m_labels)
		# metric 1: 
		#silhouette_score(X, labels, metric=’euclidean’, sample_size=None, random_state=None, **kwds)
		#print( silhouette_score( self.m_data.data, self.m_resultLabels , metric='euclidean', sample_size=None, random_state=None ) )
		# metric 2 : ????
		#print( Sum_Squared_Within( self.m_data.data, self.m_resultLabels) )

		#print( Sum_Squared_Between( self.m_data.data, self.m_resultLabels) )

		#print( Sum_Squared_Within(self.m_data.data, self.m_resultLabels ) )

		self.m_resultMetrics['silhouette_score']    = silhouette_score(   self.m_data.data,   self.m_resultLabels , metric='euclidean', sample_size=None, random_state=None )
		self.m_resultMetrics['Sum_Squared_Within']  = Sum_Squared_Within( self.m_data.data,   self.m_resultLabels)
		self.m_resultMetrics['Sum_Squared_Between'] = Sum_Squared_Between(self.m_data.data,   self.m_resultLabels)


		# metric 3 : ????

		# metric 4 : ????

		pass

	def run( self ) :
		# run the specific algorithm
		self._runAlgorithm()
		# update metrics
		self._computeMetrics()

	def updateAlgorithmParams( self, params ) :
		self.m_params

	def updateDataset( self, data ) :
		self.m_data = data

	def getResultsLabels( self ) :
		return self.m_resultLabels

	def getResultsMetrics( self ) :
		return self.m_resultMetrics

	def getData( self ) :
		return self.m_data


	def getDataScatter(self):
		sklearn_pca = sklearnPCA( n_components=2 )
		std = StandardScaler().fit_transform(self.m_data)
		feature = sklearn_pca.fit_transform(std)


		y = np.array(self.m_resultLabels)

		print(y)

		matrix_feature_kmean = np.matrix(feature)
		matrix_label_knn = np.matrix(y).transpose()
		print( matrix_feature_kmean.shape )
		print(y.shape)
		matrix_general = np.concatenate((matrix_feature_kmean, matrix_label_knn), axis=1)

		tolist_knn = matrix_general.tolist()
		return tolist_knn



	def getDataMatrix(self):
		n = len(self.m_data)
		list_set =  defaultdict(set)

		frequency =  defaultdict(list)
		for i in range(n):
			frequency[ self.m_resultLabels[i] ].append( self.m_data[i] )
		list_set = {}
		for key, value in frequency.items():
			list_set[key] = value

		#for i in range(n):
		#	list_set[ self.m_resultLabels ].add( self.m_data )

		matrix = np.zeros((n, n))
		l=0
		for m in list_set.keys():
			for i in range(len(list_set[m])):
				for j in range(len(list_set[m])):
					matrix[i+l][j+l] = 1
			l = l + len(list_set[m])
		return matrix.tolist()