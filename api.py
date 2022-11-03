import random
from flask import request
import uuid
import requests
from flask import Blueprint , jsonify
from base64 import encode

api_bp = Blueprint(
    "nba" , 
    __name__ , 
    url_prefix='/nba',
    static_folder='static',
    static_url_path='static/nba'    
)

url = "https://free-nba.p.rapidapi.com/teams"

headers = {
	"X-RapidAPI-Key": "9275b62a1fmsh3b832340dafb492p1abc77jsn58ef554feee6",
	"X-RapidAPI-Host": "free-nba.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

response.raise_for_status()
if response.status_code != 204:
    teams_json = response.json()['data']

teams_dict = {}

logos = [
    'https://user-images.githubusercontent.com/109186517/199640420-fa3c7b28-7ab6-4ef7-b7ed-b7644d7028fb.png',
    'https://user-images.githubusercontent.com/109186517/199640459-51054515-df20-4820-ba25-f9eb4965128b.png',
    'https://user-images.githubusercontent.com/109186517/199640492-d49e1e46-3ac7-41cc-95ed-e4c49b51d04e.png',
    'https://user-images.githubusercontent.com/109186517/199640537-a3421be9-8ca7-46e5-b24f-41d43b169060.png',
    'https://media.discordapp.net/attachments/902298316094717963/1036481822856577035/bulls.png',
    'https://cdn.discordapp.com/attachments/902298316094717963/1036481856662667344/cavaliers.png',
    'https://cdn.discordapp.com/attachments/902298316094717963/1036481903387217940/mavs.png',
    'https://cdn.discordapp.com/attachments/902298316094717963/1036482021691768883/nuggets.png',
    'https://cdn.discordapp.com/attachments/902298316094717963/1036482143838273607/pistons.png',
    'https://cdn.discordapp.com/attachments/902298316094717963/1036482569593692170/image-removebg-preview_1.png',
    'https://cdn.discordapp.com/attachments/902298316094717963/1036482827660828712/rockets.png',
    'https://cdn.discordapp.com/attachments/902298316094717963/1036483337570750475/image-removebg-preview_2.png',
    'https://cdn.discordapp.com/attachments/902298316094717963/1036483452196892682/clippers.png',
    'https://cdn.discordapp.com/attachments/902298316094717963/1036484104180465774/image-removebg-preview_3.png',
    'https://cdn.discordapp.com/attachments/902298316094717963/1036484246862319626/image-removebg-preview_4.png',
    'https://cdn.discordapp.com/attachments/902298316094717963/1036484797444399124/image-removebg-preview_5.png',
    'https://cdn.discordapp.com/attachments/902298316094717963/1036485074893414420/image-removebg-preview_6.png',
    'https://cdn.discordapp.com/attachments/902298316094717963/1036485189418889257/twolves.png',
    'https://cdn.discordapp.com/attachments/902298316094717963/1036485551278260324/unknown.png',
    'https://media.discordapp.net/attachments/902298316094717963/1036486385927983134/knicks.png?width=827&height=671',
    'https://cdn.discordapp.com/attachments/902298316094717963/1036486892918689823/image-removebg-preview_7.png',
    'https://media.discordapp.net/attachments/902298316094717963/1036487041409613874/magic.png?width=671&height=671',
    'https://cdn.discordapp.com/attachments/902298316094717963/1036493788971028510/sixers.png',
    'https://cdn.discordapp.com/attachments/902298316094717963/1036493947507331142/unknown.png',
    'https://cdn.discordapp.com/attachments/902298316094717963/1036494365134180382/image-removebg-preview_8.png',
    'https://cdn.discordapp.com/attachments/902298316094717963/1036494443907395595/kings.png',
    'https://cdn.discordapp.com/attachments/902298316094717963/1036494609121034302/spurs.png',
    'https://cdn.discordapp.com/attachments/902298316094717963/1036494778323456030/image-removebg-preview_9.png',
    'https://cdn.discordapp.com/attachments/902298316094717963/1036495011992309820/jazz.webp',
    'https://media.discordapp.net/attachments/902298316094717963/1036495113607729192/wizards.png?width=671&height=671',
]

for i, item in enumerate(teams_json):
    teams_dict[i] = {"likes": 0, "dislikes": 0, "name": item['full_name'].split()[-1],
                     "abbreviation": item['abbreviation'], "division": item["division"], "city": item['city'], "logo": logos[i]}


@api_bp.route('/')
def index():
    return "TEAM BRO BRO YOU ALREADY KNOW KNOW WE ARE SO FLY WE ALWAYS GO GO"


@api_bp.route('/like', methods=["POST"])
def like():
    data = request.json
    id = data["id"]
    teams_dict[id]["likes"] += 1
    return {"likes": teams_dict[id]["likes"]}


@api_bp.route('/dislike', methods=["POST"])
def dislike():
    data = request.json
    id = data["id"]
    teams_dict[id]["dislikes"] += 1
    return {"dislikes": teams_dict[id]["dislikes"]}


@api_bp.route('/teams', methods=["GET"])
def teams():
    return teams_dict