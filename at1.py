import sintatic_tree as st

def lexgen(re):
	i, n = 0, len(re)
	while i < n:
		if not re.isspace(): yield re[i]
		i+=1




def singen(re):
	operators = []
	trees = []
	w = {             # w é o peso de cada operador na ordem de precedencia
		'*': 4,
		'.': 3,
		'|': 2,
		')': 1,
		'(': 1}
	for s in lexgen('('+re+')'): 
		if s not in '(*.|)':    # Se s for um operando
			trees.append(s)
		elif len(operators) > 0:    # Se s for um operador e a pilha de operadores não estiver vazia
			while w[s] <= w[operators[-1]] and s != '(':
				if operators[-1] == '*':
					try:
						trees[-1] = st.star(trees[-1])
					except:
						print('erro de sintaxe: operador sem operando')
						return
				if operators[-1] == '.':
					try:
						trees[-1] = st.cat(trees[-1], trees[-2])
						trees.pop(-2)
					except:
						print('erro de sintaxe: operador sem operando')
						return
				if operators[-1] == '|':
					try:
						trees[-1] = st.union(trees[-1], trees[-2])
						trees.pop(-2)
					except:
						print('erro de sintaxe: operador sem operando')
						return
				if s == ')' and operators[-1] == '(':
					operators.pop()
					break

				operators.pop()
				if len(operators) == 0: break
			if s != ')':	
				operators.append(s)
		else:     # Se s for um operador e a pilha estiver vazia
			operators.append(s)
	# último tratamento de exceção		
	if len(trees) != 1: 
		print('erro de sintaxe: cadeia de operandos inválida')
		return
	return trees[0]


ex = '(a.b|b*)'
r = singen(ex)
print(r)