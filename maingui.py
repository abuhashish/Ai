from tkinter import *
import sys
import tkinter as tk
import tkinter.font as tkFont
import random
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
    self.start = originCity 
    self.goal = destinationCity
    if inputFile is not None :
      self.parseInputData( inputFile )
    if heuristicFile is not None and ".txt" in heuristicFile :
      self.parseHeuristicData( heuristicFile )
    else :
      self.heuristicData = heuristicFile
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
def dfs(visited, graph, node,destination_city,numofnodes,):
    numofnodes +=1
    if node == destination_city:
      print("destination has been reached", node)
      print("number of expanded nodes = ",numofnodes)
      sys.exit(0)
    if node not in visited :
        print (node,graph[node])
        print ("=>")
        visited.add(node)
        for neighbour,dist in graph[node]:
            dfs(visited, graph, neighbour,destination_city,numofnodes)
def dfs_iterative(graph, start,destination_city,numofnodes):
    numofnodes = 0
    stack, path = [start], []
    toprint=""
    while stack:
        numofnodes += 1
        vertex = stack.pop()
        toprint+=vertex
        toprint+="=>"
        if vertex in path:
            continue
        if destination_city == vertex:
          toprint+="\n"
          toprint+="destination has been reached "+ vertex +"\n"
          toprint+="number of expanded nodes = "+str(numofnodes)
          return toprint
        path.append(vertex)
        for neighbor,dist in graph[vertex]:
            stack.append(neighbor)

    return "there is no path"

############################ BFS implementation ###################################################
queue = []
def bfs(visited, graph, node,destination_city,numofnodes):
  visited.append(node)
  queue.append(node)
  toprint=""
  while queue:
    numofnodes +=1
    s = queue.pop(0) 
    toprint+=s
    toprint+="=>"
    if s == destination_city:
      toprint+="\n"
      toprint+="destination has been reached "+ s +"\n"
      toprint+="number of expanded nodes = "+str(numofnodes)
      return toprint
    for neighbour,dist in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
#########################################################################################
def h(self,n):
  H=self.heuristicData
  return H[n]
########################## A * Algorithm #################################################
def A_star_algorithm(model, start, goal):
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
########################################################################################
############# A * implementation #####################################################
def astartprint(graph,start,end):
    toprint=""
    path,expanded=A_star_algorithm(graph,start,end)
    paths = [p.city for p in path]
    toprint+=" --> ".join(paths)
    distance = sum(map(lambda x: x.tc, path))
    toprint+="\n"
    toprint+="nodes expanded: " + str(expanded)
    if distance and len(path) > 1:
      toprint+="        distance: "+str(distance)+"km \n"
      toprint+="route:"
      for i in range(len(path) -1):
        toprint+=path[i].city+" to "+ path[i+1].city+"="+ str(path[i+1].tc)+" km \n"
    elif len(path) == 1:
      toprint+="distance: " + str(distance)+"km \n"
      toprint+="route:"
      toprint+=path[0].city+ path[0].city +str(path[0].tc)
    else:
      toprint+="No route is possible"
    return toprint
######################## A* distance for walking function #################################
def distwalk(graph, start,end):
  path,expanded=A_star_algorithm(graph,start,end)
  paths = [p.city for p in path]
  distance = sum(map(lambda x: x.tc, path))
  if distance and len(path) > 1:
    return distance
  elif len(path) == 1:
    return distance
  else:
    return int(500*random.random())
#---------#---------#---------#---------#---------#--------#
################ A* with walking heurstics##################

##############################################################
def main() :
  # Get the file name and the other arguments.
    fName="input.txt"
    airHeurstics="arialDist.txt"
    graph = ReadData( fName,"luebeck","kassel",airHeurstics )
    visitedbfs=[]
    # dfs_iterative( graph.inputData,'berlin','dresden',0)
    # bfs(visitedbfs, graph.inputData, 'berlin',"dresden",0)
    astartprint( graph,"luebeck","kassel")
    walkingdata=graph.heuristicData
    for i in walkingdata:
      walkingdata[i]=distwalk( ReadData( fName,i,"kassel",airHeurstics ),i,"kassel")
    print(walkingdata)
    astartprint(ReadData( fName,"luebeck","kassel",walkingdata),"luebeck","kassel")
    

########################################################################################################################
class App:

  def __init__(self, root):
    #setting title
    self.x=0
    self.y=0
    root.title("Ai Project")
    width=600
    height=500
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)
    root['bg']="cyan"

    self.GLineEdit_209=tk.Entry(root)
    self.GLineEdit_209["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    self.GLineEdit_209["font"] = ft
    self.GLineEdit_209["fg"] = "#333333"
    self.GLineEdit_209["justify"] = "center"
    self.GLineEdit_209["text"] = ""
    self.GLineEdit_209.place(x=60,y=120,width=224,height=30)

    GLabel_459=tk.Label(root)
    
    ft = tkFont.Font(family='Times',size=10)
    GLabel_459["font"] = ft
    GLabel_459["fg"] = "#333333"
    GLabel_459["justify"] = "center"
    GLabel_459["text"] = "Welcome To Path-Finder ( AI Project)"
    GLabel_459['bg']="green"
    GLabel_459.place(x=90,y=20,width=402,height=30)

    GRadio_202=tk.Radiobutton(root)
    ft = tkFont.Font(family='Times',size=10)
    GRadio_202["font"] = ft
    GRadio_202["fg"] = "#333333"
    GRadio_202["justify"] = "center"
    GRadio_202["text"] = "A*"
    GRadio_202.place(x=30,y=230,width=85,height=25)
    GRadio_202["command"] = self.GRadio_202_command
    GRadio_202["value"]=0
    GRadio_202["bg"]="grey"

    GRadio_538=tk.Radiobutton(root)
    ft = tkFont.Font(family='Times',size=10)
    GRadio_538["font"] = ft
    GRadio_538["fg"] = "#333333"
    GRadio_538["justify"] = "center"
    GRadio_538["text"] = "bfs"
    GRadio_538.place(x=240,y=230,width=85,height=25)
    GRadio_538["command"] = self.GRadio_538_command
    GRadio_538["value"]=1
    GRadio_538["bg"]="grey"
    
    GRadio_210=tk.Radiobutton(root)
    ft = tkFont.Font(family='Times',size=10)
    GRadio_210["font"] = ft
    GRadio_210["fg"] = "#333333"
    GRadio_210["justify"] = "center"
    GRadio_210["text"] = "DFS"
    GRadio_210.place(x=430,y=230,width=85,height=25)
    GRadio_210["command"] = self.GRadio_210_command
    GRadio_210["value"] = 2
    GRadio_210["bg"]="grey"

    GLabel_323=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_323["font"] = ft
    GLabel_323["fg"] = "#333333"
    GLabel_323["justify"] = "center"
    GLabel_323["text"] = "Please Choose The Algorithem You want to use"
    GLabel_323.place(x=50,y=190,width=283,height=30)
    GLabel_323["bg"]="grey"

    GLabel_632=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_632["font"] = ft
    GLabel_632["fg"] = "#333333"
    GLabel_632["justify"] = "center"
    GLabel_632["text"] = "Please Choose Your StartPoint :-"
    GLabel_632.place(x=60,y=80,width=194,height=30)
    GLabel_632["bg"]="grey"
    
    GCheckBox_235=tk.Checkbutton(root)
    ft = tkFont.Font(family='Times',size=10)
    GCheckBox_235["font"] = ft
    GCheckBox_235["fg"] = "#333333"
    GCheckBox_235["justify"] = "center"
    GCheckBox_235["text"] = "Heurstics(Walk Distance)"
    GCheckBox_235.place(x=30,y=270,width=160,height=32)
    GCheckBox_235["offvalue"] = "0"
    GCheckBox_235["onvalue"] = "1"
    GCheckBox_235["command"] = self.GCheckBox_235_command
    GCheckBox_235["bg"]="grey"

    GCheckBox_632=tk.Checkbutton(root)
    ft = tkFont.Font(family='Times',size=10)
    GCheckBox_632["font"] = ft
    GCheckBox_632["fg"] = "#333333"
    GCheckBox_632["justify"] = "center"
    GCheckBox_632["text"] = "Heurstics(Airial Distance)"
    GCheckBox_632.place(x=30,y=300,width=160,height=30)
    GCheckBox_632["offvalue"] = "0"
    GCheckBox_632["onvalue"] = "2"
    GCheckBox_632["command"] = self.GCheckBox_632_command
    GCheckBox_632["bg"]="grey"
    
    
    GButton_969=tk.Button(root)
    GButton_969["bg"] = "#efefef"
    ft = tkFont.Font(family='Times',size=10)
    GButton_969["font"] = ft
    GButton_969["fg"] = "#000000"
    GButton_969["justify"] = "center"
    GButton_969["text"] = "Find"
    GButton_969.place(x=240,y=340,width=70,height=25)
    GButton_969["command"] = self.GButton_969_command
    GButton_969["bg"]="white"

    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)
    self.GMessage_543=tk.Text(root)
    ft = tkFont.Font(family='Times',size=10)
    self.GMessage_543["font"] = ft
    self.GMessage_543["fg"] = "#333333"
    self.GMessage_543.place(x=20,y=390,width=551,height=100)
    self.GMessage_543["bg"]="white"
    self.GMessage_543.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=self.GMessage_543.yview)

  
  def GRadio_202_command(self):
      self.x=3


  def GRadio_538_command(self):
      self.x=2


  def GRadio_210_command(self):
      self.x=1
      
  def GCheckBox_235_command(self):
      self.y=1


  def GCheckBox_632_command(self):
      self.y=2
      

  def GButton_969_command(self):
    toprint="*******************************************************************\n"
    fName="input.txt"
    airHeurstics="arialDist.txt"
    graph = ReadData( fName,self.GLineEdit_209.get(),"jerusalem",airHeurstics )
    walkingdata=graph.heuristicData
    for i in walkingdata:
      walkingdata[i]=distwalk( ReadData( fName,i,"jerusalem",airHeurstics ),i,"jerusalem")
    visitedbfs=[]
    if self.x == 1:
      toprint+=dfs_iterative( graph.inputData,self.GLineEdit_209.get(),'jerusalem',0)
    elif self.x == 2:
      toprint+=bfs(visitedbfs, graph.inputData, self.GLineEdit_209.get(),"jerusalem",0)
    elif self.x == 3 and self.y == 2:
      toprint+=astartprint( ReadData( fName,self.GLineEdit_209.get(),"jerusalem",airHeurstics ),self.GLineEdit_209.get(),"jerusalem")
    elif self.x == 3 and self.y == 1:
      toprint+=astartprint( ReadData( fName,self.GLineEdit_209.get(),"jerusalem",walkingdata ),self.GLineEdit_209.get(),"jerusalem")
    toprint+="\n************************************************************"
    self.GMessage_543.insert(END, toprint)

if __name__ == "__main__":
  root = tk.Tk()
  app = App(root)
  root.mainloop()
