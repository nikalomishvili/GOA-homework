import random

def guess_number():
    print("იფიქრეთ რიცხვი 1-დან 100-მდე და მე შევეცდები მის გამოცნობას 3 მცდელობით!")

    low, high = 1, 100  # დასაშვები დიაპაზონი
    attempts = 3  # მცდელობების რაოდენობა

    for _ in range(attempts):
        guess = random.randint(low, high)  # შემთხვევითი რიცხვის გამოცნობა
        print(f"მე ვფიქრობ, რომ რიცხვი არის: {guess}")
        
        response = input("თუ მაღალია - 'მაღალი', თუ დაბალია - 'დაბალი', თუ სწორია - 'სწორია': ").lower()
        
        if response == "სწორია":
            print("ვიცოდი! 🎉 თამაში დასრულდა.")
            break
        elif response == "მაღალი":
            high = guess - 1  # დიაპაზონის შემცირება
        elif response == "დაბალი":
            low = guess + 1  # დიაპაზონის გაზრდა
        else:
            print("გთხოვთ, სწორად მიუთითოთ პასუხი ('მაღალი', 'დაბალი' ან 'სწორია').")

    print("თამაში დასრულდა! 🚀")

# ფუნქციის გამოძახება
guess_number()