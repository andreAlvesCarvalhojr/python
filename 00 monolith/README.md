# 🏗️ Monolith Project

Este é um projeto Django monolítico para desenvolvimento de aplicações web completas.

## 🚀 Como usar

### Executar o servidor
```bash
uv run python manage.py runserver
```

### Criar superuser
```bash
uv run python manage.py createsuperuser
```

### Criar uma nova app
```bash
uv run python manage.py startapp nome_da_app
```

### Fazer migrações
```bash
uv run python manage.py makemigrations
uv run python manage.py migrate
```

## 📁 Estrutura
```
00 monolith/
├── manage.py           # Script de gerenciamento Django
├── monolith/           # Configurações do projeto
│   ├── settings.py     # Configurações gerais
│   ├── urls.py         # URLs principais
│   ├── wsgi.py         # Deploy WSGI
│   └── asgi.py         # Deploy ASGI
├── pyproject.toml      # Dependências do projeto
└── README.md           # Este arquivo
```

## 🛠️ Tecnologias
- Django 5.2.8+
- Python 3.9+
- UV para gerenciamento de dependências