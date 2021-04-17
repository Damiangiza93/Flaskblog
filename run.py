from flaskblog import create_app

app = create_app()

if __name__ == '__main__':                          # pozwala na odpalenie komendą python flaskblog.py
    app.run(debug=False)

