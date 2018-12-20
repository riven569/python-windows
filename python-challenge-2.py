import re

data = "" # Copy-and-paste or extract otherwise from the challenge page's
          # HTML-source; I'll leave it out here for clarity reasons.

print "".join(re.findall("[A-Za-z]", data))