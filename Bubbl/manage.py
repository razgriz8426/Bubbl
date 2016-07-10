import os
from app import create_app
from app.models import User
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app('default')
manager = Manager(app)
migrate = Migrate(app)




if __name__ == '__main__':
    manager.run()

