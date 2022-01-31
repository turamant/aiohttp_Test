from aiohttpdemo_polls.settings import BASE_DIR
from views import index, poll

def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/poll', poll)


def setup_static_routes(app):
    app.router.add_static('/static/', path=BASE_DIR / 'static', name='static')

