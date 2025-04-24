graph = [
    [0,1,2,3],
    [1,0,3,2],
    [1,2,0,4],
    [1,2,3,0]
]

node = [0,1,2,3]
start_city= 0

stack = [(start_city , [node[0]])]

while(stack):
    current_city , path = stack.pop()
    for i in range (len(graph)):
      if current_city not in path :
        print(" ")