## Sequências

Sequências guardam valores de qualquer tipo de dado e possuem uma determinada ordem, pois  possuem um índice. As sequências também são chamadas de coleções.
Criando uma lista de CPFs:

```python
lista = [11122233344, 22233344455, 33344455566]
```

Mas imagine agora que você precisa evitar que exista algum CPF duplicado nesta lista. Em muitas circunstâncias precisamos de uma coleção que não permita valores duplicados, mas nada nos impede adicionar um mesmo CPF nessa lista, por exemplo:

```python
lista.append(11122233344) #funciona!
```

Isso também funciona se fosse uma tupla! Uma tupla também permite elementos duplicados!

## Conhecendo o set

Existe uma coleção onde não podem existir elementos duplicados, o SET

O mesmo exemplo, mas agora inicializando um set:

```python
colecao = {11122233344, 22233344455, 33344455566}
```

Repare que usamos `{}` chaves para declarar os elementos iniciais

## Adicionando elementos no set

Para adicionar um elemento a um set devemos chamar a função `add` (invés da `append`):

```python
colecao.add(44455566677) #vai adicionar pois não existe ainda
```

E se usarmos um CPF que já existe? Vamos testar,e ver que o set vai ignorá-lo:

```python
colecao.add(11122233344) #nao vai adicionar pois este CPF já existe!
```

## set não possui um índice

É importante notar que o set não é uma sequência, pois não tem um índice. O código abaixo não funciona:

```python
colecao[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object does not support indexing
```

E como não temos um índice não sabemos em qual ordem vem os valores quando imprimimos um **set** de dentro de um laço `for`:

```python
for cpf in colecao:
     print(cpf)
```

Imprime:

```python
11122233344
44455566677
33344455566
22233344455
```

Repare que os elementos foram listados fora da ordem de inserção. Isso acontece porque o set não é ordenado.

## Resumindo

*Um set é uma coleção não ordenada de elementos. Cada elemento é  único, isso significa que não existem elementos duplicados dentro do  set.*


## Conhecendo o dictionary

Para criar um dicionário devemos inicializar os instrutores de um modo um pouco diferente. Veja o código:

```python
instrutores = {'Nico' : 39, 'Flavio': 37, 'Marcos' : 30}
```

Repare que usamos as chaves `{}` (como se fosse um set), mas sempre tem em pares. O primeiro par é `'Nico' : 39`, o segundo é `'Flavio': 37`, etc.

Nesse par, temos no lado esquerdo a **chave** e no lado direito o `valor`. Isso é importante pois usamos a chave para recuperar um valor e assim resolvemos nosso problema:

```python
instrutores['Flavio']
```

Imprime:

```python
37
```

