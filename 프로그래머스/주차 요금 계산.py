from collections import defaultdict
import math
convert_to_minute = lambda t:int(t[:2])*60+int(t[3:])
IN = "IN"
OUT = "OUT"
LAST_TIME = convert_to_minute("23:59")
class Info:
    def __init__(self):
        self.total = 0
        self.status = OUT
        self.in_time = 0

def solution(fees, records):
    car_info = defaultdict(Info)

    for record in records:
        record = record.split()

        t = convert_to_minute(record[0])
        number = record[1]
        status = record[2]

        if status == IN:
            car_info[number].in_time = t
            car_info[number].status = IN
        else:
            car_info[number].total += t-car_info[number].in_time
            car_info[number].in_time = 0
            car_info[number].status = OUT

    for number in car_info:
        if car_info[number].status == IN:
            car_info[number].total += LAST_TIME - car_info[number].in_time
            car_info[number].in_time = 0
            car_info[number].status = OUT
    answer = []
    for number in sorted(car_info.keys()):
        if car_info[number].total <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1]+math.ceil((car_info[number].total-fees[0])/fees[2])*fees[3])
    return answer

def convert_to_minute(t):
    return int(t[:2])*60+int(t[3:])

a = [180, 5000, 10, 600]
b = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(a,b))