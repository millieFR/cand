cand = int(input('Digite o número de um candidato:'))
nomes = ['Maria Joaquina', 'Emerson', 'Vampira', 'Flora', 'Jennie', 'Lily Bloom', 'Barbie', 'Lana Del Rey', 'Sabrina', 'Clarice', 'Billie']
parti = ['Carroseul', 'E assim que começa', 'X-men', 'Winx', 'Blackpink', 'E assim que acaba', 'World is pink', 'Black Beauty', 'Carpinteiro', 'Lispector', 'ealish']
vice = ['Cirilo', 'Atlas', 'Magneto', 'Trix', 'Rosé', 'Ryan', 'Ken', 'Billy', ' B. Carpinteiro', 'Lispector', 'Elish' ]
cargo = ['Ministra da Cultura', 'Prefeita de SC', 'Prefeita de MG', 'Governadora de SP', 'Primeira eleição', 'Prefeita de AL', 'Primeira eleição', 'Ministro da Agricultura', 'Ex-Presidente', 'Governadora de RJ', 'Senadora de PE']
idade = ['11 anos', '2 meses', '20 anos', '25 anos', '25 anos', ' 33 anos', '63 anos', '39 anos', '22 anos', '100 anos', '70 anos']


if 1 <= cand <=10:
        print(f'Candidato: {nomes[cand-1]}\nPartido: {parti[cand-1]}\n Vice: {vice[cand-1]}\nCargo: {cargo[cand-1]}\nIdade: {idade[cand-1]}')

else:
    print('\033[1;31mCandidato INVÁLIDO, Tente novamente\033[m')