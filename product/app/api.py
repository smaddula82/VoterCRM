from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api


application = Flask(__name__)
application.secret_key = 'flask-VoterCRM-1234'
api = Api(application)  # Flask restful wraps Flask app around it.

application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db/votercrm'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(application)

class States(db.Model):
    __tablename__ = 'states'

    state_code = db.Column(db.String(100), primary_key=True)
    state_name = db.Column(db.String(50))
    country = db.Column(db.String(50))

    def __init__(self, state_code, state_name, country):
        self.state_code = state_code
        self.state_name = state_name
        self.country = country

@application.route('/api/states')
def get_all_states():
    states = States.query.all()
    if states:
        state_list=[]
        for state in states:
            print(f'state name: {state.state_name}')
            state_dict={}
            state_dict['state_code']=state.state_code
            state_dict['state_name']=state.state_name
            state_dict['country']=state.country
            state_list.append(state_dict)
        return {"states": state_list}
    else:
        return {"message": "No states Available"}


if __name__ == "__main__":
    application.run(host='0.0.0.0',debug=True, port=8000)
