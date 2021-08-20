#this file accepts the inputs from the user till we develop our gui
import mysql.connector as m
import datetime
import calendar
nw = datetime.datetime.now()

#setting up a calendar object
def Day(date):
    val = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return (calendar.day_name[val])
month=calendar.monthcalendar(nw.year,nw.month )
# the above fn gives [[0, 0, 0, 0, 0, 0, 1], [2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22], [23, 24, 25, 26, 27, 28, 29], [30, 31, 0, 0, 0, 0, 0]]

#time alloted per day
time_per_day={}
for i in ['MON','TUE','WED','THURS','FRI','SAT','SUN']:
    time_slot=eval(input("plz input which of the following time slots u are free on (just the options as a list like'['a','b','c']')\na)0700-0800\nb)0800-0900\nc)0900-1000\nd)1000-1100\ne)1100-1200\nf)1200-1300\ng)1300-1400\nh)1400-1500\ni)1500-1600\nj)1600-1700\nk)1700-1800\nl)1800-1900\nm)1900-2000\nn)2000-2100\no)2100-2200\np)2200-2300\nq)2300-2400\n"))
    time_per_day[i]= time_slot

#replaces each day with the times for which the person is avlbl
for i in month:
    x=0
    for j in i:
        if j==0:
            x+=1
            pass
            
        elif j==1:
            j=time_per_day.get(time_per_day[x],default=None) 


                
            
'''
try:
    con=m.connect(host='localhost',user='root',passwd='MySql270512',db='hackathon')
    if con.is_connected():
        for i in ['SUN','MON','TUE','WED','THURS','FRI','SAT']:
            mycursor = con.cursor()     
            sql1 = f'Create table {i}_month()'
            mycursor.execute(sql1)
            con.commit()
        result = mycursor.fetchall()
        for row in result:
            print(row)
    else:
        print('connection to database not established')
except m.Error as e:
    print(e)
else:
    con.close()

'''










