
######################################################################
# Filename: Colors.py
# Author: Andres Alonso Chaparro Espinosa
# Mail: andreschaparro.aa@gmail.com
# Git: https://github.com/andreschaparroe
# Date: 24/02/2021
######################################################################

#--------------------------------------------------------------------#
# Global variables 
#--------------------------------------------------------------------#
# define a table of colors
gColorMap = {
	"black" : "Red",
	"red" : "Blue",
	"blue" : "Green",
	"green" : "Gold",
	"gold" : "Silver"
	# AC NOTE: Exted the color table by adding more entries
	# 		   similar to a C Serial comm protocol cmd table.
}

isColorValid = True
countValidColors = 0

#--------------------------------------------------------------------#
# Main Loop
#--------------------------------------------------------------------#

while isColorValid:
	
	# Prompt user for a color
	color = input("\nPlease type a color: \n> ").lower()
	
	if color in gColorMap:

		# input color is in the color table
		# send response
		print( gColorMap[color] )
		countValidColors = countValidColors + 1

	else:

		# input color is not in the color table
		# exit
		isColorValid = False
		
print("\n NUMBER OF VALID COLORS ENTERED  : ", countValidColors)
print("\n### End of Program ###\n")
#----------------------------End of File ----------------------------#
