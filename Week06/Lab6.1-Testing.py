#Program for reading lecture notes
#Author: Breeda Herlihy

from re import L


aBook = {"title":"the order of phoenix", "author":"JK"}
for key, value in aBook.items():
    print ("key", key, "has a value of", value)



def real_imag_conj(val):
    return val.real, val.imag, val.conjugate()

r, i, c = real_imag_conj(3 + 4j)
print(r, i, c)

