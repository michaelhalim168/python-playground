from random_word import RandomWords
import pygame
import math
import os

pygame.init()

WIDTH, HEIGHT = 800, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman!")

images = [pygame.image.load(os.path.join("images",f"hangman{i}.png")) for i in range(7)]

RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH-(RADIUS*2 + GAP) * 13) /2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

LETTER_FONT = pygame.font.SysFont('comicsans', 40)
hangman_status = 0
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 60
clock = pygame.time.Clock()

run = True

def draw():
    WIN.fill(WHITE)

    for letter in letters:
        x, y, ltr = letter
        pygame.draw.circle(WIN, BLACK, (x, y), RADIUS, 3)
        text = LETTER_FONT.render(ltr, 1, BLACK)
        WIN.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    WIN.blit(images[hangman_status], (150, 100))
    pygame.display.update()


while run:
    clock.tick(FPS)

    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                dis = math.sqrt((x-m_x)**2 + (y - m_y)**2)
                if dis < RADIUS:
                    print(ltr)



pygame.quit()



'''
def generate_word():
    r = RandomWords()
    return r.get_random_word(hasDictionaryDef="true")

def display(random_word):
    word_len_list = ['_' for i in random_word]
    return word_len_list

def check_board(guess, random_word, word_list, num_lives):
    if guess not in random_word:
        num_lives -= 1
    else:
        if guess in word_list:
            print("You've already guessed the word.")
        else:
            for index in range(len(word_list)):
                if guess == random_word[index]:
                    word_list[index] = guess

    print(word_list)
    return num_lives

def game_over(num_lives, word_list):
    game_on = True
    if num_lives == 0 and '_' in word_list:
        print('You lose')
        game_on = False
    elif num_lives !=0 and '_' not in word_list:
        print('You win')
        game_on = True

    return game_on

game_on = True
random_word = generate_word()
word_list = display(random_word)
num_lives = 7
print(random_word)
print(word_list)

while game_on:
    user_input = input('Guess a letter: ').lower()
    num_lives = check_board(user_input, random_word, word_list, num_lives)
    print(num_lives)
    game_on = game_over(num_lives, word_list)
'''

