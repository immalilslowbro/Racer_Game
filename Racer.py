import pygame, sys
from pygame.locals import *

SCREEN_WIDTH=640
SCREEN_HEIGHT=480
HALF_SCREEN_HEIGHT=int(SCREEN_HEIGHT/2)

def main():

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.display.set_caption("Racer")

    font=pygame.font.SysFont('Arial', 30)


    light_road=pygame.image.load('light_road.png')
    dark_road=pygame.image.load('dark_road.png')

    texture_position=0

    ddz=0.001
    dz=0
    z=0

    road_pos=0
    road_acceleration=80
    texture_position_acceleration=4
    texture_position_threshold=300
    half_texture_position_threshold=int(texture_position_threshold/2)

    while True:

        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            if event.type ==QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            road_pos+=road_acceleration
            if road_pos>=texture_position_threshold:
                road_pos=0

        texture_position=road_pos
        dz=0
        z=0
        screen.fill("blue")
        for i in range(HALF_SCREEN_HEIGHT-1,-1,-1):
            if texture_position<half_texture_position_threshold:
                screen.blit(light_road,(0,i+HALF_SCREEN_HEIGHT),(0,i,SCREEN_WIDTH,1))
            else:
                screen.blit(dark_road,(0,i+HALF_SCREEN_HEIGHT),(0,i,SCREEN_WIDTH,1))
            dz+=ddz
            z+=dz
            texture_position+=texture_position_acceleration+z
            if texture_position>=texture_position_threshold:
                texture_position=0
        pygame.display.flip()

if __name__ == "__main__":
    main()
