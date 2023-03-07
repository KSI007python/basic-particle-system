import pygame
import math
import random

pygame.init()

screen = pygame.display.set_mode((800, 800))

class particle:
    def __init__(self, x, y, radius, velocity, angle, color):
        self.x = x
        self.y = y
        self.radius = radius
        angle = math.radians(angle)
        self.vX = math.cos(angle)*velocity
        self.vY = math.sin(angle)*velocity
        self.color = color

    def update_pos(self):
        self.x -= self.vX
        self.y -= self.vY

    def show_particle(self):
        pygame.draw.ellipse(screen, self.color, (self.x-self.radius/2, self.y-self.radius/2, self.radius, self.radius))

running = True

g = 0.0098

particle_array = []

delay = 0

cooldown = delay

mouse_pressed = False

while running:
    screen.fill((0, 0, 0))

    keys = pygame.key.get_pressed()
    
    i = 0
    while i < len(particle_array) and len(particle_array) != 0:
        particle_ = particle_array[i]
        particle_.vY -= g
        particle_.radius -= 0.01
        particle_.update_pos()
        particle_.show_particle()
        if particle_.radius < 1:
            particle_array.pop(i)
            i -= 1
        if particle_.y > 800 or particle_.y < 0:
            particle_.vY *= -0.05*particle_.radius

            if particle_.y < 0:
                particle_.y = 0

            if particle_.y > 800 and not keys[pygame.K_c]:
                particle_.y = 800

        if particle_.x > 800 or particle_.x < 0:
            particle_.vX *= -0.05*particle_.radius

            if particle_.x < 0:
                particle_.x = 0

            if particle_.x > 800:
                particle_.x = 800
        i += 1
    if (mouse_pressed or keys[pygame.K_SPACE]) and cooldown == 0:
        for i in range(2):
            particle_array.append(particle(
                pygame.mouse.get_pos()[0], 
                pygame.mouse.get_pos()[1], 
                random.randint(5, 20),
                1,
                random.randint(0, 360),
                (random.randint(100, 255), random.randint(100, 255), random.randint(200, 255))
            ))
        cooldown = delay 

    if cooldown > 0:
        cooldown -= 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed = True

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pressed = False

    pygame.display.update()