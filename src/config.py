"""
Configurações gerais do app.
Centralizar aqui facilita ajustar tamanho de janela, cores, FPS, etc.
sem precisar mexer na lógica principal.
"""

import os

# --- Janela ---
LARGURA = 800
ALTURA = 600
TITULO = "Avatar Interativo - MVP"
FPS = 60

# --- Cores (RGB) ---
BRANCO = (255, 255, 255)

# --- Paths ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASTA_POSES = os.path.join(BASE_DIR, "assets", "poses")

# --- Mapeamento de teclas -> arquivo de imagem ---
# Facilita expandir para mais poses no futuro: basta adicionar uma nova entrada.
POSES = {
    1: os.path.join(PASTA_POSES, "pose_1.png"),
    2: os.path.join(PASTA_POSES, "pose_2.png"),
    3: os.path.join(PASTA_POSES, "pose_3.png"),
    4: os.path.join(PASTA_POSES, "pose_4.png"),
    5: os.path.join(PASTA_POSES, "pose_5.png"),
    6: os.path.join(PASTA_POSES, "pose_6.png"),
}

POSE_INICIAL = 1

PONTO_ANCORA = (LARGURA // 2, int(ALTURA * 0.85))