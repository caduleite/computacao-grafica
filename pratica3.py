# Aula 02 - Pratica 3: Figura Geometrica

#Bibliotecas:

import cairo

import math

# Fução

surface=cairo.ImageSurface(cairo.FORMAT_ARGB32,512,256)

# Variavel
c=cairo.Context(surface)

# Função Pintar
c.paint()

# Função Cor

c.set_source_rgb(0,0,1)

# Função Espessura

c.set_line_width(6)

# Função retangulo

c.rectangle(200,50,100,50)

# Funcao desenho
c.stroke

# Função cor
c.set_source_rgb(1,1,1)

# Função arco
c.arc(100,80,40,0,2*math.pi)

# função preencher o atual
c.fill_preserve()

# Função espessura
c.set_line_width(6)

# Função cor 
c.set_source_rgb(0,0,0)

# Função desenho
c.stroke()

# Função imagem
surface.write_to_png('pratica3.png')