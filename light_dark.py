
import datetime
import ephem  # note needed to 'sudo apt-get install python-dev' first or new packges wont install.

# DAWN / DUSK bits https://www.raspberrypi.org/forums/viewtopic.php?f=32&t=114745
print 'DAWN / DUSK Bits'
print '-------------------------------------'

#the coordinates own below is 10 Downing St, London, UK
somewhere = ephem.Observer()
somewhere.lat = '51.503364' # <== change me
somewhere.lon = '-0.1276250' # <== and change me
somewhere.elevation = 4
print somewhere.date

sun = ephem.Sun()
sunrise = somewhere.next_rising(sun)
sunrise_dt = somewhere.next_rising(sun).datetime()
sunset = somewhere.next_setting(sun)
sunset_dt = somewhere.next_setting(sun).datetime()

#Visual_sunrise=datetime.datetime.strptime(r1, "%d %b %Y %H:%M:%S")
#Visual_sunrise=datetime.combine(r1, datetime.min.time())

def DayORNight():
	now = datetime.datetime.now()
	next_sunrise_datetime = somewhere.next_rising(sun).datetime()
	next_sunset_datetime = somewhere.next_setting(sun).datetime()

	# If it is daytime, we will see a sunset sooner than a sunrise.
	if next_sunset_datetime < next_sunrise_datetime: 
		return 'DAY'
	else: 
		return 'NIGHT'
# If it is nighttime, we will see a sunrise sooner than a sunset.
#	it_is_night = next_sunrise_datetime < next_sunset_datetime
#	print("It's night." if it_is_night else "It's day.")

print ("Visual sunrise %s" % sunrise)
print ("Visual sunset %s" % sunset)

print ("Visual sunrise_dt %s" % sunrise_dt)
print ("Visual sunset_dt %s" % sunset_dt)
print 'DAY or NIGHT = ' + DayORNight()
