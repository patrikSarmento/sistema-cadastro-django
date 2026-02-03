"""
arquivo principal de configuracoes do projeto django
aqui ficam todas as definicoes que controlam como o sistema funciona
"""

# importa Path para trabalhar com caminhos de pastas e arquivos
from pathlib import Path

# define o diretorio base do projeto
# serve como referencia para outros caminhos
BASE_DIR = Path(__file__).resolve().parent.parent


# chave secreta usada pelo django para seguranca interna
# nao deve ser exposta em ambiente de producao
SECRET_KEY = 'django-insecure-v(h54e$9q^19m^0&o+8b-4imf&b@=6#^^%spt%x-hx^&t#(&ig'

# ativa ou desativa o modo debug
# quando true mostra erros detalhados
DEBUG = True

# define quais enderecos podem acessar o projeto
# vazio geralmente usado apenas em desenvolvimento
ALLOWED_HOSTS = []


# lista de aplicativos instalados no projeto
# inclui apps padrao do django e o app clientes
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'clientes',
]

# middlewares sao camadas que processam requisicoes e respostas
# cuidam de seguranca sessoes autenticacao entre outros
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# aponta para o arquivo principal de urls do projeto
ROOT_URLCONF = 'core.urls'

# configuracoes do sistema de templates html
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # diretorios extras de templates caso existam
        'DIRS': [],
        # permite buscar templates dentro dos apps
        'APP_DIRS': True,
        'OPTIONS': {
            # adiciona informacoes padrao que ficam disponiveis nos templates
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# configuracao usada por servidores web para rodar o projeto
WSGI_APPLICATION = 'core.wsgi.application'


# configuracao do banco de dados
# neste caso usando postgresql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dados_db',
        'USER': 'postgres',
        'PASSWORD': '080300',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# define para onde o usuario e enviado quando precisa fazer login
LOGIN_URL = 'login'

# pagina padrao que exige login
LOGIN_REQUIRED_URL = 'clientes'

# pagina para onde o usuario vai apos sair do sistema
LOGOUT_REDIRECT_URL = 'login'


# validacoes de senha do django
# garantem senhas mais seguras
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# configuracoes de idioma e fuso horario
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# configuracoes de arquivos estaticos como css js e imagens
STATIC_URL = '/static/'

# pastas onde o django deve procurar arquivos estaticos
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
