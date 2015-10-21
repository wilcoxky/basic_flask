import unittest
import coverage
import os
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from blog import app, db

# config the app
app.config.from_object(os.environ['APP_SETTINGS'])

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


@manager.command
def cov():
    """Runs the unit tests with coverage."""
    cov = coverage.coverage(
        branch=True,
        include='project/*'
    )
    cov.start()
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(tests)
    cov.stop()
    cov.save()
    print 'Coverage Summary:'
    cov.report()
    basedir = os.path.abspath(os.path.dirname(__file__))
    covdir = os.path.join(basedir, 'coverage')
    cov.html_report(directory=covdir)
    cov.erase()


if __name__ == '__main__':
    manager.run()
