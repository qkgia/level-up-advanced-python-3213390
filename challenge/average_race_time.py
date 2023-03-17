# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians

import re
import datetime


def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.read()
    return content


def get_time_from_line(line):
    # line_str = line.split()
    # return line_str[0]
    time = re.findall(r'\d{2}:\S+', line)[0]

    return time


def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    races_str = get_data()
    races_str = races_str.splitlines()
    times = []
    for line in races_str:
        if 'Jennifer Rhines' in line:
            times.append(get_time_from_line(line))

    return times


def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()
    total = datetime.timedelta()

    for rtime in racetimes:
        time_parts = re.split(r'[:.]', rtime)

        if len(time_parts) > 2:
            mins = time_parts[0]
            seconds = time_parts[1]
            msecond = time_parts[2]
        else:
            mins = time_parts[0]
            seconds = time_parts[1]
            msecond = '0'

        total += datetime.timedelta(minutes=int(mins),
                                    seconds=int(seconds), milliseconds=int(msecond))

    result_str = '{}'.format(total / len(racetimes))[2:-5]

    return result_str
