import httplib
 
# contants:
APIkey = 'XXXXXXXXXXXXX' #Enter yours here
 
def python2pushover(message='hello world'):
    conn = httplib.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
        urllib.urlencode({
            "token": "XXXXXXXXXXXXX",
            "user": "XXXXXXXXXXXXX",
            "message": msg,
    }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()