class Tarefa:
    def __init__(self, inicio, fim, valor):
        self.inicio = inicio
        self.fim = fim
        self.valor = valor

# Função para performar uma busca binária nas tarefas dadas, que estão ordenadas
# por tempo de fim. A função retorna o índice do última tarefa que não conflita
# com a tarefa dada, isto é, cujo tempo de fim é menor ou igual que o tempo de
# início da tarefa dada
def encontrandoUltimaTarefaNaoConflitante(tarefas, n):

    # Espaço de busca
    (baixo, alto) = (0, n)
 
    # Iterando até que todo o espaço de busca seja atendido
    while baixo <= alto:
        meio = (baixo + alto) // 2
        if tarefas[meio].fim <= tarefas[n].inicio:
            if tarefas[meio + 1].fim <= tarefas[n].inicio:
                baixo = meio + 1
            else:
                return meio
        else:
            alto = meio - 1
 
    # Retornando um índice negativo se nenhuma tarefa não-conflitante for achada
    return -1
 
# Função para printar as tarefas não-sobrepostas envolvidas na solução
# ótima usando programação dinâmica
def encontrandoTarefasDaSolucaoOtima(tarefas):
 
    # Caso base
    if not tarefas:
        return 0
 
    # Ordenando tarefas por ordem crescente dos seus tempos de fim
    tarefas.sort(key=lambda x: x.fim)
 
    # Obtendo o número de tarefas N
    n = len(tarefas)

    # 'solucaoOtima[i]' armazena o valor máximo possível para os primeiros 'i' trabalhos
    solucaoOtima = [None] * n

    # 'tarefas[i]' armazena o índice das tarefas envolvidas na solução ótima
    tarefas = [[] for _ in range(n)]
 
    # Inicializando solucaoOtima[i] e tarefas[i] com a primeira tarefa
    solucaoOtima[0] = tarefas[0].valor
    tarefas[0].append(0)
 
    # Preenchendo 'tarefas[]' e 'solucaoOtima[]' de forma bottom-up
    for i in range(1, n):
 
        # Encontrando o índice da última tarefa não-conflitante com a tarefa atual
        indice = encontrandoUltimaTarefaNaoConflitante(tarefas, i)
 
        # Incluindo a tarefa atual com suas tarefas não-conflitantes
        valorAtual = tarefas[i].valor
        if indice != -1:
            valorAtual += solucaoOtima[indice]
 
        # Se incluir a tarefa atual leva para a solução ótima
        if solucaoOtima[i - 1] < valorAtual:
            solucaoOtima[i] = valorAtual
 
            if indice != -1:
                tarefas[i] = tarefas[indice][:]
            tarefas[i].append(i)
 
        # Se excluir a tarefa atual leva para a solução ótima
        else:
            tarefas[i] = tarefas[i - 1][:]
            solucaoOtima[i] = solucaoOtima[i - 1]
 
    # 'solucaoOtima[n-1]' armazena o valor máximo
    print("O valor máximo é", solucaoOtima[n - 1])
 
    # 'tarefas[n-1' armazena o índice das tarefas envolvidas na solução ótima
    print("As tarefas envolvidas na solução ótima foram", end=' ')
    for i in tarefas[n - 1]:
        print((tarefas[i].inicio, tarefas[i].fim, tarefas[i].valor), end=' ')
 
 
if __name__ == '__main__':
 
    tarefas = [
        Tarefa(0, 6, 60), Tarefa(1, 4, 30), Tarefa(3, 5, 10),
        Tarefa(5, 7, 30), Tarefa(5, 9, 50), Tarefa(7, 8, 10)
    ]

    encontrandoTarefasDaSolucaoOtima(tarefas)