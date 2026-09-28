"""
Corpus sintetico de 40 manifestacoes de ouvidoria municipal, usado em todas as
entregas do desafio. Contem as manifestacoes explicitamente citadas no enunciado
(M003, M008, M017, M022, M031) com o texto exato fornecido, mais 35 manifestacoes
adicionais construidas para completar o corpus, respeitando as observacoes do
enunciado: ~15% de duplicatas semanticas (mesmo problema, palavras diferentes) e
5 manifestacoes longas (>500 caracteres) para o exercicio de chunking.
"""

CATEGORIAS = ["infraestrutura", "saude", "seguranca", "educacao", "meio ambiente"]

MANIFESTACOES = [
    # --- Pares de duplicatas semanticas citados no enunciado (Entrega 1) ---
    {"id": "M003", "categoria": "infraestrutura",
     "texto": "Buraco enorme na Av. Brasil, quase na altura do numero 1200, esta causando "
              "acidentes com motociclistas todos os dias e precisa de reparo urgente."},
    {"id": "M017", "categoria": "infraestrutura",
     "texto": "Asfalto todo esburacado da avenida principal do bairro, motoristas precisam "
              "desviar constantemente e o transito fica mais lento por causa disso."},

    {"id": "M008", "categoria": "saude",
     "texto": "O posto de saude do bairro Jardim das Flores esta sem medico ha mais de tres "
              "semanas, e os moradores nao tem para onde ir em caso de emergencia leve."},
    {"id": "M022", "categoria": "saude",
     "texto": "Falta atendimento no PSF da regiao norte, os pacientes chegam cedo e sao "
              "informados que nao ha profissional disponivel para consulta no dia."},

    {"id": "M031", "categoria": "infraestrutura",
     "texto": "Lampada queimada na praca central ha duas semanas, deixando o local escuro "
              "e inseguro para quem passa por ali durante a noite."},

    # --- Terceiro par de duplicatas semanticas (completa os ~15% do corpus) ---
    {"id": "M012", "categoria": "meio ambiente",
     "texto": "Lixo acumulado ha dias na esquina da rua das Palmeiras, atraindo ratos e "
              "insetos, e o mau cheiro ja incomoda os moradores da vizinhanca."},
    {"id": "M029", "categoria": "meio ambiente",
     "texto": "Entulho e residuos jogados na calcada da rua das Palmeiras nao sao recolhidos "
              "pela coleta ha muito tempo, gerando cheiro forte e proliferacao de pragas."},

    # --- Demais manifestacoes (35 restantes, sem duplicata direta) ---
    {"id": "M001", "categoria": "seguranca",
     "texto": "Falta de iluminacao na travessia de pedestres da Rua das Acacias tem causado "
              "medo entre os moradores que precisam atravessar a noite para chegar em casa."},
    {"id": "M002", "categoria": "educacao",
     "texto": "A escola municipal Monteiro Lobato esta sem professor de matematica desde o "
              "inicio do semestre, prejudicando o aprendizado dos alunos do 8 ano."},
    {"id": "M004", "categoria": "saude",
     "texto": "Demora de mais de quatro horas no atendimento da UPA central, mesmo em casos "
              "classificados como urgentes pela triagem realizada na entrada."},
    {"id": "M005", "categoria": "meio ambiente",
     "texto": "Descarte irregular de oleo de cozinha na rede de esgoto da Rua Sao Jose esta "
              "causando entupimentos frequentes e mau cheiro na regiao."},
    {"id": "M006", "categoria": "infraestrutura",
     "texto": "Semaforo quebrado no cruzamento da Avenida Central com a Rua dos Ipes ha mais "
              "de uma semana, gerando confusao no transito nos horarios de pico."},
    {"id": "M007", "categoria": "seguranca",
     "texto": "Aumento de assaltos a pedestres no entorno da estacao de onibus do centro "
              "durante o periodo noturno, moradores pedem reforco no policiamento."},
    {"id": "M009", "categoria": "educacao",
     "texto": "Creche municipal do bairro Esperanca esta com lista de espera de mais de "
              "cento e cinquenta criancas e nenhuma previsao de nova turma para o ano."},
    {"id": "M010", "categoria": "meio ambiente",
     "texto": "Poda inadequada de arvores na Praca da Matriz deixou galhos soltos que "
              "podem cair sobre pedestres em dias de vento forte."},
    {"id": "M011", "categoria": "infraestrutura",
     "texto": "Vazamento de agua constante na tubulacao da Rua Bela Vista esta desperdicando "
              "muita agua e formando poças que atrapalham a passagem de pedestres."},
    {"id": "M013", "categoria": "saude",
     "texto": "Falta de medicamentos basicos como dipirona e paracetamol na farmacia "
              "popular do bairro Centro ha mais de dez dias, segundo relato de usuarios."},
    {"id": "M014", "categoria": "seguranca",
     "texto": "Grupo de motos com escapamento aberto circula em alta velocidade durante a "
              "madrugada na Avenida Litoranea, perturbando o sossego dos moradores."},
    {"id": "M015", "categoria": "educacao",
     "texto": "Telhado da escola estadual Dom Pedro apresenta infiltracoes que molham as "
              "salas de aula sempre que chove, prejudicando materiais e equipamentos."},
    {"id": "M016", "categoria": "meio ambiente",
     "texto": "Queimada irregular em terreno baldio proximo ao bairro Vila Nova esta "
              "gerando muita fumaca e preocupando moradores com problemas respiratorios."},
    {"id": "M018", "categoria": "infraestrutura",
     "texto": "Calcada quebrada em frente ao numero 45 da Rua dos Girassois impede a "
              "passagem segura de cadeirantes e pessoas com carrinho de bebe."},
    {"id": "M019", "categoria": "saude",
     "texto": "Ambulancia do bairro Sao Francisco esta parada ha semanas aguardando peca "
              "de reposicao, deixando a regiao sem cobertura de remocao de urgencia."},
    {"id": "M020", "categoria": "seguranca",
     "texto": "Camera de monitoramento da praca principal esta quebrada ha meses, e "
              "moradores relatam aumento de pequenos furtos na regiao desde entao."},
    {"id": "M021", "categoria": "educacao",
     "texto": "Merenda escolar da escola municipal Cecilia Meireles vem chegando atrasada "
              "e em quantidade insuficiente para todos os alunos matriculados no turno."},
    {"id": "M023", "categoria": "meio ambiente",
     "texto": "Rio que corta o bairro Industrial esta com espuma e cheiro forte de produto "
              "quimico, moradores suspeitam de despejo irregular por fabrica da regiao."},
    {"id": "M024", "categoria": "infraestrutura",
     "texto": "Bueiro aberto na esquina da Rua Tiradentes com a Avenida Getulio Vargas "
              "representa risco grave de acidente para pedestres e ciclistas que passam ali."},
    {"id": "M025", "categoria": "saude",
     "texto": "Fila para agendamento de consulta com cardiologista no hospital municipal "
              "esta com mais de seis meses de espera, segundo relato de varios pacientes."},
    {"id": "M026", "categoria": "seguranca",
     "texto": "Portao da escola municipal Rui Barbosa fica aberto durante o recreio, "
              "preocupando pais com a seguranca das criancas em relacao a rua movimentada."},
    {"id": "M027", "categoria": "educacao",
     "texto": "Biblioteca da escola municipal Machado de Assis esta fechada ha meses por "
              "falta de funcionario responsavel, deixando o acervo sem uso pelos alunos."},
    {"id": "M028", "categoria": "meio ambiente",
     "texto": "Poluicao sonora de bar irregular que funciona ate de madrugada no bairro "
              "residencial Jardim Europa impede moradores vizinhos de dormir direito."},
    {"id": "M030", "categoria": "infraestrutura",
     "texto": "Ponte pedonal sobre o cordao da Avenida das Nacoes apresenta ferrugem "
              "visivel na estrutura metalica e balanca quando varias pessoas atravessam."},
    {"id": "M032", "categoria": "saude",
     "texto": "Sala de vacinacao da unidade basica de saude do bairro Alto da Serra fecha "
              "as vezes antes do horario anunciado, obrigando moradores a voltar noutro dia."},
    {"id": "M033", "categoria": "seguranca",
     "texto": "Terreno baldio abandonado na Rua das Oliveiras virou ponto de uso de drogas "
              "durante a noite, segundo relato de moradores que pedem fiscalizacao."},
    {"id": "M034", "categoria": "educacao",
     "texto": "Quadra poliesportiva da escola municipal Villa Lobos esta interditada por "
              "falta de manutencao no piso, cancelando as aulas de educacao fisica."},
    {"id": "M035", "categoria": "meio ambiente",
     "texto": "Assoreamento do cordao proximo ao Parque das Aguas esta causando alagamentos "
              "recorrentes nas ruas vizinhas mesmo em chuvas de intensidade moderada."},
    # --- 5 manifestacoes longas (>500 caracteres), para a Entrega 3 (chunking) ---
    {"id": "M041", "categoria": "infraestrutura",
     "texto": (
         "Moro na Rua das Camelias ha mais de dez anos e nunca vi a situacao da drenagem "
         "pluvial tao critica como agora. Toda vez que chove um pouco mais forte, a agua "
         "invade o quintal de varias casas e chega a entrar dentro das residencias mais "
         "baixas do quarteirao. Ja perdemos moveis, eletrodomesticos e ate parte do piso "
         "de uma vizinha por causa da umidade constante. Procuramos a subprefeitura tres "
         "vezes nos ultimos dois anos e sempre recebemos a mesma resposta, que o projeto "
         "de reforma do sistema de drenagem esta em analise. Enquanto isso, a rua continua "
         "sem manutencao nos bueiros, que ficam entupidos de folhas e lixo, e o asfalto "
         "esta cedendo em varios pontos por causa da erosao causada pela agua acumulada. "
         "Pedimos com urgencia uma vistoria tecnica no local e um cronograma claro de obras, "
         "porque a situacao so piora a cada temporada de chuvas e o risco de um acidente "
         "mais grave, como desabamento parcial da via, aumenta a cada ano que passa sem "
         "solucao definitiva para o problema."
     )},
    {"id": "M042", "categoria": "saude",
     "texto": (
         "Preciso relatar uma situacao muito grave que aconteceu com meu pai na UPA do "
         "bairro Centro na semana passada. Ele deu entrada com fortes dores no peito por "
         "volta das dez da noite e foi classificado na triagem como caso de risco "
         "intermediario. Mesmo assim, ficou aguardando por quase cinco horas em uma "
         "cadeira no corredor, sem qualquer reavaliacao durante esse periodo, ate que um "
         "outro paciente que aguardava ao lado percebeu que ele estava suando frio e "
         "avisou a equipe de enfermagem. Somente ai ele foi levado as pressas para uma "
         "sala de atendimento. Felizmente ele esta bem agora, mas a demora quase custou "
         "a vida dele. Conversando com outros pacientes na sala de espera, descobri que "
         "essa nao e uma situacao isolada, varias pessoas reclamaram do mesmo problema de "
         "reavaliacao de triagem que nao acontece com a frequencia necessaria. Gostaria "
         "de saber quais medidas estao sendo tomadas para reforcar a equipe noturna e "
         "garantir que casos de dor no peito recebam prioridade real, nao apenas no papel."
     )},
    {"id": "M043", "categoria": "seguranca",
     "texto": (
         "Sou moradora do bairro Vila Operaria ha mais de quinze anos e nunca me senti tao "
         "insegura para sair de casa a noite quanto nos ultimos meses. A rua onde moro, a "
         "Rua Coronel Fernandes, praticamente nao tem iluminacao publica funcionando, sao "
         "cerca de oito postes apagados em um trecho de apenas tres quarteiroes. Isso "
         "criou um ambiente perfeito para assaltos, que ja aconteceram pelo menos quatro "
         "vezes que eu saiba nos ultimos dois meses, sempre no mesmo trecho escuro perto "
         "da padaria. Ja registramos boletim de ocorrencia em duas dessas situacoes, mas "
         "nao vimos nenhuma acao concreta da prefeitura para resolver a questao da "
         "iluminacao, que na minha opiniao e a causa raiz do problema de seguranca. Alem "
         "disso, o ponto de onibus da esquina tambem fica as escuras, o que deixa "
         "trabalhadores do turno da noite extremamente vulneraveis enquanto esperam a "
         "conducao para casa. Pedimos com urgencia o reparo dos postes de luz e, se "
         "possivel, uma rota de ronda policial noturna passando pela regiao ate que a "
         "iluminacao seja normalizada por completo."
     )},
    {"id": "M044", "categoria": "educacao",
     "texto": (
         "Sou pai de um aluno do quinto ano da escola municipal Presidente Vargas e "
         "gostaria de relatar uma situacao que vem se arrastando desde o inicio do ano "
         "letivo. A escola nao possui professor efetivo de educacao fisica, e as aulas "
         "dessa disciplina simplesmente nao acontecem ha mais de tres meses. As criancas "
         "ficam na sala de aula fazendo atividade extra ou, em alguns casos, ficam apenas "
         "no patio sem qualquer orientacao pedagogica durante o horario que seria da "
         "materia. Isso preocupa bastante os pais, porque sabemos da importancia da "
         "atividade fisica regular para o desenvolvimento motor e social das criancas "
         "nessa idade, alem do impacto na saude como um todo. Ja conversamos com a "
         "direcao da escola em duas reunioes de pais e mestres, e a resposta sempre e a "
         "mesma, que a secretaria de educacao ainda nao enviou um substituto para a vaga "
         "aberta desde o ano passado. Gostariamos de entender quais sao os proximos "
         "passos para resolver essa lacuna, ja que estamos proximos do encerramento do "
         "semestre e as criancas praticamente nao tiveram nenhuma aula de educacao fisica "
         "em todo esse periodo."
     )},
    {"id": "M045", "categoria": "meio ambiente",
     "texto": (
         "Escrevo em nome de um grupo de moradores do bairro proximo ao Parque das "
         "Garcas para relatar o descarte irregular e recorrente de residuos industriais "
         "em uma area de preservacao ambiental que fica a poucos metros das primeiras "
         "casas do bairro. Ha cerca de dois meses, comecamos a notar caminhoes "
         "descarregando material que parece entulho de construcao misturado com o que "
         "acreditamos ser residuo quimico, pelo cheiro forte e pela coloracao estranha "
         "que fica no solo depois. Isso ja causou a morte visivel de vegetacao nativa em "
         "uma faixa considera da area e tememos contaminacao do lencol freatico, ja que "
         "varias casas da regiao ainda dependem de pocos artesianos para abastecimento de "
         "agua. Fizemos denuncia ao orgao ambiental municipal ha cerca de um mes, mas ate "
         "agora nao recebemos retorno sobre nenhuma vistoria realizada no local. Temos "
         "fotos e alguns videos dos caminhoes realizando o descarte em horarios sempre "
         "proximos ao amanhecer, o que refor a suspeita de que os responsaveis sabem que "
         "estao cometendo uma irregularidade e escolhem esse horario para dificultar a "
         "fiscalizacao. Pedimos providencias urgentes antes que o dano ambiental se torne "
         "irreversivel para toda a regiao."
     )},
]

assert len(MANIFESTACOES) == 40, f"Corpus deveria ter 40 manifestacoes, tem {len(MANIFESTACOES)}"

DUPLICATAS_REAIS = [("M003", "M017"), ("M008", "M022"), ("M012", "M029")]
IDS_LONGAS_ESPERADAS = ["M041", "M042", "M043", "M044", "M045"]

if __name__ == "__main__":
    tamanhos = [(m["id"], len(m["texto"])) for m in MANIFESTACOES]
    longas = sorted(tamanhos, key=lambda x: -x[1])[:5]
    print(f"Total de manifestacoes: {len(MANIFESTACOES)}")
    print(f"Duplicatas reais conhecidas: {DUPLICATAS_REAIS} ({len(DUPLICATAS_REAIS)*2} manifestacoes, "
          f"{len(DUPLICATAS_REAIS)*2/len(MANIFESTACOES)*100:.0f}% do corpus)")
    print("5 manifestacoes mais longas (deveriam ser M041-M045):")
    for mid, tam in longas:
        print(f"  {mid}: {tam} caracteres")
