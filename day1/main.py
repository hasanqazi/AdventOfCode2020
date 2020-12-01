ints=[]

with open("input") as f:
  for i in f:
    ints.append(int(i))

def find_sum():
  for i in ints:
    for j in ints:
      if (i+j) == 2020:
        print(i*j)
        break

def find_sum2():
  for i in ints:
    for j in ints:
      for k in ints:
        if (i+j+k) == 2020:
          print(i*j*k)
          break

find_sum()
find_sum2()