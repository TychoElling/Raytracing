import vec3


class ray:
    def __init__(self, x, y, z, dx, dy, dz):
        self.x = x
        self.y = y
        self.z = z
        self.dx = dx
        self.dy = dy
        self.orig = vec3(x, y, z)
        self.dir = vec3(dx, dy, dz)

    def at(self, t):
        return self.orig + self.dir * t
    
