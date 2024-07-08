from twocaptcha import TwoCaptcha
import configparser
import requests
import re



config = configparser.RawConfigParser()
config.read('config.ini')

# Dados de configuração do 2Captcha
API_KEY = config['TWOCAPTCHA']['API_KEY']
GOOGLE_KEY = config['DEFAULT']['recaptcha_key']

# Configurar o cliente 2Captcha
solver = TwoCaptcha(API_KEY)

url = 'https://buscatextual.cnpq.br/buscatextual/download.do'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36',
}
cookies = {
    'JSESSIONID': config['COOKIES']['JSESSIONID'],
    'BIGipServerpool_buscatextual.cnpq.br': config['COOKIES']['BIGipServerpool'],
}

try:
    recaptcha_result = solver.recaptcha(sitekey=GOOGLE_KEY, url=url)
    if recaptcha_result['code']:
        token = recaptcha_result['code']
        print(f"Token encontrado, baixando o arquivo...")

    # Body of the request (in a dictionary format)
    files = {
        'metodo': (None, 'executarDownload'),
        'tokenCaptchar': (None, token),
        'idcnpq': (None, '7583551276044375'),
        'g-recaptcha-response': (None, token)
    }

    response = requests.post(url, cookies=cookies, headers=headers, files=files)

    if 'application/zip' in response.headers.get('Content-Type', ''):
        filename = re.search(r'filename=([^;]+)', response.headers.get('Content-Disposition', '')).group(1)
        
        # Salva o conteúdo do arquivo ZIP
        with open(filename, 'wb') as f:
            f.write(response.content)

        #if 'application/zip' in response.headers.get('Content-Type', ''):
        #    with zipfile.ZipFile(io.BytesIO(response.content), 'r') as zip_ref:
        #        zip_ref.extractall(os.getcwd())
        
        print(f'Arquivo ZIP baixado e salvo como: {filename}')
    else:
        print('A resposta não é um arquivo ZIP válido.')

except Exception as e:
    print('Erro ao conectar com 2Captcha:', str(e))