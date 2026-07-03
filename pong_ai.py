import pygame
import sys

# Initialize pygame and mixer
pygame.init()
pygame.mixer.init()

# Load sounds
bounce_sound = pygame.mixer.Sound("Ball_hit.wav")
score_sound = pygame.mixer.Sound("Scoring.wav")
winlose_sound = pygame.mixer.Sound("Winning_Losing.wav")

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)

# Ball setup
BALL_SIZE = 20
ball = pygame.Rect(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)

# Paddle setup
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
player1 = pygame.Rect(50, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2 = pygame.Rect(WIDTH-60, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Scores
p1_score = 0
p2_score = 0
WIN_SCORE = 5

# Font
pygame.font.init()
font = pygame.font.SysFont("Arial", 40, bold=True)
menu_font = pygame.font.SysFont("Arial", 60, bold=True)

# Clock
clock = pygame.time.Clock()

# Game state
mode = "menu"
difficulty = None
ball_speed_x, ball_speed_y = 5, 5

def draw_paddle(rect, color):
    pygame.draw.circle(screen, color, (rect.centerx, rect.centery), 30)
    pygame.draw.rect(screen, BLACK, (rect.centerx - 5, rect.centery, 10, 50))

def set_difficulty(level):
    global PADDLE_HEIGHT, ball_speed_x, ball_speed_y, player1, player2
    if level == "easy":
        PADDLE_HEIGHT = 120
        ball_speed_x, ball_speed_y = 4, 4
    elif level == "medium":
        PADDLE_HEIGHT = 100
        ball_speed_x, ball_speed_y = 6, 6
    elif level == "hard":
        PADDLE_HEIGHT = 70
        ball_speed_x, ball_speed_y = 8, 8
    player1.height = PADDLE_HEIGHT
    player2.height = PADDLE_HEIGHT

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Menu navigation
        if mode == "menu":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    mode = "ai_select"
                elif event.key == pygame.K_2:
                    mode = "2p_select"

        # Difficulty selection
        if mode in ["ai_select", "2p_select"]:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    set_difficulty("easy")
                    mode = "ai" if mode == "ai_select" else "2p"
                elif event.key == pygame.K_m:
                    set_difficulty("medium")
                    mode = "ai" if mode == "ai_select" else "2p"
                elif event.key == pygame.K_h:
                    set_difficulty("hard")
                    mode = "ai" if mode == "ai_select" else "2p"

    # Menu screen
    if mode == "menu":
        screen.fill(BLACK)
        title = menu_font.render("PONG GAME", True, WHITE)
        option1 = font.render("Press 1: VS AI", True, BLUE)
        option2 = font.render("Press 2: 2 Player", True, RED)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 150))
        screen.blit(option1, (WIDTH//2 - option1.get_width()//2, 300))
        screen.blit(option2, (WIDTH//2 - option2.get_width()//2, 380))
        pygame.display.flip()
        continue

    # Difficulty screen
    if mode in ["ai_select", "2p_select"]:
        screen.fill(BLACK)
        title = menu_font.render("Select Difficulty", True, WHITE)
        easy = font.render("Press E: Easy", True, WHITE)
        medium = font.render("Press M: Medium", True, WHITE)
        hard = font.render("Press H: Hard", True, WHITE)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 150))
        screen.blit(easy, (WIDTH//2 - easy.get_width()//2, 300))
        screen.blit(medium, (WIDTH//2 - medium.get_width()//2, 360))
        screen.blit(hard, (WIDTH//2 - hard.get_width()//2, 420))
        pygame.display.flip()
        continue

    # Player 1 controls (W/S)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= 7
    if keys[pygame.K_s] and player1.bottom < HEIGHT:
        player1.y += 7

    # Player 2 or AI
    if mode == "2p":
        if keys[pygame.K_UP] and player2.top > 0:
            player2.y -= 7
        if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
            player2.y += 7
    else:
        if player2.centery < ball.centery:
            player2.y += 5
        if player2.centery > ball.centery:
            player2.y -= 5

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Collisions
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1
        bounce_sound.play()

    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1
        bounce_sound.play()

    # Scoring
    if ball.left <= 0:
        p2_score += 1
        score_sound.play()
        ball.center = (WIDTH//2, HEIGHT//2)
        ball_speed_x *= -1
    if ball.right >= WIDTH:
        p1_score += 1
        score_sound.play()
        ball.center = (WIDTH//2, HEIGHT//2)
        ball_speed_x *= -1

    # Winning condition
    if p1_score >= WIN_SCORE or p2_score >= WIN_SCORE:
        winlose_sound.play()
        screen.fill(BLACK)

        if mode == "ai":
            if p1_score >= WIN_SCORE:
                message = menu_font.render("YOU WIN!!!", True, BLUE)
            else:
                message = menu_font.render("YOU LOSE", True, RED)
        else:
            if p1_score >= WIN_SCORE:
                message = menu_font.render("PLAYER 1 WINS!", True, BLUE)
            else:
                message = menu_font.render("PLAYER 2 WINS!", True, RED)

        screen.blit(message, (WIDTH//2 - message.get_width()//2, HEIGHT//2 - message.get_height()//2))
        pygame.display.flip()
        pygame.time.delay(3000)

        p1_score, p2_score = 0, 0
        ball.center = (WIDTH//2, HEIGHT//2)
        mode = "menu"
        continue

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, (0, 0, WIDTH//2, HEIGHT))
    pygame.draw.rect(screen, RED, (WIDTH//2, 0, WIDTH//2, HEIGHT))
    draw_paddle(player1, BLUE)
    draw_paddle(player2, RED)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

    p1_text = font.render(f"P1: {p1_score}", True, WHITE)
    p2_text = font.render(f"{'AI' if mode=='ai' else 'P2'}: {p2_score}", True, WHITE)
    screen.blit(p1_text, (20, 20))
    screen.blit(p2_text, (WIDTH-200, 20))

    pygame.display.flip()
    clock.tick(60)
