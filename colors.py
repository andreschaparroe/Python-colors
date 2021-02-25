
# define a dictionary of colors
gColorMap = {
	"black" : "Red",
	"red" : "Blue",
	"blue" : "Green",
	"green" : "Gold",
	"gold" : "Silver"
}

isColorValid = True
countValidColors = 0

while isColorValid:
	
	color = input("Please type a color: \n> ").lower()
	
	if color in gColorMap:

		# input color is on the color map dict
		print( gColorMap[color] )
		countValidColors = countValidColors + 1

	else:

		# input color is not in the color map dict
		isColorValid = False
		
print("\nThe number of times a valid color was entered is: ", countValidColors)
print("\n### End of Program ###")