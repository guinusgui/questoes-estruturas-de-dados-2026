# Estrutura de Dados - Trabalho 2 - Fila com prioridade usando Array

Grupo 3:
- Demétrio Cardoso de Sousa
- Guilherme Gomes da Silva
- Guilherme Linhares de Andrade

Consiste na implemetnação de uma fila de pessoas em que pode haver indivíduos com prioridade, sendo eventualmente chamados antes

**Características:**
- Uso de Array: a implementação usa-a em detrimento da lista, evadindo parcialmente as limitações do tipo através de reguladores para início e fim e um método de redimensionamento
- Política de Atendimento: No caso de haver prioridades, a fila permite que uma prioridade passe a frente a cada 3 não prioridades. As prioridades são indicadas por `*` no fim dos nomes
- Capacidade de leitura de arquivo: o usuário pode optar pela leitura de um arquivo .txt como entrada em vez de adicionar cada entrada manualmente pela interfaçe
