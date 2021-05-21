#Algarismos romanos
print('Entre com um valor em algarismos Romanos: ')

#Recebe valor 
valor =  str(input()).upper()
res = ''

def convert(valor):
  if len(valor) == 1:
    if valor == 'I': return 1
    if valor == 'V': return 5
    if valor == 'X': return 10
    if valor == 'L': return 50
    if valor == 'C': return 100
    if valor == 'D': return 500
    if valor == 'M': return 1000

def romanoReal(valor):
  val = 0
  ant = 0
  for u in valor:
    atual=0
    if (u == 'V' or u == 'X'):
      atual =  (convert(u) - ant) 
      val = val - ant if val > 0 else 0
    elif (u == 'L' or u == 'C' or u == 'D' or u == 'M'):
      val = convert(u) - val 
    else: 
      atual = convert(u)    
      ant = convert(u)
    val += atual
  return val
print(f'valor: {romanoReal(valor)}')

#testes
t = [
     'I','II','III','IV','V','VI','VII','VIII','IX','X',
     'XI','XII','XIII','XIV','XV','XVI','XVII','XVIII','XIX','XX',
     'XXI','XXII','XXIII','XXIV','XXV','XXVI','XXVII','XXVIII','XXIX','XXX',
     'XXXI','XXXII','XXXIII','XXXIV','XXXV','XXXVI','XXXVII','XXXVIII','XXXIX','XL',
     'XLI','XLII','XLIII','XLIV','XLV','XLVI','XLVII','XLVIII','XLIX','L',
     'LI','LII','LIII','LIV','LV','LVI','LVII','LVIII','LIX','LX',
     'LXI','LXII','LXIII','LXIV','LXV','LXVI','LXVII','LXVIII','LXIX','LXX',
     'LXXI','LXXII','LXXIII','LXXIV','LXXV','LXXVI','LXXVII','LXXVIII','LXXIX','LXXX',
     'LXXXI','LXXXII','LXXXIII','LXXXIV','LXXXV','LXXXVI','LXXXVII','LXXXVIII','LXXXIX','XC',
     'XCI','XCII','XCIII','XCIV','XCV','XCVI','XCVII','XCVIII','XCIX','C',]
cont = 1
for a in t:
  #escrever somente se encontrar erro
  if cont != romanoReal(a): print(f'{a} = {cont} | valor: {romanoReal(a)}')
  cont+=1