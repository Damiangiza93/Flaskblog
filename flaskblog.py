from flask import Flask, escape, request, render_template

app = Flask(__name__)

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
@app.route('/home')                                 # dodaje ścieżkę dla tego programu
def home():
    return render_template('home.html', posts=posts)    # dodaje wygląd z pliku home.html|posts=posts - przypisujemy do posts w html posts z tego pliku

@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':                          # pozwala na odpalenie komendą python flaskblog.py
    app.run(debug=True)

