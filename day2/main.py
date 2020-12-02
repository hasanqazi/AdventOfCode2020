input=[]

with open("input") as f:
  for i in f:
    input.append(i)

def check_pass():
  valid_pass = 0
  check = 0
  for i in range(len(input)):
    first_limit = input[i].split('-')[0]
    second_limit = str(input[i].split('-')[1]).split(' ')[0]
    char = str(input[i].split(':')[0])[-1]
    password = input[i].split()[2]
    #print(first_limit, second_limit, char, password)
    for j in range(len(password)):
      if password[j] == char:
        check += 1
    if check >= int(first_limit) and check <= int(second_limit):
      print("Valid password")
      #print(first_limit, second_limit, check)
      check = 0
      valid_pass += 1
    else:
      print("Invalid password")
      #print(first_limit, second_limit, check)
      check = 0
  print(valid_pass)
check_pass()