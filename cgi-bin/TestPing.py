import os

def printPingTime(data):
	listPing = []
	for linha in data:
		if("TTL" in linha):
			linhaParts = linha.split("time=")[1].split(" ")
			listPing.append(str(linhaParts[0]))
		elif("Request timed out" in linha):
			listPing.append("Lost Package")
		elif("General failure" in linha):
			listPing.append("Connection closed")
		
	return listPing

def getPing():		

	if(os.path.exists('ping.txt')):
		os.remove('ping.txt')
		
	os.system("ping google.com >> ping.txt")
	data = open('ping.txt')
	return data
	
listFinalPing = []	
for x in range(1, 10):
	data = getPing()	
	listFinalPing.append(printPingTime(data))
	data.close()
 
print('Content-type: text/html\n\n')
print('<html>')
print('<head>')
print('<title>Ping screen</title>')
print('</head>')
print('<body>')

for value in listFinalPing:
	print('<p>' + str(value) + '</p>')
	
print('</body>')
print('</html>')

os.remove('ping.txt')