from flask import Blueprint, render_template

bp = Blueprint("main", __name__)

#------------ HOME ------------"
@bp.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")
#------------ LOGIN ------------"
@bp.route("/login")
def login():
    return "Implement Login"
#------------ REGISTER ------------"
@bp.route("/register")
def register():
    return "Implement Register"
#------------ logout ------------"
@bp.route("/logout")
def logout():
    #TODO MAKE SURE TO CLEAR SESSION 
    return "Implement Logout"
#------------ SPOTIFY DATA ROUTES ------------
@bp.route("/callback")
def callback():
    print("callback")
    return "Implement Callback"
    