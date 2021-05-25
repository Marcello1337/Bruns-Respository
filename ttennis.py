import pygame
import random
import sys

pygame.init()

screen_width = 1000
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)


def glatt(x, y):
    length = (x ** 2 + y ** 2) ** 0.5

    x /= length
    y /= length
    return [x, y]


class player(object):
    def __init__(self):
        self.pos = [[40, 250], [960,250]]
        self.change = [0,0]
        self.color = (250, 250, 250)

    def move(self):
        self.pos[0][1] += self.change[0]
        self.pos[1][1] += self.change[1]
        if self.pos[0][1] <= 1 or self.pos[0][1] >= 450:
            self.change[0] = 0
        if self.pos[1][1] <= 1 or self.pos[1][1] >= 450:
            self.change[1] = 0

    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), ((self.pos[0][0], self.pos[0][1]), (10, 50)))
        pygame.draw.rect(screen, (255, 255, 255), ((self.pos[1][0], self.pos[1][1]), (10, 50)))

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    self.change[1] = -5

                elif event.key == pygame.K_DOWN:
                    self.change[1] = 5

                if event.key == pygame.K_w:
                    self.change[0] = -5

                elif event.key == pygame.K_s:
                    self.change[0] = 5

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.change[0] = 0
                elif event.key == pygame.K_s:
                    self.change[0] = 0

                if event.key == pygame.K_UP:
                    self.change[1] = 0
                elif event.key == pygame.K_DOWN:
                    self.change[1] = 0


class Ball(object):
    def __init__(self):
        self.pos = [250, 250]
        self.color = (250, 250, 250)
        self.random_direction=[0,0]
        self.score = [0, 0]

    def move(self):
        self.pos[0] += self.random_direction[0]
        self.pos[1] += self.random_direction[1]
        if self.pos[1] <= 0 or self.pos[1] >= 500:
            self.random_direction[1] *= -1

    def draw(self):
        pygame.draw.circle(screen, (255, 255, 255), self.pos, 5)

    def reset(self):
        if self.pos[0] <= 0:
            self.pos[0] = 500
            self.pos[1] = 250
            self.random_direction[0] = random.randint(-10, 10)
            self.random_direction[1] = random.randint(-10, 10)
            self.score[1] += 1

        if self.pos[0] >= 1000:
            self.pos[0] = 250
            self.pos[0] = 250
            self.random_direction[0] = random.randint(-10, 10)
            self.random_direction[1] = random.randint(-10, 10)
            self.score[0] += 1

    def randm_direction(self):
        g = glatt(random.randint(-20, 20), 0.5*random.randint(-10, 10))
        self.random_direction[0] = g[0]*8
        self.random_direction[1] = g[1]*8


def show_score(x, y, score1, score2):
    score = font.render(str(score1) + " : " + str(score2), True, (255, 255, 255))
    screen.blit(score, (x, y))


font = pygame.font.SysFont("comicsansms", 20)

textX = 500
textY = 490


def main():
    clock = pygame.time.Clock()

    ball=Ball()
    players=player()

    ball.randm_direction()


    while True:
        clock.tick(60)
        screen.fill((0, 0, 0))

        ball.move()
        players.handle_keys()
        players.move()
        players.draw()
        ball.draw()
        ball.reset()

        if ball.pos[0] <= players.pos[0][0]+10 and players.pos[0][1] <= ball.pos[1] <= players.pos[0][1]+50:
            ball.random_direction[0] *= -1

        elif ball.pos[0] >= players.pos[1][0] and players.pos[1][1] <= ball.pos[1] <= players.pos[1][1]+50:
            ball.random_direction[0]  *= -1


        show_score(470, 470, ball.score[0], ball.score[1])

        pygame.display.update()


main()
