<!--
---
name: Traffic HAT
manufacturer: Ryanteck LTD.
url: http://www.ryanteck.uk/
buy: http://www.ryanteck.uk/
description: A quick and easy way to learn the basics of GPIO on a budget. All in
  a nice HAT.
pincount: 40
pin:
  '15':
    name: LED1 / Green
    direction: output
    active: high
  '16':
    name: LED2 / Amber
    direction: output
    active: high
  '18':
    name: LED3 / Red
    direction: output
    active: high
  '22':
    name: Button
    direction: input
    active: high
  '29':
    name: Buzzer
    direction: output
    active: high
-->
#Traffic HAT

###A quick and easy way to learn the basics of GPIO on a budget. All in a nice HAT.

```python
import RPi.GPIO as IO
from time import sleep


IO.setmode(IO.BCM)

IO.setup(22,IO.OUT)
IO.setup(23,IO.OUT)
IO.setup(24,IO.OUT)

#Buzz
IO.setup(5,IO.OUT)

IO.setup(25,IO.IN,pull_up_down=IO.PUD_UP)

while True:
	IO.output(22,1) 			# Turn the Green LED On / 1
	sleep(0.11) #S1
	print("Green ON")
	if(IO.input(25) == 0):
		print("BUTTON PRESS")
		IO.output(22,0)			# Turn the Green LED Off / 0
		print("Green Off")
		IO.output(23,1) 		# Turn the Yellow LED On / 1
		print("Yellow ON")	
		print("Sleep")
		sleep(2) 				# Wait for 1 Second
		print("Sleeped")
	
		IO.output(23,0) 		# Turn the Yellow LED Off / 0
		print("Yellow Off")
		IO.output(24,1)			# Turn the Red LED On / 1
		print("Red ON")
		
		print("Sleep")
		sleep(2) 				# Wait for 1 Second
		print("Sleeped")
		
		i = 0 					# Set A Counter Variable
		
		while (i<10):			# The Repeat Loop
			print("Buzz")
			IO.output(5,1) 	# Turn the Yellow LED On / 1

			sleep(0.1) 			# Wait for 0.1 Seconds

			IO.output(5,0) 		# Turn the Yellow LED Off / 0

			sleep(0.1)			# Wait for 0.1 Seconds

			i = i+1				#We add 1 to the counter to keep track of the loop
		
								# We want to blink the Yellow LED 3 Times
		print("Count Begin")
		sleep(0.5)
		i = 0
		while (i<3):			# The Repeat Loop
			print("Blink")
			IO.output(23,1) 	# Turn the Yellow LED On / 1

			sleep(0.5) 			# Wait for 0.1 Seconds

			IO.output(23,0) 		# Turn the Yellow LED Off / 0

			sleep(0.5)			# Wait for 0.1 Seconds

			i = i+1				#We add 1 to the counter to keep track of the loop

		
		print("Red Off")
		IO.output(24,0) 		# Turn the Red LED Off / 0
		print("Green ON")
		IO.output(22,1) 		# Turn the Green LED On / 1
		sleep(2)

```