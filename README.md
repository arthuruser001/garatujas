# Garatujas - A Anotação de Desenvolvimento WEB de arthuruser001

# O que é o HTML?

- O HTML é a linguagem que servirá de base para nossos sites;
- Ela **NÃO** é uma linguagem de programação, é uma linguagem de marcação;
- Funciona à base de **TAGS**
- É lido pelo Browser (Navegador) e com isso é exibido
- Não é sómente visual, ele contém acessibilidade
- Significado: HyperText Markup Language
- Tradução do significado: Linguagem de Marcação de Hipertexto

## O que são e como funcionam as **TAGS**?

- As tags são a base da linguagem HTML
- Nelas, temos uma abertura e um fechamento
- Há tags que não precisarão ser fechadas
- Exemplo: ```<!--Abertura da Tag--><!DOCTYPE html><!--Sem fechamento da Tag-->```
- Há tags que precisãrão ser fechadas
- Exemplo: ```<!--Abertura da Tag--><p>Este é um parágrafo<!--Conteúdo da tag--><p><!--Fechamento da Tag-->```
- Em si, as tags marcam um texto para fazer algo com ele, por isso linguagem de marcação.

## Código básico do HTML

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <title>Código básico em HTML</title>
</head>
<body>
  <h1>Código básico HTML</h1>
  <p>Este é um parágrafo de exemplo</p>
</body>
</html>
```
### Cada tag básica do código anterior e para que serve:

- ```<!DOCTYPE html>```: Informa ao navegador que o código que está a seguir é HTML5.
- ```<html>```: É dentro dessa tag que todo o código deve estar, dentro dela, podemos colocar o atributo ```lang="pt-BR"``` que irá dizer ao navegador que a página está em pt-BR
- ```<head>```: Dentro dessa tag, não haverá um conteúdo que será renderizado na página, só haverão coisas para o navegador entender coisas sobre a página
- ```<title>```: É o título da página, aquele que fica ao lado do icone na aba do navegador
- ```<body>```: Dentro dessa tag haverá todo o conteúdo renderizado, ou seja texto, imagem, formas e etc
- ```<h1>```: É o título renderizado, ou seja, o texto que fica grande parecendo um título(porque é para ele ser um título). Além dele, há o ```<h1> <h2> <h3> <h4> <h5> <h6>``` que são os subtítulos
- ```<p>```: É o parágrafo do texto do site.

# O que é o CSS

- É a linguagem que servirá de estilização para os nossos sites
- Ela **NÃO** é uma lingugem de programação, é uma linguagem de estilo
- Funciona à base de **Seletores** e de **Propriedades**
- É renderizado pelo browser, modificando a exibição do HTML
- Ele é somente visual
- Significado: Cascading Style Sheets
- Tradução: Folhas de Estilo em Cascata

## O que são e como funcionam os Seletores

- Seletores vão ser os responsáveis por escolher o que iremos estilizar
- Eles são muito variados, mas sempre vão seguir um padrão e uma sintaxe predefinidos pela lingugem
- Existem seletores que podem ser muito simples, e existem seletores que são muito complexos
- Exemplo de seletor simples: ```h1 {...}```
- Exemplo de seletor complexo: ```div > span + img {...}```
- Em si, os seletores só vão escolher o que estilizar, mas não vão estilizar nada sozinhos

### Exemplos de seletores no CSS
```css
h1 {
...
}
aside div#image > img {
...
}

main + span {
...
}

h1 , h2 , h3 {
...
}
```

## O que são e como funcionam as Propriedades

- Propriedades são responsáveis pela estilização
- Existem inúmeras propriedades que podem ser utilizadas, as vezes em vários elementos, as vezes em um só
- Propriedades podem alterar uma única coisa ou podem ser um agrupado de outras propriedades
- Exemplo de propriedades:
- ```css
  div {
    margin: 10px;
  }
  span {
    margin-left: 10px;
    margin-right: 10px;
    margin-top: 10px;
    margin-bottom: 10px;
  }
  ```
- Essas propriedades que estão dentro do seletor span são todas um fragmento da que está em div. Ou seja, as duas vão fazer a mesma coisa, mas com a segunda é possivel atribuir valores mais especificamente

# Atividades

## Criação de um perfil

### A base do pefil

- É recomendado planejar corretamente a criação do website antes de começar a "programar"
- Primeiro, é altamente recomendável depois de planejar, começar a fazer o HTML o mais completo possível
- Após isso vamos fazer as estilizações básicas para fazer um perfil
- A primeira coisa que vamos estilizar é colocar uma borda em cada elemento que devemos organizar para visualizar melhor o seu tamanho e organização na página. Fazemos isso usando a propriedade CSS ```border: espessura tipo cor```
- É recomendável colocar cores, espessuras e tipos diferentes para cada elemento, para facilitar a sua disitinção
- Após colocarmos as bordas, vamos começar a fazer a organização de todos os elementos na página
- Como queremos fazer como se fossem duas colunas de informação, uma com informações mais objetivas como idade, nome e etc e outra como algo mais extenso, como história e galeria, devemos organizar a página de forma que seja possível criar essas duas colunas. Para isso, usaremos o ```display: grid```
- O ```display: grid``` faz um elemento organizar os seus filhos (os elementos que estão dentro dele) em uma grade. Como nós iremos somente utilizar colunas, então teremos uma grade de 1 x 2
- Para configurarmos corretamente a nossa grade, iremos utilizar a configuração do grid com a propriedade CSS ```grid-template-columns: 250px 1fr```
- Ele simplesmente configura o número e tamanho das colunas de nossa grade, sendo que a primeira seria de 250px (pixels) e a segunda com uma fração do que sobrou, ou seja, ele vai dividir o espaço que sobrou por um e vai retornar esse valor para ser o tamanho das nossas colunas
- Agora será possível visualizar que dois filhos que foram criados para ser um aquela lateral com imagem e informações objetivas e a parte que seria com informações mais detalhadas organizadas, cada uma em seu lugar.
- Essa é a base do perfil, a partir dela, é possível estilizar e o deixar bem mais agradável aos ollhos do que algo todo quadrado. Mas o principal do CSS é aprender de pouco em pouco os seletores que deveremos usar, assim, será possível dominar de pouco a pouco a estilização de páginas web.

### A estilização do perfil