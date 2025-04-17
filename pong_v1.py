import pygame

pygame.init()  # initializes pygame library

# font that is used to show text
font20 = pygame.font.Font("freesansbold.ttf", 20)

# values for colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# how big is the screen and setting it up
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()
FPS = 60


# setup the first paddle
class Striker:  # setup location speed size and color
    def __init__(self, posx, posy, width, height, speed, color):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color

        # rect is used to control position and collision of object
        self.geekRect = pygame.Rect(posx, posy, width, height)
        self.geek = pygame.draw.rect(screen, self.color, self.geekRect)

    # show object on screen
    def display(self):
        self.geek = pygame.draw.rect(screen, self.color, self.geekRect)

    # update object on screen and track the paddles
    def update(self, yFac):
        self.posy = self.posy + self.speed * yFac

        # setting paddles to below the top of the screen cannot go above
        if self.posy <= 0:
            self.posy = 0

        # same thing for the bottom
        elif self.posy + self.height >= HEIGHT:
            self.posy = HEIGHT - self.height

        # updating the screen and other values
        self.geekRect = (self.posx, self.posy, self.width, self.height)

    def displayScore(self, text, score, x, y, color):
        text = font20.render(text + str(score), True, color)
        textRect = text.get_rect()
        textRect.center = (x, y)
        screen.blit(text, textRect)

    def getRect(self):
        return self.geekRect


# define the ball
class Ball:
    def __init__(self, posx, posy, radius, speed, color):  # creates the ball
        self.posx = posx
        self.posy = posy
        self.radius = radius
        self.speed = speed
        self.color = color
        self.xFac = 1
        self.yFac = -1
        self.ball = pygame.draw.circle(
            screen, self.color, (self.posx, self.posy), self.radius
        )
        self.firstTime = 1

    def display(self):
        self.ball = pygame.draw.circle(
            screen, self.color, (self.posx, self.posy), self.radius
        )

    def update(self):
        self.posx += self.speed * self.xFac
        self.posy += self.speed * self.yFac

        # implement collision
        if self.posy <= 0 or self.posy >= HEIGHT:
            self.yFac *= -1

        if self.posx <= 0 and self.firstTime:
            self.firstTime = 0
            return 1
        elif self.posx >= WIDTH and self.firstTime:
            self.firstTime = 0
            return -1
        else:
            return 0

    def reset(self):
        self.posx = WIDTH // 2
        self.posy = HEIGHT // 2
        self.xFac *= -1
        self.firstTime = 1

    def hit(self):
        self.xFac *= -1

    def getRect(self):
        return self.ball


# main game setup
def main():
    running = True

    # defining the objects
    geek1 = Striker(20, 0, 10, 100, 10, GREEN)
    geek2 = Striker(WIDTH - 30, 0, 10, 100, 10, GREEN)
    ball = Ball(WIDTH // 2, HEIGHT // 2, 7, 7, WHITE)

    listOfGeeks = [geek1, geek2]
    geek1Score, geek2Score = 0, 0  # initial player score
    geek1YFac, geek2YFac = 0, 0

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    geek2YFac = -1
                elif event.key == pygame.K_DOWN:
                    geek2YFac = 1
                elif event.key == pygame.K_w:
                    geek1YFac = -1
                elif event.key == pygame.K_s:
                    geek1YFac = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    geek2YFac = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    geek1YFac = 0

        # collision
        for geek in listOfGeeks:
            if pygame.Rect.colliderect(ball.getRect(), geek.getRect()):
                ball.hit()

        geek1.update(geek1YFac)
        geek2.update(geek2YFac)
        point = ball.update()

        # -1 geek 1 has scored +1 geek 2 scored 0 no one scored
        if point == -1:
            geek1Score += 1
        elif point == 1:
            geek2Score += 1

        # someone has scored ball is out of range reset
        if point:
            ball.reset()

        # display players and the ball
        geek1.display()
        geek2.display()
        ball.display()

        # score the score
        geek1.displayScore("Geek_1 : ", geek1Score, 100, 20, WHITE)
        geek2.displayScore("Geek_2 : ", geek2Score, WIDTH - 100, 20, WHITE)

        pygame.display.update()
        # adjust framerate
        clock.tick(FPS)


if __name__ == "__main__":
    main()
    pygame.quit()
