import pygame
import sys

pygame.init()
size_block=100
margin=15
width=heigth=size_block*3+margin*4

size_window=(width, heigth)
screen=pygame.display.set_mode(size_window)
pygame.display.set_caption("Tic tac toe")

black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
white=(255,255,255)
arr=[[0]*3 for i in range (3)]
query=0

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type==pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse=pygame.mouse.get_pos()
            col=x_mouse//(size_block+margin)
            row=y_mouse//(size_block+margin)
            if arr[row][col]==0:
                if query % 2 == 0:
                    arr[row][col] = 'x'
                else:
                    arr[row][col] = 'o'
                query += 1


    for row in range(3):
        for col in range(3):
            if arr[row][col]=='x':
                color=red
            elif arr[row][col]=='o':
                color=green
            else:
                color=white
            x=col*size_block+(col+1)*margin
            y=row*size_block+(row+1)*margin


    pygame.display.update()

