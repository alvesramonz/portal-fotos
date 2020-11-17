## Para rodar o site localmente "Portal Casal" é necessário seguir algumas etapas:

Inicialmente irei disponibilizar uma chave específica aws para que seja possível o link com a s3, essa chave será única e especificamente para propósitos de teste e para tal não foram feitas variáveis ambiente.

## Pré-Requisito:
   Ter instalado python em sua máquina

1º. Vá até:
  PortalFotos > PortalFotos > settings.py 
  
  Desça até o ponto onde se encontra:
  
    AWS_ACCESS_KEY_ID = 'SUA_CHAVE_ID'
    AWS_SECRET_ACCESS_KEY = 'SUA_CHAVE_SECRETA'
    AWS_STORAGE_BUCKET_NAME = 'portal-fotos-casal'  
    
  Substitua o código acima por este logo abaixo:
  
    AWS_ACCESS_KEY_ID = 'AKIAQCKZAB463NWZXH3Z'
    AWS_SECRET_ACCESS_KEY = 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''
    AWS_STORAGE_BUCKET_NAME = 'portal-fotos-casal' 

2º O seguinte site funciona da forma, um casal de amigos que irá se casar em breve e eles pediram para fazer uma brincadeira com os convidados. Eles querem criar uma galeria de fotos onde todo mundo poderá subir fotos tiradas durante o casamento. Com isso a primeira página é propícia para o envio de fotos, mas apenas o casal poderá escolher quais fotos irão aparecer na página de "Galeria".

Para se passar pelo casal utilize as credenciais abaixo para fazer a aprovação das fotos:
  Login:casal
  Senha:123456789
  
3º Por fim para rodar o site localmente, esteja no terminal inserido dentro do primeiro diretório PortalFotos e então digite: *python manage.py runserver*. Caso ocorra algum erro na rota: http://127.0.0.1:8000, opte pelo código: *python manage.py runserver 7000*
  
