// encontrando as 3 hashtags mais usadas
MATCH (h:Hashtag)<-[:POSSUI]-(t:Tweet)
WITH h, COUNT(t) AS quantidade
ORDER BY quantidade DESC
LIMIT 3
WITH COLLECT(h) AS hashMaisUsadas

// buscando 5 tweets de cada hashtag
UNWIND hashMaisUsadas AS h
CALL {
  WITH h
  MATCH (t:Tweet)-[r:POSSUI]->(h)
  RETURN t, r
  LIMIT 5
}

MATCH (a:Aluno) -[:RU]-> (ru4381452:numeroRU)

RETURN DISTINCT t, h, r, a, ru4381452
