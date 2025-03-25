'''A Python script that fetches a URL'''

import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen('http://0.0.0.0:5050/status') as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))

