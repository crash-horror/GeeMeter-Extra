#!/usr/bin/python3

## GeeMeter Extra
version = 0.62

from tkinter import *
from socket import *
from threading import *
from math import degrees
import time

km_to_mile = 0.54
kgr_to_pound = 2.205

mile = 1
pound = 1

gee_global_data = 0.0
aoa_global_data = 0.0
mach_global_data = 0.0
fuelflow_global_data = 0.0
fuel_internal_global_data = 0.0
fuel_external_global_data = 0.0
true_speed_global_data = 0.0

serverstatus = 'DOWN'
whatunits = 'METRIC'

geelist =   ['nine', 'eight', 'seven',  'six',    'five',   'four',   'three', 'two',   'one',  'zero', 'minus']
colorlist = ['red',  'red',   'orange', 'orange', 'yellow', 'yellow', 'green', 'green', 'blue', 'blue', 'red'  ]
numlist =   [ 9,      8,       7,        6,        5,        4,        3,       2,       1,      0,      -1    ]

# variablelist = ['0.Gee.y', '1.AOA', '2.Mach', '3.Engine.FuelConsumption.left', '4.Engine.FuelConsumption.right', '5.Engine.fuel_internal', '6.Engine.fuel_external', '7.Speed']

boxlist =         ['aoa',        'mach',        'travel',          'fuel.flow',       'endurance',        'range',        'internal.fuel',    'external.tanks'    ]
dispaylist =      ['displayaoa', 'displaymach', 'displaykmpermin', 'displayfuelflow', 'displayendurance', 'displayrange', 'displayinternal',  'displayexternal'   ]
unitmetric =      ['',           '',            'km/min',          'kg/min',          'min',              'km',           'kg',               'kg'                ]
unitimperial =    ['',           '',            'nM/min',          'ppm',             'min',              'nM',           'lb',               'lb'                ]

aoaindexlist =   ['top', 'center', 'bottom']
aoaindexobject = ['V', 'O', 'Ʌ']

aoabarslisttags = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg', 'hhh', 'iii', 'jjj', 'kkk', 'lll', 'mmm', 'nnn']
aoabarslist =     [  17,    16,    15,    14,    13,    12,    11,    10,     9,     8,     7,     6,     5,     4 ]

unitdisplaylist = unitmetric






##--------------------FUNCTIONS------------------------------------------------------------------------------
##-----------------------------------------------------------------------------------------------------------

def onObjectClick(event):
	global whatunits, unitdisplaylist, unitmetric, unitimperial, mile, pound

	# km_to_mile = 0.54
	# kgr_to_pound = 2.205

	# mile = 1
	# pound = 1
	
	w.delete('unittags')

	if whatunits == 'METRIC':
		whatunits = 'IMPERIAL'
		unitdisplaylist = unitimperial
		mile = 0.54
		pound = 2.205
	else:
		whatunits = 'METRIC'
		unitdisplaylist = unitmetric
		mile = 1
		pound = 1

	posit = 0
	for i in unitdisplaylist:
		w.create_text(170, 320+posit, text=i, fill='grey40', anchor='e', tags='unittags')
		posit += 100

	w.itemconfig('units', text=whatunits)
	print('Changed units to:', whatunits)
	w.update()













##-------------------TK------------------------------------------------------------------------------------
##---------------------------------------------------------------------------------------------------------

root = Tk()
root.title('Gee Meter Extra ' + str(version))
root.resizable(0,0)
w = Canvas(root, width=400, height=1120, bg='black')
w.pack()


#----GEE-METER--------------------
posit = 0
for i in geelist:
	w.create_rectangle(220, 10+posit, 380, 80+posit, fill='grey10', tags=i)
	posit += 100

posit = 0
for i in numlist:
	w.create_text(300, 45+posit, text=i, font=('Arial', 40))
	posit += 100


#----AOA-INDEXER--------------------
posit = 0
for i in aoaindexlist:
	w.create_rectangle(100, 10+posit, 180, 80+posit, fill='grey10', tags=i)
	posit += 100

posit = 0
for i in aoaindexobject:
	w.create_text(140, 45+posit, text=i, font=('Arial', 40))
	posit += 100


#----AOA-BARS---------------------
posit = 0
for i in aoabarslisttags:
	w.create_rectangle(20, 10+posit, 90, 20+posit, fill='grey10', tags=i)
	posit += 20


#----BOXES------------------------
posit = 0
for i in boxlist:
	w.create_rectangle(20, 310+posit, 180, 380+posit, fill='grey10', tags=i)
	w.create_text(100, 320+posit, text=i, fill='grey40')
	posit += 100

posit = 0
for i in unitdisplaylist:
	w.create_text(170, 320+posit, text=i, fill='grey40', anchor='e', tags='unittags')
	posit += 100

#----DATA-TEXT--------------------
posit = 0
for i in dispaylist:
	w.create_text(100, 350+posit, text='-', font=('Arial', 30), fill=('white'), tags=i)
	posit += 100


#----STATUS-----------------------
w.create_text(300, 1105, text = serverstatus, font=('Arial'), fill=('grey40'), tags='statusbar')
w.update()


#----UNITS------------------------
w.create_text(100, 1105, text = whatunits, font=('Arial'), fill=('grey40'), tags='units')
w.tag_bind('units', '<ButtonPress-1>', onObjectClick)

w.pack()













##--------------------MAIN LOOP------------------------------------------------------------------------------
##-----------------------------------------------------------------------------------------------------------
def the_main_loop():
	global geelist, numlist, whatunits, mile, pound, aoabarslisttags, aoabarslist, gee_global_data, aoa_global_data, mach_global_data, fuelflow_global_data, fuel_internal_global_data, fuel_external_global_data, true_speed_global_data
	
	##<<-------------------------------GEE-------------------------------------
	gee = round(gee_global_data)

	if gee < -1:
		gee = -1
	elif gee > 9:
		gee = 9

	onlightlist = geelist[numlist.index(gee):]

	for on in onlightlist:
		w.itemconfig(on, fill=colorlist[geelist.index(on)])

	if gee > -1:
		offlightlist = geelist[:numlist.index(gee)] + ['minus']
	else:
		offlightlist = geelist[:numlist.index(gee)]

	for off in offlightlist:
		w.itemconfig(off, fill='grey10')

	#<<----------------------------AOA-INDEXER-------------------------------
	if aoa_global_data > 12:
		w.itemconfig('top', fill='yellow')
	else:
		w.itemconfig('top', fill='grey10')

	if aoa_global_data <= 12 and aoa_global_data >= 9:
		w.itemconfig('center', fill='green')
	else:
		w.itemconfig('center', fill='grey10')

	if aoa_global_data < 9:
		w.itemconfig('bottom', fill='yellow')
	else:
		w.itemconfig('bottom', fill='grey10')

	#<<------------------------------AOA-BARS---------------------------------
	aoa = round(aoa_global_data)

	if aoa < 4:
		aoa = 4
	elif aoa > 17:
		aoa = 17

	aoaonlignt =  aoabarslisttags[aoabarslist.index(aoa)]

	for aoaoff in aoabarslisttags:
		w.itemconfig(aoaoff, fill='grey10')

	w.itemconfig(aoaonlignt, fill='green')

	#<<--------------------------------AOA-----------------------------------
	w.itemconfig('displayaoa', text=round(aoa_global_data)) 

	if aoa_global_data > 23 or aoa_global_data < 0:
		w.itemconfig('aoa', fill='red')
	elif aoa_global_data < 12 and aoa_global_data > 9:
		w.itemconfig('aoa', fill='blue')
	else:
		w.itemconfig('aoa', fill='grey10')

	#<<-------------------------------MACH-----------------------------------
	w.itemconfig('displaymach', text=mach_global_data)

	if mach_global_data >= 1:
		w.itemconfig('mach', fill='blue')
	else:
		w.itemconfig('mach', fill='grey10')

	#<<---------------------KM-PER-MIN-------------------------------
	w.itemconfig('displaykmpermin', text=round( true_speed_global_data / 60 * mile ))

	#<<-----------------------------FUEL FLOW--------------------------------
	w.itemconfig('displayfuelflow', text=round( fuelflow_global_data * pound ))

	#<<-----------------------------ENDURANCE--------------------------------
	endurance_var = 0.0
	if fuelflow_global_data != 0:
		endurance_var = (fuel_internal_global_data + fuel_external_global_data) / fuelflow_global_data 
		w.itemconfig('displayendurance', text=round( endurance_var ) )
	else:
		w.itemconfig('displayendurance', text='-')

	#<<-----------------------------RANGE-----------------------------------
	w.itemconfig('displayrange', text=round( true_speed_global_data * endurance_var / 60 * mile ))

	#<<----------------------INTERNAL-FUEL--------------------------
	w.itemconfig('displayinternal', text=round( fuel_internal_global_data * pound ))

	if fuel_internal_global_data < 500:
		w.itemconfig('internal.fuel', fill='red')
	elif fuel_internal_global_data < 1500:
		w.itemconfig('internal.fuel', fill='orange')
	else:
		w.itemconfig('internal.fuel', fill='grey10')
	
	#<<---------------------EXTERNAL-FUEL---------------------------
	w.itemconfig('displayexternal', text=round( fuel_external_global_data * pound ))

	if fuel_external_global_data < 10:
		w.itemconfig('external.tanks', fill='dark red')
	else:
		w.itemconfig('external.tanks', fill='grey10')



	w.update()
	w.after(10, the_main_loop)















##--------------------SERVER--------------------------------------------------------------------------------------------
##----------------------------------------------------------------------------------------------------------------------

def the_server():
	global gee_global_data, aoa_global_data, mach_global_data, serverstatus, fuelflow_global_data, fuel_internal_global_data, fuel_external_global_data, true_speed_global_data
	HOST = ''
	PORT = 1625
	ADDR = (HOST,PORT)
	BUFSIZE = 512

	serv = socket(AF_INET,SOCK_STREAM)
	serv.bind((ADDR))
	serv.listen(5)

	serverstatus = 'LISTENING'
	w.itemconfig('statusbar', text=serverstatus)
	w.update()
	print('Listening...')

	conn,addr = serv.accept()

	serverstatus = 'CONNECTED'
	w.itemconfig('statusbar', text=serverstatus)
	w.update()
	print('...connected!')

	while True:
		data = conn.recv(512)
		if not data:
			print('Gserver SHUTDOWN!')
			break

		datastring = str(data)
		datalist = [float(x) for x in datastring[2:-1].split()]

		# km_to_mile = 0.54
		# kgr_to_pound = 2.205

		gee_global_data = datalist[0]

		aoa_global_data = degrees(datalist[1])

		mach_global_data = datalist[2]

		fuelflow_global_data = ( datalist[3] + datalist[4] ) * 60

		fuel_internal_global_data = datalist[5]

		fuel_external_global_data = datalist[6]

		true_speed_global_data = datalist[7] / 1000 * 3600


	conn.close()
	serv.close()

	serverstatus = 'RESTARTING...'
	w.itemconfig('statusbar', text=serverstatus)

	##<<----------------RESET GLOBAL VARIABLES------------
	gee_global_data = 0.0
	aoa_global_data = 0.0
	mach_global_data = 0.0
	fuelflow_global_data = 0.0
	fuel_internal_global_data = 0.0
	fuel_external_global_data = 0.0
	true_speed_global_data = 0.0

	w.update()
	print('Restarting...')

	time.sleep(5)
	the_server()









##-----------------------------------------------------------------------------------------------------------------------
##-----------------------------------------------------------------------------------------------------------------------
t1 = Thread(target=the_server)
t1.daemon = True
t1.start()

w.after(1, the_main_loop)

root.mainloop()
