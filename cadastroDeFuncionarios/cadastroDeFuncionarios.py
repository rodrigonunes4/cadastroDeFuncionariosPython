import FreeSimpleGUI as sg

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
            
        for  funcionario in funcionarios:
            if id in funcionario:
                sg.popup('O id já está cadastrado')
                count = True
                
        if count == True:
            valores[0] = nome
            valores[1] = id
            janela.close()
            janela = layoutCadastro()
            evento, valores = janela.read()
            if evento == sg.WIN_CLOSED:
                return 0
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

    for funcionario in funcionarios:
        if delete in funcionario:
            funcionarios.remove(funcionario)
            sg.popup('Funcionário removido')
            return 1
    
    sg.popup('Funcionário não encontrado no banco de dados')
    return 0
    
def verificacaoDigit(count, id):
    if id.isdigit() == False:
        count = True
        sg.popup('Caracteres não suportados')
    return count, id

def winClose(evento):
    if evento == sg.WIN_CLOSED or evento == "Sair":
        return True
    return False



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
    sg.PopupScrolled(*funcionarios, title='Lista')
    
with open(r"cadastroDeFuncionarios\data.txt", "r") as ler:
    funcionarios = eval(ler.read())

while True:
    janela = layoutMenu()
    evento, valor = janela.read()
    janela.close()
    if winClose(evento):
        if funcionarios != [] :
            sg.PopupScrolled("Lista de funcionários cadastrados:", *funcionarios, title='lista')
        break

    if evento == 'Cadastrar Funcionário':
        janela = layoutCadastro()
        evento, valores = janela.read()
        if winClose(evento):
            continue
        cadastrar(janela, valores)

    if evento == 'Excluír Funcionário':
         if funcionarios == []:
            sg.popup('Não há funcionarios para excluír. Cadastre um funcionário primeiro.')
            continue
         janela = layoutExcluir()
         evento, valores = janela.read()
         if winClose(evento):
            continue
         excluir(valores)

    if evento == 'Listar todos Funcionários':
        if funcionarios == []:
            sg.popup('Não há funcionarios para listar. Cadastre um funcionário primeiro.')
            continue
        janela = layoutListar()
        continue
    
    janela.close()

with open(r"cadastroDeFuncionarios\data.txt", "w") as escrever:
    escrever.write(str(funcionarios))