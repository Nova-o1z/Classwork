import pygame

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

cloud_x = 100
cloud_x2 = 300
bird_x = 230
sun = 90
moon = 700

# Cloud and sun speed
cloud_speed = 3
sun_speed = 1.9
moon_speed = 1
bird_speed = 3

#SUN AND MOON STATES
sun_set = False  # To check if the sun is setting
moon_rising = False  # To check if the moon is rising
sunstay_time = 150
sunstay_counter = 0


# Background sky color variables (moved outside of the main loop)
sky_r, sky_g, sky_b = 163, 209, 255
cloud_r, cloud_g, cloud_b = 255, 255, 255

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

    # SPEED
    cloud_x += cloud_speed
    cloud_x2 += cloud_speed
    sun += sun_speed
    moon -= moon_speed
    bird_x += bird_speed

    #SUN TRACKER
    if not sun_set:
        sunstay_counter += 1
        if sunstay_counter >= sunstay_time:
            sun_set = True 

  # Adjust sky color 
    if sun_set and sun < HEIGHT + 50:
        # Reduce color
        if sky_r > 49:
            sky_r -= 1
        if sky_g > 78:
            sky_g -= 1
        if sky_b > 143:
            sky_b -= 1

        # Cloud darkening
        if cloud_r > 169:
            cloud_r -= 1
        if cloud_g > 169:
            cloud_g -= 1
        if cloud_b > 169:
            cloud_b -= 1

    # re-fresh cloud color
    cloud_color = (cloud_r, cloud_g, cloud_b)

    # Start rising the moon after sun sets
    if sun > HEIGHT + 50 and not moon_rising:
        moon_rising = True


    # Move the moon upwards
    if moon_rising:
        moon -= moon_speed

    # ONCE THE MOON reachs the top --> RESET
    if moon < -50:
        sun = 90
        moon = 700
        sky_r = 163
        sky_g = 209
        sky_b = 255
        cloud_r = 255
        cloud_g = 255
        cloud_b = 255
        sun_set = False
        moon_rising = False
        sunstay_counter = 0

    # Update the background color here
    screen.fill((sky_r, sky_g, sky_b)) 

    # MOON & stars
    if moon_rising:
        pygame.draw.circle(screen, (220, 220, 220), (549, moon), 50)
        pygame.draw.circle(screen, (180, 180, 180), (530, moon - 10), 10)
        pygame.draw.circle(screen, (180, 180, 180), (570, moon - 20), 8)

        pygame.draw.circle(screen, (255, 255, 255), (81, moon - 86), 5)
        pygame.draw.circle(screen, (255, 255, 255), (268, moon - 72), 5)
        pygame.draw.circle(screen, (255, 255, 255), (350, moon - 94), 5)
        pygame.draw.circle(screen, (255, 255, 255), (206, moon -  105), 5)
        pygame.draw.circle(screen, (255, 255, 255), (148, moon - 33), 5)
        pygame.draw.circle(screen, (255, 255, 255), (484, moon - 12), 5)


    # SUN
    if not moon_rising: 
        pygame.draw.circle(screen, (247, 232, 64), (57, sun), 50)

    # CLOUDS
    pygame.draw.circle(screen, cloud_color, (cloud_x, 100), 40)
    pygame.draw.circle(screen, cloud_color, (cloud_x + 34, 80), 40)
    pygame.draw.circle(screen, cloud_color, (cloud_x + 45, 100), 40)

    pygame.draw.circle(screen, cloud_color, (cloud_x2, 105), 35)
    pygame.draw.circle(screen, cloud_color, (cloud_x2 + 14, 130), 35)
    pygame.draw.circle(screen, cloud_color, (cloud_x2 + 35, 120), 35)

    pygame.draw.circle(screen, cloud_color, (cloud_x2 + 129, 124), 27)
    pygame.draw.circle(screen, cloud_color, (cloud_x2 + 137, 110), 27)
    pygame.draw.circle(screen, cloud_color, (cloud_x2 + 125, 133), 27)

    # WATER
    pygame.draw.rect(screen, (100, 175, 245), (0, 307, 640, 150))

    # ROCKS IN THE SAND
    COLOR = 126, 128, 127
    pygame.draw.ellipse(screen, COLOR, (1, 410, 190, 80))
    pygame.draw.ellipse(screen, (148, 148, 148), (514, 410, 90, 40))
    pygame.draw.ellipse(screen, (148, 148, 148), (1, 390, 100, 80))
    pygame.draw.ellipse(screen, COLOR, (1, 415, 80, 40))
    pygame.draw.circle(screen, COLOR, (638, 423), 40)
    pygame.draw.ellipse(screen, COLOR, (514, 415, 300, 50))

    # SAND
    pygame.draw.rect(screen, (242, 226, 143), (1, 430, 640, 50))

    # BEACH POOL/UMBRELLA
    pygame.draw.rect(screen, COLOR, (426, 360, 9, 100))
    pygame.draw.ellipse(screen, "red", (386, 358, 10, 20))
    pygame.draw.ellipse(screen, "red", (412, 358, 10, 20))
    pygame.draw.ellipse(screen, "red", (450, 358, 10, 20))
    pygame.draw.ellipse(screen, "white", (437, 358, 10, 20))
    pygame.draw.ellipse(screen, "white", (399, 358, 10, 20))
    pygame.draw.ellipse(screen, "white", (464, 358, 10, 20))

    pygame.draw.circle(screen, "white", (430, 367), 50, draw_top_right=True, draw_top_left=True)
    pygame.draw.circle(screen, "red", (430, 367), 50, draw_top_right=True, draw_top_left=True, width=5)

    # BEACH BLANKET
    pygame.draw.rect(screen, (105, 160, 214), (331, 438, 88, 35))
    pygame.draw.rect(screen, "white", (331, 438, 5, 35))
    pygame.draw.rect(screen, "white", (414, 438, 5, 35))

    # BIRDS

    pygame.draw.circle(screen, (0, 0, 0), (bird_x, 130), 25, draw_top_right=True, draw_top_left=True, width=3)
    pygame.draw.circle(screen, (0, 0, 0), (bird_x + 48, 128), 25, draw_top_right=True, draw_top_left=True, width=3)

    # Reset clouds and sun position if they go off screen
    if cloud_x > WIDTH + 40:
        cloud_x = -100
    if cloud_x2 > WIDTH + 40:
        cloud_x2 = -100
    if bird_x > WIDTH + 40:
        bird_x = -100
    if sun > HEIGHT + 50:
        sun = -1000
    if moon < -50:
        moon = 700


    # Must be the last two lines
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
