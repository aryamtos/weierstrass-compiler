# Compilador Função Weierstrass


<h3>Analisador léxico e sintático desenvolvido na disciplina de Compiladores no curso de Ciência da Computação na UESC</h3>

<br />
<h1>Sobre</h1>

<p>A função Weierstrass é um contra-exemplo que mostra a existência de uma função contínua em toda reta real e que não possui derivada em nenhum ponto</p>
<p> Sendo assim, foi realizada uma implementação dessa função e construído um analisador léxico cuja entrada recebe o arquivo em linguagem da função weierstrass, posteriormente esses tokens são passados para o analisador sintático, responsável pela construção da gramática.

<br />
<p>Segue abaixo a função utilizada como entrada</p>
<p> É importante ressaltar que a função Tosz recebe como entrada uma matriz ortogonal, cujo cálculo é realizado para geração da mesma,essa matriz é multiplicada com o vetor coluna x, portanto a entrada de Tosz é um vetor.

![image](https://user-images.githubusercontent.com/46492977/127743523-baa2f639-1e86-409e-965e-18ea97dcb5cb.png)

<br />

![image](https://user-images.githubusercontent.com/46492977/127743647-cf68244b-1e6d-426e-ac3e-541a0de2b27d.png)
  

<h3>Função Tosz</h3>

<p>A função Tosz com descrito anteriormente recebe como entrada o produto de uma matriz ortogonal R com um vetor coluna e atende as seguintes especificações:</p>

![image](https://user-images.githubusercontent.com/46492977/127743866-a557565a-ab53-471d-bb0d-19512c59d055.png)


<h2>Implementação</h2>

<p>Tendo como base esses cálculos foi realizada uma implementação da função, dado um vetor de entrada X. Sendo assim foram calculados cada pedaço da função separadamente:</p>
<p>1.Zi - o resultado de Zi é um vetor coluna</p>
<p>2.Fzero - somatório de 0 até 11</p>
<p>1.Fpen - descrita na imagem acima</p>
<p>1.R e Q - foram geradas as matrizes ortogonais com base em cálculos específicos</p>


<h2>Analisador Léxico</h2>

<p>Para construção do analisador léxico foi utilizado o PLY, cujo link encontra-se abaixo. Ele utiliza o LEX e o YACC para o parser.</p>

[https://www.dabeaz.com/ply/ply.html#ply_nn3](url)

