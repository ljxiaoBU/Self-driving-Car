#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

class carControl:
	def __init__(self):
		self.backMotorInput1 = 13
		self.backMotorInput2 = 15
		self.frontMotorInput1 = 7
		self.frontMotorInput2 = 11
		self.backMotorEn = 16
		self.frontMotorEn = 12

		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False) 

		GPIO.setup(self.backMotorInput1, GPIO.OUT)
		GPIO.setup(self.backMotorInput2, GPIO.OUT)
		GPIO.setup(self.frontMotorInput1, GPIO.OUT)
		GPIO.setup(self.frontMotorInput2, GPIO.OUT)
		GPIO.setup(self.frontMotorEn, GPIO.OUT)
		GPIO.setup(self.backMotorEn, GPIO.OUT)

		self.speed = 35
		self.backMotorPwm = GPIO.PWM(self.backMotorEn,100)
		self.backMotorPwm.start(0)


	def carMoveBackward(self):
		self.carTurnStraight()
		GPIO.output(self.backMotorInput1,GPIO.HIGH)
		GPIO.output(self.backMotorInput2,GPIO.LOW)
		#GPIO.output(frontMotorInput1,GPIO.LOW)
		#GPIO.output(frontMotorInput2,GPIO.LOW)
		self.backMotorPwm.ChangeDutyCycle(self.speed)
		
		
	def carMoveForward(self):
		self.carTurnStraight()
		GPIO.output(self.backMotorInput1 ,GPIO.LOW)
		GPIO.output(self.backMotorInput2,GPIO.HIGH)
		#GPIO.output(frontMotorInput1 ,GPIO.LOW)
		#GPIO.output(frontMotorInput2,GPIO.LOW)
		self.backMotorPwm.ChangeDutyCycle(self.speed)

	def carTurnRight(self):
		GPIO.output(self.frontMotorEn, GPIO.HIGH)
		GPIO.output(self.backMotorInput2,GPIO.HIGH)
		GPIO.output(self.backMotorInput1,GPIO.LOW)
		GPIO.output(self.frontMotorInput2 ,GPIO.LOW)
		GPIO.output(self.frontMotorInput1,GPIO.HIGH)
		self.backMotorPwm.ChangeDutyCycle(self.speed)
	def carTurnLeft(self):
		GPIO.output(self.frontMotorEn, GPIO.HIGH)
		GPIO.output(self.backMotorInput1 ,GPIO.LOW)
		GPIO.output(self.backMotorInput2,GPIO.HIGH)
		GPIO.output(self.frontMotorInput2 ,GPIO.HIGH)
		GPIO.output(self.frontMotorInput1,GPIO.LOW)
		self.backMotorPwm.ChangeDutyCycle(self.speed)
	def carTurnStraight(self):
		GPIO.output(self.frontMotorEn, GPIO.LOW)
		

	def cleanGPIO(self):
		GPIO.cleanup()
		self.backMotorPwm.stop()
		
		
if __name__ == '__main__':
	car = carControl()
	print("forward")
	car.carMoveForward()
	time.sleep(2)
	print("backward")
	car.carMoveBackward()
	time.sleep(2)
	print("left")
	car.carTurnLeft()
	time.sleep(2)
	print("right")
	car.carTurnRight()
	time.sleep(2)
	car.cleanGPIO()
		
		
