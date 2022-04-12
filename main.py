from flask import Flask, request, send_file
from certificate import Certificate
import os


app = Flask(__name__)


@app.route("/")
def home():
    name = request.args.get("name")
    lower = request.args.get("lower")
    upper = request.args.get("upper")
    report = Certificate(name, lower, upper)
    report.generate()
    return send_file(report.path, as_attachment=True, download_name="report.pdf")


app.run()

file_list = [file for file in os.listdir() if "pdf" in file]
for file in file_list:
    os.remove(file)
