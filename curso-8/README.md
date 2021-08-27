# Expressões Regulares

As expressões regulares servem para encontrar **padrões bem definidos** dentro de uma **cadeia de caracteres** em um texto ou *str* maiores. Por exemplo, se temos um e-mail com um volume textual enorme contendo um número de telefone específico, poderemos extraí-lo sem precisarmos ler todo o conteúdo.

Para isso, montaremos um padrão de expressão regular de acordo com a linguagem que estamos usando para procurá-lo dentro de um texto, retornando os padrões que queremos.

Para construirmos este padrão, o primeiro passo é conhecer os **caracteres especiais** da linguagem e saber qual é a **biblioteca responsável** por isso. Encontraremos as expressões regulares dentro do texto por meio de **métodos específicos** da linguagem também.

- Os colchetes [] são caracteres especiais que definem um *range* ou um grupo de caracteres, como [0-9], [a-z] ou [abc] por exemplo;
- Já o * pega uma ou mais ocorrências do padrão definido anteriormente;
- As chaves {} nos permitem definir uma quantidade específica de vezes que queremos que o padrão se repita ou um intervalo de possibilidades, como [abc]{5} por exemplo;
- O \w pode ser qualquer número de zero a nove ou letra de "A" a "Z" ou o _(underline);
- O \d pode ser qualquer número de 0 até 9;
- A barra | representa uma coisa ou outra como em @|$ por exemplo;
- Os parênteses () capturam um grupo.

