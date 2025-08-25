from flask import Flask, render_template, jsonify, request, Response, url_for
from database import Job, session, add_form


app = Flask(__name__)


@app.route("/")
def home():
    jobs = session.query(Job).all()
    return render_template("home.html", jobs=jobs)


@app.route("/job/<id>")
def show_job(id):
    job = session.get(Job, id)
    if job:
        dict_job = job.to_dict()
        return render_template("job_page.html", job=dict_job)
    return Response("Job not found.", status=404)


@app.route("/job/<id>/apply", methods=['POST'])
def apply_to_job(id):
    data = request.form
    add_form(data, id)
    return render_template("application_submition.html", application=data)


@app.route("/job/<id>/form", methods=['GET'])
def application_form(id):
    job = session.get(Job, id)
    if job:
        dict_job = job.to_dict()
        return render_template("application_form.html", job=dict_job)
    return Response("Job not found.", status=404)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/contact/submit", methods=['POST'])
def submit_contact():
    # Here you can add code to handle the form data,
    # like sending an email or saving it to a database.
    return render_template("contact_submition.html")


if __name__ == "__main__":
    app.run(debug=True)
