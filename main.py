import vec3
import ray
import PPM
import math

### Image

aspectRatio = 16/9
imageWidth = 400
imageHeight = int(imageWidth/aspectRatio)


### Camera

viewportHeight = 2.0
viewportWidth = 2 * aspectRatio
focalLength = 1.0

origin = vec3.vec3(0,0,0)
horizontal = vec3.vec3(viewportWidth,0,0)
vertical = vec3.vec3(0,viewportHeight,0)
lowerLeftCorner = origin - horizontal/2 - vertical/2 - vec3.vec3(0,0,focalLength)


### Render

file = PPM.PPM(imageWidth,imageHeight)
for j in range(imageHeight - 1, -1, -1):
  for i in range(0,imageWidth):
    u = i / (imageWidth - 1)
    v = j / (imageHeight - 1)
    w = lowerLeftCorner + horizontal*u + vertical*v - origin
    r = ray.ray(origin.e1, origin.e2, origin.e3, w.e1, w.e2, w.e3)
    pixelColor = vec3.vec3(int(j*256/imageHeight),0,0)
    file.writeColor(pixelColor)
  print("Line "+str(j+1)+" is finished")







