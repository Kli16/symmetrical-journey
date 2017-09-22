from flask import Flask

my_app = Flask(__name__)

@my_app.route('/')
@my_app.route('/home')
def root():
    return "<h1> HOMEEEEE </h1>";

@my_app.route('/bloop')
def bloop():
    return ">:(";

@my_app.route('/secretpage')
def secret():
    return "u found the secret page :O ";

if __name__ == '__main__':
    my_app.debug = True;
    my_app.run()
