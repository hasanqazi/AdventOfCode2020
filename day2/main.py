input=[]

with open("input") as f:
  for i in f:
    input.append(i)

def check_pass():
  valid_pass = 0
  check = 0
  for i in range(len(input)):
    first_limit = int(input[i].split('-')[0])
    second_limit = int(str(input[i].split('-')[1]).split(' ')[0])
    char = str(input[i].split(':')[0])[-1]
    password = input[i].split()[2]
    for j in range(len(password)):
      if password[j] == char:
        check += 1
    if check >= first_limit and check <= second_limit:
      print("Valid password")
      check = 0
      valid_pass += 1
    else:
      print("Invalid password")
      check = 0
  print("Valid passwords: ", valid_pass)

def check_pass2():
  valid_pass = 0
  for i in range(len(input)):
    first_char = int(input[i].split('-')[0])-1
    second_char = int(str(input[i].split('-')[1]).split(' ')[0])-1
    char = str(input[i].split(':')[0])[-1]
    password = input[i].split()[2]
    if password[first_char] == char and password[second_char] != char:
      print("Valid password")
      valid_pass += 1
    elif password[first_char] != char and password[second_char] == char:
      print("Valid password")
      valid_pass += 1
    else:
      print("Invalid password")
  print("Valid passwords: ", valid_pass)
  
check_pass()
check_pass2()