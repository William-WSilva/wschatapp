# WsChatApp
### Descrição


 📜 Este é um aplicativo de postagem de imagens desenvolvido utilizando HTML, CSS, Django e Docker, com integração de um banco de dados PostgreSQL. Possui mais de 10 telas, incluindo funcionalidades como login, cadastro, publicação de posts, alteração de dados cadastrais, busca de usuários, rede de seguidores, postagens salvas, entre outras.

<a href="https://projeto-wschatapp-8e4668852be4.herokuapp.com/" target="_blank">
Acesse o app: https://projeto-wschatapp-8e4668852be4.herokuapp.com/
</a>
<hr>
<img src="./setup/static/assets/img/wschatapp4.png" width="600px" height="800px" alt="">

 ## ⚛️ Tecnologias Utilizadas
1. HTML
2. CSS
3. Django
4. Docker
5. PostgreSQL
6. Heroku (para deploy).

## Funcionalidades Principais

1. **Autenticação e Segurança**

    - 💡 Utilização dos recursos de segurança do Django, incluindo:

        - Autenticação de usuários
        - Autorização de acesso a diferentes recursos
        - Proteção contra CSRF (Cross-Site Request Forgery)
        - Entre outros recursos de segurança disponibilizados pelo framework.

2. **Docker e Segurança**

    - Utilização de containers Docker para isolamento e facilitar a implantação do aplicativo.

    - Vantagens incluem:
        - Portabilidade
        - Consistência de ambiente entre - - desenvolvimento e produção
        - Controle de recursos e escalabilidade
        - Isolamento de processos e segurança - aprimorada.

 3. **Integração com Back-end e Validação de Formulários**

    - Conexão entre o front-end e back-end utilizando Django para fornecer uma experiência contínua ao usuário.
    - Implementação de validações de formulários para garantir a integridade dos dados recebidos.

4. **Deploy na Plataforma Heroku**

    - O aplicativo foi implantado com sucesso na plataforma Heroku, permitindo acesso online ao projeto.

## Deploy no Heroku
1. Configuração Inicial

    - Faça login na sua conta do Heroku.
    - Crie um novo aplicativo no painel do Heroku.

2. **Configuração das Variáveis de Ambiente no Heroku**

    - No painel do seu aplicativo no Heroku, navegue para a seção de configurações.
    - Configure as variáveis de ambiente necessárias conforme o seu projeto (chaves de acesso, configurações específicas). Isso pode incluir informações do banco de dados, chaves de API, etc.

3. **Push do Projeto para o Heroku**


```
git remote add heroku https://git.heroku.com/seu-aplicativo.git
git push heroku main
```

4. Acesso ao Container no Heroku 

    - Após o deploy bem-sucedido, acesse um terminal e execute:

```
heroku run bash -a seu-aplicativo
```
5. **Execução de Migrações e Arquivos Estáticos**

    - Dentro do container do Heroku:

```
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
```

6. Acesso ao Aplicativo no Heroku

Acesse o Heroku e confirme a disponibilidade do app online no servidoe Heroku.