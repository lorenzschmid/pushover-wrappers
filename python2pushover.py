import httplib, urllib
 
def python2pushover(message='hello world'):
    conn = httplib.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
        urllib.urlencode({
            "token": "",
            "user": "",
            "message": message,
    }), { "Content-type": "application/x-www-form-urlencoded" })
    return conn.getresponse()