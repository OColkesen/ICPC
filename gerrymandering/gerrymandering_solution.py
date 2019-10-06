import sys

def find_missing():
    f = sys.stdin
    contents =f.read()
    input_ = contents.split("\n")
    first_line = input_[0].split(" ")
    number_precincts = int(first_line[0])
    number_districts = int(first_line[1])

    master_list = []
    district_outcomes = []
    total_votes = 0
    total_wasteA = 0
    total_wasteB = 0


    for i in range(number_districts):
        master_list.append([])

    for i in range(1, number_precincts+1):
        precinct = input_[i].split()

        if len(master_list[int(precinct[0])-1]) > 0:
            master_list[int(precinct[0])-1][0] += int(precinct[1])
            master_list[int(precinct[0])-1][1] += int(precinct[2])
        else:
            master_list[int(precinct[0])-1].append(int(precinct[1]))
            master_list[int(precinct[0])-1].append(int(precinct[2]))

    for i in range(number_districts):
        total_votes += (master_list[i][0] + master_list[i][1])
        district_total = master_list[i][0] + master_list[i][1]
        if master_list[i][0] > master_list[i][1]:
            total_wasteB += master_list[i][1]
            master_list[i].insert(0,"A")
            wastedA = master_list[i][1] - (district_total//2 + 1)
            master_list[i].insert(1,wastedA)
            master_list[i].pop(2)
            total_wasteA += wastedA
        else:
            total_wasteA += master_list[i][0]
            master_list[i].insert(0,"B")
            wastedB = master_list[i][2] - (district_total//2 + 1)
            master_list[i].append(wastedB)
            master_list[i].pop(2)
            total_wasteB += wastedB

    for i in range (len(master_list)):
        for j in range (len(master_list[0])):
            print(master_list[i][j], end = " ")
        print()

    num = abs(total_wasteA-total_wasteB) / total_votes
    print("%0.10f"%num)

find_missing()