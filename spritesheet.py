import pygame

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image
        
    def get_image(self, framex, framey, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((framex * width), (framey * width), width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        
        return image