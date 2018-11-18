import sys

# sys.argv ar kommandot man anroppar scriptet med ex: nmap 192.168.1.1
# da '192.168.1.1' ar sys.argv[1]

if len(sys.argv)==3:
	script = sys.argv[0]
	filename = sys.argv[1]
	bajs = sys.argv[2]
	print "SCRIPT: "+script+" "+filename+" "+bajs
