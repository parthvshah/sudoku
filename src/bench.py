import csp
import genetic as gen
import backtracking as bt
import time

if __name__ == "__main__":
    f1 = open("../data/easy.txt", "r")
    f2 = open("../data/hard.txt", "r")
    f3 = open("../data/extreme.txt", "r")

    easy = f1.readlines()
    hard = f2.readlines()
    extreme = f3.readlines()

    print("Benching with easy test cases for [csp], [gen], [bt]:")
    print("[Heurestics]")
    
    csp_time = 0.0
    for t in easy:
        csp_time = 0.0 
        start = time.time()
        csp.main(t)
        end = time.time()
        csp_time += (end-start)
        # print(csp_time)

    print("Total time [csp]:", csp_time)
    print("Average time [csp]:", csp_time/len(easy))

    # gen_time = 0.0
    # for t in easy:
    #     start = time.time()        
    #     gen.main(t)
    #     end = time.time()
    #     gen_time += (end-start)

    # print("Total time [gen]:", gen_time)
    # print("Average time [gen]:", gen_time/len(easy))

    bt_time = 0.0
    for t in easy:
        bt_time =0.0
        start = time.time()        
        bt.main(t)
        end = time.time()
        bt_time += (end-start)
        # print(bt_time)

    print("Total time [bt]:", bt_time)
    print("Average time [bt]:", bt_time/len(easy))

    print("Benching with hard test cases for [csp], [bt]:")
    print("[Heurestics]")
    csp_time = 0.0
    # sum =0.0
    for t in hard:
        # csp_time =0.0
        start = time.time()
        csp.main(t)
        end = time.time()
        csp_time += (end-start)
        # sum += csp_time
        # print(csp_time)

    print("Total time [csp]:", csp_time)
    print("Average time [csp]:", csp_time/len(hard))

    bt_time = 0.0
    # sum = 0.0
    for t in hard:
    #   bt_time = 0.0
        start = time.time() 
        bt.main(t)
        end = time.time()
        bt_time += (end-start)
    #     sum += bt_time
    #     print(bt_time)

    print("Total time [bt]:", bt_time)
    print("Average time [bt]:", bt_time/len(hard))

    
    print("Benching with extreme test cases for [csp]:")
    # csp_time = 0.0
    # sum =0.0
    for t in extreme:
        csp_time =0.0
        start = time.time()
        csp.main(t)
        end = time.time()
        csp_time += (end-start)
        print(csp_time)

    