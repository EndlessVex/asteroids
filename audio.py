import pygame

pygame.mixer.init()
pygame.mixer.set_num_channels(64)
player_audio = pygame.mixer.Channel(1)
world_audio = pygame.mixer.Channel(2)
death_audio = pygame.mixer.Channel(3)
shoot_sound = pygame.mixer.Sound("audio/shoot.wav")
shoot_sound.set_volume(0.4)
asteroid_explosion = pygame.mixer.Sound("audio/asteroid_explosion.wav")
asteroid_explosion.set_volume(0.6)
death_explosion = pygame.mixer.Sound("audio/asteroid_explosion.wav")
background_music = pygame.mixer.Sound("audio/background.wav")
background_music.set_volume(0.6)