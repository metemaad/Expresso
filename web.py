#!flask/bin/python
from flask import Flask, render_template, redirect, url_for, request, flash, send_from_directory
from flask import Flask
from flask.ext.jsonpify import jsonify
import numpy as np

app =Flask(__name__)


@app.route('/score')
def b():
    my_var = request.args.get('data', None)
    t = request.args.get('t', None)
    t=float(t.encode('utf-8'))

    my_var=my_var.encode('utf-8')
    y=np.array(my_var.split(',')).astype(np.float)
    numberofFrame=y.size
    tmp=y[:numberofFrame]
    err=np.sum(tmp[tmp>t])
    good=np.sum(tmp[tmp<=t])
    finalScore=(good)/(err*4+good)
    return str(finalScore)
#sample call http://127.0.0.1:5000/score?data=0.1,0.3,0.24,0.65&t=0.5
if __name__ == '__main__':
    app.run(debug=True)



