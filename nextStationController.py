from pyswip.prolog import Prolog
from pyswip.easy import getList, registerForeign

def loadDatabase(prolog):
    prolog.consult("shortest_path(TIME).pl")
    prolog.consult("which_train.pl")

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

    train_query = "theTrainIs(" + str(path_list) + ",TRAIN)"
    train_result = list(prolog.query(train_query))

    train_list = []
    for i in range(len(train_result[0]['TRAIN'])):
        train_list.append(str(train_result[0]['TRAIN'][i]))
    
    path_type_list = []
    include_walk_query = "includeWalk(" + str(train_list) + ",PATH_TYPE)"
    include_walk_result = list(prolog.query(include_walk_query))
    for i in range(len(include_walk_result[0]['PATH_TYPE'])):
        path_type_list.append(str(include_walk_result[0]['PATH_TYPE'][i]))

    print("Train: " + str(train_list))
    print ""
    print("Train+Walk: " + str(path_type_list))
    print ""
    print("TrainLen: " + str(len(train_list)) + "->" + str(len(path_type_list)))


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
