import random 
import sys  
import pygame
from pygame.locals import * 

FPS = 32
sirina = 289
visina = 511
ekran = pygame.display.set_mode((sirina,visina))
igra = visina * 0.8
slike = {}
igrac = 'images/igrac.png'
pozadina = 'images/pozadina.png'
cijev = 'images/cijev.png'


def welcome_main_screen():
    

    p_x = int(sirina / 5)
    p_y = int((visina - slike['igrac'].get_height()) / 2)
    poruka_x = int((sirina - slike['poruka'].get_width()) / 2)
    poruka_y = int(visina * 0.13)
    b_x = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
            else:
                ekran.blit(slike['pozadina'], (0, 0))
                ekran.blit(slike['igrac'], (p_x, p_y))
                ekran.blit(slike['poruka'], (poruka_x, poruka_y))
                ekran.blit(slike['baza'], (b_x, igra))
                pygame.display.update()
                time_clock.tick(FPS)


def main_gameplay():
    score = 0
    p_x = int(sirina / 5)
    p_y = int(visina / 2)
    b_x = 0


    n_cijev1 = get_Random_Pipes()
    n_cijev2 = get_Random_Pipes()


    up_pips = [
        {'x': sirina + 200, 'y': n_cijev1[0]['y']},
        {'x': sirina + 200 + (sirina / 2), 'y': n_cijev2[0]['y']},
    ]

    low_pips = [
        {'x': sirina + 200, 'y': n_cijev1[1]['y']},
        {'x': sirina + 200 + (sirina / 2), 'y': n_cijev2[1]['y']},
    ]

    pip_Vx = -4

    p_vx = -9
    p_mvx = 10
    p_mvy = -8
    p_accuracy = 1

    p_flap_accuracy = -8
    p_flap = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if p_y > 0:
                    p_vx = p_flap_accuracy
                    p_flap = True
                    

        cr_tst = is_Colliding(p_x, p_y, up_pips,
                              low_pips)
        if cr_tst:
            return


        p_middle_positions = p_x + slike['igrac'].get_width() / 2
        for pipe in up_pips:
            pip_middle_positions = pipe['x'] + slike['cijev'][0].get_width() / 2
            if pip_middle_positions <= p_middle_positions < pip_middle_positions + 4:
                score += 1
                print(f"Your score is {score}")
                

        if p_vx < p_mvx and not p_flap:
            p_vx += p_accuracy

        if p_flap:
            p_flap = False
        p_height = slike['igrac'].get_height()
        p_y = p_y + min(p_vx, igra - p_y - p_height)


        for pip_upper, pip_lower in zip(up_pips, low_pips):
            pip_upper['x'] += pip_Vx
            pip_lower['x'] += pip_Vx


        if 0 < up_pips[0]['x'] < 5:
            new_pip = get_Random_Pipes()
            up_pips.append(new_pip[0])
            low_pips.append(new_pip[1])


        if up_pips[0]['x'] < -slike['cijev'][0].get_width():
            up_pips.pop(0)
            low_pips.pop(0)


        ekran.blit(slike['pozadina'], (0, 0))
        for pip_upper, pip_lower in zip(up_pips, low_pips):
            ekran.blit(slike['cijev'][0], (pip_upper['x'], pip_upper['y']))
            ekran.blit(slike['cijev'][1], (pip_lower['x'], pip_lower['y']))

        ekran.blit(slike['baza'], (b_x, igra))
        ekran.blit(slike['igrac'], (p_x, p_y))
        d = [int(x) for x in list(str(score))]
        w = 0
        for znamenka in d:
            w += slike['brojevi'][znamenka].get_width()
        Xoffset = (sirina - w) / 2

        for znamenka in d:
            ekran.blit(slike['brojevi'][znamenka], (Xoffset, visina * 0.12))
            Xoffset += slike['brojevi'][znamenka].get_width()
        pygame.display.update()
        time_clock.tick(FPS)


def is_Colliding(p_x, p_y, up_pipes, low_pipes):
    if p_y > igra - 25 or p_y < 0:
        return True

    for pipe in up_pipes:
        pip_h = slike['cijev'][0].get_height()
        if (p_y < pip_h + pipe['y'] and abs(p_x - pipe['x']) < slike['cijev'][0].get_width()):
            return True

    for pipe in low_pipes:
        if (p_y + slike['igrac'].get_height() > pipe['y']) and abs(p_x - pipe['x']) < \
                slike['cijev'][0].get_width():
            return True

    return False


def get_Random_Pipes():
    
    pip_h = slike['cijev'][0].get_height()
    off_s = visina / 4
    yes2 = off_s + random.randrange(0, int(visina - slike['baza'].get_height() - 1.2 * off_s))
    pipeX = sirina + 10
    y1 = pip_h - yes2 + off_s
    pipe = [
        {'x': pipeX, 'y': -y1},  
        {'x': pipeX, 'y': yes2}  
    ]
    return pipe


if __name__ == "__main__":

    pygame.init()
    time_clock = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird Game')
    slike['brojevi'] = (
        pygame.image.load('images/0.png').convert_alpha(),
        pygame.image.load('images/1.png').convert_alpha(),
        pygame.image.load('images/2.png').convert_alpha(),
        pygame.image.load('images/3.png').convert_alpha(),
        pygame.image.load('images/4.png').convert_alpha(),
        pygame.image.load('images/5.png').convert_alpha(),
        pygame.image.load('images/6.png').convert_alpha(),
        pygame.image.load('images/7.png').convert_alpha(),
        pygame.image.load('images/8.png').convert_alpha(),
        pygame.image.load('images/9.png').convert_alpha(),
    )

    slike['poruka'] = pygame.image.load('images/poruka.png').convert_alpha()
    slike['baza'] = pygame.image.load('images/baza.png').convert_alpha()
    slike['cijev'] = (pygame.transform.rotate(pygame.image.load(cijev).convert_alpha(), 180),
                          pygame.image.load(cijev).convert_alpha()
                          )

    slike['pozadina'] = pygame.image.load(pozadina).convert()
    slike['igrac'] = pygame.image.load(igrac).convert_alpha()

    while True:
        welcome_main_screen()  
        main_gameplay() 
