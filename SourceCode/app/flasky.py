import os
from app import create_app, db
from app.models import User, Whiskys

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

#Integration with the Python shell
@main.shell_context_processor
def make_shell_context():
	return dict(db=db, User=User, Whiskys=Whiskys)

#unit test launcher command
@app.cli.command()
def test():
    """Run the unit tests. """
    import unittest
    test = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
