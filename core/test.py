from sklearn import datasets 
#import KMeansAlgorithm 
from KMeansAlgorithm import *
from BirchAlgorithm import *
from SomAlgorithm import *
from sklearn.decomposition import PCA as sklearnPCA
from sklearn.preprocessing import StandardScaler
import numpy as np


#iris = datasets.load_breast_cancer()
iris = datasets.load_iris()
test = KMeansAlgorithm(iris.data, {'kmeans':2} )
test.run()
print(test.getResultsMetrics())

'''
sklearn_pca = sklearnPCA(n_components=2)
std = StandardScaler().fit_transform(iris.data)
feature = sklearn_pca.fit_transform(std)


y = np.array(test.getResultsLabels())

print(y)

matrix_feature_kmean = np.matrix(feature)
matrix_label_knn = np.matrix(y).transpose()
print(matrix_feature_kmean.shape)
print(y.shape)
matrix_general = np.concatenate((matrix_feature_kmean, matrix_label_knn), axis=1)

tolist_knn = matrix_general.tolist()
print(tolist_knn)
'''


#print(test.getDataScatter())

#print(test.getDataMatrix())


#test1 = BirchAlgorithm(iris.data, {'birch':2} )
#test1.run()
#print(test1.getResultsMetrics())


#test2 = SomAlgorithm(iris, {'som_a':1, 'som_b':3} )
#test2.run()
#print(test2.getResultsMetrics())






#l = [11,1,1,1,1,1,1]
#s = set(l)
#print(s)
	



#import metis


#cuts, parts = metis.part_graph(list_ad, 3, recursive = False, dbglvl=metis.METIS_DBG_ALL)








