from math import *
class Point:
    #methode 1
    def __init__ (self, x,y):
        self.x=x
        self.y=y
    #methode 2
    def __str__ (self):
        return f"Point({self.x}, {self.y})"
    #methode 3
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    #methode 4
    def distance_vers(self, autre_point):
        return sqrt((self.x - autre_point.x)**2 + (self.y - autre_point.y)**2)
  #methode 5
    def translater(self, dx, dy):
        self.x=self.x + dx
        self.y=self.y + dy
        
class Droite :
    def __init__ (self, P1, P2):
        self.point1=P1
        self.point2=P2
    def __str__(self):
          return f"Droite({self.point1}, {self.point2})"
    def __repr__(self):
          return f"Droite({self.point1}, {self.point2})"
    def longueur (self):
          longeur=sqrt((self.point1.x - self.point2.x)**2 + (self.point1.y - self.point2.y)**2)
          return longeur

    


class Cercle :
    def __init__ ( self , centre , rayon ) :
        self.centre = centre
        self.rayon = rayon
    def __str__ ( self ) :
        return f" Cercle ( centre ={ self.centre } , rayon ={ self.rayon })"

    def __repr__ ( self ) :
        return f" Cercle ({ self.centre } , { self.rayon })"

    def perimetre ( self ) :
        return 2 * math.pi * self.rayon

    def aire ( self ) :
        return math.pi * self.rayon ** 2

    def contient_point ( self , point ) :
        distance = self.centre.distance_vers ( point )
        return distance <= self.rayon

    def position_point ( self , point ) :
        distance = self.centre.distance_vers ( point )
        if distance < self.rayon :
            return " Dedans "
        elif distance == self.rayon :
            return " Sur "
        else :
            return " Dehors "

    def est_secant ( self , autre_cercle ) :
        distance_centres = self.centre.distance_vers ( autre_cercle.centre )
        return distance_centres <= ( self.rayon + autre_cercle.rayon ) and \
        distance_centres >= abs ( self.rayon - autre_cercle.rayon )

centre = Point(0,0)
rayon = 5
pc = Cercle(centre,rayon)
print(pc)



