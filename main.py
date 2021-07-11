import json  # To process JSON from the Internet
import urllib.request  # Deal with the Internet
import urllib.parse
import urllib.error
import ssl  # Solely used to ignore SSL errors

# Ignore SSl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Open JSON location
extracted_json = urllib.request.urlopen(input("Enter URL: "), context=ctx).read\
                 ()
parsed_json = json.loads(extracted_json)
comments = parsed_json["comments"]
sum = int()
for comment in comments:
    sum += int(comment["count"])
print("Sum", sum)
