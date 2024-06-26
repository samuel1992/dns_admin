import pytest

from app import create_app

app = create_app()


@pytest.fixture
def db():
    from extensions import db

    with app.app_context():
        db.create_all()
        yield db
        db.drop_all()
        db.session.commit()


@pytest.fixture
def client():
    from extensions import db

    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()
        db.session.commit()
