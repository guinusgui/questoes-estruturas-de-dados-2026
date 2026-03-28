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
Uma implementação em Python do clássico jogo de cartas **Vinte e Um**.

[Ver código](baralho_forma_final.py) 

### Funcionalidades

- Suporte Multiplayer: Permite definir o número de jogadores no início da partida.

- Interface Limpa: Utiliza limpeza de tela automática para manter o terminal organizado durante os turnos.

- Lógica de Baralho Realista: O baralho é embaralhado aleatoriamente e as cartas são removidas à medida que são compradas.

- Tratamento de Erros: Validação de entradas para garantir que o número de jogadores e as ações (S/P) sejam válidos.

- Cálculo Automático de Vencedor: Compara as pontuações ao final, ignora quem "estourou" e anuncia o vencedor (ou empate).

### Como funciona:

O projeto está estruturado em três classes principais:

- Carta: Define o valor e o naipe de cada carta individual.

- Baralho: Responsável por gerar as 52 cartas, embaralhá-las e gerenciar a "compra" de cartas.

- Jogador: Armazena o nome/número do jogador e sua pontuação acumulada.

Além disso, a função principal vinte_e_um() coordena o fluxo de turnos e as condições de vitória.


## Verificação de cpf
Contém um script em Python desenvolvido para validar números de CPF (Cadastro de Pessoas Físicas) implementando o algoritmo oficial da Receita Federal para o cálculo dos dígitos verificadores.

[Ver código](cpf.py)

### Como funciona:
O script está dividido em três funções:

obter_digitos(): Solicita o CPF ao usuário, remove caracteres não numéricos e garante que a entrada contenha exatamente 11 dígitos.

obter_resto(cpf, n): Realiza a lógica matemática de multiplicação ponderada para os n primeiros dígitos, retornando o resto da divisão por 11.

validacao(cpf): A função principal que orquestra a validação, checando se o CPF não é uma sequência repetida e se os dígitos calculados batem com os informados.

### Exemplo de uso:
```Python
Digite o seu CPF(11 dígitos): 123.456.789-00
CPF inválido!
```


## Cálculo de Imposto de Renda
Consiste na implementação de um sistema para o cálculo progressivo de Imposto de Renda baseado em faixas salariais.

[Ver código](imposto_de_randa.py)

### Lógica de Cálculo Progressivo
A função calcular_imposto utiliza uma lista de tuplas para representar as faixas tributárias. A lógica percorre cada faixa e utiliza a função min() para definir o teto do cálculo em relação ao valor inserido. Isso garante que o imposto seja calculado apenas sobre a parcela excedente de cada nível, respeitando a natureza progressiva do cálculo real do IRPF. Caso o valor não atinja a próxima faixa, o laço é interrompido por um break para otimização.

### Tratamento de Entradas e Robustez
O programa utiliza um bloco try-except dentro de um laço while para garantir que apenas valores numéricos válidos sejam processados. Para melhorar a experiência do usuário, é aplicado o método .replace(",", "."), permitindo que entradas com vírgula (padrão brasileiro) sejam convertidas corretamente para o tipo float sem gerar erros de execução.

### Execução
Ao ser executado, o script limpa o console e solicita o valor bruto para processamento. O resultado é exibido formatado com duas casas decimais:

```Python
# Exemplo de interação
Digite o valor para que seja calculado o imposto: 3500,50
Você terá que pagar 143.66R$ de imposto
```
