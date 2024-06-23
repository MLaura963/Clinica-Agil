# Import
import pandas as pd
from datetime import datetime

# Classe para gerenciar os pacientes e consultas
class Clinica:
    def __init__(self):
        # Tenta carregar os dados existentes dos pacientes e agendamentos
        try:
            self.pacientes_df = pd.read_excel('pacientes.xlsx', index_col=0)
        except FileNotFoundError:
            self.pacientes_df = pd.DataFrame(columns=['Nome', 'Telefone'])
        
        try:
            self.agendamentos_df = pd.read_excel('agendamentos.xlsx', index_col=0)
        except FileNotFoundError:
            self.agendamentos_df = pd.DataFrame(columns=['Paciente', 'Telefone', 'Dia', 'Hora', 'Especialidade'])

    def cadastrarPaciente(self, nome, telefone):
        # Limpar as variáveis telefone e nome de espaços em branco
        telefone = telefone.strip()
        nome = nome.strip()
        
        # Verifica se o paciente já está cadastrado
        if telefone in self.pacientes_df['Telefone'].values:
            return "Paciente já cadastrado!"
        
        # Adiciona o paciente ao DataFrame e salva no Excel
        novoPaciente = pd.DataFrame({'Nome': [nome], 'Telefone': [telefone]})
        self.pacientes_df = pd.concat([self.pacientes_df, novoPaciente], ignore_index=True)

        self.pacientes_df.to_excel('pacientes.xlsx')
        return "Paciente cadastrado com sucesso!"

    def cancelarConsulta(self, agendamento_telefone):
        # Limpar a variável de espaços em branco
        agendamento_telefone = agendamento_telefone.strip()

        # Verifica se o agendamento existe
        if agendamento_telefone not in self.agendamentos_df['Telefone'].astype(str).str.strip().values:
            return "Agendamento não existe!"

        # Remove o agendamento
        self.agendamentos_df = self.agendamentos_df[
            self.agendamentos_df['Telefone'].astype(str).str.strip() != agendamento_telefone
        ]

        # Salva a atualização no Excel
        try:
            self.agendamentos_df.to_excel('agendamentos.xlsx', index=False)
        except Exception as e:
            return f"Erro ao salvar o cancelamento do agendamento: {e}"

        return "Agendamento cancelado com sucesso!"

    def marcarConsulta(self, telefone_paciente, dia, hora, especialidade):
        # Remove espaços em branco do telefone
        telefone_paciente = telefone_paciente.strip()
        
        # Verifica se a consulta pode ser marcada
        try:
            data_consulta = datetime.strptime(f"{dia} {hora}", "%d/%m/%Y %H:%M")
            if data_consulta < datetime.now():
                return "Não é possível marcar consultas retroativas."
        except ValueError:
            return "Formato de data ou hora inválido."

        # Verifica se o horário já está ocupado
        if not self.agendamentos_df[
            (self.agendamentos_df['Dia'] == dia) & 
            (self.agendamentos_df['Hora'] == hora)
        ].empty:
            return "Este horário já está ocupado."

        # Identifica o paciente
        paciente = self.pacientes_df[self.pacientes_df["Telefone"].astype(str).str.strip() == telefone_paciente]

        if paciente.empty:
            return "Nenhum registro de paciente foi encontrado"

        paciente_info = paciente.iloc[0].to_dict()

        # Cria um novo agendamento
        novo_agendamento = pd.DataFrame({
            'Paciente': [paciente_info['Nome']],
            'Telefone': [paciente_info['Telefone']],
            'Dia': [dia],
            'Hora': [hora],
            'Especialidade': [especialidade]
        })

        # Adiciona o agendamento ao DataFrame e salva no Excel
        self.agendamentos_df = pd.concat([self.agendamentos_df, novo_agendamento], ignore_index=True)
        try:
            self.agendamentos_df.to_excel('agendamentos.xlsx', index=False)
        except Exception as e:
            return f"Erro ao salvar o agendamento: {e}"

        return "Consulta agendada com sucesso"

clinica_instancia = Clinica()

# flag para continuar loop
continua_loop = True

# Input
while continua_loop:
    print('+====================+')
    print('  MENU PRINCIPAL  ')
    print('1- Cadastrar Paciente ')
    print('2- Marcar Consulta ')
    print('3- Cancelar consulta')
    print('4- Sair ')
    print('+====================+')

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input('Digite seu nome: ')
        telefone = input('Digite seu telefone: ')
        #print('Paciente cadastrado com sucesso')
        print(clinica_instancia.cadastrarPaciente(nome, telefone))
    elif opcao == "2":
        try:
            paciente_telefone = input("Digite o número do paciente: ")
            
            dia = input("Digite o dia da consulta (dd/mm/yyyy): ")
            hora = input("Digite a hora da consulta (HH:MM): ")
            
            especialidade = input("Digite a especialidade: ")
            
            print(clinica_instancia.marcarConsulta(paciente_telefone, dia, hora, especialidade))
        except ValueError:
            print("Entrada inválida, por favor tente novamente.")
    elif opcao == "3":
        try:
            agendamento_telefone = input("Digite o Telefone do paciente: ")
            print(clinica_instancia.cancelarConsulta(agendamento_telefone))
        except ValueError:
            print("Entrada inválida, por favor tente novamente.")
    elif opcao == "4":
        print("Encerrando o programa...")
        continua_loop = False
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")