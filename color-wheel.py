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
start_angle = 0 - angle / 2

#pygame.draw.circle(screen, black, center, inner_radus, 1)
#bounds = pygame.draw.circle(screen, black, center, outer_radus, 1)

#print(bounds.x, bounds.y, bounds.height, bounds.width, bounds.center)

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

def draw_wedge(surface, inner_radius, outer_radius, start_angle, angle, center, border_color=black, fill_color=white):
	p1 = point_off_angle(center, outer_radius, start_angle)
	p2 = point_off_angle(center, inner_radius, start_angle)
	p3 = point_off_angle(center, inner_radius, start_angle+angle)
	p4 = point_off_angle(center, outer_radius, start_angle+angle)
	points = (p1, p2, p3, p4)
	pygame.draw.polygon(surface, fill_color, points)
	pygame.draw.polygon(surface, border_color, points, 1)


for i, a in enumerate(range(int(start_angle), 360, int(angle))):
	if i%(secondary_count + 1) == 0:
		draw_wedge(screen, inner_radus, outer_radus, a, angle, center, black, gray)
	else:
		draw_wedge(screen, inner_radus, outer_radus, a, angle, center, black, white)

pygame.display.flip()


if __name__ == "__main__":
	while True:
		for event in pygame.event.get():
			if event.type is locals.QUIT:
				pygame.quit()
				sys.exit()