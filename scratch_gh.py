import urllib.request
import re

url = 'https://github.com/users/HARIPRASATH2611/contributions'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req, timeout=8).read().decode('utf-8')

# Let's find each td or rect
cells = re.findall(r'<td[^>]*data-date="([^"]+)"[^>]*data-level="([^"]+)"[^>]*>', html)
print('Total cells found:', len(cells))
if cells:
    print('First 10 cells:')
    for c in cells[:10]:
        print(' ', c)
    print('Last 10 cells:')
    for c in cells[-10:]:
        print(' ', c)
