import pygame
import random

pygame.init()
width = 600
height = 400

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

snake_size = 20
snake_x = 300
snake_y = 200

x_change = 0
y_change = 0

snake_list = []
snake_length = 1

food_x = random.randrange(0, width - snake_size, 20)
food_y = random.randrange(0, height - snake_size, 20)

score = 0
font = pygame.font.SysFont(None, 35)

clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -20
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = 20
                y_change = 0
            elif event.key == pygame.K_UP:
                x_change = 0
                y_change = -20
            elif event.key == pygame.K_DOWN:
                x_change = 0
                y_change = 20

    snake_x += x_change
    snake_y += y_change

    if snake_x < 0 or snake_x >= width or snake_y < 0 or snake_y >= height:
        running = False

    screen.fill(black)

    pygame.draw.rect(screen, red, [food_x, food_y, snake_size, snake_size])

    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_list.append(snake_head)

    if len(snake_list) > snake_length:
        del snake_list[0]

    for segment in snake_list[:-1]:
        if segment == snake_head:
            running = False

    for segment in snake_list:
        pygame.draw.rect(screen, green, [segment[0], segment[1], snake_size, snake_size])
    if snake_x == food_x and snake_y == food_y:
        food_x = random.randrange(0, width - snake_size, 20)
        food_y = random.randrange(0, height - snake_size, 20)
        snake_length += 1
        score += 1
    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(10)

pygame.quit()

print("Game Over!")
print("Final Score:", score)
