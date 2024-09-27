def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {'tarefa': nome_tarefa, 'completada': False}
    tarefas.append(tarefa)
    print(f'A tarefa {nome_tarefa} foi adicionada com sucesso!')
    return

def ver_tarefas(tarefas):
    print('\nLista de tarefas')
    for indice, tarefa in enumerate(tarefas, start = 1):
        status = "✓" if tarefa['completada'] else ' '
        nome_tarefa = tarefa['tarefa']
        print(f'{indice}. [{status}] {tarefa['tarefa']}')

def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas): 
        tarefas[indice_tarefa_ajustado]['tarefa'] = novo_nome_tarefa
        print(f'Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}')
    else:
        print('Índice de tarefa inválido.')
    return

def completar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    if 0 <= indice_tarefa_ajustado < len(tarefas): 
        tarefas[indice_tarefa_ajustado]['completada'] = not tarefas[indice_tarefa_ajustado]['completada']
        status = "completada" if tarefas[indice_tarefa_ajustado]['completada'] else "não completada"
        print(f'Tarefa {indice_tarefa} marcada como {status}!!')
    else:
        print('Índice de tarefa inválido.')
    return

def deletar_tarefas_completadas(tarefas):
    for tarefa in tarefas:
        if tarefa['completada']:
            tarefas.remove(tarefa)
    print('Tarefas completadas foram deletadas.')
    return


tarefas = []
while True:
    print("""

    Gerenciador de Tarefas Diarias

    """)

    print('1. Adicionar uma tarefa')
    print('2. Visualizar tarefas')
    print('3. Atualizar nome da tarefa')
    print('4. Alterar status da tarefa')
    print('5. Deletar tarefas completadas')
    print('6. Sair')

    escolha = input('Digite a sua escolha: ')

    if escolha == '1':
        nome_tarefa = input('Digite o nome da tarefa que deseja adicionar: ')
        adicionar_tarefa(tarefas, nome_tarefa)
    elif escolha == '2':
        ver_tarefas(tarefas)
    elif escolha == '3':
        ver_tarefas(tarefas)
        indice_tarefa = input('Digite o numero da tarefa que deseja atualizar: ')
        novo_nome = input('Digite o novo nome da tarefa: ')
        atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)
    elif escolha == '4':
        ver_tarefas(tarefas)
        indice_tarefa = input('Digite o número da tarefa que deseja completar: ')
        completar_tarefa(tarefas, indice_tarefa)
    elif escolha == '5':
        deletar_tarefas_completadas(tarefas)
        ver_tarefas(tarefas)
    elif escolha == '6':
        break

print('Programa finalizado')

