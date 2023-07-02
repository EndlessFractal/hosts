import requests
import re
from datetime import datetime

# Read URLs from the file
with open("list.txt", "r") as file:
    urls = file.read().splitlines()

# Fetch and process host files from each URL
unique_domains = set()
for url in urls:
    with requests.get(url) as response:
        lines = response.text.splitlines()
        lines = [re.sub(r"\s+#.*$", "", line) for line in lines]
        lines = [line.strip().replace("||", "").replace("^", "") for line in lines if line and not line.startswith(("#", "::1"))]
        domains = [re.sub(r"^(?:\d{1,3}\.){3}\d{1,3} ", "", line).strip().lower() for line in lines if "." in line]
        unique_domains.update(domains)

# Sort the unique domains alphabetically
unique_domains = sorted(unique_domains)

# Get current date and time
now = datetime.now()
last_update = now.strftime("%d %B %Y %H:%M:%S (UTC)")

# Get the number of unique domains
num_domains = len(unique_domains)

# Create the header for the output file using f-string
header = f"""\
# Title: EndlessFractal/hosts
#
# Date of Last Update: {last_update}
# Number of Unique Domains: {num_domains}
#
# Fetch the latest version of this file: https://raw.githubusercontent.com/EndlessFractal/hosts/main/hosts.txt
# Project home page: https://github.com/EndlessFractal/hosts
#
# ===============================================================
"""

# Write the filtered hosts to a file
with open("hosts.txt", "w") as file:
    file.write(header)
    file.writelines(domain + "\n" for domain in unique_domains)
