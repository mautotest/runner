

def get_current_app():
    from flask import current_app
    from app import app
    ctx = app.app_context()
    ctx.push()
    return current_app