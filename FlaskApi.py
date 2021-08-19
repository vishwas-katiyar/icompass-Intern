from os import abort
from flask import Flask, request, abort
app = Flask(__name__)


@app.route('/v1/sanitized/input/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        print(details['input'])
        qry=details['input']
        if any(item in qry.split() for item in ["'" ,'*' , "-- (--%20)", ';' , '/*' , '(' ,')' , '--' ]):
            print(qry.split())
            return {"Code":200, "Message":"unsanitized"},200
        else:
            return {"Code":404,"Message":"sanitized"},200
    else:
        return{"Code":404,"Message":"Not Post Method"},404




        # return 'success'
    

if __name__ == '__main__':
    app.run()