### BEGIN LICENSE
# The MIT License (MIT)
#
# Copyright (C) 2015 Christopher Wells <cwellsny@nycap.rr.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
### END LICENSE
"""A script which changes the GNOME desktop wallpaper at sepcific intervals."""
from subprocess import Popen
import datetime

def main():
	"""Change the wallpaper depending on the time."""
	# Get the current time
	current_time = datetime.datetime.now()
	current_hour = current_time.hour

	#########################################
	# Set the Wallpaper based on the time	#
	#########################################
	# 5  -	7	Early Morning		#
	# 7  -	10	Late Morning		#
	# 10 -	14	Mid Day			#
	# 14 -	17	Afternoon		#
	# 17 -	20	Late Evening		#
	# 20 -	22	Night			#
	# 22 -	5	Late Night		#
	#########################################
	wallpaper_image = "~/Pictures/Wallpapers/"
	if current_hour < 5:
		wallpaper_image = wallpaper_image + "8Bit-Day-Late-Night.png"
	elif current_hour < 7:
		wallpaper_image = wallpaper_image + "8Bit-Day-Early-Morning.png"
	elif current_hour < 10:
		wallpaper_image = wallpaper_image + "8Bit-Day-Late-Morning.png"
	elif current_hour < 14:
		wallpaper_image = wallpaper_image + "8Bit-Day-Mid-Day.png"
	elif current_hour < 17:
		wallpaper_image = wallpaper_image + "8Bit-Day-Afternoon.png"
	elif current_hour < 20:
		wallpaper_image = wallpaper_image + "8Bit-Day-Late-Evening.png"
	elif current_hour < 22:
		wallpaper_image = wallpaper_image + "8Bit-Day-Night.png"
	elif current_hour < 24:
		wallpaper_image = wallpaper_image + "8Bit-Day-Late-Night.png"

	# Set the wallpaper
	Popen("gsettings set org.gnome.desktop.background picture-uri " + wallpaper_image, shell=True)

# Run the main method
if __name__ == '__main__':
	main()
