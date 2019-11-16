import csp
import backtracking as bt
import time

if __name__ == "__main__":
    f1 = open("../data/easy.txt", "r")
    f2 = open("../data/hard.txt", "r")

    easy = f1.readlines()
    hard = f2.readlines()

    print("Benching with easy test cases for [csp], [bt]:")
    print("[Heurestics]")
    csp_time = 0.0
    bt_time = 0.0
    for t in easy:
        start = time.time()
        csp.main(t)
        end = time.time()
        csp_time += (end-start)
        
    print("Total time [csp]:", csp_time)
    print("Average time [csp]:", csp_time/len(easy))

    csp_time = 0.0
    bt_time = 0.0
    for t in easy:
        start = time.time()        
        bt.main(t)
        end = time.time()
        bt_time += (end-start)

    print("Total time [bt]:", bt_time)
    print("Average time [bt]:", bt_time/len(easy))

    print("Benching with hard test cases for [csp], [bt]:")
    print("[Heurestics]")
    csp_time = 0.0
    bt_time = 0.0
    for t in hard:
        start = time.time()
        csp.main(t)
        end = time.time()
        csp_time += (end-start)

    print("Total time [csp]:", csp_time)
    print("Average time [csp]:", csp_time/len(hard))

    csp_time = 0.0
    bt_time = 0.0
    for t in hard:
        start = time.time() 
        bt.main(t)
        end = time.time()
        bt_time += (end-start)

    print("Total time [bt]:", bt_time)
    print("Average time [bt]:", bt_time/len(hard))