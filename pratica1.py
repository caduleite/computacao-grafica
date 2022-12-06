# Aula 02 - Prática 1: Criação de linhas


# Biblioteca
import cairo


# Variáveis largura, altura e escala (superfície)
widht = 4
height = 2
pixel_scale = 80


# Formato da imagem - Matricial
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, widht*pixel_scale, height*pixel_scale)


# Função Context
c = cairo.Context(surface)


# Normalização da imagem (LxA)
c.scale(pixel_scale,pixel_scale)


# Função retângulo (inicio/fim)
c.rectangle(0,0,widht,height)


# Função cor da superfície (escala decimal)
c.set_source_rgb(0.3, 1, 0.5)


# Função preenchimento
c.fill()


# Função linha 1
c.move_to(1,1)
c.line_to(0.5,0.5)


# Função linha 2
c.move_to(2,1)
c.line_to(-0.5,-0.5)


# Função cor da linha
c.set_source_rgb(0,0,1)


# Função espessura da linha
c.set_line_width(0.05)


# Função desenho
c.stroke()


# Função imagem
surface.write_to_png('pratica1.png')