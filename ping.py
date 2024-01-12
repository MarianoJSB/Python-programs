#With this program you will know if the server (url) you pass as a link argument in the function
#is it active or not?
import os

url = input("Please, enter a url: ")

def ping(host):
    res = os.system(f"Ping {host}")
    if res == 0:
        print(f"{host} is actived")
    else:
        print(f"{host} isn't actived")

ping(url)