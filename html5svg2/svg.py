# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 18:22:59 2023

@author: Borsi Romero
"""
from html5svg2.cdg import dTag, cdg, dEtq


class SVG2:
	
	def __init__(s, *ld, **js):
		s.W = 100
		s.H = 100
		s.ld = []  # lista de definiciones
		s.lc = []  # lista de contenido
		if 'W' in js:
			s.W = js['W']
		if 'H' in js:
			s.H = js['H']
		if 'letra' in js:
			s.ld.extend(dTag('style', ['text {font-family:' + f"{js['letra']}" + ';}'], {}))
		s.ajustable = False
		if 'ajustable' in ld:
			s.ajustable = True
	
	def __codigo(s):
		ls = []
		if len(s.ld) > 0:
			ls.extend(dTag('defs', s.ld, {}))
		ls.extend(s.lc)
		return ls
	
	def __arg(s, **d):
		#
		jx = {}
		if 'id' in d:
			jx['id'] = d['id']
		if 'x' in d:
			jx['x'] = d['x']
		if 'y' in d:
			jx['y'] = d['y']
		if s.ajustable:
			jx['width'] = '100%'
			jx['height'] = '100%'
			jx['viewBox'] = f'0 0 {s.W} {s.H}'
		else:
			jx['width'] = s.W
			jx['height'] = s.H
		#
		jx['xmlns'] = "http://www.w3.org/2000/svg"
		jx['xmlns:xlink'] = "http://www.w3.org/1999/xlink"
		#
		return jx
	
	def exp(s, **d):
		#
		jx = s.__arg(**d)
		return dTag('svg', s.__codigo(), jx)
	
	def gravar(s, arch, **d):
		try:
			jx = s.__arg(**d)
			ls = dTag('svg', s.__codigo(), jx)
			with open(arch, 'w', encoding='utf-8') as f:
				for o in ls:
					f.write(f"{o}\n")
		except Exception as e:
			raise Exception(e)
	
	def svg_xy(s, jo):
		try:
			obj = jo['obj']
			jx = jo['arg']
			
			id_obj = 'text'
			if obj == id_obj:
				txt = jx['txt']
				jx['y'] = s.H - jx['y']
				del jx['txt']
				return dTag(id_obj, txt, jx)
			
			id_obj = 'line'
			if obj == id_obj:
				jx['y1'] = s.H - jx['y1']
				jx['y2'] = s.H - jx['y2']
				return dEtq(id_obj, jx)
			
			id_obj = 'rect'
			if obj == id_obj:
				jx['y'] = s.H - jx['y'] - jx['height']
				return dEtq(id_obj, jx)
			
			id_obj = 'circle'
			if obj == id_obj:
				jx['cy'] = s.H - jx['cy']
				return dEtq(id_obj, jx)
			
			id_obj = 'ellipse'
			if obj == id_obj:
				jx['cy'] = s.H - jx['cy']
				if jx['ang'] != 0:
					jx['transform'] = f"rotate({-jx['ang']},{jx['cx']},{jx['cy']})"
					# print(jx)
				del jx['ang']
				return dEtq(id_obj, jx)
			
			id_obj = 'polyline'
			if obj == id_obj:
				pts = jx['pts']
				jx['points'] = " ".join(f"{x},{s.H - y}" for x, y in pts)
				del jx['pts']
				return dEtq(id_obj, jx)
			
			id_obj = 'polygon'
			if obj == id_obj:
				pts = jx['pts']
				jx['points'] = " ".join(f"{x},{s.H - y}" for x, y in pts)
				del jx['pts']
				return dEtq(id_obj, jx)
			
			id_obj = 'path'
			if obj == id_obj:
				ldx = jx['ldx']
				#
				d = ""
				for dx in ldx:
					for k, v in dx.items():
						if k in ['Z', 'z']:
							d += f"{k} "
						if k in ['H', 'h']:
							d += f"{k} {v} "
						if k == 'V':
							d += f"{k} {s.H - v} "
						if k == 'v':
							d += f"{k} {-v} "
						if k in ['M', 'L', 'T']:
							d += f"{k} {v[0]},{s.H - v[1]} "
						if k in ['Q', 'S']:
							d += f"{k} {v[0][0]},{s.H - v[0][1]} {v[1][0]},{s.H - v[1][1]} "
						if k in ['q', 's']:
							d += f"{k} {v[0][0]},{- v[0][1]} {v[1][0]},{ - v[1][1]} "
						if k == 'C':
							d += f"{k} {v[0][0]},{s.H - v[0][1]} {v[1][0]},{s.H - v[1][1]} {v[2][0]},{s.H - v[2][1]} "
						if k == 'A':
							d += f"{k} {v[0][0]},{s.H - v[0][1]} {v[1]} {v[2][0]},{s.H - v[2][1]} "
						if k == 'a':
							d += f"{k} {v[0][0]},{v[0][1]} {v[1]} {v[2][0]},{v[2][1]} {v[3][0]},{v[3][1]} "
				jx['d'] = d
				#
				del jx['ldx']
				return dEtq(id_obj, jx)
			# print(obj)
			raise Exception(f"El objeto '{obj}' no está implementado")
		except Exception as e:
			raise Exception(f"ERROR(SVG2.svg_xy)> {e}")
	
	def dibujar(s, jd):
		try:
			s.lc.extend(s.svg_xy(jd))
		except Exception as e:
			raise Exception(f"ERROR(SVG2.dibujar)> {e}")
	
	def agrupar(s, ljd, **jx):
		try:
			ls = []
			for jd in ljd:
				ls.extend(s.svg_xy(jd))
			s.lc.extend(dTag('g', ls, jx))
		except Exception as e:
			raise Exception(f"ERROR(SVG2.grupo)> {e}")