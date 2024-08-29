import colorsys

def hsv_to_rgb(hsv):
	# fast conversion algorithm.
	hsv_result = colorsys.hsv_to_rgb(hsv[0] / 360, hsv[1], hsv[2])
	return tuple(map(lambda a: a * 255, hsv_result))

def _lerp(start, end, lerp):
	# linear interpolation for calculateFromStep
	return start * (1 - lerp) + end * lerp

def calculateFromStep(start, end, lerp):
	return (
		_lerp(start[0], end[0], lerp),
		_lerp(start[1], end[1], lerp),
		_lerp(start[2], end[2], lerp),
	)