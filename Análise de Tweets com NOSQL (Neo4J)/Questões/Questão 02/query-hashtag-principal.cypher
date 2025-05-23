// encontrando a hashtag mais utilizada
MATCH (h:Hashtag)<-[:POSSUI]-(t:Tweet)
WITH h, COUNT(t) AS quantidade
ORDER BY quantidade DESC
LIMIT 1

// limitando a quantidade de relacionamentos na exibição do grafo
MATCH (t:Tweet)-[r:POSSUI]->(h)
MATCH (a:Aluno) -[:RU]-> (ru4381452:numeroRU)
RETURN t, h, r, a, ru4381452
LIMIT 10