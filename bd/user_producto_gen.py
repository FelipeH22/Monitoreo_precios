def genera_Relation():
    archivo = open("relation1.txt",'a')
    for i in range(169269,9102195+1):
        for j in range(1,6):
            print(i)
            archivo.write(str(i)+";"+str(j)+"\n")
genera_Relation()


