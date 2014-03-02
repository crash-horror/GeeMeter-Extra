GeeMeter Extra v0.62
===
Works for FC3 aircraft only <<< to be fixed.

	The "gee_extra.0.6.2.py" script creates a fixed 400 by 1120 window,
	which means you need at least 1200 vertical
	screen resolution on your second monitor.

Important:

	For this script to work you need to add the
	lines contained in the "ADD_THIS_TO_YOUR_Export.lua"
	at the end of your Export.lua file located at:
	C:\Users\~\Saved Games\DCS\Scripts\Export.lua

	or for the beta version:
	C:\Users\~\Saved Games\DCS.openbeta\Scripts\Export.lua

	If it does not exist, just create it, (the "Scripts" folder too).
WIP:

	Running this will pop a console window for debugging,
	it is intentional. To get rid of it, rename the extension
	from ".py" to ".pyw".

Note:

	In case you want to run this script on another
	computer, you just need to change the IP address
	in the Export.lua (see below) from
	host = "localhost" to host = xxx.xxx.xxx.xxx
	or host = "your_computer_network_name"
	according to your lan address you run GeeMeter on.

Troubleshoot:

	If the server is not starting/restarting:
	Open windows task manager and kill the process
	'pythonw.exe'.
	The reason is that the server may not have terminated properly.
