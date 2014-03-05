------------------------------------------------
---------START OF GEE-METER-EXTRA CODE----------
------------------------------------------------
function LuaExportStart()
	package.path  = package.path..";.\\LuaSocket\\?.lua"
	package.cpath = package.cpath..";.\\LuaSocket\\?.dll"
	socket = require("socket")
	host = "localhost"
	port = 1625
	c = socket.try(socket.connect(host, port))
	c:setoption("tcp-nodelay",true)
end
------------------------------------------------
function LuaExportAfterNextFrame()
	local Gee = LoGetAccelerationUnits()
	local AOA = LoGetAngleOfAttack()
	local Engine = LoGetEngineInfo()
	local Mach = LoGetMachNumber()
	local Speed = LoGetTrueAirSpeed()
	socket.try(c:send(string.format("%.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f",Gee.y, AOA, Mach, Engine.FuelConsumption.left, Engine.FuelConsumption.right, Engine.fuel_internal, Engine.fuel_external, Speed)))
end
------------------------------------------------
function LuaExportStop()
	c:close()
end
------------------------------------------------
----------END OF GEE-METER-EXTRA CODE-----------
------------------------------------------------
