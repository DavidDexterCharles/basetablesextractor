

thefile= open('quers.txt', 'r')
tableset={}
x=0


def getid( line ):
        for i, j in enumerate(line):
            if j == 'from':
                return i

sqlarrray=[]
sqlsyntax= " "
q=0;
i=0;
while 1:
    line= thefile.readline()
    if not line: break
    currlist=line.split()
    if "/*" in currlist:
        while "*/" not in currlist:
            line= thefile.readline()
            currlist=line.split()
            
    if "--" not in line.split() and "--where" not in line.split() and "--and" not in line.split() and "--create" not in line.split() and "--smrprle," not in line.split()   :#-- was unto the actual word so it wasnt picking up the -- so i hard coded those instances
        sqlsyntax= sqlsyntax + line + " "

thefile.close()
sqlarrray=sqlsyntax.split()

for i in range(0,len(sqlarrray)):
    if sqlarrray[i].lower()=="from":
        i=i+1
		#basicaly it started off as checking between from and where clause but then i found various cases where tables are after the from clause but not before the where clause, if anything just adding to the while and if statementbelow will deal with cases you encounter yourself
        while(sqlarrray[i].lower()!="where" and sqlarrray[i].lower()!="commit" and sqlarrray[i].lower()!="order" and sqlarrray[i].lower()!="and" and sqlarrray[i].lower()!="minus" and sqlarrray[i].lower()!="create" and sqlarrray[i].lower()!="update" and sqlarrray[i].lower()!="left" and sqlarrray[i].lower()!="inner" and sqlarrray[i].lower()!="(" and sqlarrray[i].lower()!=")" and sqlarrray[i].lower()!="union" and sqlarrray[i].lower()!="select"  and sqlarrray[i]!="(SELECT" and sqlarrray[i]!="(select"  and sqlarrray[i].lower()!="group" and sqlarrray[i].lower()!="loop" and sqlarrray[i].lower()!="insert"):
            if sqlarrray[i].lower()!="where" and sqlarrray[i].lower()!="commit" and sqlarrray[i].lower()!="order" and sqlarrray[i].lower()!="and" and sqlarrray[i].lower()!="minus" and sqlarrray[i].lower()!="create" and sqlarrray[i].lower()!="update"  and sqlarrray[i].lower()!="left" and sqlarrray[i].lower()!="inner"  and sqlarrray[i].lower()!="(" and sqlarrray[i].lower()!="from" and sqlarrray[i].lower()!=")" and sqlarrray[i].lower()!="union" and sqlarrray[i].lower()!="select" and sqlarrray[i]!="(SELECT" and sqlarrray[i]!="(select" and sqlarrray[i].lower()!="group" and sqlarrray[i].lower()!="loop" and sqlarrray[i].lower()!="insert":
                tableset[q]=sqlarrray[i]
                q=q+1
            i=i+1


result={}
#print tableset.values()
for key,value in tableset.items(): # here i just remove duplicates, and some of the duplicates were caused because of ",;)" and others because difference in upper case and lower case
    
    if value.lower().rstrip("),;")  not in result.values():
        result[key] = value.lower().rstrip("),;")


foutput=open("basetables.txt","w")
foutput.write("TABLE COUNT: " + str(len(result))+"\n\n")
foutput.write("Percent Error 4%\n\n")
for i in range (0,len(result)):
    foutput.write(result.values()[i])
    foutput.write("\n")
    print result.values()[i]
    print "\n"


print len(result)


# 
#print len(tableset)



