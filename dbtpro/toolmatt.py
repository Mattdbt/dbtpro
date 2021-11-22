
def first_step(word):
    if len(word) < 7:
        return 'Try again'

    if word.isupper() == False:
        return 'Try again'
    else:
        return 'Password ok'

def computing(a,b,c):
    res = a*b-c
    return res
