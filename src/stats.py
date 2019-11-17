import statistics

f_csp_h = open("../src/csp_h.txt", "r")
f_bt_h = open("../src/bt_h.txt", "r")

csp = f_csp_h.readlines()
bt = f_bt_h.readlines()

#csp hard testcases
csp_list_h = []
for t in csp:
    csp_list_h.append(t)
csp_list_h = [i.replace('\n','') for i in csp_list_h]
csp_list_h = [float(i) for i in csp_list_h]

#bt hard cases
bt_list_h= []
for t in bt:
    bt_list_h.append(t)
bt_list_h = [i.replace('\n','') for i in bt_list_h]
bt_list_h = [float(i) for i in bt_list_h]