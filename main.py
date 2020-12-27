import pygame
import math
import random
import sys
import time

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Sorting Algorithms")

my_font = pygame.font.SysFont('Comic Sans MS', 25)

clock = pygame.time.Clock()

in_game = True
is_sorted = False

values = []
buttons = [pygame.Rect(20, 10, 100, 60), pygame.Rect(130, 10, 100, 60), pygame.Rect(240, 10, 100, 60),
          pygame.Rect(350, 10, 100, 60), pygame.Rect(460, 10, 100, 60), pygame.Rect(570, 10, 100, 60),
          pygame.Rect(680, 10, 100, 60), pygame.Rect(350, 465, 40, 30), pygame.Rect(410, 465, 40, 30)]
words = ['MERGE', 'QUICK', 'BUBBLE', 'SHAKER', 'INSERTION', 'SELECTION', 'RESET', '-', '+']

size = 750

def random_values():
  global values, is_sorted, size
  values = [[random.randrange(376), (255, 255, 255)] for i in range(size)]
  is_sorted = False

def change_values(dir):
  global size, is_sorted
  if size >= 50 and size <= 750:
    change = 25
  elif size >= 3 and size <= 25:
    change = 1
  else:
    change = 0
  size += change * dir
  if size > 750:
    size = 750
  random_values()

def display_text():
  global words, buttons
  for i in range(9):
    text = my_font.render(words[i], False, (0, 0, 0))
    x = buttons[i].left + (buttons[i].width // 2) - (pygame.Surface.get_width(text) // 2) 
    y = buttons[i].top + (buttons[i].height // 2) - (pygame.Surface.get_height(text) // 2) 
    screen.blit(text, (x, y))
  
def draw_bars(values):
  width = 750 // len(values)
  x = 25    
  for b in range(len(values)):
    pygame.draw.line(screen, values[b][1], (x, 460 - values[b][0]), (x, 460), width)
    x += width

def refill(lst):
  screen.fill((0, 0, 0))
  draw_bars(lst)
  pygame.draw.line(screen, (255, 255, 255), (0, 80), (800, 80), 2)
  pygame.draw.line(screen, (255, 255, 255), (0, 460), (800, 460), 2)
  for i in buttons:
    pygame.draw.rect(screen, (255, 255, 255), i)
  display_text()
  pygame.display.update()
  pygame.time.delay(10)

def bubble_sort(lst):
  global is_sorted
  swapped = True
  pygame.event.pump()
  end = len(lst) - 1
  while swapped:
    swapped = False
    for j in range(end):
      if lst[j] > lst[j + 1]:
        lst[j], lst[j + 1] = lst[j + 1], lst[j]
        swapped = True
    lst[end][1] = (255, 0, 0)
    refill(lst)
    lst[end][1] = (255, 255, 255)
    end -= 1
  else:
    for c in lst:
      c[1] = (0, 255, 0)
    is_sorted = True
  return lst
     
def selection_sort(lst):
  global is_sorted
  pygame.event.pump()
  for i in range(len(lst) + 1):
    if i < len(lst):
      smallest = i
      for j in range(i + 1, len(lst)):
        if lst[j] < lst[smallest]:
          smallest = j
      lst[i][1] = (255, 0, 0)
      lst[smallest][1] = (255, 0, 0)
      lst[i], lst[smallest] = lst[smallest], lst[i]
      refill(lst)
      lst[i][1] = (255, 255, 255)
      lst[smallest][1] = (255, 255, 255)
    else:
      for c in lst:
        c[1] = (0, 255, 0)
      is_sorted = True
  return lst
  
def insertion_sort(lst):
  global is_sorted
  i = 1
  pygame.event.pump()
  while i < len(lst):
    j = i
    while j > 0 and lst[j - 1] > lst[j]:
      lst[j - 1], lst[j] = lst[j], lst[j - 1] 
      j -= 1
    lst[i][1] = (255, 0, 0)
    lst[j][1] = (255, 0, 0)
    refill(lst)
    lst[i][1] = (255, 255, 255)
    lst[j][1] = (255, 255, 255)
    i += 1
  else:
    for c in lst:
      c[1] = (0, 255, 0)
    is_sorted = True
  return lst

def shaker_sort(lst):
  global is_sorted
  swapped = True
  end = len(lst) - 1
  start = 0
  pygame.event.pump()
  while swapped:
    swapped = False
    for j in range(end):
      if lst[j] > lst[j + 1]:
        lst[j], lst[j + 1] = lst[j + 1], lst[j]
        swapped = True
    lst[end][1] = (255, 0, 0)
    refill(lst)
    lst[end][1] = (255, 255, 255)
    end -= 1

    for i in range(end):
      if lst[len(lst) - i - 1] < lst[len(lst) - i - 2]:
        lst[len(lst) - i - 1], lst[len(lst) - i - 2] = lst[len(lst) - i - 2], lst[len(lst) - i - 1]
        swapped = True
    lst[start][1] = (255, 0, 0)
    refill(lst)
    lst[start][1] = (255, 255, 255)
    start += 1
  else:
    for c in lst:
      c[1] = (0, 255, 0)
    is_sorted = True
  return lst

def partition(lst, begin, end):
  pivot = lst[end]
  i = begin - 1
  pygame.event.pump()
  for j in range(begin, end):
    if lst[j] < pivot:
      i += 1
      lst[i], lst[j] = lst[j], lst[i]
      lst[j][1] = (255, 0, 0)
      refill(lst)
      pygame.time.delay(5)
      lst[j][1] = (255, 255, 255)
  lst[i + 1], lst[end] = lst[end], lst[i + 1]
  lst[end][1] = (255, 0, 0)
  refill(lst)
  pygame.time.delay(5)
  lst[end][1] = (255, 255, 255)
  return i + 1
def quick_sort(lst, begin, end):
  global is_sorted
  if begin < end:
    part = partition(lst, begin, end)
    quick_sort(lst, begin, part - 1)
    quick_sort(lst, part + 1, end)
  if lst == sorted(lst):
    for c in lst:
      c[1] = (0, 255, 0)
    is_sorted = True
 
def merge_sort(lst, l, r):
  mid = (l + r) // 2
  if l < r:
    merge_sort(lst, l, mid)
    merge_sort(lst, mid + 1, r)
    merge(lst, l, mid, mid + 1, r)
  
def merge(lst, s1, e1, s2, e2):
  global is_sorted
  i, j = s1, s2
  temp = []
  pygame.event.pump()
  while i <= e1 and j <= e2:
    if lst[i][0] < lst[j][0]:
      lst[i][1] = (255, 0, 0)
      lst[j][1] = (255, 0, 0)
      refill(lst)
      lst[i][1] = (255, 255, 255)
      lst[j][1] = (255, 255, 255)
      temp.append(lst[i])
      i += 1
    else:
      temp.append(lst[j])
      j += 1
  while i <= e1:
    refill(lst)
    temp.append(lst[i])
    i += 1
  while j <= e2:
    refill(lst)
    temp.append(lst[j])
    j += 1
  j = 0
  for i in range(s1, e2 + 1):
    pygame.event.pump()
    lst[i] = temp[j]
    j += 1
    if e2 - s1 == len(lst) - 1:
      for c in lst:
        c[1] = (0, 255, 0)
      is_sorted = True

def find_function(pos, y):
  global is_sorted, values
  if is_sorted == False:
    if pos == 20:
      merge_sort(values, 0, len(values) - 1)
    elif pos == 130:
      quick_sort(values, 0, len(values) - 1)
    elif pos == 240:
      bubble_sort(values)
    elif pos == 350 and y == 10:
      shaker_sort(values)
    elif pos == 460:
      insertion_sort(values)
    elif pos == 570:
      selection_sort(values)
  if pos == 680:
    random_values()
  if pos == 350 and y == 465:
    change_values(-1)
  if pos == 410 and y == 465:
    change_values(1)

random_values()

while in_game:
  
  screen.fill((0, 0, 0))
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      in_game = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      mouse_pos = pygame.mouse.get_pos()
      button_clicked = [button for button in buttons if button.collidepoint(mouse_pos)]
      if len(button_clicked) > 0:
        find_function(button_clicked[0].left, button_clicked[0].top)
      
  refill(values)
  
  pygame.display.update()
  clock.tick(60)

pygame.quit()
quit()