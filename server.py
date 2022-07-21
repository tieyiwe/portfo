from statistics import mode
from flask import Flask, render_template, request,redirect
import csv
import datetime 
app = Flask(__name__)
print(__name__)

@app.route('/index.html')
def my_home():
    return render_template('index.html')

def write_to_file(data):
    with open('database.txt', mode='a') as database:
              email = data['email']
              subject = data['subject']
              message =data['message']
              file = database.write(f'\n{email} \n,{subject}\n,{message}')
              
def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
              email = data['email']
              subject = data['subject']
              message =data['message']
              logger= datetime.datetime.now()
              csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
              csv_writer.writerow([email,subject, message,logger])

#this allows pages to be added dynamically to the server we do not need to manually ad them
@app.route('/<string:page_name>')
def html_page(page_name):                       
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:  
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong.Try again!'




