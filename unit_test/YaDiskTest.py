import requests
from urllib.parse import urlencode
class YaDiskAPI():

    url_ya = 'https://cloud-api.yandex.net/v1/disk/resources'

    def __init__(self, poligon_ya, file):
        self.poligon_ya = poligon_ya
        self.file = file

    def create_file(self):
        """
        Создание папки на яндекс диске.
        """
        params_ya = {'path': f"{self.file}"}
        headers_ya = {'Authorization': f'OAuth {self.poligon_ya}'}
        response = requests.put(f"{self.url_ya}?{urlencode(params_ya)}", headers=headers_ya)
        return response
    
if __name__ == '__main__':
    poligon = input()
    file = input()
    d = YaDiskAPI(poligon, file)
    f = d.create_file()