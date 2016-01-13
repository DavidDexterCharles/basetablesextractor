
thefile= open('quers.txt', 'r')
#thefile= open('ApplicationsOnline.sql', 'r')
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
            
    if "--" not in line.split() and "--where" not in line.split() and "--and" not in line.split() and "--create" not in line.split() and "--smrprle," not in line.split()   :
        sqlsyntax= sqlsyntax + line + " "

thefile.close()
sqlarrray=sqlsyntax.split()

for i in range(0,len(sqlarrray)):
    if sqlarrray[i].lower()=="from" or sqlarrray[i].lower()=="join":
        i=i+1
        while(sqlarrray[i].lower()!="as" and sqlarrray[i].lower()!="on" and sqlarrray[i].lower()!="where" and sqlarrray[i].lower()!="commit" and sqlarrray[i].lower()!="order" and sqlarrray[i].lower()!="and" and sqlarrray[i].lower()!="minus" and sqlarrray[i].lower()!="create" and sqlarrray[i].lower()!="update" and sqlarrray[i].lower()!="left" and sqlarrray[i].lower()!="inner" and sqlarrray[i].lower()!="(" and sqlarrray[i].lower()!=")" and sqlarrray[i].lower()!="union" and sqlarrray[i].lower()!="select"  and sqlarrray[i]!="(SELECT" and sqlarrray[i]!="(select"  and sqlarrray[i].lower()!="group" and sqlarrray[i].lower()!="loop" and sqlarrray[i].lower()!="insert"):
            if sqlarrray[i].lower()!="as" and sqlarrray[i].lower()!="on" and sqlarrray[i].lower()!="where" and sqlarrray[i].lower()!="commit" and sqlarrray[i].lower()!="order" and sqlarrray[i].lower()!="and" and sqlarrray[i].lower()!="minus" and sqlarrray[i].lower()!="create" and sqlarrray[i].lower()!="update"  and sqlarrray[i].lower()!="left" and sqlarrray[i].lower()!="inner"  and sqlarrray[i].lower()!="(" and sqlarrray[i].lower()!="from" and sqlarrray[i].lower()!=")" and sqlarrray[i].lower()!="union" and sqlarrray[i].lower()!="select" and sqlarrray[i]!="(SELECT" and sqlarrray[i]!="(select" and sqlarrray[i].lower()!="group" and sqlarrray[i].lower()!="loop" and sqlarrray[i].lower()!="insert":
                tableset[q]=sqlarrray[i]
                q=q+1
            i=i+1

    #print tableset
result={}
#print tableset.values()
for key,value in tableset.items():
    
    if value.lower().rstrip("),;")  not in result.values():
        result[key] = value.lower().rstrip("),;")


foutput=open("basetables.txt","w")
tblcount=0
for i in range (0,len(result)):
    if(len(result.values()[i].strip(','))>4):#This line was include to remove aliases, it assumes that all words lower than 4 characters are aliases
        foutput.write(result.values()[i].strip(','))
        foutput.write("\n")
        print result.values()[i].strip(',')
      
        tblcount=tblcount+1


#print len(result)
print tblcount

foutput.write("\n\n TABLE COUNT: " + str(tblcount)+"\n\n")
foutput.write("Percent Error 7%\n\n")
# 
#print len(tableset)



