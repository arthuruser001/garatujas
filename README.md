# ia26-webdesign

Este guia apresenta os conceitos básicos de web design com foco em HTML e CSS. O objetivo é ajudar iniciantes a criar páginas web simples e entender como estruturá-las e como deixá-las mais bonitas.

## Antes de começar

Para seguir este conteúdo, é recomendável ter:
- Um editor de código, como o Visual Studio Code.
- Um navegador atualizado, como o Google Chrome.

## HTML - HyperText Markup Language

HTML não é uma linguagem de programação. É uma linguagem de marcação usada para organizar o conteúdo da página.

HTML diz ao navegador:
- o que é um título;
- o que é um parágrafo;
- o que é um link;
- o que é uma imagem;
- como o conteúdo está estruturado.

Cada parte do conteúdo usa uma tag. Uma tag de abertura aparece assim: `<p>` e a tag de fechamento aparece assim: `</p>`.

Por exemplo:
```html
<p>Este é um parágrafo.</p>
```

HTML também é importante para acessibilidade. Um site bem marcado ajuda leitores de tela e outros dispositivos a entenderem a página.

### Formatação em HTML

Imagine que você seleciona um texto no editor e aplica negrito ou itálico. Em HTML, isso é feito com tags.

Exemplo:
```html
<strong>lorem ipsum</strong> dolor <em>sit amet</em> potentia
```

Para aplicar cor em um trecho:
```html
<strong>lorem <span style="color: red;">ipsum dolor sit</span></strong> amet <em>sit amet</em> potentia
```

> Nota: prefira usar tags semânticas como `<strong>` e `<em>` em vez de `<b>` e `<i>`. Elas ajudam a descrever melhor o significado do texto.

### Estrutura básica de um documento HTML

Todo documento HTML começa com:
```html
<!DOCTYPE html>
```

E tem duas partes principais:
- `<head>`: informações da página, como título e links para CSS;
- `<body>`: conteúdo que aparece para o usuário.

Exemplo completo:
```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Título da Página</title>
</head>
<body>
  <h1>Olá</h1>
  <p>Bem-vindo à página.</p>
</body>
</html>
```

> Nota: o atributo `lang="pt-BR"` indica o idioma da página e `meta charset="UTF-8"` garante que acentos sejam exibidos corretamente.

### Atributos HTML

Atributos dão informações extras às tags.

Exemplo de link:
```html
<a href="https://www.google.com">Visite o Google</a>
```

Aqui, `href` indica o endereço do link.

### Onde encontrar todas as tags HTML

- [MDN Web Docs - Elementos HTML](https://developer.mozilla.org/pt-BR/docs/Web/HTML/Element)
- [W3Schools - HTML Tags](https://www.w3schools.com/TAGS/default.asp)

## CSS - Cascading Style Sheets

CSS controla a aparência da página:
- cores;
- fontes;
- margens;
- espaçamento;
- layout.

CSS fica separado do HTML para manter o código organizado.

### Exemplo de HTML e CSS juntos

HTML:
```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Exemplo de CSS</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <h1>Olá, Mundo!</h1>
  <p>Este é um exemplo de CSS.</p>
</body>
</html>
```

CSS (`styles.css`):
```css
body {
  background-color: #f0f0f0;
  font-family: Arial, sans-serif;
}

h1 {
  color: #333333;
  text-align: center;
}

p {
  color: #666666;
  font-size: 18px;
  margin: 20px;
}
```

> Nota: o CSS é incluído no `<head>` usando `<link rel="stylesheet" href="styles.css">`.

### Sintaxe do CSS

A regra básica do CSS é:
```css
seletor {
  propriedade: valor;
}
```

Por exemplo:
```css
p {
  color: blue;
}
```

### Seletores CSS

Seletores dizem ao CSS quais elementos devem receber estilo.

Tipos comuns:
- seletor de tipo: `p { }` aplica a todos os parágrafos;
- seletor de classe: `.titulo { }` aplica a elementos com `class="titulo"`;
- seletor de ID: `#paragrafo1 { }` aplica a um elemento com `id="paragrafo1"`;
- seletor de atributo: `a[href="#"] { }` aplica a links com `href="#"`;
- pseudo-classes: `p:first-child { }` aplica ao primeiro parágrafo filho.

### Hierarquia e seletores de relacionamento

A estrutura HTML importa. Por exemplo:
```html
<main>
  <section>
    <p>Este é um parágrafo dentro de uma seção.</p>
  </section>
</main>
```

Para estilizar esse parágrafo:
```css
main section p {
  color: green;
}
```

Isso significa "p dentro de section dentro de main".

Outros seletores importantes:
- `elemento1 > elemento2 { }`: filho direto;
- `elemento1 + elemento2 { }`: irmão imediato;
- `elemento1 ~ elemento2 { }`: irmãos posteriores.

## Praticando HTML e CSS

Este material apresenta os conceitos essenciais. Agora, o próximo passo é criar uma página simples usando as tags HTML corretas e aplicar estilos básicos com CSS.
