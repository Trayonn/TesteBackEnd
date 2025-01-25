# ATIVIDADE 3

faturamento = [22174.1664, 24537.6698, 26139.6134, 0.0, 0.0, 26742.6612, 0.0
               , 42889.2258, 46251.174, 11191.4722, 0.0, 0.0, 3847.4823, 373.7838, 
               2659.7563, 48924.2448, 18419.2614, 0.0, 0.0, 35240.1826, 43829.1667,
               18235.6852, 4355.0662, 13327.1025, 0.0, 0.0, 25681.8318, 1718.1221,
               13220.495, 8414.61]


def faturamento_dias(dia):
    if 1 <= dia <= len(faturamento):
        return faturamento[dia - 1]
    else:
        return "Dia não disponivel."

faturamento_menor = min(faturamento)
faturamento_maior = max(faturamento)

dias_faturamento_menor = faturamento.index(faturamento_menor) + 1
dias_faturamento_maior = faturamento.index(faturamento_maior) + 1

total = [valor for valor in faturamento if valor > 0]
media = sum(total) / len(total) if total else 0


dias_acima_da_media = len([valor for valor in total if valor > media])



print(f"Dia do menor valor de faturamento e seu valor: Dia {dias_faturamento_menor} R${faturamento_menor}")
print(f"Dia do maior valor de faturamento e seu valor: Dia {dias_faturamento_maior} R${faturamento_maior}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")