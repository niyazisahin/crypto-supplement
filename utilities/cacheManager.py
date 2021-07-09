"""
Programın kullandığı kalıcı verileri saklamak ve yönetmek için fonksiyonlar.
"""
import json
from os import path


# __file__ Bu dosyanın bulunduğu yer.
file_path = path.dirname(path.abspath(__file__))

# Yoksa cache.json dosyası oluşturuluyor
f = open(path.join(file_path,"cache.json"), "a")
if(not path.getsize(path.join(file_path,"cache.json"))):
    f.write("{}")
f.close()

def create_key(key: str, value: str = None):
    "Opsiyonel bir değerle yeni bir key oluştur."
    f = open("cache.json", "r")
    tmp = json.loads(f.read())
    tmp[key] = value
    f.close()

    with open("cache.json", "w") as f:
        json.dump(tmp, f)

def delete_key(key):
    "Bir key ve değerini siler."
    f = open("cache.json", "r")
    tmp = json.loads(f.read())
    tmp.pop(key, None)
    f.close()

    with open("cache.json", "w") as f:
        json.dump(tmp, f)

def read_value(key: str):
    """
    Eğer belirtilen anahtar json dosyasında varsa
    o değer okunur yoksa None dönderir.
    """
    with open("cache.json", "r") as f:
        tmp = json.loads(f.read())

        # Get key bulamadığında None dönderiyor
        # Ama tmp[key] şeklinde yapılsaydı Exception hatası verirdi
        
        return tmp.get(key)


def write_value(key: str,value: str):
    """
    Eğer belirtilen anahtar json dosyasında varsa
    o değer değiştirlir yoksa None dönderir.
    """
    with open("cache.json", "r") as f:
        tmp = json.loads(f.read())
        
    if tmp.get(key) != None:
    
        tmp[key] = value        
        with open("cache.json", "w") as f:
            json.dump(tmp, f)
    
    else:
        return None
        

# Fonksiyon Testleri
if __name__ == "__main__":
    print(read_value("test"))
    write_value("test", 1)
    create_key("test2")
    # delete_key("test2")