import statistics

f_csp_h = open("../data/csp_h.txt", "r")
f_bt_h = open("../data/bt_h.txt", "r")

f_csp_e = open("../data/csp_e.txt", "r")
f_bt_e = open("../data/bt_e.txt", "r")

f_csp_ex = open("../data/csp_ex.txt", "r")


csp = f_csp_h.readlines()
bt = f_bt_h.readlines()
csp_e = f_csp_e.readlines()
bt_e = f_bt_e.readlines()
csp_ex = f_csp_ex.readlines()

#csp hard testcases
csp_list_h = []
for t in csp:
    csp_list_h.append(t)
csp_list_h = [i.replace('\n','') for i in csp_list_h]
csp_list_h = [float(i) for i in csp_list_h]

mean1 = statistics.mean(csp_list_h)
var1 = statistics.variance(csp_list_h)
print ("\nVariance of csp hard test cases is :", var1)
print("Mean of csp hard test cases is: ",mean1)
#bt hard cases
bt_list_h= []
for t in bt:
    bt_list_h.append(t)
bt_list_h = [i.replace('\n','') for i in bt_list_h]
bt_list_h = [float(i) for i in bt_list_h]

mean2 = statistics.mean(bt_list_h)
var2= statistics.variance(bt_list_h)
print ("\nVariance of bt hard test cases is :", var2)
print("Mean of bt hard test cases is: ",mean2)


#csp easy testcases
csp_list_e = []
for t in csp_e:
    csp_list_e.append(t)
csp_list_e = [i.replace('\n','') for i in csp_list_e]
csp_list_e = [float(i) for i in csp_list_e]

mean3 = statistics.mean(csp_list_e)
var3 = statistics.variance(csp_list_e)
print ("\nVariance of csp easy test cases is :", var3)
print("Mean of csp hard easy cases is: ",mean3)

#bt easy cases
bt_list_e= []
for t in bt_e:
    bt_list_e.append(t)
bt_list_e = [i.replace('\n','') for i in bt_list_e]
bt_list_e = [float(i) for i in bt_list_e]
print("\n")
mean4 = statistics.mean(bt_list_e)
var4= statistics.variance(bt_list_e)
print ("\nVariance of bt easy test cases is :", var4)
print("Mean of bt easy test cases is: ",mean4)


#csp extreme testcases
csp_list_ex = []
for t in csp_ex:
    csp_list_ex.append(t)
csp_list_ex = [i.replace('\n','') for i in csp_list_ex]
csp_list_ex = [float(i) for i in csp_list_ex]

mean5 = statistics.mean(csp_list_ex)
var5 = statistics.variance(csp_list_ex)
print ("\nVariance of csp extreme test cases is :", var5)
print("Mean of csp extreme test cases is: ",mean5)
