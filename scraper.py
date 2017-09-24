# program name  : scraper.py # postach script
# date          : Sun Aug 13 10:46:33 IST 2017

## python libraries
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plot
import ast
import numpy as np

list_student_names = []
list_student_percentages = []

for i in range(314126514001, 314126514066):
    url = 'http://www.anits.edu.in/attendance.php?regdnor=on&regdno='+str(i)+'&submit=Search..&mobile='
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    row_data = soup.findAll("td")
    ## constants
    name = 7
    roll_no = 1
    attendance_percentage = 20
    ############

    student_name = ""
    student_attendance_percentage = 0.0

    for i in row_data:
        if row_data.index(i) == name:
            student_name = i.get_text()

        if row_data.index(i) == attendance_percentage:
            student_attendance_percentage = ast.literal_eval(i.get_text())

        # if len(st_name) == 3 :
        #     student_name = st_name[1]

        # if len(st_name) == 2 :
        #     student_name == st_name[1]

        # if len(st_name) > 3 :
        #     student_name = st_name[1]

    # print(len(student_name))
    st_name = []
    st_name = student_name.split()
    # print(st_name)
        
    # print(len(st_name))
    try:
        student_name = st_name[1].lower()
    except IndexError:
        student_name = ''

    if student_name == "rajya" :
        student_name = "Raji"

    if student_name == "vinay" :
        student_name = "Zarwis"

    # print(student_name)
    list_student_names.append(student_name)
    # print(student_attendance_percentage)
    list_student_percentages.append(student_attendance_percentage)

    # print(student_name)
    # print(student_attendance_percentage)

    # print(list_student_names)
    # print(list_student_percentages)

# end of for
plot.rc('xtick', labelsize=7)
x_axis = np.array([i for i in range(1, 66)])
y_axis = np.array(list_student_percentages)
x_ticks = list_student_names
plot.xticks(x_axis, x_ticks, rotation=90)
plot.bar(x_axis, y_axis, label='attendance', color='#146de4')
plot.xlabel('Student Name')
plot.ylabel('Student Attendance Percentage')
plot.title('Attendance of EEE-A students')
plot.legend()
plot.show()
