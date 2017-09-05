old_dict = {
    "#1":{ 'hostname': 'c1', 'cpu_count': 2, 'mem_capicity': 80 },
    "#2":{ 'hostname': 'c1', 'cpu_count': 2, 'mem_capicity': 80 },
    "#3":{ 'hostname': 'c1', 'cpu_count': 2, 'mem_capicity': 80 }
}

new_dict = {
    "#1":{ 'hostname': 'c1', 'cpu_count': 2, 'mem_capicity': 800 },
    "#3":{ 'hostname': 'c1', 'cpu_count': 2, 'mem_capicity': 80 },
    "#4":{ 'hostname': 'c1', 'cpu_count': 2, 'mem_capicity': 80 }
}

old_set = set(old_dict.keys())

update_list = list(old_set.intersection(new_dict.keys()))

new_list = []
del_list = []


for i in new_dict.keys():
    if i not in update_list:
        new_list.append(i)

for i in old_dict.keys():
    if i not in update_list:
        del_list.append(i)

print update_list,new_list,del_list




