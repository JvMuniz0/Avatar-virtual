"""
Avatar Interativo em Python (MVP)

Controles:
    1, 2, 3  -> alterna entre as poses do personagem
    ESC / X  -> fecha o app
"""

import sys
import pygame

from src import config
from src.character import Character


def main():
    pygame.init()
    pygame.display.set_caption(config.TITULO)

    tela = pygame.display.set_mode((config.LARGURA, config.ALTURA))
    relogio = pygame.time.Clock()

    # Mapeia teclas do pygame (K_1, K_2, K_3) para os números das poses
    teclas_para_pose = {
        pygame.K_1: 1,
        pygame.K_2: 2,
        pygame.K_3: 3,
        pygame.K_4: 4,
        pygame.K_5: 5,
        pygame.K_6: 6
    }

    try:
        personagem = Character(config.POSES, config.POSE_INICIAL)
    except FileNotFoundError as erro:
        print(f"[ERRO] {erro}")
        pygame.quit()
        sys.exit(1)

    rodando = True
    while rodando:
        # --- 1. Processar eventos ---
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False
                elif evento.key in teclas_para_pose:
                    personagem.trocar_pose(teclas_para_pose[evento.key])

        # --- 2. Atualizar estado ---
        # (nada além da troca de pose por enquanto; espaço reservado
        # para futuras animações/transições)

        # --- 3. Desenhar ---
        tela.fill(config.BRANCO)
        personagem.desenhar(tela, config.PONTO_ANCORA)
        pygame.display.flip()

        # --- 4. Controlar FPS ---
        relogio.tick(config.FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
