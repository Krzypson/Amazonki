from flask import Flask, render_template
import pandas as pd
import random

test_dataframe = pd.read_csv(r"./env/src/site_text/test.csv")
Title_value = test_dataframe.loc["Head_Title"]["value"]
paragraph1_value = test_dataframe.loc["paragraph1"]["value"]
print(test_dataframe)
print(Title_value)
app = Flask(__name__)

@app.route("/")
def test():
    return render_template("test.html", Head_Title = Title_value, paragraph1 = paragraph1_value)