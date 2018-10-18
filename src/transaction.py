import pygame 
import pickle
import astar

class Transaction :

    def __init__(self) :
        with open('image/map.dat', 'rb') as handle:
            self.nodes = pickle.load(handle)
       
        
    def find_nearest_node (self, node) :
        result = (1e6, ())
        for key in self.nodes :
            x1, y1 = node
            x2, y2 = key
            distance =  (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) 
            if distance < result[0] :
                result = (distance, (x2,y2))
                # print (result)
        return result[1]

    def find_path (self, start='', end='') :
        ### find path for car by Astar Algorithm        
        def neighbors(n):
            return self.nodes[n]

        def distance(n1, n2):
            # print (n1, n2)
            x1, y1 = n1
            x2, y2 = n2
            return (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)

        def cost(n, goal):
            x1, y1 = n
            x2, y2 = goal
            return (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)
        
        start = (start[1], start[0])
        end = (end[1], end[0])
        start = self.find_nearest_node(start) #list(self.nodes.keys())[1920]
        end   = self.find_nearest_node(end)    #list(self.nodes.keys())[490]
        
        print (astar.find_path(start=start, goal=end, 
                    neighbors_fnct=neighbors,
                    distance_between_fnct=distance,
                    heuristic_cost_estimate_fnct=cost))
        path = list(astar.find_path(start=start, goal=end, 
                    neighbors_fnct=neighbors,
                    distance_between_fnct=distance,
                    heuristic_cost_estimate_fnct=cost))
        for i in range(len(path)) :
            x, y = path[i]
            path[i] = (y,x)
        return path 



## ==== TEST ====
# a = Transaction()
# a.find_path()