from flask import Flask, render_template, request, send_file
from twocaptcha import TwoCaptcha
import configparser
import requests
import zipfile
import logging
import io
import os



# Configurar o logger
logging.basicConfig(filename='cnpq.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

app = Flask(__name__)

# Carregar configurações do arquivo config.ini
config = configparser.RawConfigParser()
config.read('config.ini')

# Configurações do 2Captcha e CNPQ
API_KEY = config['TWOCAPTCHA']['API_KEY']
GOOGLE_KEY = config['DEFAULT']['recaptcha_key']
solver = TwoCaptcha(API_KEY)

# Verificar se a pasta 'resumes' existe, se não, criar
resumes_folder = os.path.join(os.getcwd(), 'resumes')
os.makedirs(resumes_folder, exist_ok=True)

url = 'http://buscatextual.cnpq.br/buscatextual/download.do'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36',
}

def fetch_cookies():
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        cookies_list = response.headers.get('Set-Cookie', '')
        jsessionid = next((s.split('=')[1].split(';')[0] for s in cookies_list.split(', ') if s.startswith('JSESSIONID=')), None)
        bigip_serverpool = next((s.split('=')[1].split(';')[0] for s in cookies_list.split(', ') if s.startswith('BIGipServerpool_buscatextual.cnpq.br=')), None)
        if jsessionid and bigip_serverpool:
            logging.info(f'Cookies obtidos com sucesso.')
            return {'JSESSIONID': jsessionid, 'BIGipServerpool_buscatextual.cnpq.br': bigip_serverpool}
        else:
            raise Exception("Não foi possível obter os cookies necessários.")
    except requests.RequestException as e:
        raise Exception(f"Failed to fetch cookies: {e}")

def Resolve_reCAPTCHA():
    try:
        recaptcha_result = solver.recaptcha(sitekey=GOOGLE_KEY, url=url)
        if recaptcha_result['code']:
            logging.info(f'Token obtido com sucesso.')
            return recaptcha_result['code']
        else:
            raise Exception("Falha ao obter o token.")
    except requests.RequestException as e:
        raise Exception(f"Failed to Resolve reCAPTCHA: {e}")
    
def fetch_cnpq(idcnpq, token, cookies):
    files = {
        'metodo': (None, 'executarDownload'),
        'tokenCaptchar': (None, token),
        'idcnpq': (None, idcnpq),
        'g-recaptcha-response': (None, token)
    }
    try:
        response = requests.post(url, cookies=cookies, headers=headers, files=files)
        response.raise_for_status()
        if 'application/zip' in response.headers.get('Content-Type', ''):
            logging.info(f'Resposta retornou um ZIP válido.')
            return response.content
        else:
            raise Exception("Resposta não retornou um ZIP válido.")
    except requests.RequestException as e:
        raise Exception(f"Failed to fetch cnpq: {e}")
    
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            idcnpq = request.form['idcnpq']

            # Verificar se o arquivo já existe na pasta
            file_path = os.path.join(resumes_folder, f'{idcnpq}.xml')
            if os.path.exists(file_path):
                logging.info(f'Arquivo {idcnpq}.xml já existe. Retornando arquivo existente.')
                return send_file(file_path, as_attachment=True)
            
            cookies = fetch_cookies()
            token = Resolve_reCAPTCHA()
            ZIP_file = fetch_cnpq(idcnpq, token, cookies)
            
            with zipfile.ZipFile(io.BytesIO(ZIP_file), 'r') as zip_ref:
                zip_ref.extract('curriculo.xml', resumes_folder)  # Extrair apenas o curriculo.xml

                # Renomear o arquivo curriculo.xml para o nome do idcnpq
                os.rename(os.path.join(resumes_folder, 'curriculo.xml'), os.path.join(resumes_folder, f'{idcnpq}.xml'))
                logging.info(f"Arquivo extraído e renomeado para: '{idcnpq}.xml'.")

                logging.info('Retornando o arquivo exportado...')
                return send_file(os.path.join(resumes_folder, f'{idcnpq}.xml'), as_attachment=True)

        except Exception as e:
            return f'An unexpected error occurred: {str(e)}'

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)