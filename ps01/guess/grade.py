def main():
   while True:
      try:
          grade = input("grade: ")
          grade = int(grade)
          if grade < 0 or grade > 100:
             continue
          if grade >= 90:
             print("A")
          elif grade >= 80:
             print("B")
          elif grade >= 70:
             print("C")
          elif grade >= 60:
             print("D")
          else:
             print("F")
          break
      except (ValueError):
          print("value is not a number")  



main()