
year = int(input("მიუთითეთ წელი: "))


if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("შენი წელი არის ნაკიანი")
else:
    print("შენი წელი არ არის  ნაკიანი")
    
 
