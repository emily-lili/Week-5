#import 
from flask import Blueprint, render_template
site = Blueprint('site', __name__, template_folder='site_templates')

#define webpage
@site.route('/')
def home():
    return render_template('index.html')

#second route
def profile():
    return render_template('profile.html')