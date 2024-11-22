from camada_negocios import CamadaNegocios

class CamadaApresentacao:
    def __init__(self):
        self.negocios = CamadaNegocios()

    def exibir_menu(self):
        print("\n1. Adicionar Contato")
        print("2. Adicionar Compromisso")
        print("3. Listar Contatos")
        print("4. Listar Compromissos")
        print("5. Pesquisar Compromissos por Data")
        print("6. Sair")

    def adicionar_contato(self):
        nome = input("Nome do contato: ")
        telefone = input("Telefone do contato: ")
        email = input("E-mail do contato: ") 
        try:
            id_contato = self.negocios.adicionar_contato(nome, telefone, email)
            print(f"Contato adicionado com ID: {id_contato}")
        except ValueError as e:
            print(f"Erro: {str(e)}")

    def adicionar_compromisso(self):
        descricao = input("Descrição do compromisso: ")
        data = input("Data do compromisso (YYYY-MM-DD HH:MM): ")
        contato_id = input("ID do contato (opcional): ")
        try:
            id_compromisso = self.negocios.adicionar_compromisso(descricao, data, int(contato_id) if contato_id else None)
            print(f"Compromisso adicionado com ID: {id_compromisso}")
        except ValueError as e:
            print(f"Erro: {str(e)}")

    def listar_contatos(self):
        contatos = self.negocios.listar_contatos()
        for contato in contatos:
            print(f"ID: {contato[0]}, Nome: {contato[1]}, Telefone: {contato[2]}, E-mail: {contato[3]}")

    def listar_compromissos(self):
        compromissos = self.negocios.listar_compromissos()
        for compromisso in compromissos:
            contato = compromisso['contato']
            print(f"ID: {compromisso['id']}, Descrição: {compromisso['descricao']}, Data: {compromisso['data']}, "
                  f"Contato: {contato['nome'] if contato else 'N/A'}")

    def pesquisar_compromissos(self):
        data_inicio = input("Data de início (YYYY-MM-DD HH:MM): ")
        data_fim = input("Data de fim (YYYY-MM-DD HH:MM): ")
        compromissos = self.negocios.pesquisar_compromissos_por_intervalo(data_inicio, data_fim)
        for compromisso in compromissos:
            contato = compromisso['contato']
            print(f"ID: {compromisso['id']}, Descrição: {compromisso['descricao']}, Data: {compromisso['data']}, "
                  f"Contato: {contato['nome'] if contato else 'N/A'}")

    def executar(self):
        while True:
            self.exibir_menu()
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.adicionar_contato()
            elif opcao == '2':
                self.adicionar_compromisso()
            elif opcao == '3':
                self.listar_contatos()
            elif opcao == '4':
                self.listar_compromissos()
            elif opcao == '5':
                self.pesquisar_compromissos()
            elif opcao == '6':
                break
            else:
                print("Opção inválida. Tente novamente.")
