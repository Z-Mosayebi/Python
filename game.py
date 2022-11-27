import random
import operator

def random_problem():
    operators={
        '+':operator.add,
        '-':operator.sub,
        '*':operator.mul,
        '//':operator.floordiv
    }

    n1=random.randint(1,10) 
    n2=random.randint(1,10)
    op=random.choice(list(operators.keys()))
    answer=operators.get(op)(n1,n2)
    print(f'{n1} {op} {n2}:')
    return answer

def ask_question():
    answer=random_problem()
    canswer=float(input(''))
    return answer ==canswer 


score=0
while True:
    if ask_question():
        score+=1
        print('ok')
    else:
        print('you lost')
        break
print('game over')
print(f'socore={score}')        

