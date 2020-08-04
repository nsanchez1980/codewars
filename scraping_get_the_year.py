def get_member_since(username):
    import urllib.request
    full_url = "https://www.codewars.com/users/" + username
    content = urllib.request.urlopen(full_url)
    read_content = content.read()
    location = str(read_content).find("<b>Member Since:</b>")
    return str(read_content)[location+20:location+28]
   

#No BeautifulSoup attempt :D

print(get_member_since('jhoffner'), 'Oct 2012')