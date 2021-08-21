import pyrebase
from getpass import getpass
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
db=firebase.database()


 
def create_users():
    email = input(" Enter Your Email Address : ")
    name = input('Enter your name: ')
    password=input('Enter your password: ')
    confirmpass=input('Confirm Password: ')
    if password==confirmpass:
        user = auth.create_user_with_email_and_password(email, password)
        #auth.send_email_verification(user['idToken']) #sending email verification (if needed)
        print("Created")
        details={}
        uid=user['localId']
        details['uid']=uid
        details['Name']=name
        details['email']=email
        details['score']=0
        details['streak']=0
        db.child("Students").child(f'{name}-{uid}').set(details)
        return user["localId"]
def sign_in():
    email=input("Enter email:")
    password = input(" Enter Your Password : ")
    login= auth.sign_in_with_email_and_password(email,password)
    return login['localId']
choice=int(input("Enter choice:")) #1 for registering and 2 for signing in
if choice==1:
    create_users()

elif choice==2:
    sign_in()