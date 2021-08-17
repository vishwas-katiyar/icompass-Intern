from flask import Flask, request
# from flask_mysqldb import MySQL
app = Flask(__name__)


@app.route('/v1/sanitized/input/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        print(details['payload'])
        qry=details['payload']
        if any(item in qry.split() for item in ["'" ,'*' , "-- (--%20)", ';' , '/*' , '(' ,')' , '--' ]):
            return 'unsanitized'
        else:
            return'sanitized'

        # return 'success'
    # return render_template('index.html')


if __name__ == '__main__':
    app.run()