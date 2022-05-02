# DAO(Data Access Object)
# CRUD 쿼리

from db import connect as db

# %s 사이에 (value)를 넣어서 바인딩 가능하다.
# insert_one(username="ssar", password="1234")
def insert_one(**data): # {"username":"ssar", "password":"1234"}
    sql = "INSERT INTO my_member(username, password) VALUES(%(username)s, %(password)s)"
    
    # 트랜잭션 관리
    try:
        db.cursor.execute(sql, data) # 실행
    except Exception as e: #실패시
        print(e) #오류코드 출력
        db.conn.rollback() # 롤백시키고
        return -1 # -1을 리턴
    
    db.conn.commit() #성공시 커밋
    return 1 # 1을 리턴

# SELECT는 try-catch를 안타도 된다.
# 타면 좋은데, 영속성 컨텍스트에 연결된 DB의 데이터를 select할 때,
# 해당 데이터가 영속화가 되면서 Entity가 된다.
# 이 데이터(object)를 update로 변경할 때, 트랜잭션 관리(변경감지, 더티체킹)을 해야한다.
# 변경감지는 JPA가 해준다.
def selset_all():
    sql = "SELECT * FROM my_member"
    db.cursor.execute(sql)
    rows = db.cursor.fetchall() # 데이터 받기
    return rows


def select_one(**data):
    sql = "SELECT * FROM my_member WHERE id = %(id)s"
    db.cursor.execute(sql, data)
    row = db.cursor.fetchone()  # 데이터 받기
    return row


def update_one(**data):
    sql = "UPDATE my_member SET username=%(username)s, password=%(password)s WHERE id=%(id)s"

    # 트랜잭션 관리
    try:
        db.cursor.execute(sql, data) # 실행
    except Exception as e: #실패시
        print(e) #오류코드 출력
        db.conn.rollback() # 롤백시키고
        return -1 # -1을 리턴
    
    db.conn.commit() #성공시 커밋
    return 1 # 1을 리턴


def delete_one(**data):
    sql = "DELETE FROM my_member WHERE id=%(id)s"
    
    # 트랜잭션 관리
    try:
        db.cursor.execute(sql, data)  # 실행
    except Exception as e:  # 실패시
        print(e)  # 오류코드 출력
        db.conn.rollback()  # 롤백시키고
        return -1  # -1을 리턴

    db.conn.commit()  # 성공시 커밋
    return 1  # 1을 리턴
    pass