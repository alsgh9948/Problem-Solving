from collections import deque
dx = [0,-1,0,1,0]
dy = [0,0,1,0,-1]
tc = int(input())

def solv(t):
    global m,a,move_info,battery
    m,a = map(int, input().split())

    move_info = []
    move_info.append([0]+list(map(int, input().split())))
    move_info.append([0]+list(map(int, input().split())))

    battery = []
    for _  in range(a):
        y,x,c,p = map(int, input().split())
        battery.append((x-1,y-1,c,p))
    print('#%d %d'%(t,simul()))

def simul():
    user1 = [0,0]
    user2 = [9,9]

    answer = 0
    for idx in range(m+1):
        user1 = move_user(user1,move_info[0][idx])
        user2 = move_user(user2,move_info[1][idx])

        user1_battery = check_distance(user1)
        user2_battery = check_distance(user2)
        if user1_battery and user2_battery:
            if user1_battery[0][0] == user2_battery[0][0]:
                if len(user1_battery) > 1 and len(user2_battery) > 1:
                    if user1_battery[1][1] > user2_battery[1][1]:
                        answer += user1_battery[1][1]+user2_battery[0][1]
                    else:
                        answer += user1_battery[0][1]+user2_battery[1][1]
                elif len(user1_battery) > 1:
                    answer += user1_battery[1][1] + user2_battery[0][1]
                elif len(user2_battery) > 1:
                    answer += user1_battery[0][1] + user2_battery[1][1]
                elif len(user1_battery) == 1 and len(user2_battery) == 1:
                    answer += user1_battery[0][1]
            else:
                answer += user1_battery[0][1] + user2_battery[0][1]
        elif user1_battery:
            answer += user1_battery[0][1]
        elif user2_battery:
            answer += user2_battery[0][1]
    return answer

def check_distance(user):
    battery_list = []
    x,y = user
    for idx in range(a):
        bx,by,c,p = battery[idx]
        if abs(x-bx)+abs(y-by) <= c:
           battery_list.append((idx,p))

    return sorted(battery_list,key=lambda x:-x[1])
def move_user(user,d):
    x,y = user
    x += dx[d]
    y += dy[d]
    return [x,y]
for t in range(1,tc+1):
    solv(t)