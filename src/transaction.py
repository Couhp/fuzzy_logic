import pygame 
import pickle
import astar
import math

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
        
        angles = []
        for i in range(len(path)) :
            node = path[i]
            angle = self.get_angle (path, i, node)    
            angles.append(angle)
        new_angles = self.soft_move(angles)
        return path, new_angles 

    def mean(self,numbers):
        return float(sum(numbers)) / max(len(numbers), 1)

    def get_angle (self, path, i, node) :
        def cal_angle (node, next_node) :
            x1, y1 = node
            x2, y2 = next_node
            ZERO = 0.01
            if abs(x1 - x2) < ZERO : 
                if y2 > y1 : return -90
                if y2 < y1 : return 90
            else :
                angle = abs(math.degrees(math.atan( (y1-y2)/(x1-x2) )))
                if      x1 < x2 and y1 >= y2 : return angle
                elif    x1 < x2 and y1 <= y2 : return -angle
                elif    x1 > x2 and y1 >= y2 : return 180-angle
                elif    x1 > x2 and y1 <= y2 : return angle-180
            print ("Oh shit @@@ $$$")
            return 0
        #### 
        if i+5 > len(path) :
            next_node = (self.mean([x[0] for x in path[i:]]), self.mean([x[1] for x in path[i:]]))
        else :
            next_node = (self.mean([x[0] for x in path[i+5:i+10]]), self.mean([x[1] for x in path[i+5:i+10]]))
        
        angle = cal_angle(node, next_node)
        return angle

    def soft_move (self, angles) :
        new_angles = []
        RANGE = 5
        for i in range(len(angles)) :
            if i < RANGE :
                new_angles.append(self.mean(angles[:i]))
            elif i+RANGE-1 > len(angles) :
                new_angles.append(self.mean(angles[i:]))
            else :
                new_angles.append(self.mean(angles[i-RANGE:i+RANGE]))    
        return new_angles


## ==== TEST ====
# a = Transaction()
# a.find_path()