alphabet_lower= "abcdefghijklmnopqrstuvwxyz"
alphabet_upper= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

shift = 5 # Mengeser huruf sebanyak 5 kali

after_shifted_lower = alphabet_lower[shift:] + alphabet_lower[:shift] #untuk huruf non kapital
after_shifted_upper = alphabet_upper[shift:] + alphabet_upper[:shift] #untuk huruf kapital

table = str.maketrans(alphabet_lower + alphabet_upper, 
after_shifted_lower + after_shifted_upper) #Kalau huruf kapital maka di ubahnya  akan khusus yang huruf kapital dan sebaliknya 

#Kata pengubah:
print("Hello".translate(table)) #output : "Mjqqt"
print("Selamat Tahun Baru".translate(table)) #output : "Xjqfrfy Yfmzs Gfwz"


#CATATAN : MAKSIMAL ANGKA YANG BISA DI GESER ADALAH 25 