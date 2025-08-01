def FCFS(p): #p is process list [arrive_time, process_time]
    p.sort(key=lambda x:x[0])

    current_time = 0
    total_waiting = 0
    total_turnaround = 0

    for arrival, burst in p :

        if current_time < arrival :
            current_time = arrival
        wating_time = current_time - arrival
        total_waiting += wating_time
        total_turnaround += burst + wating_time
        current_time += burst

    n = len(p)

    return total_turnaround/n, total_waiting/n

#
#Shortest Job First
# def SJF(p):
#     p.sort(key = lambda x : x[0])


#     current_time = 0
#     total_waiting = 0
#     totla_turnaround = 0

#     for arrival, burst in p :
#         if current_time < arrival:
#             current_time = arrival
        
#     while (True):
        
            


