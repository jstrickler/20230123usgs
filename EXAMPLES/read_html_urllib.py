
import urllib.request

u = urllib.request.urlopen("https://www.python.org")

print(u.info())  # .info() returns a dictionary of HTTP headers
print()

print(u.read(500).decode())   # The text is returned as a bytes object, so it needs to be decoded to a string
