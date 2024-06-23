# Clínica Ágil

Desenvolvi um sistemas de consultas para uma clínica. Foi um desafio proposto pela Aceleradora Ágil.

## Algumas instruções para abrir o projeto:

É necessário a instalação da biblioteca pandas e o venv, para isso, submeta ao terminal:
1-pip install pandas
2-.venv/Scripts/activate

# Desafio

Você foi contratado para desenvolver um sistema de clínica de consultas no seu bairro.
Seus vizinhos não estão se sentindo muito bem e gostariam de agendar consultas. Para
isso, você deverá desenvolver as seguintes funcionalidades, que devem ser apresentadas
para o usuário através de um menu via terminal:
Cadastrar um paciente : O programa solicita o nome e o telefone do usuário. Após o
cadastro, exibe a mensagem "Paciente cadastrado com sucesso" e adiciona o paciente à
lista de Pacientes Cadastrados. Em seguida, retorna ao menu principal.
Marcações de consultas : Ao selecionar essa opção, o programa exibe uma lista
numerada dos pacientes cadastrados. Ao escolher o número correspondente a um
paciente, solicita o dia, a hora e a especialidade desejada para a consulta. Após o envio
desses dados, o agendamento é adicionado à lista de agendamentos e o programa
retorna ao menu principal.
Cancelamento de consultas : Ao selecionar essa opção, o programa exibe uma lista
numerada dos agendamentos existentes. Ao escolher o número correspondente ao
agendamento que deseja remarcar, é exibida uma mensagem informando a data, a hora e
a especialidade da consulta agendada. Nesse momento, o usuário pode optar por
cancelar a consulta. Ao confirmar o cancelamento, o agendamento é removido da lista e o
programa retorna ao menu principal.
Sair : O programa encerra a execução.

# Tratamento de erros:
● O paciente não pode ser cadastrado mais de uma vez. Para evitar duplicidade,
garanta que o número de telefone seja diferente para cada cadastro. Caso ocorra
uma tentativa de cadastro duplicado, exiba a mensagem "Paciente já cadastrado!"
e retorne ao menu principal.
● Pacientes não podem marcar consultas em dias e horários já agendados. Verifique
se a data e a hora selecionadas estão disponíveis antes de realizar o
agendamento.
● Consultas não podem ser marcadas antes da data atual. Certifique-se de que o
usuário não possa agendar consultas retroativas.

# Extra:
Seria muito legal se você conseguisse implementar uma maneira de armazenar as
informações dos pacientes de forma que eles continuassem existindo mesmo após o
usuário sair do sistema. Que funcionasse como uma espécie de “banco de dados”.
