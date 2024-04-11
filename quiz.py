import json



#pergunta1 =  {
#    "pergunta": "o que se come no halloween",
#    "resposta":
#    {
#        "a": "arroz",
#        "b": "doces",
#        "c": "bacalhau"
#    },
#    "respostaCerta" : "b"
#}
#pergunta2 =  {
#    "pergunta": "que tipos de filmes costumam se ver",
#    "resposta":
#    {
#        "a": "comedia",
#        "b": "romace",
#        "c": "terror"
#    },
#    "respostaCerta" : "c"
#}
#pergunta3 =  {
#    "pergunta": "qual é a frase mais conhecida?",
#    "resposta":
#    {
#        "a": "trick ou ...",
#        "b": "ola amigos,vamos jogar",
#        "c": "never bonna give u up"
#    },
#    "respostaCerta" : "a"
#}

def perguntar (pergunta):
	print(pergunta["pergunta"])
	respostas = pergunta["resposta"]

	# fazer ciclos para n repetir codigo
	for key in respostas:
	    print(key,"->",respostas[key])
	#print(respostas["a"]) #otimizavel
	#print(respostas["b"]) #otimizavel
	#print(respostas["c"]) #otimizavel

	resposta = input("R: ")
	if resposta == pergunta["respostaCerta"]: 
	    print("Resposta Certa")
	    return 1
	else:
	    print("Resposta Errada")
	    return 0

def quiz():     

	#utilizar um json para guardar os dados
	with open("your_json_file", "r") as fp:
	    file_string = fp.read()
	    lista_de_perguntas = json.loads(file_string)
	#lista_de_perguntas = [pergunta1,pergunta2,pergunta3]

	pontos_do_utilizador = 0
	for pergunta in lista_de_perguntas:
	    pontos_do_utilizador += perguntar(pergunta)
	    print("resultado atual:",pontos_do_utilizador,"\n")
	
	print("o teu resultado:",pontos_do_utilizador,'\n')


quiz()

#corremos isto uma vez para criar o json e dps não precisamos de ter os dicionarios no codigo
#with open("your_json_file", "w") as fp:
#    json.dump([pergunta1, pergunta2, pergunta3],fp)



