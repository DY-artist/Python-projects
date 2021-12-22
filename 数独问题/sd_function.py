# 计算空格总数
def count(lllnum):
    empty_count = 0
    for units in range(3):
        for unit in range(3):
            for line in range(3):
                for x in range(3):
                    if lllnum[units][unit][line][x] == 0:
                        empty_count += 1
    return empty_count

#分组，返回嵌套列表
def divide_llnum(llnum):    
    lllnum = []  
    for i in range(0,9,3):
        units = []
        for j in range(0,9,3):
            unit = [llnum[l][j:j + 3] for l in range(i,i + 3)]
            units.append(unit)
        lllnum.append(units)
    return lllnum

#判断数独矩阵是否存在空格,若存在返回True
def judge_empty(lllnum):
    for units in range(3):
        for unit in range(3):
            for line in range(3):
                for x in range(3):
                    if lllnum[units][unit][line][x] == 0:
                        return True 
    else:
        return False

#判断每一宫是否为空（空格数为0返回False，为1自动填充后返回False,其他情况返回True）
def judge_unit_empty(j_unit):
    count = 0 
    for line in range(3):
        for x in range(3):
            if j_unit[line][x] == 0:
                count += 1
    if count == 0:
        return False
    elif count == 1:
        numlst = []
        for line in range(3):
            for x in range(3):
                if j_unit[line][x] != 0:
                    numlst.append(j_unit[line][x])
                else:
                    empty_position = (x,line)
        for num in range(1,10):
            if num not in numlst:
                j_unit[empty_position[1]][empty_position[0]] = num
        return False      
    else:
        return True
      
#恢复至原始数独矩阵
def return_back(llllnum4):
    result_llnum = []  
    for units in range(3):      
        for line in range(3):
            numline = []
            for unit in range(3):
                numline += llllnum4[units][unit][line]
            result_llnum.append(numline)
    return result_llnum

#一次接受所有输入，整体输入数独矩阵，返回初级加工后的矩阵
def get_input():
    print("请输入数独矩阵（空格用0代替）：")
    nums = []
    for num in iter(input()):
        nums.append(num)
    
    while "\n" in nums:
        nums.remove("\n")
    
    for i in range(81):
        nums[i] = int(nums[i])
        
    llnum = []
    for i in range(0,81,9):
        lnum = []
        for j in range(i,i + 9):
            lnum.append(nums[j])
        llnum.append(lnum)
    return llnum

#数独算法1
def get_all_result(lllnum):
    for units in range(3):
        for u in range(3):
            for line in range(3):
                for x in range(3):
                    if lllnum[units][u][line][x] == 0:
                        judgelst = []
                        for l in range(3): 
                            judgelst += lllnum[units][u][l]
                        for un in range(3):
                            judgelst += lllnum[units][un][line]
                        for uni in range(3):
                            judgelst += [lllnum[uni][u][line][x]]
                        judgeset = set(judgelst)
                        judgeset.remove(0)
                        if len(judgeset) == 8:
                            for num in range(1,10):
                                if num not in judgeset:
                                    lllnum[units][u][line][x] = num
    return lllnum
    
#数独算法2
def judge_lines(lllnum):
    for units in range(3):
        for unit in range(3):
            if judge_unit_empty(lllnum[units][unit]):
                position_list = [] #储存空格位置坐标的列表
                for line in range(3):
                    for x in range(3):
                        if lllnum[units][unit][line][x] == 0:
                            position_list.append((x,line)) #得到当前宫中所有空格的位置坐标
                numlst = [] #储存当前宫中的所有数字，包括0（空格）
                judge_numlst = [] #储存当前宫中未确定的，未出现的数字
                for line in range(3):
                    for x in range(3):
                        numlst.append(lllnum[units][unit][line][x])
                for num in range(1,10):
                    if num not in numlst:
                        judge_numlst.append(num) #得到当前宫中数字1~9还未出现的数字 
                for judge_num in judge_numlst: #依次对未出现的数字进行判断
                    temp_position_list = position_list[:] #复制储存当前宫所有空格位置坐标的列表，临时列表
                    #遍历该临时列表，依次对每个空格进行判断，不符要求的剔除临时列表
                    for position in position_list:
                        #遍历空格所在行，不满足要求的剔除筛选列表
                        judge_numlines = [] #储存当前空格所在行的所有数字，包括0
                        for u in range(3):                           
                            judge_numlines += lllnum[units][u][position[1]]
                        for judge_line_num in judge_numlines:
                            if judge_line_num == judge_num:
                                temp_position_list.remove(position)
                                break
                                                            
                        #遍历空格所在列，不满足要求的剔除筛选列表
                        judge_numlines = []
                        for us in range(3):
                            for l in range(3):
                                judge_numlines.append(lllnum[us][unit][l][position[0]])
                        for judge_line_num in judge_numlines:
                            if judge_line_num == judge_num:
                                if position in temp_position_list:
                                    temp_position_list.remove(position)
                    #对每个空格判断完毕后，根据临时列表剩余元素情况决定是否做出更改，（仅当列表长度为一时）
                    if len(temp_position_list) == 1:
                        lllnum[units][unit][temp_position_list[0][1]][temp_position_list[0][0]] = judge_num
                        position_list.remove(temp_position_list[0]) #确定一个空格中的数字后，对储存当前宫空格位置坐标的列表进行更新
    return lllnum

#数独算法3
def get_lastone(lllnum):
    #遍历每一宫
    for units in range(3):
        for unit in range(3):
            count = 0
            for line in range(3):
                for x in range(3):
                    if lllnum[units][unit][line][x] == 0:
                        count += 1
            if count == 1:
                numlst = []
                for line in range(3):
                    for x in range(3):
                        if lllnum[units][unit][line][x] != 0:
                            numlst.append(lllnum[units][unit][line][x])
                        else:
                            last_empty_position = (x,line)
                for num in range(1,10):
                    if num not in numlst:
                        lllnum[units][unit][last_empty_position[1]][last_empty_position[0]] = num   
    #遍历每一行
    for units in range(3):
        for line in range(3):
            count = 0
            for unit in range(3):
                for x in range(3):
                    if lllnum[units][unit][line][x] == 0:
                        count += 1
            if count == 1:
                numlst = []
                for unit in range(3):
                    for x in range(3):
                        if lllnum[units][unit][line][x] != 0:
                            numlst.append(lllnum[units][unit][line][x])
                        else:
                            last_empty_position = (x,unit)
                for num in range(1,10):
                    if num not in numlst:
                        lllnum[units][last_empty_position[1]][line][last_empty_position[0]] = num                        
    #遍历每一列
    for unit in range(3):
        for x in range(3):
            count = 0
            for units in range(3):
                for line in range(3):
                    if lllnum[units][unit][line][x] == 0:
                        count += 1
            if count == 1:
                numlst = []
                for units in range(3):
                    for line in range(3):
                        if lllnum[units][unit][line][x] != 0:
                            numlst.append(lllnum[units][unit][line][x])
                        else:
                            last_empty_position = (units,line)
                for num in range(1,10):
                    if num not in numlst:
                        lllnum[last_empty_position[0]][unit][last_empty_position[1]][x] = num
    return lllnum

#整合3种数独算法
def together(lllnum0):
    count_empty = 0
    old_count_empty = 0
    while judge_empty(lllnum0):      
        old_count_empty = count_empty
        
        lllnum1 = judge_lines(lllnum0)
        lllnum2 = get_all_result(lllnum1)
        lllnum3 = get_lastone(lllnum2)
        lllnum0 = lllnum3
        
        temp_result = return_back(lllnum0)
        count_empty = count(temp_result)
        if count_empty == old_count_empty:
            break
    return temp_result

#按照完整格式打印结果
def print_result(result):
    print("-------------------------")
    for i in range(0,9,3):
        for line in range(i,i + 3):
            print("|",end = " ")
            for j in range(0,9,3):
                
                for x in range(j,j + 3):
                    print(result[line][x],end = " ")
                print("|",end = " ")
            print()
        print("-------------------------")
        
# 格式反向转换并打印
def change_reverse():
    pri_input = [] 
    for x in iter(input()):
        pri_input.append(x)
    
    for sign in '-| ':
        while sign in pri_input:
            pri_input.remove(sign)
    
    while '\n' in pri_input:
        pri_input.remove('\n')
    
    for i in range(81):
        pri_input[i] = int(pri_input[i])
    
    nums_list = []
    for line in range(0,80,9):
        lnum = []
        for x in range(line,line + 9):
            lnum.append(pri_input[x])
        nums_list.append(lnum)
        
    for line in nums_list:
        for num in line:
            print(num,end = "")
        print()


###############################################################################

#遍历数独矩阵，为每个空格重置待选数列表,并返回统计字典
def empty_reset(lllnum):
    numlst = [i for i in range(1,10)]
    dicnums = {}
    
    empty_positions = []
    for units in range(3):
        for unit in range(3):
            for line in range(3):
                for x in range(3):
                    if lllnum[units][unit][line][x] == 0:
                        empty_positions.append((units,unit,line,x))
    for position in empty_positions:
        dicnums[position] = numlst[:]
    return dicnums

#2代数独算法1.1
def first_judge1(lllnum):
    num_judge_dic = empty_reset(lllnum)  
    #遍历每一宫
    for units in range(3):
        for unit in range(3):
            if judge_unit_empty(lllnum[units][unit]):
                remove_nums = []
                empty_positions = []
                for line in range(3):
                    for x in range(3):
                        if lllnum[units][unit][line][x] != 0:
                            remove_nums.append(lllnum[units][unit][line][x])
                        else:
                            empty_positions.append((units,unit,line,x))
                for position in empty_positions:
                    for remove_num in remove_nums:
                        if remove_num in num_judge_dic[position]:
                            num_judge_dic[position].remove(remove_num)                       
    #遍历每一行
    for units in range(3):
        for line in range(3):            
            empty_count = 0
            for unit in range(3):
                for x in range(3):
                    if lllnum[units][unit][line][x] == 0:
                        empty_count += 1
            if empty_count != 0:
                if empty_count == 1:
                    numlst = []
                    for unit in range(3):
                        for x in range(3):
                            if lllnum[units][unit][line][x] != 0:
                                numlst.append(lllnum[units][unit][line][x])
                            else:
                                empty_position = (x,unit)
                    for num in range(1,10):
                        if num not in numlst:
                            lllnum[units][empty_position[1]][line][empty_position[0]] = num
                else:
                    remove_nums = []
                    empty_positions = []
                    for unit in range(3):
                        for x in range(3):
                            if lllnum[units][unit][line][x] != 0:
                                remove_nums.append(lllnum[units][unit][line][x])
                            else:
                                empty_positions.append((units,unit,line,x))
                    for position in empty_positions:
                        for remove_num in remove_nums:
                            if remove_num in num_judge_dic[position]:
                                num_judge_dic[position].remove(remove_num)   
    # 遍历每一列
    for unit in range(3):
        for x in range(3):
            empty_count = 0
            for units in range(3):
                for line in range(3):
                    if lllnum[units][unit][line][x] == 0:
                        empty_count += 1
            if empty_count != 0:
                if empty_count == 1:
                    numlst = []
                    for units in range(3):
                        for line in range(3):
                            if lllnum[units][unit][line][x] != 0:
                                numlst.append(lllnum[units][unit][line][x])
                            else:
                                empty_position = (units,line)
                    for num in range(1,10):
                        if num not in numlst:
                            lllnum[empty_position[0]][unit][empty_position[1]][x] = num
                else:
                    remove_nums = []
                    empty_positions = []
                    for units in range(3):
                        for line in range(3):
                            if lllnum[units][unit][line][x] != 0:
                                remove_nums.append(lllnum[units][unit][line][x])
                            else:
                                empty_positions.append((units,unit,line,x))
                    for position in empty_positions:
                        for remove_num in remove_nums:
                            if remove_num in num_judge_dic[position]:
                               num_judge_dic[position].remove(remove_num)
    return lllnum,num_judge_dic
            
# 2代数独算法1
def first_judge(lllnum):
    num_judge_dic = empty_reset(lllnum)
    for k,v in num_judge_dic.items():
        remove_nums = []
        for line in range(3):
            remove_nums += lllnum[k[0]][k[1]][line]
        for unit in range(3):
            remove_nums += lllnum[k[0]][unit][k[2]]
        for units in range(3):
            for line in range(3):              
                remove_nums.append(lllnum[units][k[1]][line][k[3]])
        remove_nums_set = set(remove_nums)
        remove_nums_set.remove(0)
        for remove_num in remove_nums:
            if remove_num in v:
                v.remove(remove_num)
    return num_judge_dic

#简单填充函数
def simple_fill_lllnum(lllnum,num_judge_dic):
    num_judge_dic_copy = num_judge_dic.copy()
    for k,v in num_judge_dic.items():
            if len(v) == 1:
                lllnum[k[0]][k[1]][k[2]][k[3]] = v[0]
                del num_judge_dic_copy[k]
    return lllnum,num_judge_dic_copy

#检查字典，填补满足条件的空格
def fill_lllnum(lllnum,num_judge_dic):
    for k,v in num_judge_dic.items():
        if len(v) == 1:
            lllnum[k[0]][k[1]][k[2]][k[3]] = v[0]
            
    # 检查每一宫、每一行和每一列中空格对应的待选数列表中仅出现过一次的数并填补上去     
    #检查每一宫
    for judge_num in range(1,10):
        for units in range(3):
            for unit in range(3):
                appear_count = 0
                for k,v in num_judge_dic.items():
                    if k[0] == units and k[1] == unit:
                        if judge_num in v:
                            appear_count += 1
                            appear_position = k
                if appear_count == 1:
                    lllnum[appear_position[0]][appear_position[1]][appear_position[2]][appear_position[3]] = judge_num
    # 检查每一行
    for judge_num in range(1,10):
        for units in range(3):
            for line in range(3):
                appear_count = 0
                for k,v in num_judge_dic.items():
                    if k[0] == units and k[2] == line:
                        if judge_num in v:
                            appear_count += 1
                            appear_position = k
                if appear_count == 1:
                    lllnum[appear_position[0]][appear_position[1]][appear_position[2]][appear_position[3]] = judge_num
    # 检查每一列
    for judge_num in range(1,10):
        for unit in range(3):
            for x in range(3):
                appear_count = 0
                for k,v in num_judge_dic.items():
                    if k[1] == unit and k[3] == x:
                        if judge_num in v:
                            appear_count += 1
                            appear_position = k
                if appear_count == 1:
                    lllnum[appear_position[0]][appear_position[1]][appear_position[2]][appear_position[3]] = judge_num
                   
    return lllnum

# 2代数独算法2
def second_judge(num_judge_dic):
    for judge_num in range(1,10):
        for units in range(3):
            for unit in range(3):
                for k,v in num_judge_dic.items():
                    if k[0] == units and k[1] == unit:
                        if judge_num in v:
                            judge_line = k[2]
                            judge_x = k[3]
                            break
                judge_1 = True
                for k,v in num_judge_dic.items():
                    if k[0] == units and k[1] == unit:
                        if judge_num in v:
                            if k[2] != judge_line:
                                judge_1 = False
                judge_2 = True
                for k,v in num_judge_dic.items():
                    if k[0] == units and k[1] == unit:
                        if judge_num in v:
                            if k[3] != judge_x:
                                judge_2 = False
                if judge_1 and not judge_2:
                    for k,v in num_judge_dic.items():
                        if k[0] == units and k[2] == judge_line:
                            if k[0] != units or k[1] != unit:
                                if judge_num in v:
                                    v.remove(judge_num)                                                                 
                elif not judge_1 and judge_2:
                    for k,v in num_judge_dic.items():
                        if k[1] == unit and k[3] == judge_x:
                            if k[0] != units or k[1] != unit:
                                if judge_num in v:
                                    v.remove(judge_num)
    return num_judge_dic
                    
# 2代数独算法3
def third_judge(num_judge_dic):
    # 遍历每一宫
    for units in range(3):
        for unit in range(3):
            selecting_list = []
            for k,v in num_judge_dic.items():              
                if k[0] == units and k[1] == unit:
                    selecting_list.append(v)
            for judge_lst in selecting_list:
                lst_count = 0
                for lst in selecting_list:
                    if lst == judge_lst:
                        lst_count += 1
                if lst_count >= 2 and len(judge_lst) == lst_count:
                    for k,v in num_judge_dic.items():
                        if k[0] == units and k[1] == unit:
                            if v != judge_lst:
                                for remove_num in judge_lst:
                                    if remove_num in v:
                                        v.remove(remove_num)
    # 遍历每一行
    for units in range(3):
        for line in range(3):
            selecting_list = []
            for k,v in num_judge_dic.items():
                if k[0] == units and k[2] == line:
                    selecting_list.append(v)
            for judge_lst in selecting_list:
                lst_count = 0
                for lst in selecting_list:
                    if lst == judge_lst:
                        lst_count += 1
                if lst_count >= 2 and len(judge_lst) == lst_count:
                    for k,v in num_judge_dic.items():
                        if k[0] == units and k[2] == line:
                            if v != judge_lst:
                                for remove_num in judge_lst:
                                    if remove_num in v:
                                        v.remove(remove_num)
    # 遍历每一列
    for unit in range(3):
        for x in range(3):
            selecting_list = []
            for k,v in num_judge_dic.items():
                if k[1] == unit and k[3] == x:
                    selecting_list.append(v)
            for judge_lst in selecting_list:
                lst_count = 0
                for lst in selecting_list:
                    if lst == judge_lst:
                        lst_count += 1
                if lst_count >= 2 and len(judge_lst) == lst_count:
                    for k,v in num_judge_dic.items():
                        if k[1] == unit and k[3] == x:
                            if v != judge_lst:
                                for remove_num in judge_lst:
                                    if remove_num in v:
                                        v.remove(remove_num)
    return num_judge_dic                   
                        
#判断数独矩阵是否合法
def judge_right(lllnum):
    # 判断每一宫
    for units in range(3):
        for unit in range(3):          
            num_list = []
            for line in range(3):
                for x in range(3):
                    num_list.append(lllnum[units][unit][line][x])           
            for judge_num in range(1,10):
                if num_list.count(judge_num) >= 2:
                    return False  
    # 判断每一行
    for units in range(3):
        for line in range(3):
            num_list = []
            for unit in range(3):
                for x in range(3):
                    num_list.append(lllnum[units][unit][line][x])
            for judge_num in range(1,10):
                if num_list.count(judge_num) >= 2:
                    return False   
    # 判断每一列
    for unit in range(3):
        for x in range(3):           
            num_list = []
            for units in range(3):
                for line in range(3):
                    num_list.append(lllnum[units][unit][line][x])        
            for judge_num in range(1,10):
                if num_list.count(judge_num) >= 2:
                    return False                       
    return True          
                        
# 整合2代各算法
def start_work(lllnum):
    empty_count = 0
    old_empty_count = 1
    num_judge_dic = {}
    work_times = 0
    while judge_empty(lllnum) and work_times <= 10:
        empty_count = count(lllnum)
        old_empty_count = empty_count
        
        num_judge_dic = first_judge(lllnum)
        num_judge_dic = second_judge(num_judge_dic)
        num_judge_dic = third_judge(num_judge_dic)
        lllnum = fill_lllnum(lllnum, num_judge_dic)
        empty_count = count(lllnum)
        
        if empty_count == old_empty_count:
            work_times += 1
    return lllnum,num_judge_dic                      
                        
# 复制三级列表
def copy_lllnum(lllnum0):
    lnum = [0 for i in range(9)]
    llnum = [lnum for i in range(9)]
    lllnum = divide_llnum(llnum)
    for units in range(3):
        for unit in range(3):
            for line in range(3):
                for x in range(3):
                    lllnum[units][unit][line][x] = lllnum0[units][unit][line][x]  
    return lllnum

#==================================================

#正常单轮猜测算法
# 传入盘面和所有可能
def single_guess1(lllnum,total_posis):
    judge = True

    # 循环进行多次猜测
    guess_time = 0
    while True:
       
        if guess_time == len(total_posis):
            print("需要返回上一轮猜测！") 
            print("============================")
            r_lllnum = []                       
            r_enter_point = 0 
            judge = False
            break
            
        lllnum_s = copy_lllnum(lllnum) # 重置盘面
        
        # 根据猜测结果得到数独盘面
        empty_position_guess_dic = total_posis[guess_time]
        
        for k,v in empty_position_guess_dic.items():
            lllnum_s[k[0]][k[1]][k[2]][k[3]] = v
            
        if not judge_right(lllnum_s): # 对经过猜测的盘面进行审查是否合法，不合法直接进入下一次猜测
            guess_time += 1
            continue
            
        lllnum_judge,num_dicinfor_judge = start_work(copy_lllnum(lllnum_s)) # 传入数独盘面，运行一轮计算，得到计算后的盘面和待选数统计字典
            
        if judge_right(lllnum_judge): # 对经过猜测并计算后的盘面进行审查，判断盘面是否合法（允许包含空格）
            if judge_empty(lllnum_judge): # 判断盘面是否存在空格
                # 盘面合法且仍存在一定数量的空格，说明需要进入第二轮猜测
                if count(lllnum_judge) >= 5:
                    print("第{}次猜测成功！".format(guess_time + 1))
                    print("需要进入下一轮猜测！")
                    r_lllnum = lllnum_s                 
                    r_enter_point = total_posis.index(empty_position_guess_dic)
                    break
                else:
                    guess_time += 1
                    continue
            else:
                print("第{}次猜测成功！".format(guess_time + 1))
                r_lllnum = lllnum_s
                r_enter_point = total_posis.index(empty_position_guess_dic)
                break # 盘面合法但不存在空格，说明数独已完成
        else:
            guess_time += 1
            continue # 盘面不合法，此次猜测失败，进行下一次猜测        
    
    return r_lllnum,r_enter_point,judge
                        
# 返回上一轮的猜测算法
def single_guess2(lllnum,enter_point,total_posis):
    
    judge = True
    
    # 从断点后开始循环进行多次猜测
    guess_time = enter_point + 1
    while True:
        
        if guess_time == len(total_posis):
            print("需要返回上一轮猜测！")
            print("============================")
            r_lllnum = []
            r_enter_point = 0
            judge = False
            break
    
        lllnum_s = copy_lllnum(lllnum) # 重置盘面
        
        
        # 根据猜测结果得到数独盘面
        empty_position_guess_dic = total_posis[guess_time]
        
        for k,v in empty_position_guess_dic.items():
            lllnum_s[k[0]][k[1]][k[2]][k[3]] = v
        
        if not judge_right(lllnum_s): # 对经过猜测的盘面进行审查是否合法，不合法直接进入下一次猜测
            guess_time += 1
            continue
        
        lllnum_judge,num_dicinfor_judge = start_work(copy_lllnum(lllnum_s)) # 传入数独盘面，运行一轮计算，得到计算后的盘面和待选数统计字典
            
        if judge_right(lllnum_judge): # 对经过猜测并计算后的盘面进行审查，判断盘面是否合法（允许包含空格）
            if judge_empty(lllnum_judge): # 判断盘面是否存在空格
                # 盘面合法且仍存在一定数量的空格，说明需要进入第二轮猜测
                if count(lllnum_judge) >= 5:
                    print("第{}次猜测成功！".format(guess_time + 1))
                    print("需要进入下一轮猜测！")
                    r_lllnum = lllnum_s
                    r_enter_point = total_posis.index(empty_position_guess_dic)
                    break
                else:
                    guess_time += 1
                    continue
            else:
                print("第{}次猜测成功！".format(guess_time + 1))
                r_lllnum = lllnum_s
                r_enter_point = total_posis.index(empty_position_guess_dic)
                break # 盘面合法但不存在空格，说明数独已完成
        else:
            guess_time += 1
            continue # 盘面不合法，此次猜测失败，进行下一次猜测        
    
    return r_lllnum,r_enter_point,judge           

                        
                        
                        
                        
                        
                        
                        
                        
















