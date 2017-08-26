#step one is to create graps
#see notes on phone

links_list = [(1,2),(1,3),(3,5),(7,9),(3,4),(5,2),(12,19)]

nodes = []
graph = {}

for i in links_list: #build nodes
    if i[0] not in nodes:
        nodes.append(i[0])
    if i[1] not in nodes:
        nodes.append(i[1])

for i in links_list: #build graph
    if i[0] not in graph: #if first val doesn't exit...
        graph[i[0]] = set([i[1]]) #add it plus it's pair
    elif i[1] not in graph[i[0]]: #if it does exist but pair not in it's list...
        graph[i[0]].add(i[1]) #add it's pair to list
    if i[1] not in graph: #do the reverse
        graph[i[1]] = set([i[0]])
    elif i[0] not in graph[i[1]]:
        graph[i[1]].add(i[0])

print("nodes: ", nodes)
print("graph: ", graph)

def dfs(graph, start): #this returns all links for a given node
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

def build_groups(graph, toprocess): #iterate through the dfs and process the nodes list
    id = 1 #initialise first group
    groups = {}
    while toprocess:
        b = dfs(graph,toprocess[0]) #process top value in nodes
        groups[id] = b #apply results to set 1,2,3,4..
        toprocess = [x for x in toprocess if x not in b] #remove items returned by dfs
        id += 1 #create next group
    print("groups: ", groups)

build_groups(graph,nodes)