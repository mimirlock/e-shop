from flask import Blueprint

admin_bp = Blueprint(
    'admin', 
    _name_, 
    template_folder='../../templates/admin'
    )
from . import routes