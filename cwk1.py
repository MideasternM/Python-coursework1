"""
Introduction to Programming Coursework 1

@author: Shuyu Cao 2022116049
"""


def valid_puzzle(puzzle: list) -> bool:
    length=[0]*len(puzzle)
    if type(puzzle) is not list:
        return False
    else:
        length[0]=len(puzzle[0])
        if type(puzzle[0]) is not str:
            return False
        for i in range(1,len(puzzle)):
            if type(puzzle[i]) is not str:
                return False
            else:
                length[i]=len(puzzle[i])
                if length[i-1]!=length[i]:
                    return False
        return True

def similarity_grouping(data: list) -> list:
    group=[[0]]
    group[0][0]=data[0]
    for i in range(1,len(data)):
        cnt=0
        for n in range(len(group)):
            if data[i]==group[n][0]:
                group[n].append(data[i])
                break
            else:
                cnt+=1
                if cnt==len(group):
                    group.append([data[i]])
    return group

def highest_count_items(data: str) -> list:
    times=len(data)
    if times>500:
        times+=5
    for i in range(times):
        if data[i]==",":
            if data[i+1]!=" ":
                data=data[:i+1]+" "+data[i+1:]
    items=data.split(', ')
    dic1={}
    for i in range(len(items)):
        if items[i] in dic1:
            dic1[items[i]]+=1
        else:
            dic1[items[i]]=1
    max_value=max(dic1.values())
    list1=[]
    for k,v in dic1.items():
        if v==max_value:
            list1.append([k,v])
    return list1

    


def valid_char_in_string(popList: list, charSet: list) -> bool:
    if type(charSet) is not list:
        return False
    for i in range(len(charSet)):
        if len(charSet[i])!=1:
            return False
        elif type(charSet[i]) is not str:
            return False
    for i in range(len(popList)):
        for n in range(len(popList[0])):
            if popList[i][n] not in charSet:
                return False
    return True


def total_price(unit: int) -> float:
    if type(unit) is not int:
        return 0
    if unit>6:
        packs=unit/6
        packs1=int(packs)
        single=unit-6*packs1
        price=5*packs1+1.25*single
    else:
        single=unit%6
        price=1.25*single
    if price>20:
        price=price*0.9
    return price



if __name__ == "__main__":
    # sample test for task 1.1
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    puzzle2 = ['NAROUNDDL', 'EDCIT', 'UWSWEDZYA', 'OTCONVOYV',
               'BOSEVRUCI', 'BLLCGLPBD', 'TEENAGEDL', 'TREWZLCGY',
               'RAPLEBAYG', 'ATYTBIWRA', 'YEMROFINU']

    puzzle3 = ['RUNAROU', ['EDCITOA'], ('ZYUWSWE'), 'AKOTCYV',
               'LSBOSEI', 'BOBLLCG', 'LKTEENA', 'ISTREWY',
               'AURAPLE', 'RDATYTB', 'TEYEMRO']
    puzzle4 = 'roundandround'
    print(valid_puzzle(puzzle1))
    print(valid_puzzle(puzzle2))
    print(valid_puzzle(puzzle3))
    print(valid_puzzle(puzzle4))

    # sample test for task 1.2
    data1 = [2, 1, 2, 1]
    data2 = [5, 4, 5, 5, 4, 3]
    data3 = [1, 2, 1, 3, 'a', 'b', "a",  'c']
    print(similarity_grouping(data1))
    print(similarity_grouping(data2))
    print(similarity_grouping(data3))

    # sample test for task 1.3
    data4 = ("3, 13, 7, 9, 3, 3, 5, 7, 12, 13, 11, 13, 8, 7, 5, 14, 15, 3, 9,"
             "7, 5, 9, 14, 3, 8, 2, 5, 5, 8, 14, 11, 11, 12, 8, 5, 3, 3, 10,"
             "3, 10, 7, 7, 10, 10, 2, 7, 4, 8, 1, 5")
    data5 = ("British Gas, British Gas, Ovo, Igloo, Igloo, Octopus, Bulb,"
             "Shell, E.ON, Npower, British Gas, Octopus, Igloo, Npower, Igloo,"
             "Shell, Scottish Power, Bulb, EDF, Bulb, EDF, Bulb,"
             "Scottish Power, Octopus, Scottish Power, Octopus, Octopus, EDF,"
             "Ovo, Shell, Octopus, E.ON, British Gas, Bulb, Npower, Shell,"
             "Scottish Power, Npower, Scottish Power, Npower")
    data6 = ("aac, ctt, gat, ccc, gcc, ctg, gtc, tcg, ccg, cca, ata, cca,"
             "tat, ata, cac, gcg, cca, gta, gtg, gac, taa, ata, gtc, aat, gct,"
             "gta, ggc, tgc, tca, ctt, tgt, ata, acc, tgc, gac, cgc, atc, cgt,"
             "tac, agg, ctt, cgc, cgc, tgg, gcg, tgg, taa, cta, aaa, tgc, cgt,"
             "tgc, gac, tta, aag, taa, act, cca, tac, agg, cgc, gtg, cca, gcg,"
             "gtt, gag, tca, aca, tct, gta, ata, ctt, gat, tcg, tcg, cac, cgt,"
             "tac, caa, aac, ctg, tgt, aag, ttc, ccc, tcc, ctc, cct, aga, gtt,"
             "tga, gaa, cct, ctc, tct, ggt, gcc, tct, ccc, agt, caa, gac, ccc,"
             "cgc")
    print(highest_count_items(data4))
    print(highest_count_items(data5))
    print(highest_count_items(data6))

    # sample test for task 1.4
    popList1 = ['00000', '00001', '00010', '00011', '00100']
    popList2 = ['aac', 'ctt', 'gat', 'ccc', 'gcc', 'ctg', 'gtc', 'tcg',
                'ccg', 'cca', 'ata']
    popList3 = ['aac', 'ctt', 'gat', 'ccc', 'gcc', 'ctg', 'gtc']
    charSet1 = ['0', '1']
    charSet2 = ['a', 'c', 't', 'g']
    charSet3 = ['a', 'c']
    charSet4 = '01'
    print(valid_char_in_string(popList1, charSet1))
    print(valid_char_in_string(popList2, charSet2))
    print(valid_char_in_string(popList3, charSet3))
    print(valid_char_in_string(popList1, charSet4))

    # sample test for task 1.5
    print(total_price(3))
    print(total_price(12))
    print(total_price(15))
    print(total_price(26))
