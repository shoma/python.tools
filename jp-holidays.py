import requests

u = 'http://www.google.com/calendar/feeds/ja.japanese%23holiday@group.v.calendar.google.com/public/full?alt=json&max-results=100&futureevents=true'

data = requests.get(u).json()
print data.get('feed').get('title').get('$t')

for item in data.get('feed').get('entry'):
    # gd$when
    # 'title']['$t']
    title = item['title']['$t']
    day = item['gd$when'][0]['startTime']
    print "{name}\t{day}".format(name = title.encode('utf8'), day=day.encode('utf8'))
