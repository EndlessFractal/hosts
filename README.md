# EndlessFractal/hosts

Retrieves a list of domain names from various sources and filters them to create a consolidated list of unique domains. The filtered list is then saved to a file called `hosts.txt`.

## Description

The script performs the following steps:

1. Reads from a list of URLs from which to retrieve domain lists.
2. Sends HTTP requests to each URL and retrieves the response text.
3. Parses the response text, filters out empty lines and comments, and extracts the domain names.
4. Stores the unique domain names in a set data structure.
5. Sorts the domain names in alphabetical order.
6. Retrieves the current date and time as the last update timestamp.
7. Counts the number of unique domains.
8. Constructs a header section with the last update timestamp and the number of unique domains.
9. Writes the header and the filtered domain names to the `filtered_hosts.txt` file.

## Sources

The script retrieves domain lists from the following sources:

- [Ad Wars Hosts](https://raw.githubusercontent.com/jdlingyu/ad-wars/master/hosts)
- [AdguardDNS](https://v.firebog.net/hosts/AdguardDNS.txt)
- [Admiral](https://v.firebog.net/hosts/Admiral.txt)
- [BarbBlock Hosts File](https://paulgb.github.io/BarbBlock/blacklists/hosts-file.txt)
- [Easylist](https://v.firebog.net/hosts/Easylist.txt)
- [Easyprivacy](https://v.firebog.net/hosts/Easyprivacy.txt)
- [First-Party Trackers Hosts](https://hostfiles.frogeye.fr/firstparty-trackers-hosts.txt)
- [Mandiant APT1 Report Appendix D](https://bitbucket.org/ethanr/dns-blacklists/raw/8575c9f96e5b4a1308f2f12394abd86d0927a4a0/bad_lists/Mandiant_APT1_Report_Appendix_D.txt)
- [NoTrack Malware Blocklist](https://gitlab.com/quidsup/notrack-blocklists/-/raw/master/notrack-malware.txt)
- [NoTrack Tracker Blocklist](https://gitlab.com/quidsup/notrack-blocklists/-/raw/master/notrack-blocklist.txt)
- [Referrer Spam Blacklist](https://raw.githubusercontent.com/matomo-org/referrer-spam-blacklist/master/spammers.txt)
- [Spam404 Main Blacklist](https://raw.githubusercontent.com/Spam404/lists/master/main-blacklist.txt)
- [Stalkerware Indicators](https://raw.githubusercontent.com/AssoEchap/stalkerware-indicators/master/generated/hosts)
- [Threat Intel Latest Domains](https://osint.digitalside.it/Threat-Intel/lists/latestdomains.txt)
- [VeleSila YHosts](https://raw.githubusercontent.com/VeleSila/yhosts/master/hosts)
- [W3KBL](https://v.firebog.net/hosts/static/w3kbl.txt)
- [💊 Dandelion Sprout's Anti-Malware List](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareHosts.txt)

## File Output

The filtered domain names are saved to the `filtered_hosts.txt` file, which is formatted as follows:

```
# Title: EndlessFractal/hosts 

# Date of Last Update: [Last Update Timestamp]
# Number of Unique Domains: [Number of Unique Domains]

# Fetch the latest version of this file: [Raw File URL]
# Project home page: [Project Repository URL]

# ===============================================================

[Filtered Domain 1]
[Filtered Domain 2]
[Filtered Domain 3]
...
```

The file includes a header section with the last update timestamp and the number of unique domains. It also provides links to fetch the latest version of the file and the project home page.
