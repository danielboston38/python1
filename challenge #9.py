#!/usr/bin/env python3

unsorted_time = ['09:30-10:15', '13:00-13:30', '10:00-11:00', '11:00-11:00', '13:30-14:00', '09:45-10:00']

for time_range in unsorted_time:
    start, end = time_range.split("-")

for time_range in unsorted_time:
    start, end = time_range.split("-")
    start_h, start_m = start.split(":")
    end_h, end_m = end.split(":")

start_h, start_m = int(start_h), int(start_m)
end_h, end_m = int(end_h), int(end_m)

def get_start_time(time_range):
    start, _ = time_range.split("-")   # grab the left side only
    hh, mm = map(int, start.split(":"))
    return (hh, mm)  # tuples sort naturally

sorted_time = sorted(unsorted_time, key=get_start_time)

print("Here are your sorted times:")
for t in sorted_time:
    print(t)
