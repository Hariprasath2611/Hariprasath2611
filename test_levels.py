import json
from datetime import datetime, timedelta

with open('assets/contributions.json') as f:
    d = json.load(f)

date_map = {c['date']: c for c in d.get('contributions', [])}

start_sunday = datetime(2026, 10, 18) - timedelta(days=52*7)
end_day = datetime(2026, 10, 18)

colors = ['#34225A', '#6E4FB5', '#B79CFF', '#FFB27A', '#FF8A3D']
counts_by_level = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}

for col in range(53):
    col_sunday = start_sunday + timedelta(days=col*7)
    for row in range(7):
        curr_day = col_sunday + timedelta(days=row)
        d_str = curr_day.strftime('%Y-%m-%d')
        if curr_day <= end_day:
            c_info = date_map.get(d_str, {'date': d_str, 'count': 0, 'level': 0})
        else:
            c_info = {'date': d_str, 'count': 0, 'level': 0}
        
        lvl = min(c_info.get('level', 0), 4)
        counts_by_level[lvl] += 1

print('Level distribution in full 53x7 grid:')
for lvl, cnt in counts_by_level.items():
    print(f'  Level {lvl} ({colors[lvl]}): {cnt} cells')
