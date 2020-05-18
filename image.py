########## ImageProcess.py
#	Converts a jpeg image into an array of characters based on whether 
#	a pixel is light or dark colored
#	REQUIRES Python Image Library

from __future__ import print_function
from PIL import Image

WHITE = 765 #RGB white
MAX_DIMENSIONS = 200 #Maximum allowed dimension size of image

#Takes the sum of RGB values and returns a corresponding character
def colourToChar(rgbSum, min=1):
	cRange = WHITE - min
	if rgbSum > min + cRange * 0.9:
		return "  "
	elif rgbSum <= min + cRange * 0.9 and rgbSum > min + cRange * 0.8:
		return "` "
	elif rgbSum <= min + cRange * 0.8 and rgbSum > min + cRange * 0.7:
		return "j "
	elif rgbSum <= min + cRange * 0.7 and rgbSum > min + cRange * 0.6:
		return "i "
	elif rgbSum <= min + cRange * 0.6 and rgbSum > min + cRange * 0.5:
		return "+ "
	elif rgbSum <= min + cRange * 0.5 and rgbSum > min + cRange * 0.4:
		return "< "
	elif rgbSum <= min + cRange * 0.4 and rgbSum > min + cRange * 0.3:
		return "$ "
	elif rgbSum <= min + cRange * 0.3 and rgbSum > min + cRange * 0.2:
		return "@ "
	elif rgbSum <= min + cRange * 0.2 and rgbSum > min + cRange * 0.1:
		return "& "
	else:
		return "% "

#Takes an image and returns the sum of the RGB values of the darkest pixel
def getDarkest(pic):
	darkest = 765
	for pixel in iter(pic.getdata()):
		r,g,b = pixel
		pixelVal = r + g + b
		if pixelVal < darkest:
			darkest = pixelVal
	return darkest

#Translates the image to an array of characters
def imgToArr(pic):
	pixels = []
	darkest = getDarkest(pic)

	wid, hei = pic.size

	i = 0
	tmp = []

	for pixel in iter(pic.getdata()):
		r,g,b = pixel
		pixelVal = r + g + b
		tmp.append(colourToChar(pixelVal, darkest))
		i += 1
		if i == wid:
			pixels.append(tmp)
			tmp = []
			i = 0
	return pixels

#Prints the character representation of the image
def printImgArr(imgArr):
	for i in range(len(imgArr)):
		for j in range(len(imgArr[i])):
			print(imgArr[i][j], end="")
		print("")

#Shrinks the character representation of the image by a factor of two
def shrinkImgArr(imgArr):
	newArr = []
	k = 0
	i = 0
	while i < len(imgArr) - 1:
		newArr.append([])
		j = 0
		while j < len(imgArr[i]) - 1:
			newArr[k].append(imgArr[i][j])
			j += 2
		i += 2
		k += 1
	return newArr

#Saves the character representation of the image to a text file with a specified name
def imgArrToFile(imgArr, filename):
	f = open(filename, 'w')
	for i in range(len(imgArr)):
		for j in range(len(imgArr[i])):
			f.write(imgArr[i][j])
		f.write('\n')

#EXAMPLES OF FUNCTIONS
img = Image.open("test.jpg")

pixArr = imgToArr(img)

while len(pixArr) > MAX_DIMENSIONS or len(pixArr[0]) > MAX_DIMENSIONS:
	pixArr = shrinkImgArr(pixArr)

imgArrToFile(pixArr, 'asciiArt.txt')
