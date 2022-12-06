# Aula 02 - Prática 2: Imagem vetorial


# Biblioteca

import cairo


# Função imagem vetorial

with cairo.SVGSurface("pratica2.svg",200,200) as surface:


# Função Context

cairo.Context(surface)


# Função Scale

c.scale(200,200)


# Função espessura

c.set_line_width(0.05)


# Função linha 1

c.move_to(1,1)

c.line_to(0.5,0.5)


# Função linha 2

c.move_to(2,1)

c.line_to(-0.5,-0.5)


# Função cor

c.set_source_rgb(0,0,1)


# Função desenho

c.stroke()