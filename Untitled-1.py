
def solution(v):
    
    space = []
    space.append(v)
    first = []
    second=[]
    third = []
    fourth=[]
    first.append(space[0][0])
    first.append(space[0][1])
    first.append(space[0][2])

    second.append(first[0][0])
    second.append(first[1][0])
    second.append(first[2][0])

    third = set(second)

    

    

    
    answer = print(third)
    
    
    

    return answer
p =[[1, 4], [3, 4], [3, 10]]

solution(p)
first=[]