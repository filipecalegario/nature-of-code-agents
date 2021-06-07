# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Modified by Filipe Calegario

# Draws a "vehicle" on the screen

from Vehicle import Vehicle

def setup():
    global vehicle
    size(640, 360)
    velocity = PVector(0, 0)
    vehicle = Vehicle(width / 2, height / 2, velocity)

def draw():
    background(255)
    mouse = PVector(mouseX, mouseY)
    vehicle.update()
    vehicle.display()
