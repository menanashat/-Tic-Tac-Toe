list=[['','',''],
      ['','',''],
      ['','','']]

co=0
def Draw_Shape():
	print('\n')
	global co
	for i in range(1):
		print("  {} |     {}    | {}".format(list[0][0],list[0][1],list[0][2]))
		print("-------------------")
		print("  {} |     {}    | {}".format(list[1][0],list[1][1],list[1][2]))
		print("-------------------")
		print("  {} |     {}    | {}".format(list[2][0],list[2][1],list[2][2]))
	if co==1:
		co=2
	elif co==2 or co == 0:
		co=1

	valid=True	
	while valid==True:
		try:
			x=input("Player {} enter o Or x then enter number of row and  with column space:".format(co) )
			value=x.split(" ")
			if value[0]=='o' or value[0]=='x':
				if  value[1]=='0' or value[1]=='1' or value[1]=='2':
					if  value[2]=='0' or value[2]=='1' or value[2]=='2':
						valid=False
			else :
				print("please enter right format")
			if list[ord(value[1]) - ord('0')][ord(value[2]) - ord('0')] == "":

				Update_matrix( value[0], ord(value[1]) - ord('0'),  ord(value[2]) - ord('0'))
			else:
				print("this place is Taken")
				valid=True
		except :
			pass
				# print("please enter right format")			
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


