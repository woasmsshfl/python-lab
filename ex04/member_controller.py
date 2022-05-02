# C:/User/Administator/AppData/Local/Programs/Python/Python310/Scripts
# python -m pip install flask
# flask(java의 spring 같은 python의 프레임워크. 매우가볍다.)
# python -m 을 쓰는 이유는 환경변수를 따로 설정하지 않았을 때 Scripts 폴더로 이동하기 위해서다.
# venv 가상환경을 만들어주는 라이브러리

# python은 대문자는 class에서만 사용한다.
from flask import Flask, request, jsonify
import member_dao as dao



# python에서 class는 new 해주어야 한다.
# Flask flask = new Flask() 와 같은 명령어
flask = Flask(__name__) # 내 파일에서 받아올 것인지, 라이브러리에서 inport할것인지 정하기.

# SELECT ALL
@flask.route("/my-member") # GET
def list():
    return jsonify(dao.selset_all())

# SELECT ONE
@flask.route("/my-member/<id>") # GET
def detail(id):
    return jsonify(dao.select_one(id=id))

# DELETE
@flask.route("/my-member/<id>", methods = ['DELETE']) # DELETE
def delete(id):
    return dao.delete_one(id=id)

# UPDATE
@flask.route("/my-member/<id>", methods=['PUT']) # PUT
def update(id):
    
    # data = request.data # x-www-form-urlencoded
    data = request.get_json # apllication/json
    return dao.update_one(id=id, username=data["username"], password=data["password"])

# INSERT 
@flask.route("/my-member", methods= ['POST']) # POST
def save():
    data = request.get_json()
    return dao.insert_one(id=id, username=data["username"], password=data["password"])


flask.run(
    host = "localhost", # 0.0.0.0은 키워드값. 전세계공통 모든곳에서 접속가능하게 하는 주소경로.
    port = 5000, # 기본포트가 5000, 따로 지정하지 않으면 디폴트값이다.
    debug = True # 이 부분이 설정되면 파일 저장시 서버가 자동 리로드 된다.
) 