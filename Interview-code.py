def solution(A):
    # Implement your solution here
    solution = map(lambda x: (x - 1) in A or (x + 1) in A, A)
    solution = any(list(solution))
    return solution

def solution(S):
    # Implement your solution here
    Slist  = list(S)
    banana = ["B", "A", "N", "A", "N", "A"]
    solution = 0
    while Slist:
        for letter in banana:
            try:
                Slist.pop(Slist.index(letter))              
            except:
                return solution
        solution += 1