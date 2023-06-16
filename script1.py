import re

match = []
result = {}
regexp = re.compile(r' (\d{2}:\d{2}).*([N][O][K])')
with open('events.log', 'r') as logfile:
    for line in logfile:
        try:
            line.index("NOK")
        except:
            pass
        else:
            match.append(line.rstrip())

for l in match:
    sorted = regexp.search(l)
    try:
        result[str(sorted[1])] += 1
    except KeyError:
        result[str(sorted[1])] = 1
    # result[str(sorted[1])] += 1
print(result)
