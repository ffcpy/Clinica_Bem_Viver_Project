print("2. HISTÓRICO ESCOLAR")
while True:
        question1 = input("Possui Acompanhante Terapêutica?:  ").strip().upper()
        if question1:
                break
        else: 
            print("Digite uma opção válida.")
        if question1 in ["S", "SIM"]:
            while True:
                try:
                    question1_1 = int(input("(1) - Tutora ou (2) - Auxiliar para a criança?"))
                    if question1:
                        break
                except:
                    print("Digite uma opção válida.")
        while True:
            try:
                question1_2 = input("Quanto tempo permanece com a criança?:  ")
                if question1_2:
                    break
            except:
                print("Digite uma opção válida.")
while True:
        try:
            question2 = input("Dificuldades acadêmicas relatadas (leitura, escrita, matemática):  ")
            if question2:
                break
        except:
            print("Digite uma opção válida.")