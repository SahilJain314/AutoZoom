import json
import time
import pyautogui as auto
import webbrowser
import pymsgbox as msg

time_file = 'schedule.json'
day_table = []
num_to_day = {0:'M', 1:'T', 2:'W', 3: 'TH', 4: 'F', 5:'SA', 6:'SU'}
time_buffer_min = 2
no_repeat = True
cooldown = 10
check_period = 60

def chrome_open(url, class_name = '', prompt = True):
    r = ''
    if prompt:
        r = msg.prompt("Enter anything to not go to class: " + class_name)
    if r == '':
        webbrowser.open_new(url)
    return

def sort_day(timetable):
    days = {'M':[], 'T':[], 'W':[], 'TH':[], 'F':[], 'SA':[], 'SU':[]}
    for t in timetable:
        for d in t['days']:
            idx = 0
            for i in range(len(days[d])):
                if t['time'] > days[d][i]['time']:
                    idx += 1
            days[d].insert(idx, t)
    return days

def check_and_run(day_table):
    global cooldown
    global no_repeat
    c_time = time.localtime()
    wday = c_time[6]
    hr = c_time[3]
    minute = c_time[4]
    day_stat = day_table[num_to_day[wday]]
    print(day_stat)
    for c in day_stat:
        print((c['time'] % 100) + ((c['time'] // 100) * 60) )
        if abs((c['time'] % 100) + ((c['time'] // 100) * 60) - (hr*60 + minute)) <= time_buffer_min and no_repeat:
            chrome_open(c['url'], class_name = c['class_name'], prompt = c['prompt'])
            no_repeat = False
            cooldown = 0

def cont_run(day_table):
    global cooldown
    global no_repeat
    while(True):
        print('checked')
        check_and_run(day_table)
        time.sleep(check_period)
        cooldown += 1
        if cooldown > time_buffer_min * 2 * 60 / check_period:
            no_repeat = True

f = open(time_file, 'r')
timetable = json.load(f)

print(time.localtime())
day_table = sort_day(timetable)
cont_run(day_table)
