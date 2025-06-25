import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Ping-Pong")

background_img = pygame.image.load("background.jpg")
background_img = pygame.transform.scale(background_img, (800, 500))

player1 = pygame.Rect(200, 350, 64, 64)
player2 = pygame.Rect(600, 350, 64, 64)
ball = pygame.Rect(376, 228, 48, 48)

# ===== ბურთის მოძრაობის ცვლადები =====
ball_speed = 3  # ბურთის სისწრაფე - რამდენი პიქსელით გადაადგილდეს ერთ ფრეიმში

# ბურთის მიმართულების ვექტორები:
# ball_dx = ჰორიზონტალური მიმართულება (-1 = მარცხნივ, 1 = მარჯვნივ)
# ball_dy = ვერტიკალური მიმართულება (-1 = ზემოთ, 1 = ქვემოთ)
ball_dx = random.choice([-1, 1])  # შემთხვევითად არჩევს მარცხნივ ან მარჯვნივ
ball_dy = random.choice([-1, 1])  # შემთხვევითად არჩევს ზემოთ ან ქვემოთ

movespeed = 5  # მოთამაშეების მოძრაობის სისწრაფე

# ===== დარტყმების რაოდენობის კონტროლი =====
# max_hit - ეს ცვლადი შეზღუდავს პლეიერის მხრიდან შეხებებს. მოთამაშე ერთხელ მეტჯერ ვერ მოარტყამს ბურთს
# მანამ, სანამ ბურთი შუა ხაზს არ გადაკვეთს
max_hit = 0

# მოთამაშეებისა და ბურთის სურათების ჩატვირთვა
player_1_img = pygame.image.load("player1.png")
player_2_img = pygame.image.load("player2.png")
ball_img = pygame.image.load("ball.png")

# FPS კონტროლისთვის - თამაში 60 ფრეიმს წამში იმუშავებს
clock = pygame.time.Clock()

font = pygame.font.SysFont("Sylfaen", 20)
start_label = font.render("press SPACE to start", True, (255, 255, 255))

# დაწყების ეკრანის ცვლადი
started = False

# მთავარი თამაშის ციკლი
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    while started != True:
        screen.fill((0, 0, 0))
        screen.blit(start_label, (330, 250))
        if keys[pygame.K_SPACE]:
            started = True
        pygame.display.flip()

    # ===== მოთამაშე 1-ის მართვა (WASD ღილაკები) =====
    if keys[pygame.K_w]:
        player1.y -= movespeed
    if keys[pygame.K_s]:
        player1.y += movespeed
    if keys[pygame.K_a]:
        player1.x -= movespeed
    if keys[pygame.K_d]:
        player1.x += movespeed

    # ===== მოთამაშე 2-ის მართვა (ისრის ღილაკები) =====
    if keys[pygame.K_UP]:
        player2.y -= movespeed
    if keys[pygame.K_DOWN]:
        player2.y += movespeed
    if keys[pygame.K_LEFT]:
        player2.x -= movespeed
    if keys[pygame.K_RIGHT]:
        player2.x += movespeed

    # ===== მოთამაშეების ეკრანზე შენარჩუნება =====
    # მოთამაშე 1 - მარცხენა ნახევარზე
    if player1.x < 0:
        player1.x = 0
    if player1.x > 335:
        player1.x = 335
    if player1.y < -13:
        player1.y = -13
    if player1.y > 445:
        player1.y = 445

    # მოთამაშე 2 - მარჯვენა ნახევარზე
    if player2.x < 402:
        player2.x = 402
    if player2.x > 736:
        player2.x = 736
    if player2.y < -13:
        player2.y = -13
    if player2.y > 445:
        player2.y = 445

    # ===== ბურთის მოძრაობა =====
    # ბურთის პოზიციის განახლება მიმართულებისა და სისწრაფის მიხედვით
    ball.x += ball_dx * ball_speed  # X კოორდინატი
    ball.y += ball_dy * ball_speed  # Y კოორდინატი

    # ===== ბურთის ზედა/ქვედა კიდეებთან შეჯახება =====
    # თუ ბურთი ეკრანის ზედა ან ქვედა კიდეს ეხება
    if ball.y <= 0 or ball.y >= 452:  # 452 = 500 - 48 (ბურთის სიმაღლე)
        ball_dy *= -1  # ვერტიკალური მიმართულების შებრუნება

    # ===== max_hit-ის განულება შუა ხაზის გადაკვეთისას =====
    # ეს ნაწილი ძალიან მნიშვნელოვანია! ის საშუალებას აძლევს მოთამაშეს ისევ მოარტყას ბურთს
    # ამ ლოგიკით მოთამაშე ვერ მოვარტყამს ბურთს ორჯერ ზედიზედ

    # თუ ბურთი მარჯვნივ მოძრაობს და შუა ხაზს (400) გადააჭარბა
    if ball_dx > 0 and ball.x >= 400:
        max_hit = 0  # განულება - ახლა მარჯვენა მოთამაშე შეძლებს მოარტყას

    # თუ ბურთი მარცხნივ მოძრაობს და შუა ხაზზე (400) ან მარცხნივ არის
    if ball_dx < 0 and ball.x <= 400:
        max_hit = 0  # განულება - ახლა მარცხენა მოთამაშე შეძლებს მოარტყას

    # მარცხენა მოთამაშე (player1) - რამდენიმე პირობა უნდა შესრულდეს:
    if (ball.colliderect(player1) and  # ბურთი ეხება მოთამაშეს
            ball_dx < 0 and  # ბურთი მარცხნივ მოძრაობს (მოთამაშისკენ)
            ball.x <= 335 and  # ბურთი მარცხენა ნახევარშია
            max_hit < 1):  # ჯერ არ შეხებია ბურთს

        ball_dx *= -1  # ჰორიზონტალური მიმართულების შებრუნება
        ball_dy = random.choice([-1, 0, 1])  # ვერტიკალური მიმართულების შემთხვევითი შეცვლა
        max_hit += 1  # ჰიტების მთვლელის გაზრდა (ახლა 1 არის)

    # მარჯვენა მოთამაშე (player2) - იგივე ლოგიკა:
    if (ball.colliderect(player2) and  # ბურთი ეხება მოთამაშეს
            ball_dx > 0 and  # ბურთი მარჯვნივ მოძრაობს (მოთამაშისკენ)
            ball.x >= 402 and  # ბურთი მარჯვენა ნახევარშია
            max_hit < 1):  # ჯერ არ შეხებია ბურთს

        ball_dx *= -1  # ჰორიზონტალური მიმართულების შებრუნება
        ball_dy = random.choice([-1, 0, 1])  # ვერტიკალური მიმართულების შემთხვევითი შეცვლა
        max_hit += 1  # ჰიტების მთვლელის გაზრდა (ახლა 1 არის)

    # ===== ბურთის ეკრნიდან გასვლა ("გოლი") =====
    # თუ ბურთი მარცხენა ან მარჯვენა კიდეს გასცდა
    if ball.x < 0 or ball.x > 752:  # 752 = 800 - 48 (ბურთის სიგანე)
        # ბურთის ეკრანის ცენტრში დაბრუნება
        ball.x = 376  # ეკრანის ცენტრი (800/2 - 48/2)
        ball.y = 228  # ეკრანის ცენტრი (500/2 - 48/2)
        # ახალი შემთხვევითი მიმართულებები
        ball_dx = random.choice([-1, 1])
        ball_dy = random.choice([-1, 1])
        max_hit = 0  # ჰიტების მთვლელის განულება ახალი რაუნდისთვის

    # ===== ყველაფრის ეკრანზე დახატვა =====
    screen.blit(background_img, (0, 0))
    screen.blit(player_1_img, player1)
    screen.blit(player_2_img, player2)
    screen.blit(ball_img, ball)

    # ეკრანის განახლება - ყველა ცვლილების ჩვენება
    pygame.display.flip()

    # FPS-ის შეზღუდვა 60-ზე
    clock.tick(60)

# Pygame-ის დასრულება
pygame.quit()
