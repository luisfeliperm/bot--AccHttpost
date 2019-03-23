# bot--AccHttpost
Bot para criar contas com dados aleatórios usando uma proxylist e método post do http



# Exemplo:
pagina: http://localhost/cadastro

<form method="post">
	<input type="text" name="user"><br>
	<input type="password" name="senha"><br>
	<input type="password" name="senhaConfirm"><br>
	<button>Cadastrar</button>
</form>
------------------------------------------------------
No python edite

url = "http://127.0.0.1/cadastrar/"

post = {
  'user':         login,
  'senha':        senha, 
  'senhaConfirm': senha
}
# Em post, utilize o atribuito "name" do campo de texto html

# Alterações:
- Altere a string "Registrado com sucesso" para outra que seja exibida na página se a conta for criada.

# Funcionamento
O script importa a proxy.txt e testa um por vez. Assim que o primeiro proxy é testado e se estiver funcionando, o script irá gerar dados aleatorios e enviar ao servidor usando aquele proxy. <br>
Se a requisição falhar 3 vezes será passado para o proximo proxy e o processo se repetirá.
Se o proxy não estiver funcionando, é pulado para o proximo e o processo também se repete.

# Informações
Se o servidor limita a quantidade de contas por <b>ip</b> o script irá criar o máximo que der assim que o limite for atingido, ele passará para o proximo proxy
