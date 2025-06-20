import random

def valor_booleano(v):
    """Converte booleano para string 'V' ou 'F'."""
    return 'V' if v else 'F'

def gerar_variaveis():
    """Gera valores aleatórios para P e Q."""
    P = random.choice([True, False])
    Q = random.choice([True, False])
    return P, Q

def escolher_operacao():
    """Escolhe uma operação lógica aleatória."""
    # Operações possíveis:
    # 'AND', 'OR', 'NOT_P', 'NOT_Q', 'P_IMPLICA_Q', 'P_EQUIV_Q'
    operacoes = ['AND', 'OR', 'NOT_P', 'NOT_Q', 'IMPLICA', 'EQUIV']
    return random.choice(operacoes)

def avaliar_expressao(P, Q, operacao):
    """Avalia a expressão lógica."""
    if operacao == 'AND':
        resultado = P and Q
        expr_texto = f"P AND Q"
    elif operacao == 'OR':
        resultado = P or Q
        expr_texto = f"P OR Q"
    elif operacao == 'NOT_P':
        resultado = not P
        expr_texto = f"NOT P"
    elif operacao == 'NOT_Q':
        resultado = not Q
        expr_texto = f"NOT Q"
    elif operacao == 'IMPLICA':
        # Implicação: P -> Q = not P or Q
        resultado = (not P) or Q
        expr_texto = f"P -> Q"
    elif operacao == 'EQUIV':
        # Equivalência: P <-> Q = (P and Q) or (not P and not Q)
        resultado = (P and Q) or (not P and not Q)
        expr_texto = f"P <-> Q"
    else:
        # Caso não definido (não deve ocorrer)
        resultado = False
        expr_texto = "Expressão desconhecida"

    return resultado, expr_texto

def jogar_rodada(rodada_num):
    """Executa uma rodada do jogo."""
    print(f"\nRodada {rodada_num} de 5")
    P, Q = gerar_variaveis()
    operacao = escolher_operacao()
    resultado_real, expr_texto = avaliar_expressao(P, Q, operacao)

    # Exibir a expressão com valores atribuídos
    print(f"Dadas as variáveis: P = {valor_booleano(P)}, Q = {valor_booleano(Q)}")
    print(f"Qual o resultado da expressão: {expr_texto} ? (Responda V para Verdadeiro e F para Falso)")

    # Receber resposta do usuário e validar entrada
    while True:
        resposta_usuario = input("Resposta (V/F): ").strip().upper()
        if resposta_usuario in ['V', 'F']:
            break
        else:
            print("Entrada inválida! Por favor responda com 'V' para Verdadeiro ou 'F' para Falso.")

    # Converter resposta usuário para booleano
    resposta_bool = True if resposta_usuario == 'V' else False

    # Verificar se acertou
    if resposta_bool == resultado_real:
        print("Correto! Você ganhou 1 ponto.")
        return 1
    else:
        print(f"Errado. O resultado correto era {'V' if resultado_real else 'F'}.")
        return 0

def main():
    print("=== Jogo Desafio da Verdade ===")
    print("Responda se a expressão lógica é Verdadeira (V) ou Falsa (F).")
    total_pontos = 0
    total_rodadas = 5

    for rodada in range(1, total_rodadas + 1):
        pontos = jogar_rodada(rodada)
        total_pontos += pontos

    print(f"\nVocê acertou {total_pontos} de {total_rodadas}. Parabéns!")
    if total_pontos == total_rodadas:
        print("Excelente trabalho! Você domina as tabelas verdade.")
    elif total_pontos >= total_rodadas / 2:
        print("Bom trabalho! Continue praticando para melhorar.")
    else:
        print("Não desista! A prática leva à perfeição.")

if __name__ == "__main__":
    main()

