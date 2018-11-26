# referenece http://techforcurious.website/simulation-of-spring-mass-system-vpython-tutorial-visual-python/
from vpython import*

Mass=box(pos=vector(12,0,0),velocity=vector(0,0,0),size=vector(1,1,1),mass=1.0,color=color.blue)
pivot=vector(0,0,0)
spring=helix(pos=pivot,axis=Mass.pos-pivot,radius=0.4,constant=1,thickness=0.1,coils=20,color=color.red)
eq=vector(9,0,0)
t=0
dt=0.01
while (t<50):
 rate(100)
 acc=(eq-Mass.pos)*(spring.constant/Mass.mass)
 Mass.velocity=Mass.velocity+acc*dt
 Mass.pos=Mass.pos+Mass.velocity*dt
 spring.axis=Mass.pos-spring.pos
 t=t+dt