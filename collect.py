#!/usr/bin/env python			
import os
from carControl import carControl
os.environ['SDL_VIDEODRIVER'] = 'x11'
import pygame
import time
import thread

class collect_thread(thread.threading):
	def __int__():
		pygame.init()
		pygame.display.set_mode((100,100))
		self.car = carControl()
	def run(self):
		while True:
			events = pygame.event.get()
			for event in events:
				if event.type == pygame.KEYDOWN:
					input_key = pygame.key.get_pressed()
					if input_key[pygame.K_w]:
						car.carMoveForward()
						time.sleep(0.25)
					elif	input_key[pygame.K_s] == 1:
						#car = carControl()
						car.carMoveBackward()
						time.sleep(0.25)
					elif	input_key[pygame.K_a] == 1:
						#car = carControl()
						car.carTurnLeft()
						time.sleep(0.25)
					elif	input_key[pygame.K_d] == 1:
						#car = carControl()
						car.carTurnRight()
						time.sleep(0.25)
					elif	input_key[pygame.K_q] == 1:
						#car = carControl()
						car.cleanGPIO()
						time.sleep(0.25)
				'''elif event.type == pygame.KEYUP:
					if input_key[pygame.K_w] :
						#car = carControl()
						car.carMoveForward()
						time.sleep(0.25)
					elif	input_key[pygame.K_s] == 1:
						#car = carControl()
						car.carMoveBackward()
						time.sleep(0.25)
					elif	input_key[pygame.K_a] == 1:
						#car = carControl()
						car.carTurnLeft()
						time.sleep(0.25)
					elif	input_key[pygame.K_d] == 1:
						#car = carControl()
						car.carTurnRight()
						time.sleep(0.25)
					elif	input_key[pygame.K_q] == 1:
						#car = carControl()
						car.cleanGPIO()
						time.sleep(0.25)'''
					
