import pygame as pg

ooo = pg.image.load('ooo.pns')
xxx = pg.image.load('xxx.pns')
owin = pg.image.load('owin.pns')
xwin = pg.image.load('xwin.pns')
draw = pg.image.load('draw.pns')

pg.init()
win = pg.display.set_mode((300, 300))
pg.display.set_caption('x_o')
clock = pg.time.Clock()
_field = [[' '] * 3 for i in (0, 1, 2)]
_turn = True
turnCount = 0
run = True
blockKeys = False
side = 10
x = 0
y = 0


def winCheck(chr):
    if _field[0][0] == _field[0][1] == _field[0][2] == chr: return True
    if _field[1][0] == _field[1][1] == _field[1][2] == chr: return True
    if _field[2][0] == _field[2][1] == _field[2][2] == chr: return True
    if _field[0][0] == _field[1][0] == _field[2][0] == chr: return True
    if _field[0][1] == _field[1][1] == _field[2][1] == chr: return True
    if _field[0][2] == _field[1][2] == _field[2][2] == chr: return True
    if _field[0][2] == _field[1][1] == _field[2][0] == chr: return True
    if _field[0][0] == _field[1][1] == _field[2][2] == chr: return True
    return False


def showWindow():
    global blockKeys
    win.fill((255, 255, 255))
    pg.draw.line(win, (0, 0, 0), (0, 100), (300, 100), 3)
    pg.draw.line(win, (0, 0, 0), (0, 200), (300, 200), 3)
    pg.draw.line(win, (0, 0, 0), (100, 0), (100, 300), 3)
    pg.draw.line(win, (0, 0, 0), (200, 0), (200, 300), 3)

    for i, _ in enumerate(_field):
        for j, v in enumerate(_field[i]):
            if v == 'o':
                win.blit(ooo, ((12 + 100 * i), (12 + 100 * j)))
            elif v == 'x':
                win.blit(xxx, ((12 + 100 * i), (12 + 100 * j)))

    pg.draw.rect(win, (100, 100, 100), ((50 + (100 * x)) - (side // 2), (50 + (100 * y)) - (side // 2), side, side))

    if winCheck('o'):
        win.blit(owin, (15, 110))
        blockKeys = True
    elif winCheck('x'):
        win.blit(xwin, (15, 110))
        blockKeys = True
    elif turnCount == 9:
        win.blit(draw, (15, 110))
        blockKeys = True
    pg.display.update()


while run:
    clock.tick(15)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYUP:
            if event.key == pg.K_ESCAPE:
                run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_d and x < 2 and not blockKeys:   x += 1
            if event.key == pg.K_a and x > 0 and not blockKeys:   x -= 1
            if event.key == pg.K_w and y > 0 and not blockKeys:   y -= 1
            if event.key == pg.K_s and y < 2 and not blockKeys:   y += 1
            if event.key == pg.K_SPACE and not blockKeys:
                if _turn and _field[x][y] == ' ':
                    _field[x][y] = 'x'
                    _turn = False
                    turnCount += 1
                elif not _turn and _field[x][y] == ' ':
                    _field[x][y] = 'o'
                    _turn = True
                    turnCount += 1
            if event.key == pg.K_r:
                _field = [[' '] * 3 for i in (0, 1, 2)]
                _turn = True
                turnCount = 0
                blockKeys = False

    showWindow()
pg.quit()
