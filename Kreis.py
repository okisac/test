class Kreis:
    def __init__ (self,radiusCM,pCM):
        self.radius = radiusCM
        self.p = pCM
    def get_fleache(self):
        self.fleache = (self.radius**2)*self.p
        return self.fleache
    def get_umfang(self):
        self.umfang = (2*self.p*self.radius)
        return self.umfang
p=3.14
circle=Kreis(5,p)
print(circle.get_fleache())
print(circle.get_umfang())

