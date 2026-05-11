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
