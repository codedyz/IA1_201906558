def heuristic(start, end, h):
    if h == 1:  # tiles out
        tiles_out = sum(1 for i in range(len(start)) if start[i] != end[i])
        return tiles_out
    elif h == 2:  # Manhattan
        return sum(abs(i - end.index(start[i])) for i in range(len(start)))

def successors(n, e, h):
    suc = []
    for i in range(len(n[0]) - 1):
        tmp = n[0][i]
        child = n[0][:i] + n[0][i+1] + tmp + n[0][i+2:]
        suc.append([child, heuristic(child, e, h), inc()])
    return suc

id_counter = 1
def inc():
    global id_counter
    id_counter += 1
    return id_counter

def bestfirst(start, end, h, colinas = False):
    cont = 0
    dot = 'graph G{\n'
    list = [[start, heuristic(start, end, h), inc()]]
    dot += f'{list[0][2]} [label="{list[0][0]}"];\n'
    while list:
        current = list.pop(0)
        if current[0] == end:
            dot += '}'
            return dot
        temp = successors(current, end, h)

        if(colinas):
            temp.sort(key=lambda x: x[1])
            temp = temp[:1]

        for val in temp:
            dot += f'{val[2]} [label="{val[0]}"];\n{current[2]}--{val[2]} [label="{val[1]}"];\n'
        list.extend(temp)
        list.sort(key=lambda x: x[1])
        cont += 1
        if cont > 100:
            print("The search is looped!")
            dot += '}'
            return dot
    dot += '}'
    return dot
