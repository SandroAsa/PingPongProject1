import pygame

pygame.init()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Ping-Pong")

background_img = pygame.image.load("background.jpg")
background_img = pygame.transform.scale(background_img, (800, 500))

# Players and ball
player1 = pygame.Rect(200, 350, 64, 64)
player2 = pygame.Rect(600, 350, 64, 64)
ball = pygame.Rect(376, 228, 48, 48)

movespeed = 5
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

    # Draw everything
    screen.blit(background_img, (0, 0))
    screen.blit(player_1_img, (player1.x, player1.y))
    screen.blit(player_2_img, (player2.x, player2.y))
    screen.blit(ball_img, (ball.x, ball.y))

    pygame.display.flip()
    clock.tick(120)

pygame.quit()
