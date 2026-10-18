import json
from datetime import datetime, timedelta

with open('assets/contributions.json') as f:
    d = json.load(f)

date_map = {c['date']: c for c in d.get('contributions', [])}

# Today is 2026-10-18 (Sunday)
# In GitHub, the calendar ends on the current week's Saturday or today.
# Let's align 53 weeks such that:
# Week 52 (col 52) includes today.
# Since today is Sunday (2026-10-18), Week 52 starts on Sunday 2026-10-18.
# 52 weeks prior: start_sunday = 2026-10-18 - 52 * 7 days = 2025-10-19.
# Let's verify 2025-10-19:
start_sunday = datetime(2026, 10, 18) - timedelta(days=52*7)
print('Start Sunday:', start_sunday.strftime('%Y-%m-%d (%A)'))
end_day = datetime(2026, 10, 18)
print('End Day:', end_day.strftime('%Y-%m-%d (%A)'))

# Total 53 weeks * 7 = 371 days
grid_cells_data = []
for col in range(53):
    col_sunday = start_sunday + timedelta(days=col*7)
    for row in range(7):
        curr_day = col_sunday + timedelta(days=row)
        d_str = curr_day.strftime('%Y-%m-%d')
        if curr_day <= end_day:
            c_info = date_map.get(d_str, {'date': d_str, 'count': 0, 'level': 0})
        else:
            c_info = {'date': d_str, 'count': 0, 'level': 0, 'future': True}
        grid_cells_data.append(c_info)

print('Total grid cells:', len(grid_cells_data))
active_cells = [c for c in grid_cells_data if c.get('count', 0) > 0]
print('Active cells in GitHub aligned grid:', len(active_cells))
print('Total contributions in grid:', sum(c.get('count', 0) for c in grid_cells_data))

# Breakdown of non-zero weeks across all 53 weeks
non_zero_weeks = 0
for col in range(53):
    w_cells = grid_cells_data[col*7 : (col+1)*7]
    w_count = sum(c['count'] for c in w_cells)
    if w_count > 0:
        non_zero_weeks += 1
print('Non-zero weeks:', non_zero_weeks, 'out of 53 weeks')
