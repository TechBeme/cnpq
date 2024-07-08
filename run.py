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
JSESSIONID = config['COOKIES']['JSESSIONID']
BIGipServerpool = config['COOKIES']['BIGipServerpool']

# Configurar o cliente 2Captcha
solver = TwoCaptcha(API_KEY)

url = 'http://buscatextual.cnpq.br/buscatextual/download.do'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36',
}
cookies = {
    'JSESSIONID': config['COOKIES']['JSESSIONID'],
    'BIGipServerpool_buscatextual.cnpq.br': config['COOKIES']['BIGipServerpool'],
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        idcnpq = request.form['idcnpq']
        logging.info(f'Request feito para o idcnpq ID: {idcnpq}')

        # Resolver reCAPTCHA
        try:
            recaptcha_result = solver.recaptcha(sitekey=GOOGLE_KEY, url=url)
            if recaptcha_result['code']:
                logging.info(f'Token obtido com sucesso.')
                token = recaptcha_result['code']

            else:
                logging.error(f'Falha ao obter o token.')

            # Body da requisição para fazer o download
            files = {
                'metodo': (None, 'executarDownload'),
                'tokenCaptchar': (None, token),
                'idcnpq': (None, idcnpq),
                'g-recaptcha-response': (None, token)
            }

            # Fazer a requisição POST
            response = requests.post(url, cookies={'JSESSIONID': JSESSIONID, 'BIGipServerpool_buscatextual.cnpq.br': BIGipServerpool},
                                     headers=headers, files=files)
            logging.info(f'Resposta retornou o status: {response.status_code}')
            # Verificar se a resposta é um arquivo ZIP
            if 'application/zip' in response.headers.get('Content-Type', ''):
                with zipfile.ZipFile(io.BytesIO(response.content), 'r') as zip_ref:
                    zip_ref.extract('curriculo.xml', os.getcwd())  # Extrair apenas o curriculo.xml

                logging.info('Retornando o arquivo exportado...')
                return send_file('curriculo.xml', as_attachment=True)

            else:
                logging.error('A resposta não é um arquivo ZIP válido.')
                return 'A resposta não é um arquivo ZIP válido.'

        except Exception as e:
            logging.error(f'Erro ao conectar com 2Captcha: {str(e)}')
            return f'Erro ao conectar com 2Captcha: {str(e)}'

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)