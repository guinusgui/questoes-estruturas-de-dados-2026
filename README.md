# Estrutura de Dados - Trabalho 1 - Resolução de questões

Grupo:
- Demétrio Cardoso de Sousa
- Guilherme Gomes da Silva
- Guilherme Linhares de Andrade

## Frações
Consiste na implementação de um tipo operável para frações

[Ver cógigo](fracc.py)

### Construtor
O método construtor recebe dois parâmetros, **num** para numerador e **den** para denominador. O método é implementado com duas importantes características que evitam erros através da definição da class: o uso de um **assertion error** para limitar o escopo dos parâmetros para apenas inteiros, e uma condicional para a aplicação de **ZeroDivisionError**  quando den for 0.

### Métodos de operação
Os métodos de operação são implementados sobrecarregando os métodos _built-in_, add, sub, mul e truediv. As operações são feitas somente **entre frações**, testando através da função isinstance() para checar se o outro operando é uma fração.

### Método para simplificação de frações
As frações são retornadas através simplificadas usando uma implementação do algoritimo de Euclides, representada pela função mdc(), que encontra  o máximo divisor comum de dois números através de uma operação recursiva.

### Execução
Assim, uma fração representada por essa classe seria apresentada de maneira semelhante ao exemplo abaixo:
```Python
um_meio = frac(1,2)
tres_quartos = frac(3,4)

print(um_meio) #imprime '1 / 2'
print(um_meio + tres_quartos) #imprime '5 / 4', já simplificado
```

## Jogo de Cartas
[Ver código](baralho_forma_final.py) 

## Verificação de cpf
[Ver código](cpf.py)

## Cálculo de Imposto de Renda
[Ver código](imposto_de_randa.py)
