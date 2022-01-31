import aiohttp_jinja2
import jinja2
from aiohttp import web

from aiohttpdemo_polls.db import pg_context
from aiohttpdemo_polls.middlewares import setup_middlewares
from aiohttpdemo_polls.routes import setup_routes, setup_static_routes
from aiohttpdemo_polls.settings import config, BASE_DIR

app = web.Application()
app['config'] = config
setup_middlewares(app)
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(BASE_DIR / 'aiohttpdemo_polls' / 'templates')))
setup_routes(app)
setup_static_routes(app)
app.cleanup_ctx.append(pg_context)
web.run_app(app)

