import math
def area(a, b, c):
    def distance(p1, p2):
        return math.hypot(p1[0]-p2[0], p1[1]-p2[1])

    side_a = distance(a, b)
    side_b = distance(b, c)
    side_c = distance(c, a)
    s = 0.5 * ( side_a + side_b + side_c)
    return math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))



#print(area((0,0),(2,0),(1,1))  )



import metis                                                                             

s = [ [1, 0.75, 0.5, 0.25, 0, 0, 0],
	[0.75, 1, 0.5, 0, 0.25, 0, 0],
	[0.5, 0.5, 1, 0.25, 0, 0, 0],
	[0.25, 0, 0.25, 1, 0.5, 0, 0],
	[0, 0.25, 0, 0.5, 1, 0.25, 0.25],
	[0, 0, 0, 0, 0.25, 1, 0.75],
	[0, 0, 0, 0, 0.25, 0.75, 1]
]


list_ad = [ [(1,5),(2,1)],
	[(0,5),(3,1)],
	[(0,1), (3,5)],
	[(1,1),(2,5)]

]


list_ad2 = [ [(1,1),(2,5)],
	[(0,1),(3,5)],
	[(0,5), (3,1) ],
	[(1,5),(2,1)]


]



cuts, parts = metis.part_graph(list_ad2, 2, recursive = False, dbglvl=metis.METIS_DBG_ALL)
print(parts)



