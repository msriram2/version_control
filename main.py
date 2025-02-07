import datetime as date

version.md = open('written_file', 'w')

current_time = date.datetime.now()
version.md.write(current_time)
version.md.close()

print(current_time)

