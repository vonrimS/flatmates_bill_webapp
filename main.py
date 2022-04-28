from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from flatmates_bill import flat


app = Flask(__name__)

class HomePage(MethodView):
    def get(self):
        # return '<h1>Hello 11546546 hello hello hello</h1>'
        return render_template('index.html')

class BillFormPage(MethodView):
    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html', billform=bill_form)

class ResultsPage(MethodView):
    def post(self):
        billform = BillForm(request.form)

        the_bill = flat.Bill(int(billform.amount.data), int(billform.period.data))
        flatmate1 = flat.Flatmate(billform.name1.data, int(billform.days_in_house1.data))
        flatmate2 = flat.Flatmate(billform.name2.data, int(billform.days_in_house2.data))

        return f'{flatmate1.name} pays {flatmate1.pays(the_bill, flatmate2)}'


class BillForm(Form):
    amount = StringField('Bill Amount: ')
    period = StringField('Bill Period: ')
    name1 = StringField('Name: ')
    days_in_house1 = StringField('Days in the house: ')
    name2 = StringField('Name: ')
    days_in_house2 = StringField('Days in the house: ')
    button = SubmitField('Calculate')


# routing
app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill_form', view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))

app.config['TEMPLATES_AUTO_RELOAD'] = True
# app.run(debug=True)
# app.run(port=5050)
app.run(debug=True, port=5051)