target_num = int(input("Enter number: "))
match (target_num % 2):
  case 0:
    print(f"{target_num} is Even")
  case _:
    print(f"{target_num} is Odd")
