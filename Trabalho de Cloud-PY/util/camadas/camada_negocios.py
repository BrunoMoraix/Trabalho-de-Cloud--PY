from camada_dados import CamadaDados

class CamadaNegocios:
    def __init__(self):
        self.dados = CamadaDados()

    def adicionar_contato(self, nome, telefone, email):
        if not nome or not telefone or not email:
            raise ValueError("Nome, telefone e e-mail são obrigatórios")
        return self.dados.adicionar_contato(nome, telefone, email)

    def adicionar_compromisso(self, descricao, data, contato_id=None):
        if not descricao or not data:
            raise ValueError("Descrição e data são obrigatórios")
        return self.dados.adicionar_compromisso(descricao, data, contato_id)

    def listar_contatos(self):
        return self.dados.listar_contatos()

    def listar_compromissos(self):
        compromissos = self.dados.listar_compromissos()
        return [
            {
                'id': c[0],
                'descricao': c[1],
                'data': c[2],
                'contato': {'id': c[3], 'nome': c[4]} if c[3] else None
            }
            for c in compromissos
        ]

    def pesquisar_compromissos_por_intervalo(self, data_inicio, data_fim):
        compromissos = self.dados.pesquisar_compromissos_por_intervalo(data_inicio, data_fim)
        return [
            {
                'id': c[0],
                'descricao': c[1],
                'data': c[2],
                'contato': {'id': c[3], 'nome': c[4]} if c[3] else None
            }
            for c in compromissos
        ]
