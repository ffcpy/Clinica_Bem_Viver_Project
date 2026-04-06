from datetime import datetime 

#-----------EVERTHING OK, BUT I HAVE SOME BUGS --------------#
def init_menu():
    print("FICHA DE ANAMNESE MULTIDISCIPLINAR")
    print("1. IDENTIFICAÇÃO DA CRIANÇA")
    child_ident()
def child_ident():
    while True:
        try:
            name = input("Nome completo:  ").strip()
            if name:
                break 
            else:
                print("Digite um nome válido.")
        except:
            print("Resposta não registrada, digite uma opção válida.")
    while True:
        date_birth = input("Data de nascimento:  ")
        try:
            date_birth == datetime.strptime(date_birth, "%d/%m/%Y")
            break
        except:
            print("Resposta não registrada, digite uma opção válida.")
    while True:
        try:
            age = int(input(f"Qual a idade do(a) {name}?:   "))
            if age > 0:
                break
            else:
                print("Resposta não registrada, digite uma opção válida.")
        except ValueError:
            print("Resposta não registrada, digite uma opção válida.")


    while True:
        gender = input("(M) MASCULINO - (F) FEMININO:  ").upper()
        if gender in ["M", "F"]:
            break
        else:
            print("Resposta não registrada, digite uma opção válida.")
    while True:
        try:
            postal = input("Endereço da criança:  ")
            if postal: 
                break
            else:
                print("Resposta não registrada, digite uma opção válida.")
        except:
            print("Resposta não registrada, digite uma opção válida.")
    while True:
        nacionality = input("Naturalidade:  ")
        if nacionality:
            break
        else:
            print("Resposta não registrada, digite uma opção válida.")
    parents()
def parents():
    print("1.1 IDENTIFICAÇÃO DOS RESPONSÁVEIS")
    while True:
        try:
            name_p = input("Nome da mãe:  ")
            break
        except:
            print("Resposta não registrada, digite uma opção válida.")
    while True:
        try:
            job_p = input("Profissão:  ")
            break
        except:
            print("Resposta não registrada, digite uma opção válida.")
    while True:
        try:
            tel_p = input("Telefone: ")
            break
        except:
            print("Resposta não registrada, digite uma opção válida.")
    school()
def school():
    print("1.2 DADOS ESCOLARES")
    while True:
        try:
            school_name = input("Escola:  ").strip().upper()
            if school_name:
                break 
        except:
            print("Digite um nome válido.")
    while True:
        type_school = int(input("(1) - Particular\n (2) - Pública\n(3) - Bilingue?:\n"))
        try:
            if type_school in [1, 2, 3]:
                break 
        except:
            print("Digite uma opção válida.")

    while True:
        period = int(input("Horário de aula:\n(1) - Manhã\n(2) - Tarde\n(3) - Integral  "))
        try:
            if period in [1, 2, 3]:
                break 
        except:
            print("Digite uma opção válida.")
    while True:
            try:
                teacher = input("Professor(a):  ").strip().upper()
                if teacher:
                    break 
                else:
                    print("Digite um nome válido.")
            except:
                print("Digite uma opção válida.")
    historical_school()
def historical_school():
    print("2. HISTÓRICO ESCOLAR")
    while True:
        question1 = input("Possui Acompanhante Terapêutica?:  ").strip().upper()
        if question1 in ["S", "SIM", "N", "NÃO"]:
            break
        else:
            print("Digite uma opção válida.")
        if question1 in["S", "SIM"]:
            while True:
                try:
                    question1_1 = int(input("(1) - Tutora ou (2) - Auxiliar para a criança?"))
                    if question1_1 in [1, 2]:
                        break
                    else:
                        print("Digite 1 ou 2 ")
                except:
                    print("Digite uma opção válida.")
                while True:
                    question1_2 = input("Quanto tempo permanece com a criança?:  ")
                    if question1_2:
                        break
                    else:
                        print("Digite uma opção válida.")
    while True:
        question2 = input("Dificuldades acadêmicas relatadas (leitura, escrita, matemática):  ")
        if question2:
            break
        else:
                print("Digite uma opção válida.")
    while True:
        question3 = input("Comportamento na sala de aula (comportamento com professor, colegas, participação):  ")
        if question3:
            break 
        else:
            break
    while True: 
        try:
            question4 = int(input("Relação com professores e coordenação:\n(1) - BOA\n(2) - MÉDIA\n(3) - RUIM\n"))
            if question4 in [1, 2, 3, 4]:
                break
        except:
            print("Digite uma opção válida.")
    while True:
        question5 = input("Adaptações/ACPs/Planos Pedagógicos existentes:\n")
        if question5:
            break
        else:
            print("Campo Obrigatório.")
    while True:
        try:
            question6 = int(input("Uso de recursos escolares (monitoria, sala de apoio, AVA, etc)\n(1) - Sim\n(2) - Não\n"))
            if question6 in [1, 2]:
                break
        except:
            print("Campo Obrigatório.")
    while True:
        question7 = input("Transporte escola-casa (quem acompanha/tempo de deslocamento):\n")
        if question7:
            question7_1 = input("Tempo de deslocamento:\n")
            if question7_1:
                break
            else:
                print("Campo Obrigatório.")
    diagnostic()
def diagnostic():
    print("3. QUADRO DIAGNÓSTICO E HISTÓRICO DO CLIENTE")
    while True:
        complaint = input("Queixa Principal (motivo da procura de atendimento e principais demandas de acordo com os pais):\n")
        if complaint:
            break
        else: 
            print("Campo Obrigatório.")
    while True:
        print("Histórico do quadro (diagnóstico) atual:")
        try:
            context = int(input("Qual idade descobriu?\n"))
            break
        except:
            print("Campo Obrigatório.")
    while True: 
        context1 = input("Qual profissional diagnosticou?\n")
        if context1:
            break
        else:
            print("Campo Obrigatório.")
    while True:
        context1_1 = input("Quais tratamentos já realizou?:\n")
        if  context1_1:
            break
        else:
            print("Campo Obrigatório.")
    while True:
            try:
                medication = int(input("Faz Uso de Medicação?:\n(1) - Sim\n(2) - Não\n"))
                if medication in [1, 2]:
                    break
                else:
                    print("Digite 1 ou 2")
            except:
                print("Digite um Número válido.")
    if  medication == 1:
        while True:
                medication_name = input("Nome:\n")
                if  medication_name:
                    break
                else:
                    print("Campo Obrigatório.")

        while True:           
            medication_time = input("Horário:\n")
            if medication_time:
                break
            else:
                print("Campo Obrigatório.")
        while True:
            medication_dose = input("Dosagem:\n")
            if medication_dose:
                break
            else:
                print("Campo Obrigatório.")
                
    while True:
        try:
            allergy = int(input("Alergias ou Dietas Especificas?:\n(1) - Sim\n(2) - Não\n"))
            if allergy in [1, 2]:
                break
        except:
            print("Campo Obrigatório.")
    if allergy == 1:
        while True:
            allergy1 = input("Quais?:\n")
            if allergy:
                break
            else:
                print("Campo Obrigatório.")
    while True:
        try:
            vacionation = int(input("Vacinação em dia?:\n(1) - Sim\n(2) - Não\n"))
            if vacionation in [1, 2]:
                break
            else:
                print("Campo Obrigatório.")
        except:
            print("Digite um Número válido.")
    while True:
        try:
            health = int(input("Possui condições médicas crônicas? (ASMA, DIABETES, REFLUXO, ETC.)\n(1) - Sim\n(2) - Não\n"))
            if health in [1, 2]:
                break
            else:
                print("Digite um Número válido.")
        except:
            print("Campo Obrigatório.")
    if health == 1:
        while True:
            health1 = input("Quais?\n")
            if health1:
                break
            else:
                print("Campo Obrigatório.")
    birth()            
def birth():
    print("3.1. HISTÓRICO GESTACIONAL E DE NASCIMENTO")
    while True:
        question8 = input("Gestação (Planejada, complicações, medicações, consumo de substâncias):\n")
        if question8: 
            break 
        else:
            print("Campo Obrigatório.")
    while True:
        question9 = input("Parto (termo, prematuro, cesárea, fórceps):\n")
        if question9:
            break
        else:
            print("Campo Obrigatório.")
    while True:
        try:
            question10 = float(input("Peso ao nascer (Kg):\n"))       
            if question10 > 0 and question10 < 15:
                break
            else:
                print("Digite um número válido")
        except:
             print("Campo Obrigatório.")
    while True:
        try:
            question11 = int(input("Houve internação hospitalar ao nascer\n(1) - Sim\n(2) - Não\n"))
            if question11 in [1, 2]:
                break 
            else:
                print("Digite um número válido")
        except:
            print("Campo Obrigatório.")
    while True:
            question12 = input("Tempo de aleitamento:\n")
            if question12: 
                break 
            else:
                print("Campo Obrigatório.")
    neuro_dsnv_histc()
#LEMBRAR DE CHAMAR FUNCOES (DEF) FORA DO WHILE ---  FEITO

#EVERTHING IS OK RIGHT THERE
def neuro_dsnv_histc():
    print("3.2. HISTÓRICO DE DESENVOLVIMENTO NEUROPSICOMOTOR")
    while True:
        question13 = input("1 - Sentar")
        if question13:
            break
        else:
            print("Campo Obrigatório.")
    while True: 
            question13_1 = input("2 - Engatinhar\n")
            if question13_1:
                break
            else:
                print("Campo Obrigatório.")
    while True:
        question13_2 = input("3 - Andar\n")
        if question13_2:
            break
        else:
            print("Campo Obrigatório.")
    while True:
        question13_3 = input("4 - Primeiras Palavras\n")
        if question13_3:
            break
        else:
            print("Campo Obrigatório.")
    while True:
        question13_4 = input("5 - Controle de Fralda\n")
        if question13_4:
            break
        else:
            print("Campo Obrigatório.")
    while True:
        question14 = input("Apresenta dificuldades motoras ou de coordenação?\n")
        if question14:
            break
        else:
            print("Campo Obrigatório.")
    while True:
            question15 = input("Já há atrasos identificados?\n").strip().upper()
            if question15 in ["S", "SIM", "N", "NÃO", 'NAO']:
                break
            else:
                print("Campo Obrigatório.")
    while True:
            question16 = input("História de convulsões, trauma craniano, internações?\n").strip().upper()
            if question16 in ["N", "NÃO"]:
                break
            elif question16 in ["S", "SIM"]:
                while True:
                    question16_1 = input("Quais?:\n")
                    if question16_1:
                        break
                    else:
                        print("Campo Obrigatório.")
                break
            else:
                print("Digite Sim ou Nào.")
    psiqui()
#EVERTHING IS OK RIGHT THERE

#DEIXAR PROFISSIONAIS MAISCULOS TIPO (PSICOLOGO) - FEITO 
def psiqui():
    print("4. ATENDIMENTOS ATUAIS / HISTÓRICOS")
    psiqui_name = obrigatory_question("PSIQUIATRA\n(1) - Nome:\n")
    psiqui_tel = int_question("(2) - Contato\n")
    psiqui3 = obrigatory_question("Qual o diagnóstico atual e há quanto tempo foi estabelecido?\n")
    psiqui4 = obrigatory_question("Como e com que frequência o(a) paciente é acompanhado (retornos, ajustes)")
    neuro()
def neuro():
    print("--------------------------------------------")
    neurop_name = obrigatory_question("NEUROPEDIATRA\n(1) - Nome:\n")
    neurop_tel = int_question("(2) - Contato\n")
    neurop3 = question_sn("Há laudos/relatórios/avaliações neurológicas recentes?\n")
    neurop4 = obrigatory_question("Existe recomendação de exames, medicações ou intervenções específicas?")
    neurop5 = obrigatory_question("Quais sinais neurológicos/observações motoras foram apontadas?")
    psico()
def psico():
    print("--------------------------------------------")
    psico_name = obrigatory_question("PSICÓLOGO\n(1) - Nome:\n")
    psico_tel = int_question("(2) - Contato\n")
    psico3 = obrigatory_question("Quais objetivos do acompanhamento atual?\n")
    psico4 = obrigatory_question("Quais estratégias/intervenções estão sendo usadas em sessão e em casa?\n")
    psico5 = obrigatory_question("Qual a frequência das sessões e adesão do paciente/família?\n")
    fono()
#DEIXAR PROFISSIONAIS MAISCULOS TIPO (PSICOLOGO) - FEITO


# CHAMAR FUNC's -- FEITO
def fono():
    print("--------------------------------------------")
    fono_name = obrigatory_question("FONOAUDIÓLOGO\n(1) - Nome:\n")
    fono_tel = int_question("(2) - Contato\n")
    fono3 = obrigatory_question("Qual o nível atual da linguagem (compreensão, expressão, pragmática, fonologia)?\n")
    fono4 = question_sn("Há uso de recursos alternativos de comunicação (PECS, comunicador, gestos)")
    t_o()
def t_o():
    print("--------------------------------------------")
    t_o_name = obrigatory_question("TERAPIA OCUPACIONAL\n(1) - Nome:\n")
    t_o_tel = int_question("(2) - Contato\n")
    t_o3 = obrigatory_question("Há queixas sensoriais (hipersensibilidade, hipossensibilidade) ou motoras?\n")
    t_o4 = obrigatory_question("Quais objetivos funcionais estão sendo trabalhados (coordenação, regulação, atividades de vida diária)?\n")
    t_o5 = obrigatory_question("Quais adaptações ambientais ou materiais foram sugeridos?\n")
    nutri()
def nutri():
    print("--------------------------------------------")
    nutri_name = obrigatory_question("TERAPIA OCUPACIONAL\n(1) - Nome:\n")
    nutri_tel = int_question("(2) - Contato\n")
    psipeda()
def psipeda():
    print("--------------------------------------------")
    psipeda_name = obrigatory_question("TERAPIA OCUPACIONAL\n(1) - Nome:\n")
    psipeda_tel = int_question("(2) - Contato\n")
    psimot()
def psimot():
    print("--------------------------------------------")
    psimo_name = obrigatory_question("TERAPIA OCUPACIONAL\n(1) - Nome:\n")
    psimo_tel = int_question("(2) - Contato\n")
    a_t()
def a_t():
    print("--------------------------------------------")
    a_t_name = obrigatory_question("TERAPIA OCUPACIONAL\n(1) - Nome:\n")
    a_t_tel = int_question("(2) - Contato\n")
    musico()
def musico():
    print("--------------------------------------------")
    musico_name = obrigatory_question("TERAPIA OCUPACIONAL\n(1) - Nome:\n")
    musico_tel = int_question("(2) - Contato\n")
    ling_and_comunic()
#CHAMAR FUNC's -- FEITO 

def ling_and_comunic():
    print("--------------------------------------------")
    question17 = question_sn("Há atraso no desenvolvimento da linguagem? (sim / não)\n")
    question18 = obrigatory_question("Como a criança se comunica ou tenta se comunicar? (gestos, apontar, trocas de figura, dispositivos)?\n")
    question19 = question_sn("Uso de linguagem repetitiva (ecolalia)?\n")
    question20 = question_sn("Há tentativa de iniciar/manter conversas com adultos/crianças?\n")
    question21 = question_sn("O vocabulário é adequado à idade?\n")
    question22 = question_sn("A fala é compreensível para outras pessoas?\n")
    behavior()




#PADRONIZAR FORMATACAO DE MODO GERAL TIPO (:) --- NAO FIZ AINDA
def behavior():
    print("--------------------------------------------")
    question23 = question_sn("A criança/adolescente procura interagir com pessoas próximas a ela? (s/n)\n")
    question24 = question_sn("A criança interage com outras crianças de alguma forma ou em algum outro momento?\n")
    question25 = question_sn("Interage e/ou desenvolve amizade/relacionamento com adultos?\n")
    question26 = question_sn("Demonstra interesse por brincadeiras e jogos?\n")
    question27 = question_sn("Brinca de faz de conta ou imitação?\n")
    question28 = obrigatory_question("Descrição do comportamento de brincar?\n(Quais os principais itens que brinca, e como brinca com esses mesmos itens?)\n")
    question29 = obrigatory_question("Como reage a mudanças de rotina? (resiste, aceita, necessita preparo)?\n")
    question30 = question_sn("Apresenta movimentos repetitivos / estereotipias?\n")
    question31 = obrigatory_question("Hiperfoco / interesses restritos e intensos (descrever):\n")
    question32 = obrigatory_question("Respostas a frustrações/limites (choro, birra, agressividade, retirada):\n")
    question33 = question_sn("Apresenta comportamentos heterolesivos ou autolesivos?\n")
    question34 = obrigatory_question("Mostra medos, ansiedade ou sensibilidade sensorial (som, textura, luz):\n")
    activity()

def activity():
    print("--------------------------------------------")

#DESCOBRI O FOGO E MINHA VIDA ESTA 10000X MAIS FACIL COM ESSAs FUNC
def question_sn(texto):
    while True:
        resp = input(texto).strip().upper()
        if resp in ["S", "SIM", "N", "NAO", "NÃO"]:
            return resp
        print("Digite S ou N.")
def int_question(texto):
    while True:
        try:
            valor = int(input(texto))
            return valor
        except ValueError:
            print("Digite um número inteiro válido.")
def float_question(texto):
    while True:
        try:
            valor = float(input(texto))
            return valor
        except ValueError:
            print("Digite um número válido.")
def obrigatory_question(texto):   
     while True:
        resp = input(texto)
        if resp:
            return resp
        print("Campo obrigatório.")         
#DESCOBRI O FOGO E MINHA VIDA ESTA 10000X MAIS FACIL COM ESSAs FUNC       

init_menu()




    