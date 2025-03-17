import random
ans=random.randint(10,20)
while True:
  guess=int(input("Enter a number between10-20:"))
  if guess==ans:
    print("conguatulations!")
    break
