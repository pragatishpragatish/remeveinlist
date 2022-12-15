l=[]
l=input("Enter integers in the list: ")
b=list(map(int,l.split(",")))
t=int(input("Enter the element to be removed from the list: ")
while t in b:
	b.remove(t)
 print(b)
