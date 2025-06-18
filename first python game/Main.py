import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Ping-Pong")

background_img = pygame.image.load("background.jpg")
background_img = pygame.transform.scale(background_img, (800, 500))

# Players and ball
player1 = pygame.Rect(200, 350, 64, 64)
player2 = pygame.Rect(600, 350, 64, 64)
ball = pygame.Rect(376, 228, 48, 48)

ball_speed = 3
ball_dx = random.choice([-1, 1])
ball_dy = random.choice([-1, 1])

movespeed = 5
max_hit = 0

# Player and ball images
player_1_img = pygame.image.load("player1.png")
player_2_img = pygame.image.load("player2.png")
ball_img = pygame.image.load("ball.png")

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    # Move left paddle
    if keys[pygame.K_w]:
        player1.y -= movespeed
    if keys[pygame.K_s]:
        player1.y += movespeed
    if keys[pygame.K_a]:
        player1.x -= movespeed
    if keys[pygame.K_d]:
        player1.x += movespeed

    # Move right paddle
    if keys[pygame.K_UP]:
        player2.y -= movespeed
    if keys[pygame.K_DOWN]:
        player2.y += movespeed
    if keys[pygame.K_LEFT]:
        player2.x -= movespeed
    if keys[pygame.K_RIGHT]:
        player2.x += movespeed

    # Keep paddles on screen and on their half
    if player1.x < 0:
        player1.x = 0
    if player1.x > 335:
        player1.x = 335
    if player1.y < -13:
        player1.y = -13
    if player1.y > 445:
        player1.y = 445

    if player2.x < 402:
        player2.x = 402
    if player2.x > 736:
        player2.x = 736
    if player2.y < -13:
        player2.y = -13
    if player2.y > 445:
        player2.y = 445

    # ball moving depending on speed
    ball.x += ball_dx * ball_speed
    ball.y += ball_dy * ball_speed

    # if touch top or bottom of screen, reverse direction
    if ball.y <= 0 or ball.y >= 452:
        ball_dy *= -1

    # Reset max_hit when ball crosses midpoint (so paddles can hit again)
    if ball_dx > 0 and ball.x >= 400:
        max_hit = 0
    if ball_dx < 0 and ball.x <= 400:
        max_hit = 0

    # if touch left or right paddle, reverse direction and randomize speed
    if ball.colliderect(player1) and ball_dx < 0 and ball.x <= 335 and max_hit < 1:
        ball_dx *= -1
        ball_dy = random.choice([-1, 0, 1])
        max_hit += 1
    if ball.colliderect(player2) and ball_dx > 0 and ball.x >= 402 and max_hit < 1:
        ball_dx *= -1
        ball_dy = random.choice([-1, 0, 1])
        max_hit += 1

    # if ball goes out of bounds, reset position and randomize direction
    if ball.x < 0 or ball.x > 752:
        ball.x = 376
        ball.y = 228
        ball_dx = random.choice([-1, 1])
        ball_dy = random.choice([-1, 1])
        max_hit = 0

    # Draw everything
    screen.blit(background_img, (0, 0))
    screen.blit(player_1_img, player1)
    screen.blit(player_2_img, player2)
    screen.blit(ball_img, ball)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
