from PySimpleGUI import PySimpleGUI as sg

def cadastrar(janela, valores):
    count = True
    while count == True:
        count = False
        
        nome = valores[0]
        id = valores[1]
        count, id = verificacaoDigit(count, id)

        nomeAux = nome
        nome = nome.replace(" ", "")
        if nome.isalpha() == False:
            sg.popup('Caracteres não suportados')
            count = True

        nome = nomeAux
            
        for x in funcionarios:
            if id in x:
                sg.popup('O id já está cadastrado')
                count = True
        if count == True:
            valores[0] = nome
            valores[1] = id
            janela.close()
            janela = layoutCadastro()
            evento, valores = janela.read() # type: ignore
            continue
        else:
            break

    funcionarios.append([nome, id])
    sg.popup('Funcionário cadastrado')
    janela.close()
    return 1

def excluir(valores):
    count = True
    count, delete = verificacaoDigit(count, valores[0])

    for func in funcionarios:
        if delete in func:
            funcionarios.remove(func)
            sg.popup('Funcionário removido')
            return 1
    
    sg.popup('Funcionário não encontrado no banco de dados')
    return 0
    
def verificacaoDigit(count, id):
    if id.isdigit() == False:
        count = True
        sg.popup('Caracteres não suportados')
        return count, id
    return count, id

sg.theme('Reddit')

def layoutMenu():
    layoutMenu = [
        [sg.Text('Bem-vindo ao sistema de cadastro da empresa X. Selecione a opção desejada. \n')],
        [sg.Button('Cadastrar Funcionário')],
        [sg.Button('Excluír Funcionário')],
        [sg.Button('Listar todos Funcionários')],
        [sg.Button('Sair')]
    ]
    return sg.Window('Menu', layoutMenu)
    
def layoutCadastro():
    layoutCadastro = [
        [sg.Text('Nome'), sg.Input()],
        [sg.Text('Id'), sg.Input()],
        [sg.Button('Entrar')]
    ]
    return sg.Window('Cadastro', layoutCadastro)

def layoutExcluir():
    layoutExcluir = [
    [sg.Text('Digite o id do funcionário'), sg.Input()],
    [sg.Button('Enviar')]
    ]
    return sg.Window('Excluir', layoutExcluir)

def layoutListar():
    layoutListar = [
        [sg.PopupScrolled(*funcionarios, title='Lista')]
    ]

funcionarios = []

while True:
    janela = layoutMenu()
    evento, valor = janela.read() # type: ignore
    janela.close()

    if evento == sg.WIN_CLOSED or evento == 'Sair':
        break

    if evento == 'Cadastrar Funcionário':
        janela = layoutCadastro()
        evento, valores = janela.read() # type: ignore
        if evento == sg.WIN_CLOSED:
            continue
        cadastrar(janela, valores)

    if evento == 'Excluír Funcionário':
         if funcionarios == []:
            sg.popup('Não há funcionarios para excluír. Cadastre um funcionário primeiro.')
            continue
         janela = layoutExcluir()
         evento, valores = janela.read() # type: ignore
         if evento == sg.WIN_CLOSED:
            continue
         excluir(valores)

    if evento == 'Listar todos Funcionários':
        if funcionarios == []:
            sg.popup('Não há funcionarios para listar. Cadastre um funcionário primeiro.')
            continue
        janela = layoutListar()
        continue
    
    janela.close()
