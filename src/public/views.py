"""
Logic for dashboard related routes
"""
from flask import Blueprint, render_template
from .forms import vstupkarty
from ..data.database import db
from ..data.models import LogUser, karty
from sqlalchemy import func
blueprint = Blueprint('public', __name__)

@blueprint.route('/', methods=['GET'])
def index():
    return render_template('public/index.tmpl')

@blueprint.route('/kartyinput',methods=['GET', 'POST'])
def InsertLogUser():
    form = Karty()
    if form.validate_on_submit():
        karty.create(**form.data)
    return render_template("public/karty.tmpl", form=form)

@blueprint.route('/loguserlist',methods=['GET'])
def ListuserLog():
    pole = db.session.query(LogUser).all()
    return render_template("public/listuser.tmpl",data = pole)

@blueprint.route('/vystup',methods=['GET'])
def vystup():
    pole = db.session.query(karty.Cislo_Karty.label("Cislo_Karty"),func.strftime('%Y-%m-%d %H:%M', karty.TIME).label("time")).group_by(func.strftime('%Y-%m', karty.Time)).all()
    return render_template("public/vystup.tmpl",data = pole)