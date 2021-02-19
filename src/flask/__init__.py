from markupsafe import escape
from markupsafe import Markup
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

'''
app 总体流程
blueprints  
config    配置
ctx       web会话
globals   active context 的全局代理对象比如g, session, request等
helpers   各种工具
logging   werkzeug 的代理日志
blinker   基于blinker实现的信号
templating  基于jinja2的桥接
views     类似django的基于类的视图
cli       命令行工具，是在__main__.py 中于__name__ 之下载入

__version__ = ''  挺好玩
'''

from . import json          # 一个包，调用里面的__init__.py  里面有个__all__ = ['', '']
from .app import Flask      # 当前目录
from .app import Request
from .app import Response
from .blueprints import Blueprint
from .config import Config
from .ctx import after_this_request
from .ctx import copy_current_request_context
from .ctx import has_app_context
from .ctx import has_request_context
from .globals import _app_ctx_stack
from .globals import _request_ctx_stack
from .globals import current_app
from .globals import g
from .globals import request
from .globals import session
from .helpers import flash
from .helpers import get_flashed_messages
from .helpers import get_template_attribute
from .helpers import make_response
from .helpers import safe_join
from .helpers import send_file
from .helpers import send_from_directory
from .helpers import stream_with_context
from .helpers import url_for
from .json import jsonify
from .signals import appcontext_popped
from .signals import appcontext_pushed
from .signals import appcontext_tearing_down
from .signals import before_render_template
from .signals import got_request_exception
from .signals import message_flashed
from .signals import request_finished
from .signals import request_started
from .signals import request_tearing_down
from .signals import signals_available
from .signals import template_rendered
from .templating import render_template
from .templating import render_template_string

__version__ = "2.0.0.dev"
