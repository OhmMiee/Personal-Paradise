# Personal-Paradise
def yippy(year):
    #year = int(input())
    if year%400==0:
      print("29")
    elif year%100==0:
      print("28")
    elif year%4==0:
      print("29")
    else:
      print("28")
