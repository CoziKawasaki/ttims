from flask import Blueprint

app_id = 'common'

# defined Blueprint
app = Blueprint(
    app_id, 
    __name__, 
    template_folder='./templates/' + app_id, 
    static_folder='./static'
)
