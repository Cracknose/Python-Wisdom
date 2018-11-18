import urllib
import urllib.request

# Hämtar en hemsida och printar ut html responsen, behöver 'import urllib.request'
def fetch_webpage(s_url):
	request = urllib.request.Request(s_url)   #lägg till $Show_ID i urlen
	request.add_header("User-Agent", "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36")
	opener = urllib.request.build_opener()
	response = opener.open(request) # makes the HTTP request
	html = response.read()
	return(html)

fetch_webpage("http://www.omni.se")