# Ambient-Light-Monitoring

Scripts to point to twards methods to monitor the ambient light levels. Applied in various actions in Raspberry Pi controlled illumination in birdboxes. 

1) ambient_lightMonitor.py
Generates ambient light stats by reading light level via a light dependent resistor.
Also takes an image and measures image brightness to file.

2) light_dark.py
Uses pyephem python module to identify if it is before dusk (ie light) or after dusk (ie dark).

http://nestboxtech.blogspot.co.uk/
