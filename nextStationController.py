from pyswip.prolog import Prolog
from pyswip.easy import getList, registerForeign

def loadDatabase(prolog):
    prolog.consult("shortest_path(TIME).pl")

def inputFromTo():
    from_input = str(raw_input("from: "))
    to_input = str(raw_input("to: "))
    return from_input, to_input

def findShortestPath(from_input, to_input):
    prolog = Prolog()
    loadDatabase(prolog)
    prolog_query = "path(" + from_input + "," + to_input + ",PATH,COST)"
    shortest_path_result = list(prolog.query(prolog_query))
    path_list = []
    shortest_path_lst = shortest_path_result

    if len(shortest_path_lst) <= 0:
        return False

    for i in range(len(shortest_path_lst[0]['PATH'])):
        path_list.append(str(shortest_path_result[0]['PATH'][i]))

    return path_list, shortest_path_result[0]['COST']

def printOut(path_list, cost):
    print("Path: " + str(path_list))
    print("Cost: " + str(cost))
    print("")

def mainActivity():
    from_input, to_input = inputFromTo()
    path_lst, cost = findShortestPath(from_input, to_input)
    printOut(path_lst, cost)


if __name__ == '__main__':
    mainActivity()
