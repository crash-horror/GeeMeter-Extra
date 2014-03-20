GeeMeter Extra v0.63
====================
Works for FC3 aircraft only.

![Screenshot](http://i.imgur.com/l286aMg.png)

Features:
=========
* G-meter.
* Angle of attack indexer.
* Angle of attack number.
* Mach number.
* Kilometers (or miles) you cover in a minute.
* Fuel flow for both engines combined in kg/min (or lb/min).
* Endurance in minutes, you can fly at current engine power.
* Range in km (or miles), you can fly at current engine power.
* Internal fuel quantity in kg (or lb).
* External fuel tanks quantity in kg (or lb).

You can switch the unit system by clicking at the "METRIC" or "IMPERIAL" label.

Important:
==========
	For this script to work you need to add the
	lines contained in the "ADD_THIS_TO_YOUR_Export.lua"
	at the end of your Export.lua file located at:
	C:\Users\~\Saved Games\DCS\Scripts\Export.lua

	or for the beta version:
	C:\Users\~\Saved Games\DCS.openbeta\Scripts\Export.lua

	If it does not exist, just create it, (the "Scripts" folder too).

Note:

	The script creates a fixed 400 by 1120 window,
	which means you need at least 1200 vertical
	screen resolution on your second monitor.

	In case you want to run this script on another
	computer, you just need to change the IP address
	in the Export.lua, from
	host = "localhost" to host = xxx.xxx.xxx.xxx
	or host = "your_computer_network_name"
	according to your lan address you run GeeMeter on.

Troubleshoot:

	If the server is not starting/restarting:
	Open windows task manager and kill the process
	'pythonw.exe'.
	The reason is that the server may not have terminated properly.
