import www.orm
from www.models import User, Blog, Comment

def test():
    yield from www.orm.create_pool(loop=1,user='python', password='python', database='python')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()

for x in test():
    pass