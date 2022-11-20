from flask import Flask, render_template, request, json
from requests import get
from datetime import datetime as dt

# functions
from website_basic_functions import get_details

app = Flask(__name__)

datapoint = 'https://api.npoint.io/a851943134af3d5f028a'
data = get(datapoint).json()

changing_vars = {'CURRENT_YEAR': dt.now().year,
                 'support_email': 'rajdwivedipc@gmail.com'}


@app.route('/')
def homepage():
    return render_template('pages/resume.html', changing_vars=changing_vars)


@app.route('/view_post/<puid>')
def view_post(puid: int):
    for post in data:
        if post['puid'] == puid:
            return render_template('pages/post.html', post_data=post, changing_vars=changing_vars)


@app.route('/contact', methods=['GET', 'POST'])  # get method needs to be on the list for normal page to open
def contact_me():
    if request.method == 'POST':
        get_details(request.form.to_dict())
        # with open('file.json', 'w') as f:  # dump the data into a file
        return render_template('pages/contact.html', changing_vars=changing_vars, usr_feedback="form-sent")
    else:
        return render_template('pages/contact.html', changing_vars=changing_vars)


@app.route('/elements-preview/')
def elements_preview():
    return render_template('pages/post-elements.html', changing_vars=changing_vars)


# @app.route('/send-mail', )
# def send_contact_mail():
#     print(request.form['email'], request.form['message'], request.form['name'])
#     return homepage

# view CV

@app.route('/raj/resume')
def view_cv():
    return render_template('pages/resume.html', changing_vars=changing_vars)



if __name__ == 'main':
    app.run(host="0.0.0.0", port=5000, debug=True)

