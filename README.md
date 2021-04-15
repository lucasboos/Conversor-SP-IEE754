# Conversor de Precisão Simples IEE754

O Padrão IEEE para Aritmética de Ponto Flutuante é um padrão técnico para aritmética de ponto flutuante. Abordando muitos dos problemas encontrados nas diversas implementações de ponto flutuante que os tornavam difíceis de usar de forma confiável e portátil . Muitas unidades de ponto flutuante de hardware usam o padrão IEEE 754.  

A precisão simples usa 32bits:<br>
✔ 1bit para o sinal<br>
✔ 8bits para o expoente<br>
✔ 23bits para a mantissa<br>
Observação: A bias do expoente é 127<br>

Exemplo de layout do ponto flutuante de 32bits:<br>
<img src="src/img-layout.png">
