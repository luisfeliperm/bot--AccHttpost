<h1><a id="botAccHttpost_0"></a>bot–AccHttpost</h1>
<p>Bot para criar contas com dados aleatórios usando uma proxylist e método post do http</p>
<h1><a id="Exemplo_5"></a>Exemplo:</h1>
<p>&lt;form method=“post”&gt;<br>
&lt;input type=“text” name=“user”&gt;&lt;br&gt;<br>
&lt;input type=“password” name=“senha”&gt;&lt;br&gt;<br>
&lt;input type=“password” name=“senhaConfirm”&gt;&lt;br&gt;<br>
&lt;button&gt;Cadastrar&lt;/button&gt;<br>
&lt;/form&gt;</p>
<hr>
<p>No python edite</p>
<p>url = &quot;<a href="http://127.0.0.1/cadastrar/">http://127.0.0.1/cadastrar/</a>&quot;</p>
<p>post = {<br>
‘user’:         login,<br>
‘senha’:        senha,<br>
‘senhaConfirm’: senha<br>
}</p>
<h1><a id="Alteraes_22"></a>Alterações:</h1>
<ul>
<li>Altere a string “Registrado com sucesso” para outra que seja exibida na página se a conta for criada.</li>
<li>Em post, utilize o atribuito “name” do campo de texto html</li>
</ul>
<h1><a id="Funcionamento_26"></a>Funcionamento</h1>
<p>O script importa a proxy.txt e testa um por vez. Assim que o primeiro proxy é testado e se estiver funcionando, o script irá gerar dados aleatorios e enviar ao servidor usando aquele proxy.<br>
Se a requisição falhar 3 vezes será passado para o proximo proxy e o processo se repetirá.<br>
Se o proxy não estiver funcionando, é pulado para o proximo e o processo também se repete.</p>
<h1><a id="Informaes_31"></a>Informações</h1>
<p>Se o servidor limita a quantidade de contas por &lt;b&gt;ip&lt;/b&gt; o script irá criar o máximo que der assim que o limite for atingido, ele passará para o proximo proxy</p>
