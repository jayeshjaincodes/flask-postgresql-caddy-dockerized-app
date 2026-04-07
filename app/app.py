from flask import Flask
from app.models import db, User
import os
import time

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    f"postgresql://{os.getenv('POSTGRES_USERNAME')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOSTNAME')}/{os.getenv('POSTGRES_DATABASE')}"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# 🔥 AUTO CREATE + SEED DATA
with app.app_context():
    for i in range(5):
        try:
            db.create_all()

            # check if table already has data
            if User.query.count() == 0:
                users = [
                    User(name="Jayesh"),
                    User(name="Docker"),
                    User(name="Flask")
                ]
                db.session.add_all(users)
                db.session.commit()
                print("Dummy data inserted")

            break
        except Exception as e:
            print("DB not ready, retrying...")
            time.sleep(2)


@app.route("/")
def home():
    users = User.query.all()
    return str([(u.id, u.name) for u in users])
