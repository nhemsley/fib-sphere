import time

from numpy import arange, pi, sin, cos, arccos

from vpython import *


import pprint
pp = pprint.PrettyPrinter(indent=4)

def generate_epsilon(n):
  if n >= 600000:
    epsilon = 214
  elif n>= 400000:
    epsilon = 75
  elif n>= 11000:
    epsilon = 27
  elif n>= 890:
    epsilon = 10
  elif n>= 177:
    epsilon = 3.33
  elif n>= 24:
    epsilon = 1.33
  else:
    epsilon = 0.33

  return epsilon

def points_on_sphere_fib(n):

  epsilon =  0.36 #generate_epsilon(n)

  goldenRatio = (1 + 5**0.5)/2
  i = arange(0, n) 
  theta_a = 2 *pi * i / goldenRatio
  phi_a = arccos(1 - 2*(i+epsilon)/(n-1+2*epsilon))
  return [vector(cos(theta) * sin(phi), sin(theta) * sin(phi), cos(phi)) for theta, phi in zip(theta_a, phi_a)];

# pp.pprint(values)


n = 0
up = True
nmax = 200

while True:
  time.sleep(0.01)
  if up is True: n = n + 1
  if up is False: n = n - 1
  if n > nmax: up = False
  if n == 0: up = True
  values = points_on_sphere_fib(n)
  for obj in scene.objects:
    obj.visible = False
    del obj
  
  print(n)
  for coords in values:
    sphere(pos=coords, radius=max(0.05, (1-(n/nmax) ) / 5))
