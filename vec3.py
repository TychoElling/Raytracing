import math
class vec3:
    def __init__ (self,e1,e2,e3):
        self.e1 = e1
        self.e2 = e2
        self.e3 = e3
    def __add__(self,v1):
        self.e1 += v1.e1
        self.e2 += v1.e2
        self.e3 += v1.e3
        return self
    def neg (self):
        self.e1 = -self.e1
        self.e2 = -self.e2
        self.e3 = -self.e3
    def mult(self,t):
        self.e1 *= t
        self.e2 *= t
        self.e3 *= t
    def __sub(self,v):
        return self + v.mult(-1)
    def __truediv__(self,t):
        self.mult(1/t)
    def len(self):
        return math.sqrt(self.e1**2 + self.e2**2 + self.e3**2)
    def print(self):
        print(self.e1,self.e2,self.e3)
    def dot(self,v):
        v1 = vec3(self.e1*v.e1,self.e2*v.e2,self.e3*v.e3)
        return v1
    def __mul__(self,t):
        v1 = vec3(self.e1 * t, self.e2 * t, self.e3 * t)
        return v1
def cross(v,u):
    return vec3(
        u.e2*v.e3 - u.e3*v.e2,
        u.e3*v.e1 - u.e1-v.e3,
        u.e1*v.e2 - u.e2*v.e1
    )