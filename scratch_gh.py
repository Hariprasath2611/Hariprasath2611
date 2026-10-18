import urllib.request
import re

url = 'https://github.com/users/HARIPRASATH2611/contributions'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req, timeout=8).read().decode('utf-8')
    # Find all table cells for contribution days
    # <td ... data-date="2025-10-19" ... data-level="1" ...>
    matches = re.findall(r'data-date="(\d{4}-\d{2}-\d{2})"[^>]*data-level="(\d+)"', html)
    print('Found days count in GitHub page:', len(matches))
    if matches:
        print('First 5 days:', matches[:5])
        print('Last 5 days:', matches[-5:])
        non_zero = [m for m in matches if int(m[1]) > 0]
        print('Non-zero days in live GitHub graph:', len(non_zero))
except Exception as e:
    print('Error:', e)
