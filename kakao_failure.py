import operator

def kakao(n, stage):
    # nowIndex → point
    nowIndex = 0

    # variable
    count = 0 
    length = len(stage)
    stageNum = 1
    
    # failure, temp list
    failure = {}
    rst = []
    
    # sort stage
    stage.sort()

    # break point 
    if max(stage)  > n :
        breakPoint = stage.index(max(stage))
    else : breakPoint = length
    
    # main
    for i in  range(0,breakPoint):
        if stageNum < stage[nowIndex] :
            while stage[nowIndex] != stageNum :
                failure[stageNum] = 0
                stageNum += 1
        count += 1
        if isSame(stage, nowIndex) != True:
            rst = (count / (count + (length-nowIndex-1)))
            failure[stage[nowIndex]] = round(rst,3)
            count = 0
            stageNum += 1
        nowIndex += 1
        
    print(failure)
    failure = sorted(failure.items(), key=operator.itemgetter(1), reverse = True)
    print(failure)
    
    '''
    failure.sort(key=failure.values())
    print(failure)
    '''

    
def isSame(stage, nowIndex):
    if nowIndex < len(stage)-1 :
        if stage[nowIndex] == stage[nowIndex+1] : return True
        return  False
    return False    


n = 5
stages = [2,1,2,6,2,4,3,3]

kakao(n, stages)

