"""
  include_ports - A list of ports as a list of high-low pairs that are lists of length two
  exclude_ports - A list of ports to exclude as a list of high-low pairs that are lists of length two

  This function first iterates over exclude_ports for to split each item in include_ports to exclude those numbers. 
  It then orders the resulting list and iterates over the result again to minimize the list. 
"""
def apply_port_exclusions(include_ports, exclude_ports):
    inc_ports = []
    for i in include_ports:
        add = [i]
        for a in add:
            for e in exclude_ports:
                if a[0] < e[1] < a[1] or a[0]< e[0] < a[1]:
                    if e[0] < a[0] < e[1]:
                        a = [e[1]+1, a[1]]
                    elif e[0] < a[1] < e[1]:
                        a = [a[0], e[0]-1]
                    else:
                        add.append([e[1]+1, a[1]])
                        a = [a[0], e[0]-1]
            inc_ports += [a]
    inc_ports.sort(key=lambda p: p[0])
    merge = []
    flag = True
    output = []
    for i in inc_ports:
        if flag:
            merge = i
            flag = False
        else:
            if merge[1] >= i[0]-1: merge[1] = i[1]
            else: 
                output.append(merge)
                output.append(i)
                flag = True
    return output
