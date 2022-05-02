# 데이터 클래스화 시키기
class Weather:
    def __init__(self, tm, totalCityName, doName, cityName, cityAreaId, kmaTci, TCI_GRADE):
        self.tm = tm
        self.totalCityName = totalCityName
        self.doName = doName
        self.cityName = cityName
        self.cityAreaId = cityAreaId
        self.kmaTci = kmaTci
        self.TCI_GRADE = TCI_GRADE
        
    @staticmethod # static method 로 만들어주는 어노테이션, self를 못쓴다.
    def dictToEntity(data):
        weather = Weather(
            data["tm"],
            data["totalCityName"],
            data["doName"],
            data["cityName"],
            data["cityAreaId"],
            data["kmaTci"],
            data["TCI_GRADE"]
        )
        return weather

