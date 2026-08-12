"""
Classe responsável por gerenciar as poses do personagem:
- Carrega todas as imagens uma única vez (fora do loop principal).
- Mantém o estado da pose atual.
- Sabe desenhar a si mesmo centralizado na tela.

Pensado para ser fácil de estender: no futuro, trocar 'pose_atual'
por uma máquina de estados com transições, animações intermediárias, etc.
"""

import pygame
import os


class Character:
    def __init__(self, poses_paths: dict, pose_inicial: int):
        """
        poses_paths: dict {numero_da_pose: caminho_da_imagem}
        pose_inicial: número da pose exibida ao iniciar o app
        """
        self.imagens = {}
        self._carregar_imagens(poses_paths)

        self.pose_atual = pose_inicial

    def _carregar_imagens(self, poses_paths: dict):
        """Carrega todas as imagens de uma vez, com convert_alpha()
        para performance e suporte a transparência."""
        for numero, caminho in poses_paths.items():
            if not os.path.exists(caminho):
                raise FileNotFoundError(
                    f"Imagem da pose {numero} não encontrada em: {caminho}\n"
                    f"Verifique se o arquivo existe na pasta assets/poses/"
                )
            imagem = pygame.image.load(caminho).convert_alpha()
            self.imagens[numero] = imagem

    def trocar_pose(self, numero_pose: int):
        """Troca a pose atual, se ela existir no dicionário carregado."""
        if numero_pose in self.imagens:
            self.pose_atual = numero_pose

    def desenhar(self, tela: pygame.Surface, ponto_ancora: tuple):
        """Desenha a pose atual centralizada na tela."""
        imagem_atual = self.imagens[self.pose_atual]
        rect = imagem_atual.get_rect(midbottom=ponto_ancora)
        tela.blit(imagem_atual, rect)
