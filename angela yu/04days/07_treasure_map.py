row1=["@_@","#_#","$_$"]
row2=["%_%","&_&","^_^"]
row3=["+_+","o_o","0_0"]
map =[row1,row2,row3]
print(f"{row1}\n,{row2}\n,{row3}")
position = input(("Where you want to put the treasure ?"))
column = int(position[0])
row = int(position[1])

# new_row= map[row-1]
# new_row[column-1] ="x"

map[row-1][column-1] ="x"

print(f"{row1}\n,{row2}\n,{row3}")