# Conversor de Precisão Simples IEE754

O Padrão IEEE para Aritmética de Ponto Flutuante é um padrão técnico para aritmética de ponto flutuante. Abordando muitos dos problemas encontrados nas diversas implementações de ponto flutuante que os tornavam difíceis de usar de forma confiável e portátil . Muitas unidades de ponto flutuante de hardware usam o padrão IEEE 754.  

A precisão simples usa 32bits:
✔ 1bit para o sinal
✔ 8bits para o expoente
✔ 23bits para a mantissa
Observação: A bias do expoente é 127

Exemplo de layout de ponto flutuante de 32bits:<br>
<img src="src/img-layout.png">

