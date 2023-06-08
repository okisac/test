class kugle:
    PI=3.1415
    def __init__(self,radius):
        self.radius = radius
    def get_flaeche(self):
        flaeche = 4*(self.radius**2) * self.PI
        return flaeche
kug1 = kugle(5)
print(kug1.get_flaeche())

        
        