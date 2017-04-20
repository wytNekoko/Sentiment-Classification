# delete blank line at the same time
def splictDataset(infile1,infile2,trainfile,validfile,testfile):
    info1 = open(infile1,'r')
    info2 = open(infile2,'r')
    train=open(trainfile,'w')
    valid=open(validfile,'w')
    test=open(testfile,'w')
    lines1 = info1.readlines()
    lines2 = info2.readlines()
    for i in range(1,len(lines1)):
        t1=lines1[i].replace("-LRB-","(")
        t2=t1.replace("-RRB-",")")
        ### restore bracket
        k=lines2[i].strip().split(",")
        t=t2.strip().split('\t')
        # train
        if k[1]=='1':
            train.writelines(t[1])
            train.writelines("\n")
        # test
        elif(k[1]=='2'):
            valid.writelines(t[1])
            valid.writelines("\n")
        # dev valid
        elif(k[1]=='3'):
            test.writelines(t[1])
            test.writelines("\n")
    #print("end")
    info1.close()
    info2.close()
    train.close()
    valid.close()
    test.close()      

# combine labels with sentences
def tag(infile1,infile2,outputfile3):
    info1 = open(infile1,'r')
    info2 = open(infile2,'r')
    info3 = open(outputfile3,'w')
    lines1 = info1.readlines()
    lines2 = info2.readlines()
    text={}
    for i in range(0,len(lines1)):
        s=lines1[i].strip().split("|")
        text[s[1]]=s[0]
    for j in range(1,len(lines2)):
           k=lines2[j].strip().split("|")
           if k[0] in text:
               info3.writelines(text[k[0]])
               info3.writelines("\n")
               info3.writelines(k[1])
               info3.writelines("\n")
    #print("end2d1")
    info1.close()
    info2.close()
    info3.close()
            
 # get train and test labels and combine labels with sentences
def getLabel(infile0,infile1,infile2,infile3,infile4,infile5,infile6):
    allsen= open(infile0,'r') # all label
    info1 = open(infile1,'r') # train
    info2 = open(infile2,'r') # valid
    info3 = open(infile3,'r') # test
    info4 = open(infile4,'w') # train1
    info5 = open(infile5,'w') # valid1
    info6 = open(infile6,'w') # test1
    lines0 = allsen.readlines()
    lines1 = info1.readlines()
    lines2 = info2.readlines()
    lines3 = info3.readlines()   
    for i in range(0,len(lines0),2):
        if  lines0[i] in lines1: # text
            #info4.writelines(lines0[i])
            info4.writelines(lines0[i+1])
        if  lines0[i] in lines2:
           #info5.writelines(lines0[i])
           info5.writelines(lines0[i+1])
        if lines0[i] in lines3:
            #info6.writelines(lines0[i])
            info6.writelines(lines0[i+1])
 
    #print("end3d1")
    info0.close()
    info1.close()
    info2.close()
    info3.close()
    info4.close()
    info5.close()
    info6.close()


splictDataset("database/datasetSentences.txt","database/datasetSplit.txt","train.txt","valid.txt","test.txt")
tag("database/dictionary.txt","database/sentiment_labels.txt","allsentimet.txt")
getLabel("allsentimet.txt","train.txt","valid.txt","test.txt","train_label.txt","valid_label.txt","test_label.txt")
