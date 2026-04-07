from datetime import datetime 
import json


def anamnese_create():
    return {
        "Identificacao" : {},
        "Responsaveis" : {},
        "Dados_Escolares": {},
        "Historico_Escolar": {},
        "Diagnostico": {},
        "Gestacao": {},
        "Desenvolvimento": {},
        "Atendimentos_atuais": {
            "Psiquiatra": {},
            "Neuropediatra": {},
            "Psicologo": {},
            "Fonoaudiologo": {},
            "Terapia_Ocupacional": {},
            "Nutricionista": {},
            "Psicopedagogo": {},
            "Psicomotricista": {},
            "Acompanhante_Terapeutica": {},
            "Musicoterapia": {},
        },
        "Comunicacao_e_Linguagem" : {},
        "Interacao_social_e_comportamento" : {},
        "Atividades_Telas_e_rotina" : {},
        "Rotina_do_Sono" : {},
        "Alimentacao" : {},
        "Higiene_e_Autonomia" : {},
        "Historico_Familiar" : {},
        "Rotina_Diaria" : {},
        "Atividades_e_Trabalho_dos_Pais" : {},
        "Objetivos_e_Expectativas": {},
        "Observacoes": {},
        "encaminhamento" : {},
        "finalizacao" : {}

    }

anamnese = anamnese_create


#-----------EVERTHING OK, BUT I HAVE SOME BUGS --------------#
def init_menu():
    print("FICHA DE ANAMNESE MULTIDISCIPLINAR")
    print("1. IDENTIFICAÇÃO DA CRIANÇA")
    child_ident(anamnese)
def child_ident(anamnese):
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

    anamnese["Identificacao"] = {
        "Nome" : name,
        "Data_de_Nascimento" : date_birth,
        "Idade" : age,
        "Genero": gender,
        "Endereco" : postal,
        "Naturalidade" : nacionality
    }
    parents(anamnese)
    
def parents(anamnese):
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

    anamnese["Responsaveis"] = {
        "Nome_da_mae" : name_p,
        "Profissao" : job_p,
        "Telefone" : tel_p
    }
    school(anamnese)

def school(anamnese):
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

    anamnese["Dados_Escolares"] = {
        "Nome_da_Escola" : school_name,
        "Tipo_de_escola" : type_school,
        "Periodo" : period,
        "Professor" : teacher
    }
    historical_school(anamnese)

def historical_school(anamnese):
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

    anamnese["Historico_Escolar"] = {
        "Acompanhante_Terapeutico" : {
            "Tipo" : question1_1,
            "Tempo" : question1_2
        },
        "Dificuldades_Academicas" : question2,
        "Comportamento" : question3,
        "Relacao_Professores" : question4,
        "Adaptacoes_Acp_Planos" : question5,
        "Recursos_Escolares" : question6,
        "Transporte" : question7
    }
    diagnostic(anamnese)
def diagnostic(anamnese):
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
            if allergy1:
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

    anamnese["Diagnostico"] = {
        "Queixa" : complaint,
        "Idade_Diagnostico" : context,
        "Profissional_Diagnostico" : context1,
        "Tratamentos" : context1_1,
        "Uso_de_Medicacao" : medication,
        "Info_medicacao" : {
            "Nome_medicacao" : medication_name,
            "Horario_medicacao" : medication_time,
            "Dose_medicacao" : medication_dose
        },
        "Alergia" : allergy,
        "Quais_alergias" : allergy1,
        "Vacinacao_em_dia" : vacionation,
        "Condicoes_medicas" : health,
        "Quais_condicoes" : health1
            
    }
    birth(anamnese)            
def birth(anamnese):
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

    anamnese["Gestacao"] = {
        "Sobre_gestacao" : question8,
        "Tipo_parto" : question9,
        "Peso_nascimento" : question10,
        "Internacao_ao_nascer" : question11,
        "Tempo_aleitamento" : question12
    }
    neuro_dsnv_histc(anamnese )
#LEMBRAR DE CHAMAR FUNCOES (DEF) FORA DO WHILE ---  FEITO

#EVERTHING IS OK RIGHT THERE
def neuro_dsnv_histc(anamnese):
    print("3.2. HISTÓRICO DE DESENVOLVIMENTO NEUROPSICOMOTOR")
    print("INDIQUE A IDADE APROXIMADA AO:")
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

    anamnese["Desenvolvimento"] = {
        "Idade_ao:" : {
            "Engatinhar" : question13_1,
            "Andar" : question13_2,
            "Primeras_palavras" : question13_3,
            "COntrole_de_fralda" : question13_4,
        },
        "Dificuldade_motora" : question14, 
        "Atrasos_identificados" : question15,
        "Conv_traumas_intern" : question16,
        "Quais" : question16_1
    }
    psiqui(anamnese)
#EVERTHING IS OK RIGHT THERE

#DEIXAR PROFISSIONAIS MAISCULOS TIPO (PSICOLOGO) - FEITO 
def psiqui(anamnese):
    print("4. ATENDIMENTOS ATUAIS / HISTÓRICOS")
    psiqui_name = obrigatory_question("PSIQUIATRA\n(1) - Nome:\n")
    psiqui_tel = int_question("(2) - Contato\n")
    psiqui3 = obrigatory_question("Qual o diagnóstico atual e há quanto tempo foi estabelecido?\n")
    psiqui4 = obrigatory_question("Como e com que frequência o(a) paciente é acompanhado (retornos, ajustes)")
    
    anamnese["Psiquiatra"] = {
        "Nome" : psiqui_name,
        "Contato" : psiqui_tel,
        "Diagnostico_e_tempo" : psiqui3,
        "Frequencia" : psiqui4
        }
    
    neuro(anamnese)
def neuro(anamnese):
    print("--------------------------------------------")
    neurop_name = obrigatory_question("NEUROPEDIATRA\n(1) - Nome:\n")
    neurop_tel = int_question("(2) - Contato\n")
    neurop3 = question_sn("Há laudos/relatórios/avaliações neurológicas recentes?\n")
    neurop4 = obrigatory_question("Existe recomendação de exames, medicações ou intervenções específicas?")
    neurop5 = obrigatory_question("Quais sinais neurológicos/observações motoras foram apontadas?")
    
    anamnese["Neuropediatra"] = {
        "Nome" : neurop_name,
        "Contato" : neurop_tel,
        "Laudos_rel_aval" : neurop3,
        "Recomend_especif" : neurop4,
        "Sinais_apontados" : neurop5
    }
    
    psico(anamnese)
def psico(anamnese):
    print("--------------------------------------------")
    psico_name = obrigatory_question("PSICÓLOGO\n(1) - Nome:\n")
    psico_tel = int_question("(2) - Contato\n")
    psico3 = obrigatory_question("Quais objetivos do acompanhamento atual?\n")
    psico4 = obrigatory_question("Quais estratégias/intervenções estão sendo usadas em sessão e em casa?\n")
    psico5 = obrigatory_question("Qual a frequência das sessões e adesão do paciente/família?\n")
    
    anamnese["Psicologo"] = {
        "Nome" : psico_name,
        "Contato" : psico_tel,
        "Objetivos" : psico3,
        "Estrategias" : psico4,
        "Frequencia" : psico5,
    }
    
    fono(anamnese)
#DEIXAR PROFISSIONAIS MAISCULOS TIPO (PSICOLOGO) - FEITO


# CHAMAR FUNC's -- FEITO
def fono(anamnese):
    print("--------------------------------------------")
    fono_name = obrigatory_question("FONOAUDIÓLOGO\n(1) - Nome:\n")
    fono_tel = int_question("(2) - Contato\n")
    fono3 = obrigatory_question("Qual o nível atual da linguagem (compreensão, expressão, pragmática, fonologia)?\n")
    fono4 = question_sn("Há uso de recursos alternativos de comunicação (PECS, comunicador, gestos)")
   
    anamnese["Fonoaudiologo"] = {
        "Nome" : fono_name,
        "Contato" : fono_tel,
        "Nivel_linguagem" : fono3,
        "Recursos_alt" : fono4
        
    }
    
   
    t_o(anamnese)
def t_o(anamnese):
    print("--------------------------------------------")
    t_o_name = obrigatory_question("TERAPIA OCUPACIONAL\n(1) - Nome:\n")
    t_o_tel = int_question("(2) - Contato\n")
    t_o3 = obrigatory_question("Há queixas sensoriais (hipersensibilidade, hipossensibilidade) ou motoras?\n")
    t_o4 = obrigatory_question("Quais objetivos funcionais estão sendo trabalhados (coordenação, regulação, atividades de vida diária)?\n")
    t_o5 = obrigatory_question("Quais adaptações ambientais ou materiais foram sugeridos?\n")
   
    anamnese["Terapia_Ocupacional"] = {
        "Nome" : t_o_name,
        "Contato" : t_o_tel,
        "Queixas" : t_o3,
        "Objetivos" : t_o4,
        "Adaptacoes" : t_o5,
    }
    
   
    nutri(anamnese)
def nutri(anamnese):
    print("--------------------------------------------")
    nutri_name = obrigatory_question("NUTRICIONISTAL\n(1) - Nome:\n")
    nutri_tel = int_question("(2) - Contato\n")
    
    anamnese["Nutricionista"] = {
        "Nome" : nutri_name,
        "Contato" : nutri_tel

    }
    
    
    psipeda(anamnese)
def psipeda(anamnese):
    print("--------------------------------------------")
    psipeda_name = obrigatory_question("PSICOPEDAGOGO\n(1) - Nome:\n")
    psipeda_tel = int_question("(2) - Contato\n")
   
    anamnese["Psicopedagogo"] = {
        "Nome" : psipeda_name,
        "Contato" : psipeda_tel
        
    }
    
   
    psimot(anamnese)
def psimot(anamnese):
    print("--------------------------------------------")
    psimo_name = obrigatory_question("PSICOMOTRICISTA\n(1) - Nome:\n")
    psimo_tel = int_question("(2) - Contato\n")
   
    anamnese["Psicomotricista"] = {
        "Nome" : psimo_name,
        "Contato" : psimo_tel
        
    }
   
    a_t(anamnese)
def a_t(anamnese):
    print("--------------------------------------------")
    a_t_name = obrigatory_question("ACOMPANHANTE TERAPÊUTICO\n(1) - Nome:\n")
    a_t_tel = int_question("(2) - Contato\n")
   
    anamnese["Acompanhnate_Terapuetica"] = {
        "Nome" : a_t_name,
        "Contato" : a_t_tel
        
    }
   
    musico(anamnese)
def musico(anamnese):
    print("--------------------------------------------")
    musico_name = obrigatory_question("MUSICOTERAPIA\n(1) - Nome:\n")
    musico_tel = int_question("(2) - Contato\n")
    
    anamnese["Musicoterapia"] = {
        "Nome" : musico_name,
        "Contato" : musico_tel
        
    }
    
    ling_and_comunic(anamnese)
#CHAMAR FUNC's -- FEITO 

def ling_and_comunic(anamnese):
    print("--------------------------------------------")
    print("5. COMUNICAÇÃO E LINGUAGEM")
    question17 = question_sn("Há atraso no desenvolvimento da linguagem? (sim / não)\n")
    question18 = obrigatory_question("Como a criança se comunica ou tenta se comunicar? (gestos, apontar, trocas de figura, dispositivos)?\n")
    question19 = question_sn("Uso de linguagem repetitiva (ecolalia)?\n")
    question20 = question_sn("Há tentativa de iniciar/manter conversas com adultos/crianças?\n")
    question21 = question_sn("O vocabulário é adequado à idade?\n")
    question22 = question_sn("A fala é compreensível para outras pessoas?\n")
    
    anamnese["Comunicacao_e_linguagem"] = {
        "Atraso_linguagem" : question17,
        "Como_comunica" : question18,
        "Ecolalia" : question19,
        "Conv_interp" : question20,
        "Voc_adequeado_idade" : question21,
        "Fala_compreensivel" : question22
    }
    
    behavior(anamnese)




#PADRONIZAR FORMATACAO DE MODO GERAL TIPO (:) --- NAO FIZ AINDA
def behavior(anamnese):
    print("--------------------------------------------")
    print("6. INTERAÇÃO SOCIAL E COMPORTAMENTO")
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
    
    anamnese["Interacao_social_e_comportamento"] = {
        "Interacao" : question23,
        "Interacao_adultos" : question25,
        "Inte_brincadeiras" : question26,
        "Faz_d_conta/imitacao" : question27,
        "Comportamento_brincar" : question28,
        "Mudanca_rotina" : question29,
        "Movimento_rep" : question30,
        "Hiperfoco" : question31,
        "Resposta_frustracao" : question32,
        "Hetero/autolesivo" : question33,
        "Medo_ans_sens_sensorial" : question34
    }
    
    
    activity(anamnese)

def activity(anamnese):
    print("--------------------------------------------")
    print("7. ATIVIDADES, TELAS E ROTINA DE TEMPO LIVRE")
    print("--------------------------------------------")
    question35 = obrigatory_question("Tempo diário médio de uso de telas (tipo: TV, tablet, celular, jogos)\n")
    question36 = obrigatory_question("Preferências de brincadeiras (solitárias / com adultos / com pares):\n")
    question37 = obrigatory_question("Quais brinquedos/itens atraem mais (carros, bonecos, jogos digitais, etc.):\n")
    
    anamnese["Atividades_Telas_e_rotina"] = {
        "Tempo_dia_tela" : question35,
        "Pref_brincadeiras" : question36,
        "Brinquedos_pref" : question37
    }
    
    sleep_routine(anamnese)

def sleep_routine(anamnese):
    print("--------------------------------------------")
    print("8. ROTINA DO SONO")
    print("--------------------------------------------")
    question38 = obrigatory_question("Horário para dormir (Noite):\n")
    question39 = obrigatory_question("Horário de acordar:\n")
    question40 = float_question("Tempo médio de sono (Horas):\n")
    question41 = obrigatory_question("Dificuldades para iniciar/manter sono? (despertar noturno, pesadelos):\n")
    question42 = obrigatory_question("Há rotinas/rituais para dormir? (leitura, música, calmantes):\n")

    anamnese["Rotina_do_Sono"] = {
        "Horario_dormir" : question38,
        "Horario_acordar" : question39,
        "Media_sono" : question40,
        "Dificuldade_sono" : question41,
        "Rituais_dormir" : question42
    
    }

    food(anamnese)


def food(anamnese):
    print("--------------------------------------------")
    print("9. ALIMENTACAO")
    print("--------------------------------------------")
    question43 = obrigatory_question("Tipo de alimentação (variada / seletiva / restritiva):")
    question44 = obrigatory_question("Há intolerâncias ou restrições alimentares (lactose, glúten, etc):")
    question45 = obrigatory_question("Apresenta seletividade / rejeição a texturas/temperaturas:")
    question46 = obrigatory_question("Horários das refeições e rotina alimentar:")
    question47 = question_sn("Faz uso de suplementos ou fórmulas:")
    question48 = question_sn("Apresenta episódios de engasgo, refluxo ou vômitos:")
    question49 = obrigatory_question("Como está o intestino e características padrão das fezes:")

    
    anamnese["Alimentacao"] = {
        "tipo_alim" : question43,
        "intolerancia_alim" : question44,
        "seletividade_alim" : question45,
        "hor_alim" : question46,
        "uso_supemento" : question47,
        "refluxos_vomitos" : question48,
        "fezes" : question49
    }

    higyene(anamnese)

def higyene(anamnese):
    print("--------------------------------------------")
    print("9. HIGIENE")
    print("--------------------------------------------")
    question50 = obrigatory_question("Nível de autonomia em higiene (trocar roupa, escovar dente, banheiro):\n")
    question51 = question_sn("Enurese / encoprese (sim/não; frequência):\n")
    if question51 in ["S", "SIM"]:
        question51_1 = obrigatory_question("Frequência")
    
    anamnese["Higiene_e_autonomia"] = {
        "nivel_autonomia" : question50,
        "enurese_encoprese" : question51,
        "frequencia" : question51_1
    }

    family_hist(anamnese)

def family_hist(anamnese):
    print("--------------------------------------------")
    print("9. HISTORICO FAMILIAR")
    print("--------------------------------------------")
    question52 = question_sn("Há antecedentes familiares de atraso no desenvolvimento,\n transtornos psiquiátricos, TDAH, autismo, deficiência intelectual, ou outros?\n")
    question53 = obrigatory_question("Estrutura familiar (quem mora com a criança):\n")
    question54 = obrigatory_question("Relacao entre os pais/responsaveis:\n")
    question55 = obrigatory_question("Relação com avós e presença de rede de apoio (quem ajuda, frequência):\n")

    anamnese["Historico_familiar"] = {
        "antecedentes_fam" : question52,
        "quem_mora" : question53,
        "rel_pais" : question54,
        "rel_rdapoio" : question55
    }

    day_rout(anamnese)


def day_rout(anamnese):
    print("--------------------------------------------")
    print("10. ROTINA DIARIA")
    print("--------------------------------------------")
    question56 = obrigatory_question("Descreve um dia típico da criança:\nManhã:\n")
    question56_1 = obrigatory_question("Tarde:\n")
    question56_2 = obrigatory_question("Noite:\n")
    question57 = obrigatory_question("Com quem a criança passa a maior parte do tempo?\n(ex.: na escola, com familiares, sozinho, em dispostivos:\n")
    question58 = obrigatory_question("Quais atividades ela mais gosta de fazer:\n")
    question59 = question_sn("Há regras e combinados em casa:")
    question60 = question_sn("A família participa dos atendimentos e acompanhamentos:\n")
    question61 = obrigatory_question("Descrição de comportamentos típicos da criança em ambientes:\n")


    anamnese["Rotina_Diaria"] = {
        "dia_tipico" : {
            "manha" : question56,
            "tarde" : question56_1,
            "noite" : question56_2
        },
        "maior_parte_tempo" : question57,
        "atividades" : question58,
        "regras_casa" : question59,
        "familia_atendimentos" : question60,
        "comportamentos_ambiente" : question61
    }

    parents_job(anamnese)


def parents_job(anamnese):
    print("--------------------------------------------")
    print("11. ATIVIDADES EXTRACURRICULARES / TRABALHO DOS PAIS")
    print("--------------------------------------------")
    question62 = obrigatory_question("Atividades que a criança realiza fora da escola (esporte, música, reforço):\n")
    question63 = obrigatory_question("Condições de trabalho dos pais (horários, disponibilidade para acompanhamento):\n")
    question64 = obrigatory_question("Possibilidade/tempo de qualidade com a criança:\n")

    anamnese["Atividades_e_Trabalho_dos_Pais"] = {
        "atividades_crianca" : question62,
        "cond_trab_pais" : question63,
        "temp_qual_crianca" : question64
    }

    objetives(anamnese)


def objetives(anamnese):
    print("--------------------------------------------")
    print("11. OBJETIVOS E EXPECTATIVAS ATUAIS")
    print("--------------------------------------------")
    question65 = obrigatory_question("Quais são as principais expectativas da família para o tratamento?\nCurto Prazo:\n")
    question65_1 = obrigatory_question("Médio Prazo:\n")
    question65_2 = obrigatory_question("Longo Prazo:\n")
    question66 = obrigatory_question("Objetivos que consideram mais importantes:")

    anamnese["Objetivos_e_Expectativas"] = {
        "expec_curto_prazo" : question65,
        "expec_medio_prazo" : question65_1,
        "expec_longo_prazo" : question65_2,
        "objetivos" : question66
    }
                                     
    obs(anamnese)


def obs(anamnese):
    print("--------------------------------------------")
    print("12. OBSERVACOES DO PROFISSIONAL")
    print("--------------------------------------------")
    question67 = obrigatory_question("Atitude ao chegar/Impressões iniciais:\n")
    question68 = obrigatory_question("Interesse/atenção na atividade proposta:\n")
    question69 = obrigatory_question("Linguagem/expressividade durante a anamnese:\n")
    question70 = obrigatory_question("Comportamentos observados relevantes:\n")

    anamnese["Observacoes"] = {
        "imp_inicias" : question67,
        "int_proposta" : question68,
        "expr_dur_anamnese" : question69,
        "comportamentos" : question70
    }

    sug_enc(anamnese)

def sug_enc(anamnese):
    print("--------------------------------------------")
    print("SUGESTAO DE ENCAMINHAMENTO INICIAL")
    print("--------------------------------------------")
    psicologia = question_sn("Encaminhar para Psicologia: (S/N)\n")
    if psicologia in ["S", "SIM"]:
        psicoterapia = question_sn("Psicoterapia? (S/N)\n")
        aba = question_sn("ABA (Análise do Comportamento)? (S/N)\n")
    fono = question_sn("Encaminhar para Fonoaudilogia?: (S/N)\n")
    t_o = question_sn("Encaminhar para Terapia Ocupacional: (S/N)\n")
    psipeda = question_sn("Encaminhar para Psicopedagogia: (S/N)\n")
    nutri = question_sn("Encaminhar para Nutricionista: (S/N)\n")
    music = question_sn("Encaminhar para Musicoterapia: (S/N)\n")
    psimot = question_sn("Encaminhar para Psicomotricidade: (S/N)\n")


    anamnese["encaminhamento"] = {
        "psicologia" : {
            "encaminhar" : psicologia,
            "psicoterapia" : psicoterapia,
            "aba": aba
        },
        "fonoaudilogia" : fono,
        "terapia_ocupacional" : t_o,
        "psicopedagogia" : psipeda,
        "nutricionista" : nutri,
        "musicoterapia" : music,
        "psicomotricidade" : psimot
    }

    finish(anamnese)

def finish(anamnese):
    print("\n---------- FINALIZAÇÃO ----------\n")
    data = datetime.now().strftime("%d/%m/%Y")

    print(f"Data Automática: {data}")

    profissional = obrigatory_question("Profissional Responsável pela Anamnese:\n")
    crp = int_question("CRP / Registro:\n")

    anamnese["finalizacao"] = {
        "data_preenchimento" : data,
        "profissional_resp" : profissional,
        "crp_registro" : crp
    }

    save_tksgod(anamnese)

def save_tksgod(anamnese): 
    nome = anamnese ["identificacao"]["nome"]
    nome_arquivo = nome.replace(" ", "_").lower()

    with open(f"{nome_arquivo}.json", "w", encoding = "utf-8") as arquivo:
        json.dump(anamnese, arquivo, indent = 4, ensure_ascii = False)

        print(f"Salvo como: {nome_arquivo}.json")


#DESCOBRI O FOGO E MINHA VIDA ESTA 10000X MAIS FACIL COM ESSAs FUNC
def question_sn(texto):
    while True:
        resp = input(texto).strip().upper()
        if resp in ["S", "SIM"]:
            return True
        elif resp in ["N", "NAO", "NÃO"]:
            return False
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
    