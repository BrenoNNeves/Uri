money=int(input())

nota100=money//100
rest100=money%100

nota50=rest100//50
rest50=rest100%50

nota20=rest50//20
rest20=rest50%20

nota10=rest20//10
rest10=rest20%10

nota5=rest10//5
rest5=rest10%5

nota2=rest5//2
rest2=rest5%2

nota1=rest2

print(money)
print('{} nota(s) de R$ 100,00'.format(nota100))
print('{} nota(s) de R$ 50,00'.format(nota50))
print('{} nota(s) de R$ 20,00'.format(nota20))
print('{} nota(s) de R$ 10,00'.format(nota10))
print('{} nota(s) de R$ 5,00'.format(nota5))
print('{} nota(s) de R$ 2,00'.format(nota2))
print('{} nota(s) de R$ 1,00'.format(nota1))
