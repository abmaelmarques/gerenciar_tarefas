import json

tarefas = []
def salvar_tarefas():
  with open('tarefas.json', 'w') as arquivo:
    json.dump(tarefas, arquivo)
  print("tarefas salvas com sucesso!")

def carregar_tarefas():
  try:
    with open('tarefas.json', 'r') as arquivo:
      tarefas = json.load(arquivo)
      print("tarefas carregadas com sucesso!")
      return tarefas
  except:
    print("Nenhuma tarefa encontrada. Começando uma nova lista!")
    return []

def adicionar_tarefa(nome, prioridade):
  tarefa = {
      'nome': nome,
      'prioridade': prioridade
  }
  tarefas.append(tarefa)
  print("tarefa adicionada:", tarefa)

def listar_tarefas():
  print("Lista de Tarefas:")
  for tarefa in tarefas:
    print(f"-{tarefa['nome']} (Prioridade: {tarefa['prioridade']})")

def remover_tarefa(nome):
  for tarefa in tarefas:
    if tarefa['nome'] == nome:
      tarefas.remove(tarefa)
      print("Tarefa removida:", tarefa)
      break
  else:
      print("Tarefa não encontrada na lista.")

tarefas = carregar_tarefas()

while True:
  print("** Menu de Opções **")
  print("1. Adicionar tarefa")
  print("2. Listar tarefas")
  print("3. Remover tarefa")
  print("4. Salvar tarefa")
  print("5. Sair")

  opcao = input("escolha uma opção:")
  if opcao == '1':
    nome = input("digite o nome da tarefa:")
    prioridade = input("digite a prioridade da tarefa:")
    adicionar_tarefa(nome, prioridade)

  elif opcao == '2':
    listar_tarefas()

  elif opcao == '3':
    nome= input("digite a tarefa a ser removida:")
    remover_tarefa(nome)

  elif opcao == '4':
    salvar_tarefas()

  elif opcao == '5':
    print("Saindo do programa.")
    break

  else:
    print("Opção inválida. Por favor, escolha 1 ou 2.")