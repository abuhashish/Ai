import sys
import math

class node(object):
  def __init__(self, city,g = 0, tc = 0,f = 0,parent = None):
    self.city = city
    self.g = g
    self.f = f
    self.tc = tc
    self.parent = parent
    
######################################
class ReadData(object) :
  def __init__( self, inputFile = "input.txt", originCity = None, destinationCity = None, heuristicFile = None) :
    self.inputData = {}
    self.heuristicData = {}
    if inputFile is not None :
      self.parseInputData( inputFile )
    if heuristicFile is not None :
      self.parseHeuristicData( heuristicFile )
################## read g(n)#####################################
  def parseInputData( self, inputFile ) :
    try:
      fp = open(inputFile, 'r')
      lines = fp.read().replace('\r', '' ).split( '\n' )

      for line in lines:
        if line and line != 'END OF INPUT':
          line_arr = line.strip().split(' ')
          if line_arr[0].lower() in self.inputData:
            self.inputData[line_arr[0].lower()].append((line_arr[1].lower(), int(line_arr[2])))
          else:
            self.inputData[line_arr[0].lower()] = []
            self.inputData[line_arr[0].lower()].append((line_arr[1].lower(), int(line_arr[2])))

          if line_arr[1].lower() in self.inputData:
            self.inputData[line_arr[1].lower()].append((line_arr[0].lower(), int(line_arr[2])))
          else:
            self.inputData[line_arr[1].lower()] = []
            self.inputData[line_arr[1].lower()].append((line_arr[0].lower(), int(line_arr[2])))
    finally:
      fp.close()
#######################read h(n)##############################################################
  def parseHeuristicData( self, inputFile ) :
    try:
      fp = open(inputFile, 'r')
      lines = fp.read().replace('\r', '' ).split( '\n' )

      for line in lines:
        if line and line != 'END OF INPUT':
          line_arr = line.strip().split(' ')
          self.heuristicData[line_arr[0].lower()] = int(line_arr[1])
    finally:
      fp.close()
#######################################################################################
##########################DFS implementation ########################################
def dfs(visited, graph, node,destination_city,numofnodes):
    numofnodes +=1
    if node == destination_city:
      print("destination has been reached", node)
      print("number of expanded nodes = ",numofnodes)
      exit()
    if node not in visited:
        print (node,graph[node])
        print ("=>")
        visited.add(node)
        for neighbour,dist in graph[node]:
            dfs(visited, graph, neighbour,destination_city,numofnodes)

############################ BFS implementation ###################################################
queue = []
def bfs(visited, graph, node,destination_city,numofnodes):
  numofnodes +=1
  visited.append(node)
  queue.append(node)
  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 
    if node == destination_city:
      print("destination has been reached", node)
      print("number of expanded nodes = ",numofnodes)
      exit()
    for neighbour,dist in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
#########################################################################################
########################################################################################
def performSearch(model, start, goal):
  opened = set()
  closed = set()
  fvalue = getFValue(model, start)
  expanded = 1
  startNode = node(start,0,0, fvalue[1], parent = None)
  opened.add(startNode)
  current = start

  while opened:
    current = getLeastFvalueNode(opened)
    neighbours = getNeighbor(model, current)
    neighboursNodes = generateNodes(model, neighbours, current)

    if current.city == goal:
      path = []
      while current.parent:
        path.append(current)
        current = current.parent
      path.append(current)
      return (path[::-1],expanded)

    opened.remove(current)
    closed.add(current)

    for nodes in neighboursNodes:
      if neighboursNodes[nodes] in closed:
        continue

      if nodes not in [cities.city for cities in closed]:
        if neighboursNodes[nodes] not in opened and nodes != model.start:
          opened.add(neighboursNodes[nodes])
    expanded +=1

  return ([],expanded)  
def getLeastFvalueNode(nodes):
  leastFNode = None
  for node in nodes:
    if leastFNode is None:
      leastFNode = node 
    elif leastFNode.f > node.f:
      leastFNode = node
  return leastFNode

def getTentativeCost(cities, node):
  for city in cities:
    if city[0] == node:
      return city[1]
  return 0

def getCost(model, node, parentCost):
  cost = 0
  if model.start != node:
    cost = parentCost.g + getTentativeCost(model.inputData[parentCost.city], node)
  return cost

def getFValue(model, node, parentCost = None):
  heuristic = 0
  cost = 0
  if node in model.heuristicData:
    heuristic = model.heuristicData[node]

  if model.start != node:
    cost = getCost(model, node, parentCost)
   
  return  (cost, cost + heuristic)
  
def getNeighbor(model, node):
  return model.inputData[node.city]
  
def generateNodes(model, neighbours, parent):
  Nodes = {}
  for nbour in neighbours:
    cost, fvalue = getFValue(model, nbour[0], parent)
    Nodes[nbour[0]] = node(nbour[0],cost,nbour[1], fvalue,parent)  
  return  Nodes
#---------#---------#---------#---------#---------#--------#
def main() :
  # Get the file name and the other arguments.
    fName="input.txt"
    hName="arialDist.txt"
    graph = ReadData( fName, hName )
    # path,expanded = performSearch(graph,origin_city, destination_city)
    visitedbfs=[]
    visiteddfs=set()
    bfs(visitedbfs, graph.inputData,'berlin','dresden',0)
    dfs(visiteddfs, graph.inputData, 'berlin',"dresden",0)
  #   paths = [p.city for p in path]
  #   print(" --> ".join(paths))
  #   distance = sum(map(lambda x: x.tc, path))
  #   print("nodes expanded: %d"%(expanded))
  #   if distance and len(path) > 1:
  #     print("distance: %d km"%(distance))
  #     print("route:")
  #     for i in range(len(path) -1):
  #       print("%s to %s, %d km"%(path[i].city, path[i+1].city, path[i+1].tc))
  #   elif len(path) == 1:
  #     print("distance: %d km"%(distance))
  #     print("route:")
  #     print("%s to %s, %d km"%(path[0].city, path[0].city, path[0].tc))
  #   else:
  #     print("distance: infinity")
  #     print("route: none")
  # else:
  #   print("Please enter all the required parameters")

main()