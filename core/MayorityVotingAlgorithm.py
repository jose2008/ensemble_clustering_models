'''

def finish(self):
		"""
		Finish the ensemble by majority vote
		"""
		labels = np.zeros(self.N).astype(int)
		currCluster = 1
		x = self.co_matrix.as_matrix()

		for i in range(0, self.N):
			for j in range(i+1, self.N):

				if x[i,j] > self.threshold:
					# the clusters should be set to the same value and if both belong to an existing cluster, all 
					# members of the clusters should be joined
					if labels[i] and labels[j]:
						cluster_num = min(labels[i] , labels[j])
						cluster_toChange = max(labels[i] , labels[j])

						indices = [k for k, x in enumerate(labels) if x == cluster_toChange]
						labels[indices] = cluster_num
					elif not labels[i] and not labels[j]: #a new cluster
						labels[i] = currCluster
						labels[j] = currCluster
						currCluster += 1
					else: #one of them is in a cluster and one is not, one will be assigned the same thing, but saves an if
						cluster_num = max(labels[i] , labels[j])
						labels[i] = cluster_num
						labels[j] = cluster_num

				else: #else don't join them and give them an assignment the first time they are traversed
					if not labels[i]:
						labels[i] = currCluster
						currCluster += 1
					if not labels[j]:
						labels[j] = currCluster
						currCluster += 1

		#Add a cleanup state, if there are any cluster numbers that jump, move them down
		clusters = np.sort(np.unique(labels))
		for ind in range(0,len(clusters)-1): #operating on ind+1
			if clusters[ind+1] != clusters[ind]+1:

				cluster_num = clusters[ind] + 1
				#print("updating cluster num %d to %d")%(clusters[ind+1], cluster_num)
				indices = [k for k, x in enumerate(labels) if x == clusters[ind+1]]
				labels[indices] = cluster_num
				clusters[ind+1] = cluster_num 





self.labels = labels


'''