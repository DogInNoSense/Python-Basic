import random
price=random.randint(1000,1500)
print('guess price [1000,1500]')
def fun():
    guess = int(input())
    if guess>price:
        print('bigger')
        fun()
    elif guess<price:
        print('smaller')
        fun()
    else:
        print('correct')
        return
if __name__ == '__main__':
    fun()