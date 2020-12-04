def apply_port_exclusions(include_ports, exclude_ports):
    output = []
    for i in include_ports:
        alpha = [i]
        for a in alpha:
            for e in exclude_ports:
                if a[0] < e[1] < a[1] or a[0]< e[0] < a[1]:
                    if e[0] < a[0] < e[1]:
                        a = [e[1]+1, a[1]]
                    elif e[0] < a[1] < e[1]:
                        a = [a[0], e[0]-1]
                    else:
                        alpha.append([e[1]+1, a[1]])
                        a = [a[0], e[0]-1]
            output += [a]
    output.sort(key=lambda p: p[0])
    merge = []
    flag = False
    truoutput = []
    for o in output:
        if not flag:
            merge = o
            flag = True
        else:
            if merge[1] >= o[0]-1: merge[1] = o[1]
            else: 
                truoutput.append(merge)
                truoutput.append(o)
                flag = False
    print(truoutput)    
    return truoutput
