import requests
import re
from datetime import datetime

# Read URLs from the file
with open("list.txt", "r") as file:
    urls = file.read().splitlines()

filtered_hosts = set()

# Fetch and process host files from each URL
for url in urls:
    response = requests.get(url)
    lines = response.text.splitlines()
    for line in lines:
        line = re.sub(r"\s+#.*$", "", line)
        line = line.strip().replace("||", "").replace("^", "")
        if line and not line.startswith(("#", "::1")):
            domain = re.sub(r"^(?:\d{1,3}\.){3}\d{1,3} ", "", line).strip().lower()
            if "." in domain:
                filtered_hosts.add(domain)

# Sort the filtered hosts alphabetically
filtered_hosts = sorted(filtered_hosts)

# Get current date and time
now = datetime.now()
last_update = now.strftime("%d %B %Y %H:%M:%S (UTC)")

# Get the number of unique domains
num_domains = len(filtered_hosts)

# Create the header for the output file
header = """\
# Title: EndlessFractal/hosts
#
# Date of Last Update: {}
# Number of Unique Domains: {}
#
# Fetch the latest version of this file: https://raw.githubusercontent.com/EndlessFractal/hosts/main/hosts.txt
# Project home page: https://github.com/EndlessFractal/hosts
#
# ===============================================================
""".format(last_update, num_domains)

# Write the filtered hosts to a file
with open("hosts.txt", "w") as file:
    file.write(header)
    for domain in filtered_hosts:
        file.write(domain + "\n")
