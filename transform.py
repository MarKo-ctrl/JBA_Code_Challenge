import re
from datetime import datetime, timedelta


def lines_to_dict(lines):
    data_dict = {'Xref': [], 'Yref': [], 'Date': [], 'Value': []}

    for i in range(len(lines)):
        if re.search(r'Grid-\w+=\s+[0-9]+,\s*[0-9]+', lines[i]):
            for k in range(120):
                data_dict['Xref'].append(re.split(r'Grid-\w+=\s+',	lines[i])
                                         [1].rstrip().split(',')[0])
                data_dict['Yref'].append(re.split(r'Grid-\w+=\s+', lines[i])
                                         [1].rstrip().split(',')[1].rstrip())
        else:
            for k in re.findall(r'[0-9]{1,5}', lines[i]):
                data_dict['Value'].append(k)
    return data_dict


def datelist(dates):
    start, end = [datetime.strptime(_, "%m/%d/%Y") for _ in dates]
    def total_dates(dt): return dt.month + 12 * dt.year
    dlist = []
    for t_m in range(total_dates(start)-1, total_dates(end)):
        y, m = divmod(t_m, 12)
        dlist.append(datetime(y, m+1, 1).strftime("%m/%d/%Y"))

    dlist_full = []
    for n in range(5226):
        for m in range(len(dlist)):
            dlist_full.append(dlist[m])
    return dlist_full
