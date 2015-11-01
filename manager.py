import unittest
import os
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from app import app, db

# config the app
# app.config.from_object(os.environ['APP_SETTINGS'])

# Handle migration commands
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


# handle Testing commands
@manager.command
def test():
    """Runs the unit tests without coverage."""
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
