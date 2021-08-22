import csv
import pyrebase
import db
import os
firebaseConfig={'apiKey': "AIzaSyA-s0Bjin-4gmuOUc_PVXRmY0dMHFMk_BE",
    'authDomain': "hackathon-9bd4b.firebaseapp.com",
    'databaseURL': "https://hackathon-9bd4b-default-rtdb.firebaseio.com",
    'projectId': "hackathon-9bd4b",
    'storageBucket': "hackathon-9bd4b.appspot.com",
    'messagingSenderId': "57880205401",
    'appId': "1:57880205401:web:4a75c6e81602ef95573948",
    'measurementId': "G-ME8ZRNZZGF"
  }
firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()
database=firebase.database()
def bubbleSort(arr,arr1,arr2,arr3):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if int(arr[j]) > int(arr[j+1]) :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                arr1[j],arr1[j+1]=arr1[j+1],arr1[j]
                arr2[j],arr2[j+1]=arr2[j+1],arr2[j]
                arr3[j],arr3[j+1]=arr3[j+1],arr3[j]
    return arr,arr1,arr2,arr3
                
            
        
def reading(classcode): #collecting data from firebase in a sorted manner

    a=database.child("Classes").child(classcode).get().val()
    reader=[]
    
    for i in a:
        if i!="ClassName" and i!="Teacher" and i!="Teacherid" and i!="Rewards":
            
            reader+=[[a[i]["Name"],a[i]["Score"],a[i]["Streak"],i]]
    
    score=[]
    name=[]
    streakcalc=[]
    userid=[]
    for i in reader:
            
        name+=[i[0]]
        score+=[int(i[1])]
        streakcalc+=[int(i[2])]
        userid+=[i[3]]

    score,name,streakcalc,userid=bubbleSort(score,name,streakcalc,userid)
    return score,name,streakcalc,userid
        
    
  
def startclass(classcode):
    i=0
    score,name,streakcalc,userid=reading(classcode)
    
    while True:
        if i<len(score):

            print(f"{name[i]} has a score of {score[i]}")
            
            s=int(input("Enter interaction score:"))
            bonus=int(input("Enter bonus points:"))
            if s+bonus>=4:
                streakcalc[i]+=1
                
            else:
                streakcalc[i]=0
            if streakcalc[i]!=0 and streakcalc[i]%3==0:
                score[i]+=5 #the points added due to streak of 3 interactions rated above 4
            score[i]+=s+bonus
        else:
            i=0
            score,name,streakcalc,userid=bubbleSort(score,name,streakcalc,userid)
            continue
            
        print("Do u wanna end the class:")
        
        i+=1
        if input()=="yes":
            endclass(score,name,streakcalc,userid,"teacher.csv",classcode)
            break
        
def endclass(score,name,streakcalc,userid,filename,classcode):
    with open(filename,"w",newline="") as fh:
        writer=csv.writer(fh)
        writer.writerow(["Name","Score","Streak"])
        for i in range(len(score)):
            writer.writerow([name[i],score[i],streakcalc[i]])
            db.update_student_score(score[i],streakcalc[i],classcode,userid[i])
        db.rewards(classcode)
def openfile(file):
    os.startfile(file)
email=input("Enter email:")
password = input(" Enter Your Password : ")
login= auth.sign_in_with_email_and_password(email,password)
teacherid=login['localId']
classcodes=db.get_classcode(teacherid)
classname=input("Enter classname:")
classcode=classcodes[classname]
startclass(classcode)

openfile("teacher.csv")
