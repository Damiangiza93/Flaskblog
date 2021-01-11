from flask import render_template, url_for, flash, redirect
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post


posts = [
    {
        'author': 'Damian Giza',
        'title': 'Blog Post 1',
        'content': 'great content',
        'date_posted': 'Januray 5, 2021'
    },
    {
        'author': 'Kasia Ku',
        'title': 'Blog Post 2',
        'content': 'better content',
        'date_posted': 'Januray 4, 2021'
    }
]



@app.route('/')
@app.route('/home')                                     # dodaje ścieżkę dla tego programu
def home():
    return render_template('home.html', posts=posts)    # dodaje wygląd z pliku home.html|posts=posts - przypisujemy do posts w html posts z tego pliku

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])                        # formularz rejestracyjny
def register():
    form = RegistrationForm()
    if form.validate_on_submit():                                       # potwierdzenie rejestracji
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')         # generowanie ukrytego hasła
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)   # tworzenie nowego usera z formularza
        db.session.add(user)                                                                        # dodanie i commit usera do db
        db.session.commit()
        flash(f'Utworzono konto {form.username.data}! Możesz się zalogować', 'success')             # flash pozwala na wyrzucenie informacji która pojawi się raz
        return redirect(url_for('login'))                        
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])                           # formularz logowania
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('Logowanie udane', 'success')
            return redirect(url_for('home'))
        else:
            flash('Logowanie nieudane. Sprawdź nazwę i hasło', 'danger')
    return render_template('login.html', title='Login', form=form)