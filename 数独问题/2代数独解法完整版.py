import sd_function as sd

llnum = sd.get_input()
lllnum = sd.divide_llnum(llnum)

total = sd.count(lllnum)
print("共有{}个空格，".format(total))
lllnum,num_judge_dic = sd.start_work(lllnum)
remain_empty = sd.count(lllnum)
print("已解出{}个，还剩{}个".format(total - remain_empty,remain_empty))
print("解答如下：")
temp_result = sd.return_back(lllnum)
sd.print_result(temp_result)

end = False
while sd.count(lllnum) >= 5 and not end: # 若盘面存在空格，判断空格数量是否大于等于5,若满足该条件则进入猜测环节
    
    print("进入猜测环节：")

    # 确定可能需要的最多猜测轮次
    total_round = sd.count(lllnum) // 5
    temp_appear_lllnum = [[] for i in range(total_round)] # 创建列表，记录每一轮猜测结束后得到的盘面
    guessing_empty_infor2 = [0 for i in range(total_round)] # 创建2号断点列表，储存相邻轮次间的2号断点信息（满足条件的可能）索引
    guessing_empty_infor1 = [] # 创建1号断点列表，储存各轮次的1号断点信息（空格坐标+参数列表），元素为字典（格式 空格坐标：参数列表）
    
    #筛选各轮猜测所用的空格，每轮5个，元素类型为列表
    total_empty_position = list(num_judge_dic.keys()) 
    total_empty_position.sort(key = lambda x :len(num_judge_dic[x])) # 得到所有空格的坐标，并按照参数列表长度排列
    for roud in range(total_round):
        empty_position_guess_dic = {}
        for i in range(roud * 5,roud * 5 + 5):
            empty_position_guess_dic[total_empty_position[i]] = num_judge_dic[total_empty_position[i]]
        guessing_empty_infor1.append(empty_position_guess_dic) # 得到各轮猜测所用的每组5个空格以及相应的参数列表
    
    # 确定各轮猜测所有可能的猜测结果
    all_posis = [] # 储存各轮猜测所有可能猜测结果的列表，元素为单轮猜测所有可能结果的列表（元素为字典，格式为空格坐标：猜测数，包含5个键值对）
    for dicinfor in guessing_empty_infor1:
        single_all_posis = [] # 储存单轮猜测所有可能的列表,元素为字典（格式 空格坐标：猜测数）
        empty_position_guess_list = list(dicinfor.keys())
        for guess_num0 in num_judge_dic[empty_position_guess_list[0]]:
            for guess_num1 in num_judge_dic[empty_position_guess_list[1]]:
                for guess_num2 in num_judge_dic[empty_position_guess_list[2]]:
                    for guess_num3 in num_judge_dic[empty_position_guess_list[3]]:
                        for guess_num4 in num_judge_dic[empty_position_guess_list[4]]:
                            empty_num_dic = {}
                            empty_num_dic[empty_position_guess_list[0]] = guess_num0
                            empty_num_dic[empty_position_guess_list[1]] = guess_num1
                            empty_num_dic[empty_position_guess_list[2]] = guess_num2
                            empty_num_dic[empty_position_guess_list[3]] = guess_num3
                            empty_num_dic[empty_position_guess_list[4]] = guess_num4
                            single_all_posis.append(empty_num_dic)
        all_posis.append(single_all_posis)
 
    work_time = 0
    end = False
    judge = True
    while True:
        
        if judge:
            work_time += 1
            print("进入第{}轮猜测：".format(work_time))
            
            lllnum,end_point,judge = sd.single_guess1(lllnum,all_posis[work_time - 1])
            
            if judge:
                temp_appear_lllnum[work_time - 1] = lllnum
                guessing_empty_infor2[work_time - 1] = end_point
           
        else:
            work_time -= 1
            print("进入第{}轮猜测：".format(work_time))
           
            lllnum,end_point,judge = sd.single_guess2(temp_appear_lllnum[work_time - 1], guessing_empty_infor2[work_time - 1],all_posis[work_time - 1])
        
            if judge:
                temp_appear_lllnum[work_time - 1] = lllnum
                guessing_empty_infor2[work_time - 1] = end_point
      
        if judge:
            temp_lllnum,num_judge_dic = sd.start_work(sd.copy_lllnum(lllnum))              
            if not sd.judge_empty(temp_lllnum):
                print("猜测完成！")
                result = sd.return_back(temp_lllnum)
                print("解答如下：")
                sd.print_result(result)
                end = True
                break





































