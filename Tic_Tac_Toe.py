list=[['','',''],
      ['','',''],
      ['','','']]

co=0
def Draw_Shape():
	print('\n')
	global co
	for i in range(1):
		print("  {} |     {}    |{}".format(list[0][0],list[0][1],list[0][2]))
		print("-------------------")
		print("  {} |     {}    |{}".format(list[1][0],list[1][1],list[1][2]))
		print("-------------------")
		print("  {} |     {}    |{}".format(list[2][0],list[2][1],list[2][2]))
	if co==1:
		co=2
	elif co==2 or co == 0:
		co=1	
	x=input("Player {} enter O Or X then enter number of row and  with column space:".format(co) )
	value=x.split(" ")

	Update_matrix( value[0], ord(value[1]) - ord('0'),  ord(value[2]) - ord('0'))

def Update_matrix(Charater,position_Row,position_column):
	win=False
	list[position_Row][position_column]=Charater
	if (list[0][0]==list[0][1]==list[0][2] and (list[0][0]!='' and list[0][1]!='' and list[0][2]!='')):
		print("player {} is the Winnner ".format(co))
		win=True
	elif (list[1][0]==list[1][1]==list[1][2] and (list[1][0]!='' and list[1][1]!='' and list[1][2]!='')):
		print("player {} is the Winnner ".format(co))
		win=True
	elif (list[2][0]==list[2][1]==list[2][2] and (list[2][0]!='' and list[2][1]!='' and list[2][2]!='')):
		print("player {} is the Winnner ".format(co))
		win=True
	elif (list[0][0]==list[1][0]==list[2][0] and (list[0][0]!='' and list[1][0]!='' and list[2][0]!='')):
		print("player {} is the Winnner ".format(co))
		win=True
	elif (list[0][1]==list[1][1]==list[2][1] and (list[0][1]!='' and list[1][1]!='' and list[2][1]!='')):
		print("player {} is the Winnner ".format(co))
		win=True
	elif (list[0][2]==list[1][2]==list[2][2] and (list[0][2]!='' and list[1][2]!='' and list[2][2]!='')):
		print("player {} is the Winnner ".format(co))
		win=True
	elif (list[0][0]==list[1][1]==list[2][2] and (list[0][0]!='' and list[1][1]!='' and list[2][2]!='')):
		print("player {} is the Winnner ".format(co))
		win=True
	elif (list[0][2]==list[1][1]==list[2][0]  and (list[0][2]!='' and list[1][1]!='' and list[2][0]!='')):
		print("player {} is the Winnner ".format(co))
		win=True
	elif win==False:
		Draw_Shape()

if __name__ == "__main__":
	Draw_Shape()


