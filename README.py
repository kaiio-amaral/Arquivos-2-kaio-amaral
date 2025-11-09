with open("filmes.csv", "r", encoding="utf-8") as f:
    filmes = list(csv.reader(f))

avaliacoes = []
for ano, titulo in filmes:
    while True:
        try:
            nota = float(input(f"Digite a nota para '{titulo}' ({ano}): "))
            if 0 <= nota <= 10:
                avaliacoes.append([ano, titulo, nota])
                break
        except ValueError:
            pass

with open("filmes_avaliacao.csv", "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows([["Ano", "Título", "Nota"]] + avaliacoes)

with open("filmes_avaliacao.csv", "r", encoding="utf-8") as f:
    filmes = list(csv.DictReader(f))

filmes.sort(key=lambda x: (-float(x["Nota"]), x["Título"]))
top5 = filmes[:5]

with open("filmes_indicacao.csv", "w", newline="", encoding="utf-8") as f:
    csv.DictWriter(f, fieldnames=["Ano", "Título", "Nota"]).writeheader()
    csv.DictWriter(f, fieldnames=["Ano", "Título", "Nota"]).writerows(top5)

with open("filmes_indicacao.csv", "r", encoding="utf-8") as f:
    filmes = sorted(csv.DictReader(f), key=lambda x: -float(x["Nota"]))

for f in filmes:
    print(f'{f["Título"]} ({f["Ano"]}) - Nota: {f["Nota"]}')
