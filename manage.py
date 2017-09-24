# manage.py

from flask_script import Manager

from project import app

manager = Manager(app)

@manager.command
def recreated_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
    

if __name__ == '__main__':
    manager.run()