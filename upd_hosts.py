import requests
import re
from datetime import datetime

def fetch_and_process_hosts(url):
    try:
        with requests.get(url) as response:
            if response.status_code == 200:
                lines = [re.sub(r"\s+#.*$|^\s*[\^|\|]+\s*|\s+$", "", line).strip().lower() for line in response.text.splitlines() if "." in line]
                return lines
            else:
                print(f"Failed to fetch {url}. Skipping...")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
    return []

# Read URLs from the file
with open("list.txt", "r") as file:
    urls = file.read().splitlines()

# Fetch and process host files from each URL
unique_domains = set()
for url in urls:
    domains = fetch_and_process_hosts(url)
    unique_domains.update(domains)

# Remove "localhost" from the unique domains
unique_domains.discard("localhost")

# Sort the remaining unique domains alphabetically
unique_domains = sorted(unique_domains)

# Get current date and time
now = datetime.now()
last_update = now.strftime("%d %B %Y %H:%M:%S (UTC)")

# Get the number of unique domains
num_domains = len(unique_domains)

# Create the header for the output file using f-string
header = f"""\
# Title: EndlessFractal/hosts
# Homepage: https://github.com/EndlessFractal/hosts
# Release: https://github.com/EndlessFractal/hosts/releases
# Licence: https://github.com/EndlessFractal/hosts/blob/master/LICENSE
# Expires: 1 days
#
# Last Update: {last_update}
# Unique Domains: {num_domains:,}
#
# ===============================================================
"""

# Write the filtered hosts to a file
with open("hosts.txt", "w") as file:
    file.write(header + "\n")
    file.writelines(domain + "\n" for domain in unique_domains)
