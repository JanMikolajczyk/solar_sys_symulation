import numpy as np
import pygame
from ursina import *


def initialize_audio(file):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    pygame.event.wait()

def update_planetary_movement(entity, t, angle, radius):
    entity.x = np.cos(t + angle) * radius
    entity.z = np.sin(t + angle) * radius
    entity.y = np.sin(t + angle) * radius
    entity.rotation_y += 50 * radius * time.dt
    entity.rotation_x += 12 * radius * time.dt

def update_sun():
    global t
    t = t + 0.01
    angle = np.pi * 40 / 180
    handle_camera_movement()
    handle_audio_controls()
    update_planetary_movement(sun, t, angle, 1)

def update_mercury():
    global t
    t = t + 0.01
    angle = np.pi * 40 / 180
    handle_camera_movement()
    handle_audio_controls()
    update_planetary_movement(mercury, t, angle, 1.2)

def update_venus():
    global t
    t = t + 0.01
    angle = np.pi * 40 / 180
    handle_camera_movement()
    handle_audio_controls()
    update_planetary_movement(venus, t, angle, 1.4)

def update_earth():
    global t
    t = t + 0.01
    angle = np.pi * 40 / 180
    handle_camera_movement()
    handle_audio_controls()
    update_planetary_movement(earth, t, angle * 2, 1.8)

def update_mars():
    global t
    t = t + 0.01
    angle = np.pi * 40 / 180
    handle_camera_movement()
    handle_audio_controls()
    update_planetary_movement(mars, t, angle * 3, 2.2)

def update_jupiter():
    global t
    t = t + 0.01
    angle = np.pi * 40 / 180
    handle_camera_movement()
    handle_audio_controls()
    update_planetary_movement(jupiter, t, angle * 4, 2.6)

def update_saturn():
    global t
    t = t + 0.01
    angle = np.pi * 40 / 180
    handle_camera_movement()
    handle_audio_controls()
    update_planetary_movement(saturn, t, angle * 5, 3)

def update_uranus():
    global t
    t = t + 0.01
    angle = np.pi * 40 / 180
    handle_camera_movement()
    handle_audio_controls()
    update_planetary_movement(uranus, t, angle * 6, 3.4)

def update_neptune():
    global t
    t = t + 0.01
    angle = np.pi * 40 / 180
    handle_camera_movement()
    handle_audio_controls()
    update_planetary_movement(neptune, t, angle * 7, 3.8)



def handle_camera_movement():
    camera.z += held_keys["e"] * 10 * time.dt
    camera.z -= held_keys["r"] * 10 * time.dt
    camera.x += held_keys["d"] * 10 * time.dt
    camera.x -= held_keys["a"] * 10 * time.dt
    camera.y += held_keys["w"] * 10 * time.dt
    camera.y -= held_keys["s"] * 10 * time.dt


def handle_audio_controls():
    if held_keys["b"]:
        pygame.mixer.music.pause()
    if held_keys["p"]:
        pygame.mixer.music.unpause()




def create_entities():
    sun = Entity(model='sphere', texture='2k_sun', scale=2)
    mercury = Entity(model='sphere', texture='2k_mercury', scale=0.2)
    venus = Entity(model='sphere', texture='2k_venus_surface', scale=0.3)
    earth = Entity(model='sphere', texture='2k_earth_daymap', scale=0.4)
    mars = Entity(model='sphere', texture='2k_mars', scale=0.3)
    jupiter = Entity(model='sphere', texture='2k_jupiter', scale=0.6)
    saturn = Entity(model='sphere', texture='2k_saturn', scale=0.5)
    uranus = Entity(model='sphere', texture='2k_uranus', scale=0.5)
    neptune = Entity(model='sphere', texture='2k_neptune', scale=0.5)


    Sky(texture="8k_stars")

    return sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune


if __name__ == "__main__":
    file = 'ggg.wav'
    initialize_audio(file)
    handle_camera_movement()
    app = Ursina()
    sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune = create_entities()

    t = -np.pi
    app.run()
