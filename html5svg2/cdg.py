# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 18:11:20 2023

@author: Borsi Romero
"""


def __dTag(tag, txt, js):
	#
	p = "".join(f' {k}="{js[k]}"' for k in js)
	s = f"<{tag}{p}>{txt}</{tag}>"
	return [s]


def __dTagl(tag, ls, js):
	#
	p = "".join(f' {k}="{js[k]}"' for k in js)
	rs = [f"<{tag}{p}>"]
	for tx in ls:
		rs.append(f"  {tx}")
	rs.append(f"</{tag}>")
	return rs


def dTag(tag, obj, js):
	"""
	Codifica lenguaje de marcado tipo <tag clave1="valor1" .. > obj </tag>
	:param tag: nombre. Ej. h1.
	:param obj: texto o lista de textos.
	:param js: diccionario de parámetros. Ej. {'id':'ID01', }
	:return: list
	"""
	if type(obj).__name__ == 'list':
		rs = __dTagl(tag, obj, js)
	else:
		rs = __dTag(tag, obj, js)
	return rs


def dEtq(etq, js):
	"""
	Codifica lenguaje de marcado tipo <etiqueta clave1="valor1" .. />
	:param etq: nombre de etiqueta.
	:param js: diccionario de parámetros. Ej. {'color': 'blue', }
	:return: list
	"""
	p = "".join(f' {k}="{js[k]}"' for k in js)
	p = f"<{etq}{p} />"
	return [p]


def dCmt(obj):
	"""
	Codifica comentario tipo <!-- este es un comentario -->
	:param obj: texto o lista de textos.
	:return: list
	"""
	if type(obj).__name__ == 'list':
		if len(obj) == 0:
			ls = []
		elif len(obj) == 1:
			ls = [f"<!-- {obj[0]} -->"]
		else:
			ls = ["<!--"]
			for tx in obj:
				ls.append(f"  {tx}")
			ls.append("-->")
	else:
		ls = [f"<!-- {obj} -->"]
	return ls


def cdg(etq, jx, js):
	for k, v in jx.items():
		js[k] = v
	return dEtq(etq, js)


def obj(nombre, jx, js):
	for k, v in jx.items():
		js[k] = v
	return dict(obj=nombre,	arg=js)

	
def linea(p1, p2, **jx):
	try:
		x1, y1 = p1
		x2, y2 = p2
		js = {'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2}
		return obj('line', jx, js)
	except Exception as e:
		raise Exception(f"ERROR(linea)> {e}")


def rectangulo(px, w, h, **jx):
	try:
		x, y = px
		js = {'x': x, 'y': y, 'width': w, 'height': h}
		return obj('rect', jx, js)
	except Exception as e:
		raise Exception(f"ERROR(rectangulo)> {e}")
	

def circulo(po, r, **jx):
	try:
		x, y = po
		js = {'cx': x, 'cy': y, 'r': r}
		return obj('circle', jx, js)
	except Exception as e:
		raise Exception(f"ERROR(circulo)> {e}")


def elipse(po, rx, ry, ang, **jx):
	try:
		cx, cy = po
		js = {'cx': cx, 'cy': cy, 'rx': rx, 'ry': ry, 'ang': ang}
		return obj('ellipse', jx, js)
	except Exception as e:
		raise Exception(f"ERROR(elipse)> {e}")


def polilinea(pts, **jx):
	try:
		js = {'pts': pts}
		return obj('polyline', jx, js)
	except Exception as e:
		raise Exception(f"ERROR(polilinea)> {e}")


def poligono(pts, **jx):
	try:
		js = {'pts': pts}
		return obj('polygon', jx, js)
	except Exception as e:
		raise Exception(f"ERROR(poligono)> {e}")


def trayectoria(ldx, **jx):
	try:
		js = {'ldx': ldx}
		return obj('path', jx, js)
	except Exception as e:
		raise Exception(f"ERROR(trayectoria)> {e}")


def texto(px, tx, **jx):
	try:
		x, y = px
		js = {'x': x, 'y': y, 'txt': tx}
		return obj('text', jx, js)
	except Exception as e:
		raise Exception(f"ERROR(texto)> {e}")
	