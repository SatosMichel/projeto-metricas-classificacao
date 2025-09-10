# -*- coding: utf-8 -*-
"""
Projeto de Estudo (DIO): Cálculo de Métricas de Avaliação de Aprendizado

Este script calcula as principais métricas de avaliação para modelos de classificação
(Acurácia, Precisão, Sensibilidade, Especificidade e F1-Score) com base em 
uma matriz de confusão definida arbitrariamente.
"""

def calcular_acuracia(vp, vn, fp, fn):
    """
    Calcula a Acurácia do modelo.
    Fórmula: (VP + VN) / (VP + VN + FP + FN)
    """
    numerador = vp + vn
    denominador = vp + vn + fp + fn
    # Evita divisão por zero se a matriz estiver vazia
    if denominador == 0:
        return 0.0
    return numerador / denominador

def calcular_precisao(vp, fp):
    """
    Calcula a Precisão do modelo.
    Fórmula: VP / (VP + FP)
    """
    numerador = vp
    denominador = vp + fp
    if denominador == 0:
        return 0.0
    return numerador / denominador

def calcular_sensibilidade(vp, fn):
    """
    Calcula a Sensibilidade (Recall ou Revocação) do modelo.
    Fórmula: VP / (VP + FN)
    """
    numerador = vp
    denominador = vp + fn
    if denominador == 0:
        return 0.0
    return numerador / denominador

def calcular_especificidade(vn, fp):
    """
    Calcula a Especificidade do modelo.
    Fórmula: VN / (VN + FP)
    """
    numerador = vn
    denominador = vn + fp
    if denominador == 0:
        return 0.0
    return numerador / denominador

def calcular_f_score(precisao, sensibilidade):
    """
    Calcula o F-Score do modelo, que é a média harmônica entre precisão e sensibilidade.
    Fórmula: 2 * (Precisão * Sensibilidade) / (Precisão + Sensibilidade)
    """
    numerador = 2 * precisao * sensibilidade
    denominador = precisao + sensibilidade
    if denominador == 0:
        return 0.0
    return numerador / denominador

# --- Bloco Principal de Execução ---
if __name__ == "__main__":
    # 1. Definição da Matriz de Confusão Arbitrária
    # Contexto Exemplo: Um modelo que detecta se um e-mail é SPAM.
    # Classe Positiva: SPAM
    # Classe Negativa: NÃO SPAM
    
    VP = 95  # O modelo previu SPAM e era SPAM.
    VN = 950 # O modelo previu NÃO SPAM e era NÃO SPAM.
    FP = 15  # O modelo previu SPAM, mas era NÃO SPAM (Erro Tipo I).
    FN = 5   # O modelo previu NÃO SPAM, mas era SPAM (Erro Tipo II).

    print("="*50)
    print("PROJETO DE ESTUDO: MÉTRICAS DE AVALIAÇÃO")
    print("="*50)
    print(f"Matriz de Confusão Escolhida:")
    print(f"Verdadeiros Positivos (VP): {VP}")
    print(f"Verdadeiros Negativos (VN): {VN}")
    print(f"Falsos Positivos (FP):    {FP}")
    print(f"Falsos Negativos (FN):    {FN}\n")

    # 2. Cálculo das Métricas
    acuracia = calcular_acuracia(VP, VN, FP, FN)
    precisao = calcular_precisao(VP, FP)
    sensibilidade = calcular_sensibilidade(VP, FN)
    especificidade = calcular_especificidade(VN, FP)
    
    # O F-Score depende da precisão e da sensibilidade, então as calculamos primeiro.
    f_score = calcular_f_score(precisao, sensibilidade)

    # 3. Apresentação dos Resultados
    print("--- Resultados das Métricas ---")
    print(f"Acurácia:       {acuracia:.4f} ou {acuracia:.2%}")
    print(f"Precisão:       {precisao:.4f} ou {precisao:.2%}")
    print(f"Sensibilidade:  {sensibilidade:.4f} ou {sensibilidade:.2%}")
    print(f"Especificidade: {especificidade:.4f} ou {especificidade:.2%}")
    print(f"F-Score:       {f_score:.4f} ou {f_score:.2%}")
    print("="*50)