from sklearn.cluster import KMeans
from IClusteringAlgorithm import *
from sklearn import datasets
import somLib
import pandas as pd


class SomAlgorithm ( IClusteringAlgorithm ) :

	def __init__( self, data, params ) :
		super( SomAlgorithm, self ).__init__( data, params )
		print("entrooooo")
		self.params = params
		# define some specific kmeans algorithm properties ...
		# like objects from sklearn, etc.

	

	def _runAlgorithm( self ) :
		# define here your algorithm ...
		# and update your labels
		# ...

		iris = self.m_data
		df_train = pd.DataFrame( self.m_data.data, columns=iris.feature_names)
		agri_som = somLib.SOM(self.params['som_a'] , self.params['som_b'] ,4)
		df_train = df_train / df_train.max()
		agri_som.train(df_train.values,
	              num_epochs=200,
	              init_learning_rate=0.01
	              )

		def predict(df):
			bmu, bmu_idx = agri_som.find_bmu(df.values)
			df['bmu'] = bmu
			df['bmu_idx'] =  bmu_idx[1]#bmu_idx
			return df
		clustered_df = df_train.apply(predict, axis=1)
		print(clustered_df)

		self.m_resultLabels = clustered_df['bmu_idx']

		pass

