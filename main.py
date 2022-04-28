from flask.views import MethodView
from wtforms import Form
from flask import Flask, render_template


app = Flask(__name__)

class HomePage(MethodView):
    def get(self):
        # return '<h1>Hello 11546546 hello hello hello</h1>'
        return render_template('index.html')

class BillFormPage(MethodView):
    def get(self):
        return '<h1>I am the bill form page!</h1>'

class ResultsPage(MethodView):
    pass

class BillForm(Form):
    pass


#routing
app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill_form', view_func=BillFormPage.as_view('bill_form_page'))

app.config['TEMPLATES_AUTO_RELOAD'] = True
# app.run(debug=True)
# app.run(port=5050)
app.run(debug=True, port=5051)