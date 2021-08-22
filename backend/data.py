import pyrebase
import csv
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
def update_student_score(score,streak,classcode,student_id): #to update student scores
    database.child("Classes").child(classcode).child(student_id).update({"Score":score,"Streak":streak})
    database.child("Students").child(student_id).child(classcode).update({"Score":score,"Streak":streak})
        

def add_teacher(teacherid,teacheremail,teachername):#to add teachers to database
    database.child("Teachers").child(teacherid).set({"Name":teachername,"Email":teacheremail})
    
def add_classes(classname,teacherid):
    a=database.child("Classes").get().val()
    b=database.child("Teachers").child(teacherid).child("Classes").get().val()
    b.update({len(b):classname})
    database.child("Teachers").child(teacherid).child("Classes").update(b)
    teachername=database.child("Teachers").child(teacherid).get().val()["Name"]
    
    database.child("Classes").push({"Teacher":teachername,"Teacherid":teacherid,"ClassName":classname,"Rewards":{"R1":{"Score":100},"R2":{"Score":200},"R3":{"Score":300},"R4":{"Score":400},"R5":{"Score":400}}})
    code={}
    for i in a:
        code.update({a[i]["ClassName"]:i})
    return code # returns code for classnames

def studentdata(studentid,studentname,studentemail): #adds new student
    database.child("Students").child(studentid).set({"Name":studentname,"Email":studentemail})
def join_class(studentid,classcode): # to join a class with classcode
    classname=database.child("Classes").child(classcode).get().val()["ClassName"]
    database.child("Students").child(studentid).child(classcode).update({"ClassName":classname,"Score":0,"Streak":0})
    a=database.child("Classes").child(classcode).get().val()
    name=database.child("Students").child(studentid).get().val()["Name"]
    a.update({studentid:{"Name":name,"Score":0,"Streak":0}})
    database.child("Classes").child(classcode).set(a)
    
def get_classcode(teacherid): # gets classcode for corresponding classnames
    a=database.child("Classes").get().val()
    code={}
    for i in a:
        if a[i]["Teacherid"]==teacherid:
            code.update({a[i]["ClassName"]:i})
    return code

def rewards(classcode):
    #calling this function after every class ends
    a=database.child("Classes").get().val()
    for i in a:
        if i==classcode:
            for k in a[i]:
                if k!="ClassName" and k!="Teacherid" and k!="Teacher" and k!="Rewards":
                    score=a[i][k]["Score"]
                    d=a[i]["Rewards"]
                
                    for j in d:
                        
                        if d[j].get(k)!="Already Redeemed":
                            if score>=d[j]["Score"]:
                                a[i]["Rewards"][j].update({k:"Redeemable"})
                            else:
                                a[i]["Rewards"][j].update({k:"Not Redeemable"})
                        
                        
    database.child("Classes").update(a)
            
def student_scores(studentid):
    a=database.child("Students").child(studentid).get().val()
    name=a["Name"]
    for i in a:
        
        if i!="Email" and i!="Name":
            classname=a[i].get("ClassName")
            scores=a[i]["Score"]
            Streak=a[i]["Streak"]
            print(f"{name}|{classname}|{scores}|{Streak}")
        
def displayrewardstatus(studentid,classname):# get studentid from login['localId']
    a=database.child("Classes").get().val()
    for i in a:
        if i==classcode:
            for k in a[i]:
                if k!="ClassName" and k!="Teacherid" and k!="Teacher" and k!="Rewards":
                    score=a[i][k]["Score"]
                    d=a[i]["Rewards"]
                    for j in d:
                        print(d[j],d[j][studentid])
                        if d[j][studentid]=="Redeemable":
                            y=input('Do you wanna redeem it:').lower()
                            if y=="yes":
                                a[i]["Rewards"][j].update({studentid:"Already Redeemed"})
                            
                            
                
                    
                        
                        
    
                    
    
def lastclass():
    pass
if __name__=="__main__":
    choice=int(input("1 or 2 or 3 or 4:"))
    if choice==1: #adds students 
        email = input(" Enter Your Email Address : ")
        password=input('Enter your password: ')
        confirmpass=input('Confirm Password: ')
        if password==confirmpass:
            user = auth.create_user_with_email_and_password(email, password)
            #auth.send_email_verification(user['idToken']) #sending email verification (if needed)
            print("Created")
            print("Enter name:")
            studentname=input()
            studentid=user["localId"]
            studentemail=user["email"]
            
                
            
            studentdata(studentid=studentid,studentemail=studentemail,studentname=studentname)
            classcode=input("Enter classcode to join:")
            join_class(classcode=classcode,studentid=studentid)
    elif choice==2: #adds teacher to classes and teachers nodes
        
        email = input(" Enter Your Email Address : ")
        password=input('Enter your password: ')
        confirmpass=input('Confirm Password: ')
        if password==confirmpass:
            user = auth.create_user_with_email_and_password(email, password)
            #auth.send_email_verification(user['idToken']) #sending email verification (if needed)
            print("Created")
            classnames=[]
            
            print("Enter name:")
            name=input()
            teacherid=user["localId"]
            teacheremail=user["email"]
            for i in range(int(input("Enter number of classes:"))):
                classnames+=[input("Enter class name:")]
        
        add_teacher(teacherid=teacherid,teacheremail=email,teachername="Ross")
        add_classes(classnames)
                
    elif choice==3: #--> to get classnames and classcode for teachers
        email=input("Enter email:")
        password = input(" Enter Your Password : ")
        login= auth.sign_in_with_email_and_password(email,password)
        teacherid=login['localId']
        classnames=get_classcode(teacherid) #--> dictionary with classname as keys and classcodes as values
        print(classnames)
    elif choice==4: # to get student's scores and streaks
        email=input("Enter email:")
        password = input(" Enter Your Password : ")
        login= auth.sign_in_with_email_and_password(email,password)
        studentid=login['localId']
        print(student_scores(studentid))
    classcode=input("Enter classcode to join:")
    join_class(classcode=classcode,studentid='sLISGuQLrKU1Tunqdn5KGJMYEfI2')
        
'''
after signing in check whether the user is teacher by checkin login['localId'] in database.child('Teachers') or database.child('Students')
'''