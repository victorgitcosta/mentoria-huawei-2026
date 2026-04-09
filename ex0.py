input_categoria = ["nome", "sobrenome", "idade"] #Lista com categorias preenchíveis
usuarios = [] #Lista de Listas com todos os Usuários já cadastrados

usuario_deseja_adicionar = True #Booleano para o loop while

print("""==========================================
------Sistema de Cadastro de Usuário------
==========================================""")

while usuario_deseja_adicionar:
    input_valores = [] #Lista de valores preenchidos por usuário, apaga a cada iteração do loop while
    for categoria in input_categoria:
        valor = input(f"Digite o seu {categoria}:") #Digite o seu nome: 
        input_valores.append(valor) #Valor inserido no fim da lista
    usuarios.append(input_valores) #Lista de listas com os dados do usuário
    print("""==========================================
-----Usuários cadastrados-----
==========================================""")
    for usuario in usuarios: #loop for pra printar todos os usuários cadastrados
        print(f"{input_categoria[0]}: {usuario[0]}, {input_categoria[1]}: {usuario[1]}, {input_categoria[2]}: {usuario[2]}\n")
    continuar = input(f"Deseja adicionar mais 1 usuário?\nDigite 'S' para Sim e 'N' para Não:\n") #valida se o loop while continua ou termina
    if continuar.upper() != "S":
        usuario_deseja_adicionar = False
        print("""==========================================
Obrigado pelo seu uso da nossa plataforma!     
==========================================""")