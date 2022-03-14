import pygame

WIDTH, HEIGHT = 1920*4, 1280*4

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mandlebrot Set Drawer")
WIN.fill((255, 255, 255))

RS, RE = -2, 1
IS, IE = -1, 1
maxIter = 100

def mandlebrot(p):
  z = 0
  n = 0
  while abs(z) <= 2 and n < maxIter:
    z = z*z + p
    n += 1
  return n

while maxIter < 101:
  print(maxIter)
  pygame.display.update()
  for x in range(WIDTH):
    print(x)
    for y in range(HEIGHT):
      point = complex(RS + (x / WIDTH) * (RE - RS), IS + (y / HEIGHT) * (IE - IS))
      #print(point)
      color = 255 - int(mandlebrot(point) * 255 / maxIter)
      WIN.set_at((x, y), (color, color, color))
      keys_pressed = pygame.key.get_pressed()
      if keys_pressed[pygame.K_ESCAPE]:
        pygame.quit()
        exit()
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()
  pygame.image.save(WIN, f"MandelbrotPics/{maxIter}iterations{WIDTH}x{HEIGHT}px.jpeg")
  maxIter = maxIter + 1

while True:
  keys_pressed = pygame.key.get_pressed()
  if keys_pressed[pygame.K_ESCAPE]:
    pygame.quit()
    exit()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()