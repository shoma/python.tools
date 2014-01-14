import requests
import sys

u = 'http://www.google.com/calendar/feeds/ja.japanese%23holiday@group.v.calendar.google.com/public/full'
params =  {
    'alt': 'json',
    'max-results': 100,
    'futureevents': 'true'
}

res = requests.get(u, params=params)
res.raise_for_status()

data = res.json()
print data.get('feed').get('title').get('$t')

for item in data.get('feed').get('entry'):
    # ['title']['$t']
    title = item['title']['$t']
    # gd$when
    day = item['gd$when'][0]['startTime']
    print "{name}\t{day}".format(name = title.encode('utf8'), day=day.encode('utf8'))
