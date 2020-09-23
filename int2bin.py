import sys

def binaryRepresentaion(num):  
  if num>1:
    yield num%2
    yield from binaryRepresentaion(num//2)
  else: 
    yield num

def main():
  number = int(sys.argv[1])
  print([bit for bit in binaryRepresentaion(number)][::-1])

if __name__ == "__main__":
  main()
