# site connectivity checker
import urllib.request as urllib

def main(url):
    print("Checking connectivity...")

    response = urllib.urlopen(url)
    print("Connected to", url, "successfully")
    print("The response code was:", response.getcode())

print("***THIS IS A SITE CONNECTIVITY CHECKER***")
input_url = input("Paste a URL to check: ")

main(input_url)