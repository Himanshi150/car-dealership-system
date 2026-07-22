"""
Seed script: creates (or promotes) a default admin account for testing.

Run this once after setting up the backend:
    python seed_admin.py

Default admin credentials (change these below if you like):
    email:    admin@dealership.com
    password: admin123
"""
from app.database import SessionLocal, engine, Base
from app import models, security

ADMIN_EMAIL = "admin@dealership.com"
ADMIN_PASSWORD = "admin123"


def seed_admin():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        user = db.query(models.User).filter(models.User.email == ADMIN_EMAIL).first()

        if user:
            user.is_admin = True
            db.commit()
            print(f"Existing user '{ADMIN_EMAIL}' promoted to admin.")
        else:
            new_admin = models.User(
                email=ADMIN_EMAIL,
                hashed_password=security.hash_password(ADMIN_PASSWORD),
                is_admin=True,
            )
            db.add(new_admin)
            db.commit()
            print(f"Admin account created: {ADMIN_EMAIL} / {ADMIN_PASSWORD}")
    finally:
        db.close()


if __name__ == "__main__":
    seed_admin()