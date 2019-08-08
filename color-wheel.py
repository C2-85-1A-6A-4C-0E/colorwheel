import pygame, pygame.locals as locals, sys, math

size = height, width = 600, 600
black = (0,0,0)
white = (255,255,255)
gray = grey = (127,127,127)
primary_count = 3
secondary_count = 3
center = center_x, center_y = [i//2 for i in size]
inner_radus = 100
outer_radus = 250


pygame.init()
screen = pygame.display.set_mode(size)
screen.fill(white)

wedges = primary_count * (secondary_count + 1)
angle = (360 / wedges)
start_angle = angle / 2

pygame.draw.circle(screen, black, center, inner_radus, 1)
bounds = pygame.draw.circle(screen, black, center, outer_radus, 1)

print(bounds.x, bounds.y, bounds.height, bounds.width, bounds.center)


def draw_line_at_angle(surface, angle, center, radus, inner_radus=0):
	radians = math.radians(angle)
	if inner_radus is 0:
		x1, y1 = center
	else:
		x1 = ( inner_radus * math.sin(radians) ) + center[0]
		y1 = -( inner_radus * math.cos(radians) ) + center[1]
	x2 = (radus * math.sin(radians)) + center[0]
	y2 = -(radus * math.cos(radians)) + center[1]

	p1 = x1, y1
	p2 = x2, y2

	pygame.draw.line(surface, black, p1, p2, 1)

def point_off_angle(center, radius, angle):
	radians = math.radians(angle)
	x = (radius * math.sin(radians)) + center[0]
	y = -(radius * math.cos(radians)) + center[1]
	return int(x), int(y)



for i, a in enumerate(range(int(start_angle), 90, int(angle))):
	draw_line_at_angle(screen, a, center, outer_radus, inner_radus)
	if i%(secondary_count + 1) == 0:
		an = pygame.draw.arc(screen, gray, bounds, a-angle, a, 50)
		print(an.x, an.y, an.width, an.height)
		pygame.draw.circle(screen, black, point_off_angle(center, 150, a-start_angle), 20)

pygame.display.flip()


if __name__ == "__main__":
	while True:
		for event in pygame.event.get():
			if event.type is locals.QUIT:
				pygame.quit()
				sys.exit()