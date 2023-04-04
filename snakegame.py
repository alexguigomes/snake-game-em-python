import pygame
import random

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BLOCK_SIZE = 10
SPEED = 30

class Snake:
    def __init__(self):
        self.body = [(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)]
        self.direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])

    def move(self):
        x, y = self.body[0]
        dx, dy = self.direction
        new_block = (x + dx * BLOCK_SIZE, y + dy * BLOCK_SIZE)
        self.body.insert(0, new_block)
        self.body.pop()

class Food:
    def __init__(self):
        self.position = (random.randint(0, SCREEN_WIDTH/BLOCK_SIZE-1) * BLOCK_SIZE,
                         random.randint(0, SCREEN_HEIGHT/BLOCK_SIZE-1)* BLOCK_SIZE) 
    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), (self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    snake= Snake()
    food = Food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    function.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:

                    main()

        if snake.body[0][0] < 0 or snake.body[0][0] > SCREEN_WIDTH or snake.body[0][1] < 0 or snake.body[0][1] > SCREEN_HEIGHT:

            main()



        keys = pygame.key.get_pressed()


        if keys[pygame.K_LEFT]:
            snake.direction = (-1, 0)

        elif keys[pygame.K_RIGHT]:
            snake.direction=(1,0)
        
        elif keys[pygame.K_UP]:
            snake.direction = (0, -1)

        elif keys [pygame.K_DOWN]:
            snake.direction = (0, 1)

        snake.move()

        if snake.body[0] == food.position:
            snake.body.append(snake.body[-1])
            food = Food()

        screen.fill((0, 0, 0))
        for block in snake.body:
            pygame.draw.rect(screen, (255, 255, 255), (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))
        food.draw(screen)


        pygame.display.update()
        clock.tick(SPEED)

if __name__==  '__main__':
    main()