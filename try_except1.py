# mengimpor modul sys untuk exit()
import sys
def main():
  # membuat judul program
  print("PROGRAM PEMBAGIAN BILANGAN")
  
  # meminta user memasukkan bilangan
  a = float(input("Masukkan a: "))
  b = float(input("Masukkan b: "))
  
  # mendefinisikan blok try...except
  try:
  hasil = a / b
  except ZeroDivisionError:
  sys.exit(1) # menghentikan program
  # menampilkan hasil
  print("\na : ", a)
  print("b : ", a)
  print("a / b = ", hasil)
  
if __name__ == "__main__":
  main()
