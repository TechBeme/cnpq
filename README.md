<div align="center">

# 🎓 Baixador de Currículo Lattes CNPq

**Ferramenta automatizada para baixar currículos Lattes do CNPq com bypass de reCAPTCHA**

[![Python](https://img.shields.io/badge/Python-3.7+-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0+-green?logo=flask)](https://flask.palletsprojects.com/)
[![2Captcha](https://img.shields.io/badge/2Captcha-API-orange)](https://2captcha.com/)
[![Licença](https://img.shields.io/badge/Licença-Proprietária-red)](LICENSE)

[Funcionalidades](#-funcionalidades-principais) • [Início Rápido](#-início-rápido) • [Instalação](#-instalação) • [Configuração](#%EF%B8%8F-configuração) • [Uso](#-uso) • [Licença](#-licença)

**Idiomas:** [🇺🇸 English](README.en.md) • [🇪🇸 Español](README.es.md)

</div>

---

## 📋 Índice

- [Visão Geral](#-visão-geral)
- [Funcionalidades Principais](#-funcionalidades-principais)
- [Stack Tecnológico](#%EF%B8%8F-stack-tecnológico)
- [Início Rápido](#-início-rápido)
- [Instalação](#-instalação)
- [Configuração](#%EF%B8%8F-configuração)
- [Uso](#-uso)
- [Deploy como Serviço](#-deploy-como-serviço)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Licença](#-licença)
- [Aviso Legal](#%EF%B8%8F-aviso-legal)

---

## 🎯 Visão Geral

O **Baixador de Currículo Lattes CNPq** é uma ferramenta automatizada projetada para baixar currículos da Plataforma Lattes do CNPq. O sistema ignora automaticamente a proteção reCAPTCHA usando o serviço 2Captcha, permitindo baixar o currículo depois que o desafio é resolvido.

**Principais capacidades:**
- Resolução automática de reCAPTCHA com integração 2Captcha
- Interface web Flask para downloads fáceis de currículos
- Gerenciamento de cookies para controle de sessão
- Extração automática de currículos em XML
- Sistema de armazenamento local para arquivos baixados
- Script de linha de comando para processamento em lote
- Suporte a serviço systemd para deploy em produção

**Casos de uso:**
- Pesquisadores acadêmicos
- Departamentos de RH
- Projetos de coleta de dados
- Análise acadêmica
- Instituições de pesquisa

---

## ✨ Funcionalidades Principais

### 🔐 Bypass de reCAPTCHA
- Resolução automática de reCAPTCHA usando API 2Captcha
- Retry quando o 2Captcha não retorna um token aceito
- Tratamento de erros e mecanismos de retry

### 🌐 Interface Web
- Formulário Flask para informar o identificador do currículo Lattes
- Status de download em tempo real
- Entrada de ID de currículo via formulário
- Servir arquivos automaticamente

### 💾 Gerenciamento de Armazenamento
- Armazenamento automático de arquivos locais na pasta `resumes/`
- Cache de arquivos para evitar downloads duplicados
- Extração de currículos XML de arquivos ZIP
- Nomenclatura organizada de arquivos com ID Lattes

### 🔄 Modos de Uso
- Interface web com Flask (`run.py`)
- Script de linha de comando (`cnpq.py`)
- Interface web alternativa (`render.py`)
- Serviço systemd para deploy em produção

### 📝 Logging
- Sistema de logging abrangente
- Rastreamento de informações de debug
- Relatórios de erros e monitoramento

---

## 🛠️ Stack Tecnológico

| Tecnologia | Versão | Propósito |
|------------|---------|----------|
| ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) | 3.7+ | Linguagem de programação principal |
| **Flask** | 3.0+ | Framework web para interface |
| **2Captcha** | Mais recente | Serviço de resolução de reCAPTCHA |
| **Requests** | Mais recente | Cliente HTTP para requisições web |
| **Gunicorn** | Mais recente | Servidor HTTP WSGI para produção |

---

## 🚀 Início Rápido

### Pré-requisitos

- Python 3.7 ou superior
- Chave API 2Captcha ([Obtenha uma aqui](https://2captcha.com/))
- ID Lattes do CNPq (número de 16 dígitos)

### 1. Clone o Repositório

```bash
git clone https://github.com/TechBeme/cnpq.git
cd cnpq
```

### 2. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 3. Configure

Copie `config.ini.example` para `config.ini` e adicione suas credenciais:

```ini
[DEFAULT]
recaptcha_key = 6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI

[TWOCAPTCHA]
API_KEY = sua_chave_api_2captcha_aqui
```

### 4. Execute a Interface Web

```bash
python run.py
```

Acesse a aplicação em `http://localhost:5000`

---

## 📦 Instalação

### Opção 1: Instalação Padrão

```bash
# Clone o repositório
git clone https://github.com/TechBeme/cnpq.git
cd cnpq

# Crie um ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Configure
cp config.ini.example config.ini
# Edite config.ini com suas credenciais

# Execute
python run.py
```

### Opção 2: Deploy em Produção

```bash
# Instale e configure como acima
# Então configure o serviço systemd

sudo cp cnpq.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable cnpq
sudo systemctl start cnpq
sudo systemctl status cnpq
```

---

## ⚙️ Configuração

### config.ini

Crie um arquivo `config.ini` baseado em `config.ini.example`:

```ini
[DEFAULT]
# Chave do site reCAPTCHA do CNPq (geralmente esta)
recaptcha_key = 6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI

[TWOCAPTCHA]
# Sua chave API do 2Captcha
API_KEY = sua_chave_api_2captcha_aqui
```

### Obtendo sua Chave API 2Captcha

1. Cadastre-se em [2Captcha](https://2captcha.com/)
2. Navegue até seu painel
3. Copie sua chave API
4. Cole no arquivo `config.ini`

### Encontrando IDs Lattes

Os IDs Lattes são números de 16 dígitos encontrados nas URLs dos currículos Lattes do CNPq:

```
http://lattes.cnpq.br/1234567890123456
                      ^^^^^^^^^^^^^^^^
                         ID Lattes
```

---

## 🎮 Uso

### Interface Web (Recomendado)

1. Inicie o servidor Flask:
   ```bash
   python run.py
   ```

2. Abra seu navegador e vá para `http://localhost:5000`

3. Digite o ID Lattes (16 dígitos)

4. Clique em "Download"

5. O arquivo XML será baixado automaticamente

**Nota:** Os arquivos baixados são armazenados na pasta `resumes/` com o formato `{id_lattes}.xml`

### Script de Linha de Comando

Para downloads únicos sem a interface web:

```bash
python cnpq.py
```

**Nota:** Edite o script para definir o ID Lattes desejado antes de executar.

### Interface Web Alternativa

Uma versão simplificada sem logging ou cache:

```bash
python render.py
```

---

## 🚀 Deploy como Serviço

### Serviço Systemd (Linux)

O arquivo `cnpq.service` incluído permite executar a aplicação como um serviço systemd.

**Instalação:**

```bash
# Copie o arquivo de serviço
sudo cp cnpq.service /etc/systemd/system/

# Atualize os caminhos no arquivo de serviço se necessário
sudo nano /etc/systemd/system/cnpq.service

# Recarregue o systemd
sudo systemctl daemon-reload

# Habilite o serviço (iniciar no boot)
sudo systemctl enable cnpq

# Inicie o serviço
sudo systemctl start cnpq

# Verifique o status
sudo systemctl status cnpq
```

**Comandos de Gerenciamento:**

```bash
# Iniciar
sudo systemctl start cnpq

# Parar
sudo systemctl stop cnpq

# Reiniciar
sudo systemctl restart cnpq

# Ver logs
sudo journalctl -u cnpq -f
```

---

## 📁 Estrutura do Projeto

```
cnpq/
├── cnpq.py               # Script de linha de comando
├── run.py                # Aplicação Flask principal com logging
├── render.py             # Aplicação Flask alternativa
├── config.ini.example    # Template de configuração
├── config.ini            # Sua configuração (ignorada pelo git)
├── cnpq.service          # Arquivo de serviço systemd
├── requirements.txt      # Dependências Python
├── templates/
│   └── index.html        # Template da interface web
├── resumes/              # Arquivos de currículo baixados
└── cnpq.log              # Logs da aplicação
```

---

## 📝 Licença

**Licença Proprietária - Todos os Direitos Reservados**

Copyright © 2026 Rafael Vieira (TechBeme)

### ❌ Restrições

- **Sem uso comercial** sem permissão explícita
- **Sem modificações** ou trabalhos derivados
- **Sem distribuição** ou sublicenciamento
- **Sem engenharia reversa**
- **Sem hospedagem pública** sem autorização

### ✅ Uso Permitido

- Visualizar código-fonte para fins educacionais
- Executar para uso pessoal e de pesquisa não comercial
- Fork para estudo pessoal apenas (não para distribuição)

### 📧 Licenciamento Comercial

Para uso comercial, soluções white-label ou desenvolvimento personalizado:

**Contato:** [contact@techbe.me](mailto:contact@techbe.me)

---

## ⚠️ Aviso Legal

Esta ferramenta é fornecida **apenas para fins educacionais e de pesquisa**.

- Este projeto é **independente** e **NÃO afiliado** ao CNPq ou ao governo brasileiro
- Os usuários são responsáveis pela conformidade com os Termos de Serviço do CNPq
- Coleta apenas dados publicamente disponíveis
- Limitação de taxa integrada para respeitar recursos do servidor
- Os usuários devem cumprir as leis de proteção de dados aplicáveis (LGPD, GDPR, etc.)
- O desenvolvedor não é responsável pelo uso indevido desta ferramenta

**Use com responsabilidade e ética.**

---

<div align="center">

**Desenvolvido por [Rafael Vieira](https://github.com/TechBeme)**

[![GitHub](https://img.shields.io/badge/GitHub-TechBeme-181717?logo=github)](https://github.com/TechBeme)
[![Fiverr](https://img.shields.io/badge/Fiverr-Tech__Be-1DBF73?logo=fiverr)](https://www.fiverr.com/tech_be)
[![Upwork](https://img.shields.io/badge/Upwork-Profile-14a800?logo=upwork)](https://www.upwork.com/freelancers/~01f0abcf70bbd95376)
[![Email](https://img.shields.io/badge/Email-contact@techbe.me-EA4335?logo=gmail)](mailto:contact@techbe.me)

</div>
