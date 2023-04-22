def confirm (a,b):
  if len(a - b) > 10**(-8):
    +a
    +b
def vec3Test():
  # Zero properties
  z = vec3.vec3(0,0,0)
  a = vec3.vec3(0,-10,5)
  b = vec3.vec3(1,2,3)
  c = vec3.vec3(3,-1,3)

    # Multiply
  confirm(z, z * z)
  confirm(z, z * a)
  confirm(z, z * b)
  confirm(z, z * c)

    # Add
  confirm(z, z + z)
  confirm(a, z + a)
  confirm(b, z + b)
  confirm(c, z + c)

    # Adding
  confirm(a + b, b + a)
  confirm(a + c, c + a)
  confirm(c + b, b + c)
  confirm(a + b, vec3.vec3(1,-8,8))
  confirm(a + c, vec3.vec3(3,-11,8))
  confirm(c + b, vec3.vec3(4,1,6))