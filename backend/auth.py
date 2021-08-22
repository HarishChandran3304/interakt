#IMPORTS
import pyrebase as pb


#SETUP
firebaseConfig={'apiKey': "AIzaSyA-s0Bjin-4gmuOUc_PVXRmY0dMHFMk_BE",
    'authDomain': "hackathon-9bd4b.firebaseapp.com",
    'databaseURL': "https://hackathon-9bd4b-default-rtdb.firebaseio.com",
    'projectId': "hackathon-9bd4b",
    'storageBucket': "hackathon-9bd4b.appspot.com",
    'messagingSenderId': "57880205401",
    'appId': "1:57880205401:web:4a75c6e81602ef95573948",
    'measurementId': "G-ME8ZRNZZGF"
  }
firebase=pb.initialize_app(firebaseConfig)
auth=firebase.auth()
database=firebase.database()


#FUNCTIONS
def sign_up(email, pwd):
    try:
        creds = auth.create_user_with_email_and_password(email, pwd)
        print("Signup Successful")
        return creds
    except:
        print("Signup Error")
        
def log_in(email, pwd):
    try:
        creds = auth.sign_in_with_email_and_password(email, pwd)
        print("Login Successful")
        return creds
    except:
        print("Login Error")
    