try:
    from flask import Flask
    from flask import Flask, request, \
        render_template, redirect, url_for,\
        session, send_file

    # Flask WTF FORMS
    from flask_wtf import FlaskForm,RecaptchaField
    from wtforms import (StringField,SubmitField,
                         DateTimeField, RadioField,
                         SelectField,TextAreaField, DateField)

    from wtforms.validators import DataRequired

except Exception as e:
    print("Some Modules are Missing {}".format(e))


app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"

app.config["RECAPTCHA_PUBLIC_KEY"] = "KEY GOES HERE "
app.config["RECAPTCHA_PRIVATE_KEY"] = "PRIVATE KEY GOES HEREE"


class Widgets(FlaskForm):
    recaptcha = RecaptchaField()

    name = StringField(label="Name", validators=[DataRequired()])

    radio = RadioField(label ="Please select Your Programming language ",
                       choices=[('Python', "Python"), ["C++","C++"]])

    select = SelectField(label='select', choices=[("1", "WebApp"), ("2","Web Scrapping")])
    comments = TextAreaField(label="comments")
    date = DateTimeField(label="Birthday" , format='%Y-%m-%d')

    submit = SubmitField(label="Submit")


@app.route("/", methods=("GET", "POST"))
def home():
    form = Widgets()
    if request.method == "POST":
        if form.validate_on_submit():
            session["name"] = form.name.data
            print("Name ENtered {}".format(form.name.data))
            return redirect(url_for('result'))

    if request.method == "GET":
        return render_template("list.html", form=form)


@app.route("/result", methods=["GET", "POST"])
def result():
    return "Thanks {}".format(session["name"])


if __name__ == "__main__":
    app.run(debug=True)
