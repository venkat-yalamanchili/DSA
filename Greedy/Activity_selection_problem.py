def print_activites(activites):
    activites.sort(key =lambda x:x[2])
    print(activites[0][0])
    last_finish_time = activites[0][2]

    for j in range (1, len(activites)):
        if activites[j][1] >= last_finish_time:
            print(activites[j][0])
            last_finish_time = activites[j][2]

activites = [["A1",0,6],
             ["A2",3,4],
             ["A3",1,2],
             ["A4",5,8],
             ["A5",5,7],
             ["A6",8,9]
             ]

print_activites(activites)