from app import create_app, db
from app.models import Student

app = create_app()

if __name__ == '__main__':
    app.run()
