from flask import Blueprint , jsonify

api_bp = Blueprint(
    "api" , 
    __name__ , 
    url_prefix='/api',
    static_folder='static',
    static_url_path='static/api'    
)

@api_bp.route('/decode/<code>')
def decode(code):
    if len(code) != 20 or not code.isnumeric():
        return "invalid code"

    save_dict = dict()

    ore = int(code[:10].lstrip("0"))
    upgrade_1 = int(code[10:12].lstrip("0"))
    upgrade_2 = int(code[12:14].lstrip("0"))
    upgrade_3 = int(code[14:16].lstrip("0"))
    upgrade_4 = int(code[16:18].lstrip("0"))
    upgrade_5 = int(code[18:20].lstrip("0"))

    save_dict["ore"] = ore
    save_dict["upgrade_one"] = upgrade_1
    save_dict["upgrade_two"] = upgrade_2
    save_dict["upgrade_three"] = upgrade_3
    save_dict["upgrade_four"] = upgrade_4
    save_dict["upgrade_five"] = upgrade_5

    return jsonify(save_dict)