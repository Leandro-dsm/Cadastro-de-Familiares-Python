from tkinter import *
# Função para atualizar lista de familiares
def atualizar_exibicao():
    texto = ""
    for i, familia in enumerate(familiares, 1):
        # Tenta converter idade para inteiro para definir maioridade, senão mostra como inválida
        try:
            idade_int = int(familia["idade"])
            maior = "Maior de idade" if idade_int >= 18 else "Menor de idade"
        except:
            maior = "Idade inválida"
        texto += f"{i}. Nome: {familia['nome']} | Idade: {familia['idade']} ({maior}) | Telefone: {familia['telefone']} | Parentesco: {familia['parentesco']}\n"
    label_exibicao.config(text=texto)
# Função no botão cadastrar
def cadastrar():
    nome = inserir_nome.get()
    idade = inserir_idade.get()
    telefone = inserir_telefone.get()
    parentesco = inserir_parentesco.get()
    # Validação: verifica se campos obrigatórios estão preenchidos
    if nome == "" or idade == "" or telefone == "" or parentesco == "":
        label_status.config(text="Por favor, preencha todos os campos obrigatórios.", fg="red")
        return
    # Adicionar o familiar na lista
    familiares.append({
        "nome": nome,
        "idade": idade,
        "telefone": telefone,
        "parentesco": parentesco,
    })
    # Limpar os campos
    inserir_nome.delete(0, END)
    inserir_idade.delete(0, END)
    inserir_telefone.delete(0, END)
    inserir_parentesco.delete(0, END)

    label_status.config(text="Familiar cadastrado com sucesso!", fg="green")
    # Atualizar a exibição
    atualizar_exibicao()
# Lista inicial de familiares
familiares = [
    {"nome": "Toshio Suoeka", "idade": "76", "telefone": "1111-2222", "parentesco": "Pai"},
    {"nome": "Marli Sabino", "idade": "56", "telefone": "3333-4444", "parentesco": "Mãe"},
    {"nome": "Rose Gouveia", "idade": "39", "telefone": "5555-6666", "parentesco": "Irmã"},
    {"nome": "Mateus", "idade": "20", "telefone": "7777-8888", "parentesco": "Sobrinho"},
    {"nome": "Guilherme", "idade": "15", "telefone": "7777-8888", "parentesco": "Sobrinho"},
]
# Criar janela
window = Tk()
window.title("Cadastro de Familiares")
window.geometry("700x550")
# Labels e entradas
Label(window, text="Nome:").pack()
inserir_nome = Entry(window)
inserir_nome.pack()

Label(window, text="Idade:").pack()
inserir_idade = Entry(window)
inserir_idade.pack()

Label(window, text="Telefone:").pack()
inserir_telefone = Entry(window)
inserir_telefone.pack()

Label(window, text="Grau de Parentesco:").pack()
inserir_parentesco = Entry(window)
inserir_parentesco.pack()
# Botão cadastrar
botao_cadastrar = Button(window, text="Cadastrar", command=cadastrar)
botao_cadastrar.pack(pady=10)
# Label para mostrar status (erros ou sucesso)
label_status = Label(window, text="")
label_status.pack()
# Label para exibir os familiares cadastrados
label_exibicao = Label(window, text="", justify=LEFT, anchor="w")
label_exibicao.pack(fill=BOTH, expand=True, padx=10, pady=10)
# Exibe os familiares iniciais
atualizar_exibicao()
window.mainloop()