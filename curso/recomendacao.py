from math import sqrt

baseUser = {'Ana':
		{'Freddy x Jason': 2.5,
		 'O Ultimato Bourne': 3.5,
		 'Star Trek': 3.0,
		 'Exterminador do Futuro': 3.5,
		 'Norbit': 2.5,
		 'Star Wars': 3.0},

	  'Marcos':
		{'Freddy x Jason': 3.0,
		 'O Ultimato Bourne': 3.5,
		 'Star Trek': 1.5,
		 'Exterminador do Futuro': 5.0,
		 'Star Wars': 3.0,
		 'Norbit': 3.5},

	  'Pedro':
	    {'Freddy x Jason': 2.5,
		 'O Ultimato Bourne': 3.0,
		 'Exterminador do Futuro': 3.5,
		 'Star Wars': 4.0},

	  'Claudia':
		{'O Ultimato Bourne': 3.5,
		 'Star Trek': 3.0,
		 'Star Wars': 4.5,
		 'Exterminador do Futuro': 4.0,
		 'Norbit': 2.5},

	  'Adriano':
		{'Freddy x Jason': 3.0,
		 'O Ultimato Bourne': 4.0,
		 'Star Trek': 2.0,
		 'Exterminador do Futuro': 3.0,
		 'Star Wars': 3.0,
		 'Norbit': 2.0},

	  'Janaina':
	     {'Freddy x Jason': 3.0,
	      'O Ultimato Bourne': 4.0,
	      'Star Wars': 3.0,
	      'Exterminador do Futuro': 5.0,
	      'Norbit': 3.5},

	  'Leonardo':
	    {'O Ultimato Bourne':4.5,
             'Norbit':1.0,
	     'Exterminador do Futuro':4.0}
}

baseFilm = {'Freddy x Jason':
		{'Ana': 2.5,
		 'Marcos:': 3.0 ,
		 'Pedro': 2.5,
		 'Adriano': 3.0,
		 'Janaina': 3.0 },

	 'O Ultimato Bourne':
		{'Ana': 3.5,
		 'Marcos': 3.5,
		 'Pedro': 3.0,
		 'Claudia': 3.5,
		 'Adriano': 4.0,
		 'Janaina': 4.0,
		 'Leonardo': 4.5 },

	 'Star Trek':
		{'Ana': 3.0,
		 'Marcos:': 1.5,
		 'Claudia': 3.0,
		 'Adriano': 2.0 },

	 'Exterminador do Futuro':
		{'Ana': 3.5,
		 'Marcos:': 5.0 ,
		 'Pedro': 3.5,
		 'Claudia': 4.0,
		 'Adriano': 3.0,
		 'Janaina': 5.0,
		 'Leonardo': 4.0},

	 'Norbit':
		{'Ana': 2.5,
		 'Marcos:': 3.0 ,
		 'Claudia': 2.5,
		 'Adriano': 2.0,
		 'Janaina': 3.5,
		 'Leonardo': 1.0},

	 'Star Wars':
		{'Ana': 3.0,
		 'Marcos:': 3.5,
		 'Pedro': 4.0,
		 'Claudia': 4.5,
		 'Adriano': 3.0,
		 'Janaina': 3.0}
}
###############################################################################

def euclidean(base, user1, user2):
    si = {}
    for item in base[user1]:
        if item in base[user2]:
            si[item] = 1
    if len(si) == 0:
        return 0
    soma = sum([pow(base[user1][item] - base[user2][item], 2)
                    for item in base[user1] if item in base[user2]])
    return 1/(1 + sqrt(soma))


def getSimilarity(base, user):
    similarity = [(euclidean(base, user, outro), outro)
                        for outro in base if outro != user]
    similarity.sort()
    similarity.reverse()
    return similarity[0:30]

def getRecomendations(base, user):
    totais={}
    sumSim={}
    for outro in base:
        if outro == user: continue
        similarity = euclidean(base, user, outro)

        if similarity <=0: continue
        for item in base[outro]:
            if item not in base[user]:
                totais.setdefault(item, 0)
                totais[item] += base[outro][item] * similarity
                sumSim.setdefault(item,0)
                sumSim[item] += similarity
    rankings = [((total/sumSim[item]), item) for item, total in totais.items()]
    rankings.sort()
    rankings.reverse()
    return rankings[0:30]

#a funcao abaixo carrega em um dicionario films o id e o nome do filme
def loadMovieLens(path='./ml-100k'):
	films = {}
	for line in open(path + '/u.item', encoding = "ISO-8859-1"):
		(id, title) = line.split('|')[0:2] #pega as duas primeiras colunas e seta em id e titulo
		films[id] = title
	# print(films)
	base = {}
	for line in open(path + '/u.data', encoding = "ISO-8859-1"):
		(user, idFilm, rate, time) = line.split('\t') #splita por tab
		base.setdefault(user, {})
		base[user][films[idFilm]]  = float(rate)# aqui pegamos um usuario e setamos como valor o nome do filme que eh indicado pela linha idFilm
	return base
