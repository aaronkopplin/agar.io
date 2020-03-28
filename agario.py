import pygame
import sys
import random
import time
import math

pygame.init()

class game():
	def __init__(self):
		self.colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
		self.width = 1000
		self.height = 1000
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.num_points = 50

		# game objects
		self.points = []
		self.players = []

		#create points game object
		self.spawn_players()
		self.spawn_points()
		
		# last step
		self.run()

	def spawn_players(self):
		self.players.append(player())

	def spawn_points(self):
		for i in range(self.num_points):
			self.points.append(self.new_random_point())

	def add_points(self):
		if len(self.points) < self.num_points:
			self.points.append(self.new_random_point())

	def new_random_point(self):
		x = random.randint(0, self.width)
		y = random.randint(0, self.height)
		c = random.randint(0, len(self.colors)-1)
		return point(x, y, self.colors[c])

	def draw(self, color, x, y, r):
		pygame.draw.circle(self.screen, color, (int(x), int(y)), r)

	def draw_objects(self):
		for p in self.points:
			self.draw(p.color, p.x, p.y, p.r)
		for p in self.players:
			self.draw(p.color, p.x, p.y, p.r)

	def update_players(self):
		for p in self.players:
			p.update()

	def handle_collisions(self):
		for p in reversed(self.players):
			for b in reversed(self.points):
				distance = math.sqrt(pow((b.x - p.x), 2) + pow((b.y - p.y), 2))
				if distance < p.r + b.r:
					p.increase_size()
					self.points.remove(b)

	def run(self):
		frame = time.time()
		running = True
		while running:
			next_frame = time.time()
			if next_frame - frame > 1.0/60.0:
				frame = time.time()
				self.screen.fill((100, 100, 100))

				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_LEFT:
							print("left")
					if event.type == pygame.QUIT:
						pygame.quit()
						sys.exit(0)

				self.add_points()
				self.handle_collisions()
				self.draw_objects()
				self.update_players()
				pygame.display.update()

class player():
	def __init__(self, x=50, y=50):
		self.r = 10
		self.x = x
		self.y = y
		self.color = (255, 255, 255)
		self.speed = 1
		self.easing = .01
		self.growth_factor = 1

	def update(self):
		mouse_coordinate = pygame.mouse.get_pos()
		target_x = mouse_coordinate[0]
		dx = target_x - self.x
		self.x += (dx * self.easing)

		target_y = mouse_coordinate[1]
		dy = target_y - self.y
		self.y += (dy * self.easing)

	def increase_size(self):
		print(self.r)
		self.r += 1
class point():
	def __init__(self, x, y, color):
		self.r = 5
		self.x = x
		self.y = y
		self.color = color


game = game()