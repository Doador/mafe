import streamlit as st
import pandas as pd
from PIL import Image
from datetime import datetime


# Função para adicionar imagem de fundo na página Home
def add_bg_image(image_path):
    try:
        img = Image.open(image_path)
        st.image(img, use_column_width=True)
    except FileNotFoundError:
        st.warning(f"Imagem não encontrada em {image_path}. Verifique o caminho.")

# Função para salvar os dados em um CSV
def salvar_doador(nome, idade, sexo, tipo_sanguineo):
    arquivo = "doadores.csv"
    try:
        df = pd.read_csv(arquivo)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Nome", "Idade", "Sexo", "Tipo Sanguíneo"])
    novo_doador = pd.DataFrame([[nome, idade, sexo, tipo_sanguineo]], columns=["Nome", "Idade", "Sexo", "Tipo Sanguíneo"])
    df = pd.concat([df, novo_doador], ignore_index=True)
    df.to_csv(arquivo, index=False)

# Função para salvar o agendamento em CSV
def salvar_agendamento(nome, idade, sexo, tipo_sanguineo, local, data_hora, hora, notas):
    df_agendamento = pd.DataFrame({
        "Nome": [nome],
        "Idade": [idade],
        "Sexo": [sexo],
        "Tipo Sanguíneo": [tipo_sanguineo],
        "Local": [local],
        "Data": [data_hora],
        "Hora": [hora],
        "Notas": [notas if notas else "Nenhuma"]
    })
    df_agendamento.to_csv('C:/mafe/python/doadores.csv', index=False, mode='a', header=False)

# Interface Streamlit
st.title("Sistema de Doação de Sangue")

# Botões para navegação entre as páginas
st.sidebar.title("Navegação")
pagina = st.sidebar.radio("Ir para:", 
                          ("Home","Importância", "Requisitos para Doação", "Etapas para Doação", "Testemunhos", 
                           "Elegibilidade de Doação", "Agendamento","Cadastro para Voluntários", "Vídeo", "Fim"))

# Lógica para exibir a página selecionada
if pagina == "Home":
    st.subheader("Bem-vindo ao Sistema de Doação de Sangue")
    st.write("""Dia 14 de Junho, comemora-se o Dia Mundial do Doador de Sangue. A data foi instituída pela 
    Organização Mundial da Saúde (OMS) para lembrar da importância da conscientização quanto à 
    necessidade da doação de sangue e como uma forma de agradecimento aos doadores.""")
    
    st.subheader("Bem-vindo ao Sistema de Doação de Órgãos")
    st.write("""Dia 14 de Junho, comemora-se o Dia Mundial do Doador de Sangue. A data foi instituída pela 
    Organização Mundial da Saúde (OMS) para lembrar da importância da conscientização quanto à 
    necessidade da doação de sangue e como uma forma de agradecimento aos doadores.""")

    st.subheader("Bem-vindo ao Sistema de Doação de Medula Óssea")
    st.write("""O Dia Mundial da Doação de Medula Óssea é celebrado no terceiro sábado de setembro. Essa data, estabelecida pela World Marrow Donor Association (WMDA), tem como objetivo aumentar a conscientização sobre a doação de medula óssea e promover o registro de novos doadores. O dia também destaca a importância de contar com uma base diversificada de doadores cadastrados, já que a compatibilidade entre doadores e receptores é complexa e depende de fatores genéticos.
No Brasil, o Instituto Nacional do Câncer (INCA) e os hemocentros estaduais realizam campanhas regulares para incentivar o cadastro de novos doadores no Registro Nacional de Doadores Voluntários de Medula Óssea (REDOME). A doação de medula óssea pode ser decisiva para pacientes com doenças graves, como leucemias, linfomas e outras doenças hematológicas.""")
    add_bg_image("doe.png")

elif pagina == "Importância":
    st.title("A Importância da Doação de Sangue, Medula Óssea e Órgãos")
    
    # Explicação sobre a importância da doação de sangue
    st.subheader("A Importância da Doação de Sangue")
    st.write("""
    A doação de sangue é um ato de solidariedade e amor ao próximo que ajuda a salvar inúmeras vidas diariamente. O sangue doado é essencial para 
    tratamentos médicos, como em cirurgias, acidentes e no suporte a pacientes com doenças graves, como câncer e anemias. 
    Cada doação pode beneficiar até três pessoas, pois o sangue é separado em componentes (plasma, plaquetas e glóbulos vermelhos), 
    utilizados para necessidades distintas.
    """)

    # Explicação sobre a importância da doação de medula óssea
    st.subheader("A Importância da Doação de Medula Óssea")
    st.write("""
    A doação de medula óssea é vital para pacientes com doenças hematológicas graves, como leucemia, linfoma e anemia aplástica. 
    A medula óssea, responsável pela produção de células sanguíneas, precisa ser substituída por uma saudável em casos de danos graves. 
    O procedimento de doação é seguro e pode salvar vidas, especialmente em crianças e jovens. 
    Registre-se em bancos de medula, como o REDOME e HEMOBRAZ, e faça a diferença.
    """)

    # Explicação sobre a importância da doação de órgãos
    st.subheader("A Importância da Doação de Órgãos")
    st.write("""
    A doação de órgãos é uma forma de garantir que pessoas com falência de órgãos tenham uma segunda chance de vida. 
    Um único doador pode salvar várias vidas, doando órgãos como coração, rins, fígado e pulmões, além de tecidos como córnea e pele. 
    A decisão de ser um doador deve ser informada à família, pois o consentimento é fundamental para que a doação seja realizada.
    """)


if pagina == "Elegibilidade de Doação":
    st.title("Verificação de Elegibilidade para Doação de Sangue, Medula Óssea e Órgãos")

    # Criando colunas para os formulários
    col1, col2, col3 = st.columns(3)

    # Formulário de Elegibilidade para Doação de Sangue na coluna 1
    with col1:
        st.subheader("Verificação de Condições de Saúde para Doação de Sangue")
        with st.form(key="form_elegibilidade"):
            hiv = st.radio("Já teve HIV?", ("Sim", "Não"))
            hepatite = st.radio("Já teve Hepatite?", ("Sim", "Não"))
            malaria = st.radio("Já teve Malária?", ("Sim", "Não"))
            doencas_cronicas = st.radio("Possui alguma doença crônica?", ("Sim", "Não"))

            if doencas_cronicas == "Sim":
                dc = st.multiselect('Quais doenças crônicas?', 
                                    options=['Diabetes', 'Hipertensão', 'Asma', 'AVC', 'Obesidade', 'Depressão'])
                if dc:
                    st.write(f"Você selecionou: {', '.join(dc)}")

            if hepatite == "Sim":
                hp = st.multiselect('Qual tipo de Hepatite?', options=['A', 'B', 'C'])
                if hp:
                    st.write(f"Você teve Hepatite do tipo: {', '.join(hp)}")

            dst = st.multiselect('Você já teve alguma das seguintes Doenças Sexualmente Transmissíveis (DSTs)?',
                                 options=['Sífilis', 'Gonorreia', 'Herpes', 'HPV', 'Outras'])
            if dst:
                st.write(f"Você teve: {', '.join(dst)}")

            tuberculose = st.radio("Já teve Tuberculose?", ("Sim", "Não"))
            drogas = st.radio("Faz ou já fez uso de Drogas?", ("Sim", "Não"))
            if drogas == "Sim":
                dg = st.multiselect('Quais drogas?', options=['Maconha', 'Cocaína', 'Crack'])
                if dg:
                    st.write(f"Você fez uso de: {', '.join(dg)}")

            fumar = st.radio("Fuma?", ("Sim", "Não"))
            bebidas = st.radio("Faz uso de bebidas alcoólicas?", ("Sim", "Não"))

            verificar_button = st.form_submit_button(label="Verificar Elegibilidade")

            # Exibir o resultado da elegibilidade
            if verificar_button:
                if hiv == "Sim" or hepatite == "Sim" or malaria == "Sim" or doencas_cronicas == "Sim":
                    st.error("Infelizmente, você não pode doar sangue devido a uma condição médica.")
                else:
                    st.success("Você está apto(a) para doar sangue!")

    # Formulário de Avaliação para Doação de Medula Óssea na coluna 2
    with col2:
        st.subheader("Avaliação de Elegibilidade para Doação de Medula Óssea")
        with st.form(key="form_medula"):
            nome_medula = st.text_input("Nome Completo:")
            idade_medula = st.number_input("Idade:", min_value=18, max_value=55)
            sexo_medula = st.selectbox("Sexo:", ["Masculino", "Feminino", "Outro"])
            
            condicoes = st.multiselect("Você tem alguma das seguintes condições de saúde?",
                                        options=[
                                            "Doenças autoimunes (ex: lupus, artrite reumatoide)",
                                            "Câncer",
                                            "Infecções crônicas (ex: HIV, hepatite)",
                                            "Doenças do sangue (ex: anemia, leucemia)",
                                            "Doenças cardíacas",
                                            "Diabetes",
                                            "Outras (especifique)"
                                        ])
            
            tratamento = st.radio("Você está atualmente sob tratamento médico?", ("Sim", "Não"))
            transfusao = st.radio("Você já realizou uma transfusão de sangue?", ("Sim", "Não"))
            alergia = st.radio("Você é alérgico a algum medicamento ou substância?", ("Sim", "Não"))
            
            fumo = st.radio("Você fuma?", ("Sim", "Não"))
            alcool = st.radio("Você consome bebidas alcoólicas?", ("Sim", "Não"))
            drogas_recreativas = st.radio("Você faz uso de drogas recreativas?", ("Sim", "Não"))
            
            consentimento = st.radio("Você está disposto a realizar exames de compatibilidade?", ("Sim", "Não"))
            ciente = st.radio("Você está ciente de que poderá ser chamado para realizar a doação a qualquer momento, se compatível?", ("Sim", "Não"))
            
            submit_medula = st.form_submit_button("Verificar Elegibilidade para Doação de Medula Óssea")
            
            # Verificação de elegibilidade para doação de medula
            if submit_medula:
                if idade_medula < 18 or idade_medula > 55:
                    st.error("Você deve ter entre 18 e 55 anos para doar medula óssea.")
                elif "Câncer" in condicoes or "Doenças autoimunes (ex: lupus, artrite reumatoide)" in condicoes:
                    st.error("Infelizmente, você não pode doar medula óssea devido a uma condição médica.")
                else:
                    st.success("Você está apto(a) para doar medula óssea!")

    # Formulário de Avaliação para Doação de Órgãos na coluna 3
    with col3:
        st.subheader("Verificação de Elegibilidade para Doação de Órgãos")
        with st.form(key="form_orgaos"):
            nome_orgaos = st.text_input("Nome Completo:")
            idade_orgaos = st.number_input("Idade:", min_value=18)
            sexo_orgaos = st.selectbox("Sexo:", ["Masculino", "Feminino", "Outro"])
            
            doencas_orgaos = st.multiselect("Você possui alguma das seguintes condições?", 
                                            options=["Câncer", "Doença Cardíaca", "Diabetes", 
                                                     "Doenças infecciosas (ex: HIV, Hepatite)", "Outras"])
            
            historico_cirurgico = st.radio("Você já passou por alguma cirurgia importante?", ("Sim", "Não"))
            habito_fumo = st.radio("Você fuma?", ("Sim", "Não"))
            uso_alcool = st.radio("Você consome álcool regularmente?", ("Sim", "Não"))
            
            consentimento_orgaos = st.radio("Você expressou sua vontade de ser doador para seus familiares?", ("Sim", "Não"))
            
            submit_orgaos = st.form_submit_button("Verificar Elegibilidade para Doação de Órgãos")

            # Verificação de elegibilidade para doação de órgãos
            if submit_orgaos:
                if idade_orgaos < 18:
                    st.error("Você deve ter pelo menos 18 anos para doar órgãos.")
                elif "Câncer" in doencas_orgaos or "Doenças infecciosas (ex: HIV, Hepatite)" in doencas_orgaos:
                    st.error("Infelizmente, você não está apto(a) para doar órgãos devido a uma condição médica.")
                else:
                    st.success("Você está apto(a) para doar órgãos!")

elif pagina == "Agendamento":
    st.title("Agendamento de Doação de Sangue")
    
    # Cadastro do Doador
    st.subheader("Cadastro do Doador")

    with st.form(key="cadastro_form"):
        nome = st.text_input("Nome")
        idade = st.number_input("Idade", min_value=1, max_value=120)
        sexo = st.selectbox("Sexo", ["Masculino", "Feminino", "Outro"])
        tipo_sanguineo = st.selectbox("Tipo Sanguíneo", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
        submit_cadastro = st.form_submit_button(label="Cadastrar")

    # Validação dos dados de cadastro
    if submit_cadastro:
        if not nome or idade < 1 or idade > 120 or sexo not in ["Masculino", "Feminino", "Outro"] or tipo_sanguineo not in ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]:
            st.error("Por favor, preencha todos os campos corretamente.")
        else:
            # Armazenar dados do doador no estado da sessão
            st.session_state.nome = nome
            st.session_state.idade = idade
            st.session_state.sexo = sexo
            st.session_state.tipo_sanguineo = tipo_sanguineo
            st.success("Doador cadastrado com sucesso!")

    # Agendamento da Doação
    if 'nome' in st.session_state:
        st.subheader("Agendar Doação")
        with st.form(key="agendamento_form"):
            local = st.selectbox("Local de Doação", ["Hemocentro A", "Hemocentro B", "Hemocentro C"])
            data_hora = st.date_input("Data")
            hora = st.time_input("Hora")
            notas = st.text_area("Notas (opcional)")
            submit_agendamento = st.form_submit_button(label="Agendar Doação")

        if submit_agendamento:
            salvar_agendamento(st.session_state.nome, st.session_state.idade, st.session_state.sexo, 
                               st.session_state.tipo_sanguineo, local, data_hora, hora, notas)
            st.success("Agendamento realizado com sucesso!")

elif pagina == "Requisitos para Doação":
    st.title("Requisitos para Doação de Sangue, Medula Óssea e Órgãos")
    
    st.subheader("Requisitos para Doação de Sangue")
    st.write(""" 
    - Apresentar boa condição de saúde.
    - Ter entre 16 e 69 anos.
    - Pesar no mínimo 51 quilos.
    - Estar descansado (dormido pelo menos seis horas nas 24 horas anteriores).
    - Estar alimentado (evitar alimentação gordurosa nas 4 horas anteriores).
    - Apresentar documento original com foto recente.
    """)
    st.write(""" 
    Fatores que podem impedir a doação:
    - Doenças crônicas, HIV, Hepatite, Malária.
    - Uso de drogas ilícitas.
    - Gravidez ou amamentação.
    - Recentes procedimentos cirúrgicos ou transfusões de sangue.
    """)

    st.subheader("Requisitos para Doação de Medula Óssea")
    st.write("""
    - Ter entre 18 e 55 anos.
    - Estar em boas condições de saúde.
    - Não ter doenças autoimunes, HIV, Hepatite ou outras doenças graves.
    - Não ter histórico de câncer.
    - Estar disposto a se cadastrar e realizar os exames necessários.
    """)

    st.subheader("Requisitos para Doação de Órgãos")
    st.write("""
    - Ser maior de idade (no Brasil, é necessário ter 18 anos).
    - Não ter doenças que impeçam a doação (ex: câncer, doenças infecciosas).
    - Informar a família sobre a decisão de ser doador.
    - Assinar o documento de doação ou ser registrado em um sistema de doação de órgãos.
    """)

elif pagina == "Etapas para Doação":
    st.title("Etapas para Doação de Sangue, Medula Óssea e Órgãos")

    st.subheader("Etapas para Doação de Sangue")
    st.write("""
    1. *Registro*: O doador deve se registrar na unidade de coleta de sangue.
    2. *Triagem*: Avaliação de saúde e verificação dos requisitos.
    3. *Coleta*: O sangue é coletado de forma segura.
    4. *Pós-Coleta*: O doador recebe orientações sobre cuidados após a doação e um lanche.
    """)

    st.subheader("Etapas para Doação de Medula Óssea")
    st.write("""
    1. *Cadastro*: O interessado deve se cadastrar em um banco de sangue de medula óssea.
    2. *Coleta de Amostra*: O doador fornece uma amostra de sangue para tipagem HLA.
    3. *Triagem*: Avaliação médica e exames de saúde.
    4. *Procedimento de Coleta*: A medula é coletada por aferese ou punção.
    5. *Acompanhamento*: Monitoramento da saúde do doador após a doação.
    """)

    st.subheader("Etapas para Doação de Órgãos")
    st.write("""
    1. *Cadastro*: O interessado deve se cadastrar e informar a família.
    2. *Consentimento*: Garantir que a família concorda com a doação.
    3. *Avaliação Médica*: Análise da possibilidade de doação em caso de morte cerebral.
    4. *Coleta*: Os órgãos são removidos em ambiente cirúrgico.
    5. *Acompanhamento*: Monitoramento dos receptores dos órgãos.
    """)

elif pagina == "Etapas para Doação":
    st.title("Etapas para Doação de Sangue")
    st.write("""
    As etapas para realizar a doação de sangue são:
    1. *Cadastro:* Preenchimento de um formulário com dados pessoais e de saúde.
    2. *Triagem:* Avaliação médica para verificar se o doador está apto.
    3. *Coleta:* Realização da coleta de sangue, que leva cerca de 15 minutos.
    4. *Pós-doação:* Descanso e ingestão de líquidos para recuperação.
    """)

elif pagina == "Testemunhos":
    print('Testemunhos')
    st.title("Testemunhos de Doador e Receptor")
    
    testemunhos = [
        {"Nome": "João", "Testemunho": "Doar sangue é uma maneira incrível de ajudar os outros."},
        {"Nome": "Maria", "Testemunho": "Eu doei sangue pela primeira vez e foi uma experiência muito gratificante."},
        {"Nome": "Carlos", "Testemunho": "Saber que meu sangue pode salvar vidas me motiva a doar regularmente."},
        {"Nome": "Luara", "Testemunho": "Doar sangue é uma maneira maravilhosa para salvar vidas."},
        {"Nome": "Ana", "Testemunho": "A doação de sangue é um ato de amor e solidariedade."},
        {"Nome": "Pedro", "Testemunho": "Cada gota conta, e sua doação pode fazer toda a diferença."},
        {"Nome": "Fernanda", "Testemunho": "Fazer o bem é sempre gratificante, e a doação de sangue é um ótimo jeito."},
        {"Nome": "Ricardo", "Testemunho": "Eu sempre me sinto bem após doar sangue, sabendo que ajudo alguém."},
        {"Nome": "Juliana", "Testemunho": "A doação é simples e rápida, mas o impacto é enorme."},
        {"Nome": "Lucas", "Testemunho": "Se você pode ajudar, não hesite! Doe sangue e salve vidas."}
    ]
    
    for t in testemunhos:
        st.subheader(t["Nome"])
        st.write(t["Testemunho"])

def salvar_voluntario(nome, idade, sexo, contato, interesse):
    arquivo = "voluntarios.csv"
    try:
        df = pd.read_csv(arquivo)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Nome", "Idade", "Sexo", "Contato", "Interesse"])
    
    novo_voluntario = pd.DataFrame([[nome, idade, sexo, contato, interesse]], columns=["Nome", "Idade", "Sexo", "Contato", "Interesse"])
    df = pd.concat([df, novo_voluntario], ignore_index=True)
    df.to_csv(arquivo, index=False)

def salvar_voluntario(nome, idade, sexo, contato, interesse):
    arquivo = "voluntarios.csv"
    try:
        df = pd.read_csv(arquivo)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Nome", "Idade", "Sexo", "Contato", "Interesse"])
    
    novo_voluntario = pd.DataFrame([[nome, idade, sexo, contato,interesse]], columns=["Nome", "Idade", "Sexo", "Contato", "Interesse"])
    df = pd.concat([df, novo_voluntario], ignore_index=True)
    df.to_csv(arquivo, index=False)

if pagina == "Cadastro para Voluntários":
    st.title("Cadastro para Voluntários")
    
    # Cadastro do Doador
    st.subheader("Cadastro de Voluntários")


    # Formulário de Cadastro
    with st.form(key="cadastro_voluntario"):
        nome = st.text_input("Nome Completo")
        idade = st.number_input("Idade", min_value=1, max_value=120)
        sexo = st.selectbox("Sexo", ["Masculino", "Feminino", "Outro"])
        contato = st.text_input("Contato (Telefone ou Email)")
        interesse = st.selectbox("Interesse", ["Divulgação", "Organização de Eventos", "Apoio Emocional", " Atividades Administrativas"])


        submit_cadastro = st.form_submit_button(label="Cadastrar")

    # Validação e salvamento dos dados de cadastro
    if submit_cadastro:
        if not nome or idade < 1 or sexo not in ["Masculino", "Feminino", "Outro"] or not contato:
            st.error("Por favor, preencha todos os campos corretamente.")
        else:
            salvar_voluntario(nome, idade, sexo, contato, interesse)
            st.success("Voluntário cadastrado com sucesso!")

elif pagina == "Vídeo":
    st.title("Vídeo Explicativo sobre a Doação de Sangue")
    st.write("Aqui pode ser exibido um vídeo sobre o processo de doação.")
    st.video("Vídeo.mp4")
    
elif pagina == "Fim":
    add_bg_image("imagemfim.png")
