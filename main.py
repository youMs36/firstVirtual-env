
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return 'here I am'

@app.get('/about')
def about():
    return {'data':'about page'}

@app.get('/contact-us')
@app.get('/contact-me')
def contact():
    return {'data': {
                    'name' : 'Umesh',
                     'adddress' : 'pune',
                     'contact' : '8793449336'
                    }
            }