def add_time(start, duration, day=None):
  days = [
    'Monday', 'Tuesday', 'Wednesday', 'Tuesday', 'Friday', 'Saturday', 'Sunday'
  ]

  start = start.split()
  time1_split = start[0].split(':')
  time2_split = duration.split(':')
  count_minute = (int(time1_split[1]) + int(time2_split[1]))
  count_hour = int(time1_split[0]) + int(
    time2_split[0]) + int(count_minute) // 60
  count_minute = str(int(count_minute) % 60)
  count_halfdays = int(count_hour) // 12

  count_hour = str(int(count_hour) % 12)
  if count_hour == '0':
    count_hour = '12'
    count_halfdays += 1
  if int(count_minute) < 10:
    count_minute = '0' + count_minute

  if int(count_halfdays) % 2 != 0 and start[1] == 'PM':
    start[1] = 'AM'
    count_halfdays += 1
  elif int(count_halfdays) % 2 != 0 and start[1] == 'AM':
    start[1] = 'PM'

  if count_halfdays == 2:
    next_day = ' (next day)'
  elif count_halfdays == 0 or count_halfdays == 1:
    next_day = ''
  else:
    next_day = ' (' + str(count_halfdays // 2) + ' days later)'

  if day is None:
    new_time = count_hour + ':' + count_minute + ' ' + start[1] + next_day
  else:
    for n in range(len(days)):
      if day.title() == days[n]:
        day = days[(n + int(count_halfdays / 2)) % 7]
    new_time = count_hour + ':' + count_minute + ' ' + start[
      1] + ', ' + day.title() + next_day

  return new_time
