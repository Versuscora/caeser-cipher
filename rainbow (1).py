# All functions return tuples, keep in mind!
from calc import hsv_to_rgb, calculateFromStep

def rainbowInit(os=None):
	OS = os
	if not os:
		OS = __import__("os")
	OS.system("clear")

def rainbowBlock(length, push=0, mode="hsv", charsBy=1):
	return rainbowText(
		"█" * length,
		colors=[(-push, 1, 1), (360-push, 1, 1)],
		mode=mode,
		charsBy=charsBy,
	)
	
def rainbowText(text, colors=None, start=(0, 1, 1), end=(360, 1, 1), mode="hsv", charsBy=1, printResult=False, printEnd="\n"):
	# extended rainbow for maximum emotional damage
	# for step-related calculations
	length = len(text)
	curAt = 0
	
	f = None
	result = ""

	cstep = None

	if colors:
		cstep = (1 / (len(colors) - 1))
	
	if mode == "hsv":
		f = lambda a: hsv_to_rgb(a)
	elif mode == "rgb":
		f = lambda a: a
	else:
		raise Exception("If specifying <mode>, choose from hsv and rgb, or do not specify it for hsv value reperesentation.")
	
	for char in text:
		# get hsv values from calculateFromStep
		if colors:
			# get at for interval at
			at = int((curAt / length) // cstep)
			wt = ((curAt / length) % cstep) / cstep
			
			(r, g, b) = f(calculateFromStep(colors[at], colors[at + 1], wt))
		else:
			(r, g, b) = f(calculateFromStep(start, end, curAt / length))

		r = int(r)
		g = int(g)
		b = int(b)
		
		result += (f"\033[38;2;{r};{g};{b}m" if curAt % charsBy == 0 else "") + char
		curAt += 1

	if printResult:
		print(result, end=printEnd)
	
	return result