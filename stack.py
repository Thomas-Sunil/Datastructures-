stack=[]
def popele():
	if not stack:
		print("Empty Stack")
	else:
		e=stack.pop()
		print("The poped item is ",e)
		print("The stack is ")
		print(stack)
def push():
	print("Enter the element to be pushed into the stack")
	element=int(input())
	stack.append(element)
	print("The stack is ")
	print(stack)
while True :
	print("1 to push \n2 to pop \n3 To exit")
	print("Enter the choice")
	ch=int(input())
	if ch==1:
		push()
	elif ch==2:
		popele()
	elif ch==3:
		break
	else:
		print("Wrong chopice!!!")

