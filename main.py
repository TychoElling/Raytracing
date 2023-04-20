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

origin = vec3(0,0,0)
horizontal = vec3(viewportWidth,0,0)
vertical = vec3(0,viewportHeight,0)
lowerLeftCorner = origin - horizontal/2 - vertical/2 - vec3(0,0,focalLength)


### Render

file = PPM()
file.