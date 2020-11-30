import time

def sprint(string):
  for l in string:
    print(l,end = "", flush = True)
    time.sleep(0.03)
  print("\n")

class Stack():

  def __init__(self,maxLength):
    self.items = []
    self.maxLength = maxLength
    self.methods = ("isfull","push","pop","isempty","help","state","showitems")
  
  def showitems(self):
    if self.items:
      for i in range(len(self.items)):
        if i == 0: print("\nBOTTOM".ljust(8), self.items[i])
        elif i == self.maxLength - 1: print("TOP".ljust(8), self.items[i])
        else: print(str(i+1),self.items[i])
    else: print("Stack is empty.")
  
  def isfull(self):
    if len(self.items) == self.maxLength:  
      return True;
    else: return False
  
  def isempty(self):
    if not self.items: return True
    else: return False
  
  def push(self,item):
    if self.isfull(): 
      print("Stack is full.")
    
    else: 
      self.items.append(item); 
      for i in range(len(self.items)): 
        print(str(i+1), self.items[i])
      print("\n")
  
  def state(self):
    if self.isfull():
      setState = "%d out of %d slots taken -- [FULL]" %(len(self.items),self.maxLength) 
    elif self.isempty():
      setState = "0 out of %d slots taken -- [EMPTY]" %(self.maxLength)
    else: setState = "%d out of %d slots taken -- [%d SLOTS LEFT]" %(len(self.items),self.maxLength, self.maxLength-len(self.items))
    sprint("CURRENT STATE > "+ setState) 

    
  
  def pop(self):
    if self.items: print(self.items[-1]); return(self.items.pop(-1));
    else: print("Stack is empty.")
  

books = Stack(4)

while True:

  command = input(">>> ").replace("\"",""); 
  
  if command.lower() in books.methods:
    if command.lower() == "push":
      item = input("ENTER ITEM TO ADD > ").replace("\"","")
      prompt = (f'books.push("{str(item)}")')
    
    elif command.lower() == "help":
      print("\n--HELP PAGE--\n")
      print("[Type \"push\" to add a value to the stack. When asked for an item, don't place it in quotes.]\n")
      print("[Type \"pop\" to take the book at the top of the shelf off and print its name.]\n")
      print("[Type \"state\" to see how big the stack is, and whether it's full or empty.]\n")
      continue

    else:
      prompt = (f'books.{command.lower()}()')
    
    eval(prompt)
  else:
    print("Not a command.")
