# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 18:13:59 2023

@author: Borsi Romero
"""
from html5svg2.cdg import dTag, dEtq, dCmt


class HTML5:
	def __init__(s, js):
		s.lh = []  # lista de objetos contenidos en head
		s.lb = []  # lista de objetos contenidos en body
		s.__title(js)
		s.__meta(js)
		s.__link(js)
		s.__style(js)
	
	def __title(s, js):
		ttl = 'Sin título'
		if 'title' in js:
			ttl = js['title']
		s.lh.extend(dTag('title', ttl, {}))
	
	def __meta(s, js):
		if 'meta' not in js:
			return
		jx = js['meta']
		if 'charset' in jx:
			s.lh.extend(dEtq('meta', {'charset': jx['charset']}))
		if 'name_content' in jx:
			for t in jx['name_content']:
				s.lh.extend(dEtq('meta', {'name': t[0], 'content': t[1]}))
	
	def __link(s, js):
		if 'link' not in js:
			return
		for jx in js['link']:
			s.lh.extend(dEtq('link', jx))
	
	def __style(s, js):
		if 'style' not in js:
			return
		s.lh.extend(dTag('style', js['style'], {}))
	
	def contenido(s, o):
		if type(o).__name__ == 'list':
			s.lb.extend(o)
		else:
			s.lb.append(o)
	
	def listado(s):
		lo = ['<!DOCTYPE html>']
		ls = dCmt('Generado por lgkHTML5 ...')
		ls.extend(dTag('head', s.lh, {}))
		ls.append('')
		ls.extend(dTag('body', s.lb, {}))
		ls.append('')
		lo.extend(dTag('html', ls, {}))
		return lo
	
	def gravar(s, arch):
		lo = s.listado()
		with open(arch, mode='w', encoding='utf-8') as f:
			for tx in lo:
				f.write(f"{tx}\n")
