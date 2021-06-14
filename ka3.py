# в качестве бесконечности
MAX_INT = 2**64


def get_data_from_file(path_to_file="in.txt"):
    matrix = []
    matrix_str = ""
    with open(path_to_file, "r") as file:
        rows_count = int(file.readline())
        matrix_str = file.read()  
    all_lines = matrix_str.split("\n")
    lines = all_lines[:-2]
    dest = int(all_lines.pop())
    source = int(all_lines.pop())
    # print(source)
    # print(dest)
    for line in lines:
        sep_line = line.split(" ")
        matrix.append(sep_line)
        
    print(matrix)
    return (matrix, source, dest)
    
def write_in_file(data):
    with open('out.txt', '+w') as file:
        file.write(data)  
    
    
def get_distances(current_line, source, matrix_len):
    distances = []
    for i in range(matrix_len):
        distances.append(MAX_INT)
    
    for i in  range(0, len(current_line), 2):
        current_node = int(current_line[i])
        if current_node == 0:
            break
        distances[current_node - 1] = int(current_line[i + 1])
    return distances
    
def initialize_prev_points(matrix, source):    
    prev_points = []
    for i in range(len(matrix)):
        prev_points.append(source)
    prev_points[source - 1] = 0
    print("init previous points:", prev_points)
    return prev_points
    
def find_min_dist_ind(distances, visited):
    min_d = MAX_INT
    ind = 0;
    for i in range(len(distances)):
        if distances[i] < min_d and (i+1) not in visited:
            min_d = distances[i]
            ind = i
    return ind
    
def calculate_distances(matrix, distances, node, source, prev_points):
    from_node_distances = get_distances(matrix[node-1], source, len(matrix)) 
    new_distances = list(distances)    
    # print(from_node_distances)    
    for i in range(len(distances)):
        if (i == source -1) or (i == node -1):
            continue
        distance_to_next_node = from_node_distances[i]
        if distances[i] <= distances[node - 1] + distance_to_next_node:
            min_value = distances[i]
        else:
            min_value = distances[node - 1] + distance_to_next_node
            prev_points[i] = node
            
        new_distances[i] = min_value
    # print(new_distances)
    return new_distances
    
def get_path(source, dest, prev_points):
    ind = dest
    path = []
    path.append(ind)
    while ind != source:
        ind = prev_points[ind-1]
        path.append(ind)    
    return reversed(path)
   
def find_path_dijkstra(matrix, source, dest):
    visited = []
    visited.append(source)
    prev_points = initialize_prev_points(matrix, source)
    current_line = matrix[source-1]
    distances = get_distances(current_line, source, len(matrix))
    print("init distances:",distances)
    
    for node in visited:
        ind = find_min_dist_ind(distances, visited)
        visited.append(ind + 1)
        distances = calculate_distances(matrix, distances, ind + 1, source, prev_points)
        print("node", ind + 1,"visited", visited,"distances", distances,"prev_points",prev_points)
        if len(visited) == len(matrix):
            if distances[dest-1] == MAX_INT:
                return (distances[dest - 1] , None)
            return (distances[dest - 1] , get_path(source, dest, prev_points))
    
    
    
matrix, source, dest = get_data_from_file()
distance, path = find_path_dijkstra(matrix, source, dest)
data_to_print = ""
if path == None:
    data_to_print = "N"
else:
    data_to_print = "Y\n"
    for i in path:
        data_to_print += str(i)+" "
    data_to_print += "\n" + str(distance)
print(data_to_print)
write_in_file(data_to_print)




