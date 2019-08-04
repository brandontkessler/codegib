import unittest
from flask import current_app
from app import create_app, db
from app.models import User, Blog


class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_blogging_capabilities(self):
        u1 = User(email='test1@gmail.com', password='dog',
                confirmed=True, blog_priv=True, admin_priv=True)
        u2 = User(email='test2@gmail.com', password='dog',
                confirmed=True, blog_priv=True, admin_priv=False)
        u3 = User(email='test3@gmail.com', password='dog',
                confirmed=True, blog_priv=False, admin_priv=True)
        u4 = User(email='test4@gmail.com', password='dog',
                confirmed=False, blog_priv=True, admin_priv=False)

        db.session.add_all([u1, u2, u3, u4])

        # Create posts
        blog1 = Blog(title='ablogtitle1', _content='thisiscontent',
                    headline='headliner', tags='all, python, javascript',
                    user_id=u1.id)
        blog2 = Blog(title='ablogtitle2', _content='thisiscontent',
                    headline='headliner', tags='all, python, javascript',
                    user_id=u2.id)
        blog3 = Blog(title='ablogtitle3', _content='thisiscontent',
                    headline='headliner', tags='all, python, javascript',
                    user_id=u3.id)
        blog4 = Blog(title='ablogtitle4', _content='thisiscontent',
                    headline='headliner', tags='all, python, javascript',
                    user_id=u4.id)

        for blog in [blog1, blog2, blog3, blog4]:
            db.session.add(blog)
            db.session.commit()

        self.assertTrue(Blog.query.filter_by(title='ablogtitle1').first() is not None)
        self.assertTrue(Blog.query.filter_by(title='ablogtitle2').first() is not None)
        self.assertTrue(Blog.query.filter_by(title='ablogtitle3').first() is not None)
        self.assertTrue(Blog.query.filter_by(title='ablogtitle4').first() is not None)    
