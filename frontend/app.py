from flask import Flask, render_template, request, redirect, url_for, session
import requests
app = Flask(__name__)

app.secret_key = "student_erp_secret"

BACKEND_URL = "http://127.0.0.1:8000"


@app.route("/")
def home():
    return redirect(url_for("login"))


# ------------------------
# LOGIN
# ------------------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]

        password = request.form["password"]

        response = requests.post(

            f"{BACKEND_URL}/auth/login",

            json={

                "username": username,

                "password": password

            }

        )

        if response.status_code == 200:

            data = response.json()

            session["token"] = data["access_token"]
            session["student_id"] = data["student_id"]
            session["username"] = data["username"]
            session["email"] = data["email"]
            session["role"] = data["role"]

            return redirect(url_for("dashboard"))



        else:

            return render_template(

                "login.html",

                error="Invalid Username or Password"

            )

    return render_template("login.html")


# ------------------------
# REGISTER
# ------------------------

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        payload = {

            "username": request.form["username"],

            "email": request.form["email"],

            "password": request.form["password"],

            "student_id": request.form["student_id"]

        }

        response = requests.post(

            f"{BACKEND_URL}/auth/register",

            json=payload

        )

        if response.status_code == 200:

            return redirect(url_for("login"))

        else:

            return render_template(

                "register.html",

                error=response.json()["detail"]

            )

    return render_template("register.html")


# ------------------------
# DASHBOARD
# ------------------------

@app.route("/dashboard")
def dashboard():

    if "token" not in session:
        return redirect(url_for("login"))

    token = session["token"]
    student_id = session["student_id"]

    headers = {
        "Authorization": f"Bearer {token}"
    }

    # ---------------- Student ----------------

    student_response = requests.get(
        f"{BACKEND_URL}/students/{student_id}",
        headers=headers
    )

    student = student_response.json()

    # ---------------- Fees ----------------

    fee_response = requests.get(
        f"{BACKEND_URL}/fees/student/{student_id}",
        headers=headers
    )

    fee = fee_response.json()

    # ---------------- Marks ----------------

    marks_response = requests.get(
        f"{BACKEND_URL}/marks/student/{student_id}",
        headers=headers
    )

    marks = marks_response.json()

    # ---------------- Calculate Average ----------------

    avg_marks = 0
    subject_count = 0

    if isinstance(marks, list) and len(marks) > 0:

        subject_count = len(marks)

        total = sum(subject["marks"] for subject in marks)

        avg_marks = round(total / subject_count, 2)

    return render_template(

        "dashboard.html",

        username=session["username"],

        email=session["email"],

        student_id=student_id,

        student=student,

        fee=fee,

        avg_marks=avg_marks,

        subject_count=subject_count
    )


#-------------------------
#PROFILE
#-------------------------
@app.route("/profile")
def profile():

    token = session.get("token")

    if not token:
        return redirect(url_for("login"))

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        f"{BACKEND_URL}/students/me",
        headers=headers
    )

    if response.status_code != 200:
        return response.text

    student = response.json()

    return render_template(
        "student_profile.html",
        student=student
    )


    
#marks 
#---------------------------

# @app.route("/marks")
# def marks():

#     token = session.get("token")

#     if not token:
#         return redirect("/login")

#     headers = {
#         "Authorization": f"Bearer {token}"
#     }

#     student_id = session.get("student_id")
#     response = requests.get(
#         f"{BACKEND_URL}/marks/student/{student_id}",
#         headers=headers
#     )

#     if response.status_code != 200:
#         return response.text

#     marks = response.json()

#     return render_template(
#         "marks.html",
#         marks=marks
#     )
    
@app.route("/marks")
def marks():

    token = session.get("token")
    student_id = session.get("student_id")

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        f"{BACKEND_URL}/marks/student/{student_id}",
        headers=headers
    )

    if response.status_code != 200:
        return response.text

    return render_template(
        "marks.html",
        marks=response.json()
    )
    
    
    
        
#fees
#----------------------------

@app.route("/fees")
def fees():

    token = session.get("token")
    student_id = session.get("student_id")

    if not token:
        return redirect(url_for("login"))

    headers = {
        "Authorization": f"Bearer {token}"
    }

    # ---------------- Fee Details ----------------

    fee_response = requests.get(
        f"{BACKEND_URL}/fees/{student_id}",
        headers=headers
    )
    print("Status Code:", fee_response.status_code)

    try:
        print("Response:", fee_response.json())
    except Exception:
        print("Response Text:", fee_response.text)

    if fee_response.status_code == 200:
        fee = fee_response.json()
    else:
        fee = {}

   
   

    print("Fee:", fee)        # ✅ ADD HERE

    # ---------------- Payment History ----------------

    payment_response = requests.get(
        f"{BACKEND_URL}/payments/student/{student_id}",
        headers=headers
    )

    if payment_response.status_code == 200:
        payments = payment_response.json()
    else:
        payments = []

    print("Payments:", payments)    # ✅ ADD HERE

    return render_template(
        "fees.html",
        fee=fee,
        payments=payments
    )
# ------------------------
# LOGOUT
# ------------------------

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))






if __name__ == "__main__":

    app.run( debug=True)