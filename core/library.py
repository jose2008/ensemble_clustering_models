def PolygonArea(corners):
	n = len(corners) # of corners
	area = 0.0
	for i in range(n):
		j = (i + 1) % n
		area += corners[i][0] * corners[j][1]
		area -= corners[j][0] * corners[i][1]
	area = abs(area) / 2.0
	return area



def Wachspress(corners):
	n = len(corners)
	listWeight = []
	#print("show...")
	for i in range(n-1):
		if i == 0:
			c  = PolygonArea( [corners[i],corners[i+1],corners[n-2]] )
			a0 = PolygonArea( [ corners[i],corners[i+1],corners[n-1]])
			an = PolygonArea( [corners[i],corners[n-2],corners[n-1]])
		elif i==n-2 :
			c  = PolygonArea( [corners[i],corners[i-1],corners[0]] )
			a0 = PolygonArea( [ corners[i],corners[i-1],corners[n-1]])
			an = PolygonArea( [corners[i],corners[0],corners[n-1]])
		else :
			c  = PolygonArea( [corners[i],corners[i+1],corners[i-1]] )
			a0 = PolygonArea( [ corners[i],corners[i+1],corners[n-1]])
			an = PolygonArea( [corners[i],corners[i-1],corners[n-1]])
		#print(c, a0, an)
		if(a0==0): 
			a0=0.00001
		if(an==0):
			an=0.00001
		listWeight.append(c/(a0*an))
	return listWeight