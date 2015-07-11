#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


##############BIBLIOTECAS A IMPORTAR E DEFINICOES####################

import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmc,xbmcaddon,HTMLParser,base64,xmltosrt,os
from BeautifulSoup import BeautifulStoneSoup,BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP
from xbmcgui import ListItem
from tools import *
import mechanize, cookielib, base64
import re, htmlentitydefs
import urlresolver
import jsunpack
try:
    import json
except:
    import simplejson as json
h = HTMLParser.HTMLParser()


versao = '1.1'
addon_id = 'plugin.video.iptvbrondemand.mobile'
selfAddon = xbmcaddon.Addon(id=addon_id)
addonfolder = selfAddon.getAddonInfo('path')
artfolder = addonfolder + '/resources/img/'
fanart = addonfolder + '/fanart.jpg'
filmes_base = 'http://www.filmesonline2.com/category/acao/'
series_base = 'http://assistirserieshd.com/'
art = 'https://copy.com/Vq3DQcVHwXf6thbC'
novelas_base = 'https://assistirnovelas.tv/'
links = 'https://copy.com/'
ver_intro = True
 

###################################################MENUS############################################


def Ver_intro():
	xbmc.Player(xbmc.PLAYER_CORE_AUTO).play(art+'?download=1')
	return True

	
def  menus():
	intro = Ver_intro()        		
	dialog = xbmcgui.Dialog()
	dialog.ok("SEJAM BEM VINDOS", "[B]PRONTOS PARA CURTIREM OS MELHORES CANAIS DE TV,FILMES,SÉRIES,DESENHOS,ANIMES,FUTEBOL E LUTAS DO UFC EM CASA ?                                                                                               ENTÃO PREPAREM A PIPOCA QUE É HORA DO SHOW !!![/B]")
	addDir('[B][COLOR green]*[/COLOR][/B][B][COLOR red]FILMES HD/SD[/COLOR][/B]','-',24,artfolder + 'Movies-icon.png')	
	addDirM('[B][COLOR green]*[/COLOR][/B][B][COLOR red]SÉRIES HD/SD[/COLOR][/B]','-',5,artfolder + 'Icon_series.png')	
	addDir('[B][COLOR green]*[/COLOR][/B][B][COLOR red]TV AO VIVO[/COLOR][/B]','-',6,artfolder + 'live-events.png')
	addDir('[B][COLOR green]*[/COLOR][/B][B][COLOR red]ANIMAÇÃO[/COLOR][/B]','-',15,artfolder + 'animacao.png')
	addDirM('[B][COLOR green]*[/COLOR][/B][B][COLOR red]PROGRAMAS DE TV[/COLOR][/B]','-',46,'http://www.propertytrader.ae/images/products/editor_images/tv.png')	
	
	
def  filmes_hd_sd():
	addDir('[B][COLOR green]*[/COLOR][/B][B]FILMES HD[/B]','-',2,artfolder + 'Movies-icon.png')
	addDir('[B][COLOR green]*[/COLOR][/B][B]FILMES SD[/B]','-',4,artfolder + 'Movies-icon.png')
	addDir('[B][COLOR red]ADDONS RELACIONADOS[/COLOR][/B]','-',45,artfolder + 'Movies-icon.png')	
	

def  temporarios():
	dialog = xbmcgui.Dialog()
	dialog.ok("FILMES VARIADOS", "[B]OS FILMES A SEGUIR SÃO DE BAIXA QUALIDADE,SE DESEJAR ASSISTIR EM QUALIDADE FULL HD VÁ PARA A OPÇÃO FILMES HD,OU SE DESEJAR CONTINUAR CLICK EM OK!!![/B]")
	addDir('[B][COLOR green]*[/COLOR][/B][B]FILMES VARIADOS[/B]','https://copy.com/hmyyzK71z8yMvo8S?download=1',3,artfolder + 'Movies-icon.png')
	addDir('[B][COLOR green]*[/COLOR][/B][B]FILMES SD[/B]','-',8,artfolder + '2k.png')	


def  series_qualidade():
	dialog = xbmcgui.Dialog()
	dialog.ok("SÉRIES ON DEMAND", "[B]               SUAS SÉRIES FAVORITAS A UM CLICK!!![/B]")
	addDirM('[B][COLOR green]*[/COLOR][/B][B]SÉRIES HD[/B]','-',37,artfolder + 'Icon_series.png')
	addDir('[B][COLOR green]*[/COLOR][/B][B]SÉRIES SD[/B]','-',38,artfolder + 'Icon_series.png')


def  series_qualidade_hd():	
	addDirM('[B][COLOR green]*[/COLOR][/B][B]SÉRIES HD[/B]','-',16,artfolder + 'Icon_series.png')
	addDirM('[B][COLOR green]*[/COLOR][/B][B]SÉRIES HD POR LETRA[/B]','-',23,artfolder + 'Icon_series.png')
	addDirM('[B][COLOR green]*[/COLOR][/B][B]PESQUISAR SÉRIES HD[/B]','-',30,artfolder + 'lupa.png')

	
def  series_qualidade_sd():
	addDir('[B][COLOR green]*[/COLOR][/B][B]SÉRIES SD[/B]','http://www.armagedomfilmes.biz/?cat=21|1',10,artfolder + 'Icon_series.png')
	addDir('[B][COLOR green]*[/COLOR][/B][B]PESQUISAR SÉRIES SD[/B]','-',14,artfolder + 'lupa.png')	
	

def  categorias():
	dialog = xbmcgui.Dialog()
	dialog.ok("FILMES SOB DEMANDA", "[B]       SELECIONE A CATEGORIA DO FILME DESEJADO !!![/B]")
	addDir('[B]AÇÃO[/B]','https://copy.com/Iyt3UBHMKPehfPPs?download=1',3,artfolder + 'acao.jpg')
	addDir('[B]ANIMAÇÃO[/B]','https://copy.com/rdkdvoVAFOoD6FVu?download=1',3,artfolder + 'animacao.jpg')
	addDir('[B]AVENTURA[/B]','https://copy.com/RK9DFiXkF6BRenUv?download=1',3,artfolder + 'AVENTURA.jpg')
	addDir('[B]COMÉDIA[/B]','https://copy.com/PMDC1RJbl06erivh?download=1',3,artfolder + 'comedia.jpg')
	addDir('[B]DRAMA[/B]','https://copy.com/VQzV2J4YDwigMRor?download=1',3,artfolder + 'DRAMA.jpg')
	addDir('[B]GUERRA[/B]','https://copy.com/e4gfUvkzwIVKDvCH?download=1',3,artfolder + 'GUERRA.jpg')
	addDir('[B]NACIONAL[/B]','https://copy.com/vgLne99gBhJlkQyE?download=1',3,artfolder + 'NACIONAL.jpg')
	addDir('[B]RELIGIOSO[/B]','https://copy.com/eolYU1Zfh6sSOT3L?download=1',3,artfolder + 'RELIGIOSO.jpg')
	addDir('[B]ROMANCE[/B]','https://copy.com/KgOtLnPaaKPqFUp4?download=1',3,artfolder + 'ROMANCE.jpg')
	addDir('[B]SUSPENSE[/B]','https://copy.com/NaVFwAKelkVEmC4O?download=1',3,artfolder + 'SUSPENSE.jpg')
	addDir('[B]TERROR[/B]','https://copy.com/HgCH4omqtdRAr76O?download=1',3,artfolder + 'TERROR.jpg')
	
	
def Armagedom_categorias():
	addDir('[B]BLURAY[/B]','http://www.armagedomfilmes.biz/?cat=5529',33,artfolder + 'Movies-icon.png')
	addDir('[B]LEGENDADOS[/B]','http://www.armagedomfilmes.biz/?s=legendado',33,artfolder + 'Movies-icon.png')
	addDir('[B]AÇÃO[/B]','http://www.armagedomfilmes.biz/?cat=3227',33,artfolder + 'Movies-icon.png')
	addDir('[B]ANIMAÇÃO[/B]','http://www.armagedomfilmes.biz/?cat=3228',33,artfolder + 'Movies-icon.png')
	addDir('[B]AVENTURA[/B]','http://www.armagedomfilmes.biz/?cat=3230',33,artfolder + 'Movies-icon.png')
	addDir('[B]COMÉDIA[/B]','http://www.armagedomfilmes.biz/?cat=3229',33,artfolder + 'Movies-icon.png')
	addDir('[B]COMÉDIA ROMANTICA[/B]','http://www.armagedomfilmes.biz/?cat=3231',33,artfolder + 'Movies-icon.png')
	addDir('[B]DRAMA[/B]','http://www.armagedomfilmes.biz/?cat=3233',33,artfolder + 'Movies-icon.png')
	addDir('[B]FAROESTE[/B]','http://www.armagedomfilmes.biz/?cat=18',33,artfolder + 'Movies-icon.png')
	addDir('[B]FICÇÃO CIENTÍFICA[/B]','http://www.armagedomfilmes.biz/?cat=3235',33,artfolder + 'Movies-icon.png')
	addDir('[B]LUTAS UFC[/B]','http://www.armagedomfilmes.biz/?cat=3394',33,artfolder + 'Movies-icon.png')
	addDir('[B]NACIONAL[/B]','http://www.armagedomfilmes.biz/?cat=3226',33,artfolder + 'Movies-icon.png')
	addDir('[B]POLICIAL[/B]','http://www.armagedomfilmes.biz/?cat=72',33,artfolder + 'Movies-icon.png')
	addDir('[B]RELIGIOSO[/B]','http://www.armagedomfilmes.biz/?cat=20',33,artfolder + 'Movies-icon.png')
	addDir('[B]ROMANCE[/B]','http://www.armagedomfilmes.biz/?cat=3232',33,artfolder + 'Movies-icon.png')
	addDir('[B]SHOWS[/B]','http://www.armagedomfilmes.biz/?cat=30',33,artfolder + 'Movies-icon.png')
	addDir('[B]SUSPENSE[/B]','http://www.armagedomfilmes.biz/?cat=3239',33,artfolder + 'Movies-icon.png')
	addDir('[B]TERROR[/B]','http://www.armagedomfilmes.biz/?cat=3238',33,artfolder + 'Movies-icon.png')
	addDir('[B]THRILLER[/B]','http://www.armagedomfilmes.biz/?cat=30',33,artfolder + 'Movies-icon.png')


def categorias_cine(url):

	addDirC('[B]FULL HD 1080P[/B]','http://www.cinefilmeshd.com/category/1080p/',35,artfolder + 'Movies-icon.png')
	addDirC('[B]AÇÃO[/B]','http://www.cinefilmeshd.com/category/acao/',35,artfolder + 'Movies-icon.png')
	addDirC('[B]ANIMAÇÃO[/B]','http://www.cinefilmeshd.com/category/animacao/',35,artfolder + 'Movies-icon.png')
	addDirC('[B]AVENTURA[/B]','http://www.cinefilmeshd.com/category/aventura/',35,artfolder + 'Movies-icon.png')
	addDirC('[B]COMÉDIA[/B]','http://www.cinefilmeshd.com/category/comedia/',35,artfolder + 'Movies-icon.png')
	addDirC('[B]COMÉDIA ROMANTICA[/B]','http://www.cinefilmeshd.com/category/comedia-romantica/',35,artfolder + 'Movies-icon.png')
	addDirC('[B]DOCUMENTÁRIOS[/B]','http://www.cinefilmeshd.com/category/documentario/',35,artfolder + 'Movies-icon.png')
	addDirC('[B]DRAMA[/B]','http://www.cinefilmeshd.com/category/drama/',35,artfolder + 'Movies-icon.png')
	addDirC('[B]FICÇÃO CIENTÍFICA[/B]','http://www.cinefilmeshd.com/category/ficcao-cientifica/',35,artfolder + 'Movies-icon.png')
	addDirC('[B]GUERRA[/B]','http://www.cinefilmeshd.com/category/guerra/',35,artfolder + 'Movies-icon.png')
	addDirC('[B]INGLÊS[/B]','http://www.cinefilmeshd.com/category/ingles/',35,artfolder + 'Movies-icon.png')
	addDirC('[B]LEGENDADO[/B]','http://www.cinefilmeshd.com/category/legendados/',35,artfolder + 'Movies-icon.png')
	addDirC('[B]MUSICAL[/B]','http://www.cinefilmeshd.com/category/musical/',35,artfolder + 'Movies-icon.png')
	addDirC('[B]NACIONAL[/B]','http://www.cinefilmeshd.com/category/nacional/',35,artfolder + 'Movies-icon.png')
	addDirC('[B]ROMANCE[/B]','http://www.cinefilmeshd.com/category/romance/',35,artfolder + 'Movies-icon.png')
	addDirC('[B]SUSPENSE[/B]','http://www.cinefilmeshd.com/category/suspense/',35,artfolder + 'Movies-icon.png')
	addDirC('[B]TERROR[/B]','http://www.cinefilmeshd.com/category/terror/',35,artfolder + 'Movies-icon.png')	

	
	
def  tv_ao_vivo():	
	dialog = xbmcgui.Dialog()
	dialog.ok("CANAIS DE TV","[B]ASSISTA CANAIS DE TV DO BRASIL E DO MUNDO AQUI !!![/B]")
	addDir('[B][COLOR green]*[/COLOR][/B][B]TV ABERTA[/B]',links + 'wwRMUE88YpbBHq1R?download=1',3,'http://tvabcd.com.br/system/uploads/ck/1/images/assistir-tv-online.png')
	addDir('[B][COLOR green]*[/COLOR][/B][B]ESPORTES[/B]',links + '4pDaNzKgy0gpgAwm?download=1',3,'http://tvabcd.com.br/system/uploads/ck/1/images/assistir-tv-online.png')
	addDir('[B][COLOR green]*[/COLOR][/B][B]JORNALISMO[/B]',links + 'aZLzoTmIFohZtir0?download=1',3,'http://tvabcd.com.br/system/uploads/ck/1/images/assistir-tv-online.png')
	addDir('[B][COLOR green]*[/COLOR][/B][B]FILMES[/B]',links + 'jup1OwG1MZT7UsvR?download=1',3,'http://tvabcd.com.br/system/uploads/ck/1/images/assistir-tv-online.png')
	addDir('[B][COLOR green]*[/COLOR][/B][B]DOCUMENTÁRIOS[/B]',links + 'c1ydCNbYq7t9S6kv?download=1',3,'http://tvabcd.com.br/system/uploads/ck/1/images/assistir-tv-online.png')
	addDir('[B][COLOR green]*[/COLOR][/B][B]INFANTIL[/B]',links + 'esYvzMA88EPCZf3L?download=1',3,'http://tvabcd.com.br/system/uploads/ck/1/images/assistir-tv-online.png')
	addDir('[B][COLOR green]*[/COLOR][/B][B]MÚSICA[/B]',links + 'wqXSmdse6ZfplZTh?download=1',3,'http://tvabcd.com.br/system/uploads/ck/1/images/assistir-tv-online.png')
	addDir('[B][COLOR green]*[/COLOR][/B][B]RELIGIOSO[/B]',links + '3Zyy7d7LEfZVlgr3?download=1',3,'http://tvabcd.com.br/system/uploads/ck/1/images/assistir-tv-online.png')
	
	
	
def Animacao():	
	dialog = xbmcgui.Dialog()
	dialog.ok("ASSISTA AQUI:", "[B]      OS MELHORES ANIMES E DESENHOS 24 HORAS!!![/B]")
	addDir('[B][COLOR green]*[/COLOR][/B][B]ANIMES[/B]','-',25,artfolder + 'anime.png')	
	addDir('[B][COLOR green]*[/COLOR][/B][B]DESENHOS 24hrs[/B]','https://copy.com/0ZeS9pyD92GXM9rM?download=1',3,artfolder + 'Desenhos.png')


def Animes():
	addDir('[B]CATEGORIAS[/B]','http://anitube.xpg.uol.com.br/categories',26,artfolder + 'categorias5.png')
	addDir('[B]RECENTES[/B]','http://anitube.xpg.uol.com.br/videos/basic/mr',27,artfolder + 'recentes.png')
	addDir('[B]BUSCAR ANIME[/B]','http://anitube.xpg.uol.com.br/',29,artfolder + 'pesquisa.png')
	xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	xbmc.executebuiltin('Container.SetViewMode(500)')

	
def Armagedom():
	addDir('[B]CATEGORIAS[/B]','-',32,artfolder + 'Movies-icon.png')
	addDir('[B]LANÇAMENTOS[/B]','http://www.armagedomfilmes.biz/?cat=3236',33,artfolder + 'Movies-icon.png')
	addDir('[B]PESQUISAR FILMES[/B]','-',34,artfolder + 'lupa.png')


def Cine_hd(url):	
	addDirC('[B]CATEGORIAS[/B]','-',21,artfolder + 'Movies-icon.png')
	addDirC('[B]LANÇAMENTOS[/B]','http://www.cinefilmeshd.com/category/lancamento/',35,artfolder + 'Movies-icon.png')
	addDirC('[B]BLURAY[/B]','http://www.cinefilmeshd.com/category/bluray/',35,artfolder + 'Movies-icon.png')
	addDirC('[B]PESQUISAR[/B]','-',36,artfolder + 'lupa.png')

	
def Addons():
	addDir('[B][COLOR green]*[/COLOR][/B][B]ARMAGEDOM FILMES[/B]','-',31,artfolder + 'icon.png')
	addDirC('[B][COLOR green]*[/COLOR][/B][B]CINEFILMES HD[/B]','-',20,artfolder + 'cinefilmes.jpg')
	
	
def Tv_Gravada():
	addDirM('[B][COLOR green]*[/COLOR][/B][B]TV GRAVADA[/B]','-',51,'http://www.apkdad.com/wp-content/uploads/2013/02/Live-TV-for-Android-Icon.png')


def Programas_tv():
    #addDirD(name, url, mode, iconimage, total=0, pasta=True, plot='', fanart=''):
    addDirD("[B]NOVELAS[/B]","0",42,'http://www.apkdad.com/wp-content/uploads/2013/02/Live-TV-for-Android-Icon.png')	
    addDirD("[B]SÉRIES[/B]","1",53,'http://www.apkdad.com/wp-content/uploads/2013/02/Live-TV-for-Android-Icon.png')
    addDirD("[B]JORNALISMO[/B]","2",42,'http://www.apkdad.com/wp-content/uploads/2013/02/Live-TV-for-Android-Icon.png')
    addDirD("[B]VARIEDADES[/B]","3",42,'http://www.apkdad.com/wp-content/uploads/2013/02/Live-TV-for-Android-Icon.png')
    addDirD("[B]ESPORTES[/B]","4",42,'http://www.apkdad.com/wp-content/uploads/2013/02/Live-TV-for-Android-Icon.png')
    xbmcplugin.setContent(int(sys.argv[1]), 'movies')
    xbmc.executebuiltin('Container.SetViewMode(51)')	
	

def Listar_categorias_novelas(url=novelas_base,cat=0):
    print url
    html = abrir_url2(url)
    #html = html.encode('ascii','xmlcharrefreplace')
    soup = BeautifulSoup(html)

    a = []
    menu = soup("div", {"class": "Box"})[int(cat)]
    # print menu
    links = menu("a")
    #resultados = content.findAll("td",  { "width" : "1%" })
    for link in links:
        if not link['href'] == '#' and not html_replace_clean(link.text.encode('ascii', 'xmlcharrefreplace')) == 'Pagina Inicial':
            # print link['href']
            addDirD(html_replace_clean(link.text.encode('ascii', 'xmlcharrefreplace')), link['href'], 43, 'http://www.apkdad.com/wp-content/uploads/2013/02/Live-TV-for-Android-Icon.png', len(links), True)
    xbmcplugin.setContent(int(sys.argv[1]), 'movies')
    xbmc.executebuiltin('Container.SetViewMode(51)')


def Listar_categorias_novelas2(url=novelas_base,cat=0):
    print url
    html = abrir_url2(url)
    #html = html.encode('ascii','xmlcharrefreplace')
    soup = BeautifulSoup(html)

    a = []
    menu = soup("div", {"class": "Box"})[int(cat)]
    # print menu
    links = menu("a")
    #resultados = content.findAll("td",  { "width" : "1%" })
    for link in links:
        if not link['href'] == '#' and not html_replace_clean(link.text.encode('ascii', 'xmlcharrefreplace')) == 'Pagina Inicial':
            # print link['href']
            addDirD(html_replace_clean(link.text.encode('ascii', 'xmlcharrefreplace')), link['href'], 52, 'http://www.apkdad.com/wp-content/uploads/2013/02/Live-TV-for-Android-Icon.png', len(links), True)
    xbmcplugin.setContent(int(sys.argv[1]), 'movies')
    xbmc.executebuiltin('Container.SetViewMode(51)')	


def Listar_episodios_novelas(url):
    print url
    html = abrir_url2(url)
    #html = unicode(html, 'ascii', errors='ignore')
    soup = BeautifulSoup(html)

    a = []
    categorias = soup("div", {"class": "Caixa"})[1]
    #print categorias
    episodios = categorias("div", {"class": "Imagem"})
    for episodio in episodios:
        img = episodio.a.img['src']
	#print img
        titulo = html_replace_clean(episodio.a.img['alt'].encode('ascii', 'xmlcharrefreplace'))  # episodio.img['alt']
        url = episodio.a['href']
        # addDir(name,url,mode,iconimage,total=0,pasta=True)
        addDirD(titulo, url, 44, img, len(episodios), False)
    paginacao = categorias("a", {"class": "right"})[0]
    addDirD(html_replace_clean(paginacao.text.encode('ascii', 'xmlcharrefreplace')), paginacao['href'], 43, '', len(episodios) + 1)

    xbmcplugin.setContent(int(sys.argv[1]), 'episodes')
    xbmc.executebuiltin('Container.SetViewMode(503)')


def Episodios_novelas(url):
    print url
    html = abrir_url2(url)
    #html = unicode(html, 'ascii', errors='ignore')
    soup = BeautifulSoup(html)

    a = []
    categorias = soup("div", {"class": "Caixa"})[1]
    #print categorias
    episodios = categorias("div", {"class": "Imagem"})
    for episodio in episodios:
        img = episodio.a.img['src']
	#print img
        titulo = html_replace_clean(episodio.a.img['alt'].encode('ascii', 'xmlcharrefreplace'))  # episodio.img['alt']
        url = episodio.a['href']
        # addDir(name,url,mode,iconimage,total=0,pasta=True)
        addDirD(titulo, url, 44, img, len(episodios), False)

    xbmcplugin.setContent(int(sys.argv[1]), 'episodes')
    xbmc.executebuiltin('Container.SetViewMode(503)')	
 

def Resolve_episodio_novelas(url):
    # print url
    pg = 0
    mensagemprogresso = xbmcgui.DialogProgress()
    mensagemprogresso.create('Trabalhando', 'Gerando playlist', 'Por favor aguarde...')
    pg += 10
    mensagemprogresso.update(pg)
    html = abrir_url(url)
    soup = BeautifulSoup(html)
    playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
    playlist.clear()
    pg += 10
    mensagemprogresso.update(pg)
    br = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)
    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    br.addheaders = [('Referer', url)]
    pg += 10
    mensagemprogresso.update(pg)
    br.open('https://assistirnovelas.tv')
    form = base64.b64decode('PGZvcm0gYWN0aW9uPSJodHRwczovL2Fzc2lzdGlybm92ZWxhcy50di9Mb2dpblVzdWFyaW8ucGhwIiBpZD0iZm9ybTEiIG1ldGhvZD0icG9zdCI+DQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxsaT5FLW1haWw8L2xpPg0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8bGk+PGlucHV0IHR5cGU9InRleHQiIHZhbHVlPSIiIG5hbWU9ImVtYWlsIiBjbGFzcz0iQ2FtcG9Mb2dpbiIgcGxhY2Vob2xkZXI9IlNldSBlLW1haWwiPjwvbGk+DQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxsaT5TZW5oYTwvbGk+DQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxsaT48aW5wdXQgdmFsdWU9IiIgbmFtZT0ic2VuaGEiIGNsYXNzPSJDYW1wb0xvZ2luIiBwbGFjZWhvbGRlcj0iU3VhIHNlbmhhIiB0eXBlPSJwYXNzd29yZCI+PC9saT4NCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPGxpPjxpbnB1dCB0eXBlPSJzdWJtaXQiIGNsYXNzPSJMb2dpbkluaWNpbyIgdmFsdWU9IkVudHJhciI+PC9saT4NCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPGxpPjxhIGhyZWY9Imh0dHBzOi8vYXNzaXN0aXJub3ZlbGFzLnR2L2NhZGFzdHJvLnBocCI+UmVnaXN0cmFyPC9hPjwvbGk+DQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxsaT48YSBocmVmPSJodHRwczovL2Fzc2lzdGlybm92ZWxhcy50di9sZW1icmFyX3NlbmhhLnBocCI+TGVtYnJhciBzZW5oYTwvYT48L2xpPg0KICAgICAgICAgICAgICAgICAgPC9mb3JtPg==')
    res = mechanize._form.ParseString(form, "https://assistirnovelas.tv")
    br.form = res[1]
    # br.select_form(nr=0)
    br.form['senha'] = base64.b64decode('MTIzNDU2')
    br.form['email'] = base64.b64decode('YXJsZWlyYS5jYXN0cm9AZ21haWwuY29t')
    br.submit()
    pg += 10
    mensagemprogresso.update(pg)
    page = br.open(url).read()
    iframe = re.findall("var url = '(.*?)'",page)[0]+"html5iframe/"
    print iframe
    page1 = br.open(iframe).read()
    print page1
    links = re.findall("'(.*?)',", page1)
    pg += 10
    mensagemprogresso.update(pg)
    if links:
	for link in links:
	    listitem = xbmcgui.ListItem('Epsodio', thumbnailImage='')
	    listitem.setInfo('video', {'Title': 'Episodio'})
	    playlist.add(url=link, listitem=listitem, index=7)
	mensagemprogresso.update(100)
	xbmc.Player(xbmc.PLAYER_CORE_AUTO).play(playlist)
    else:
        mensagemprogresso.update(100)
        dialog = xbmcgui.Dialog()
        dialog.ok("Indisponivel", "Este ainda não esta disponivel, tente novamente em breve.") 
	
	

def Listar_categorias2(url):
	print url
	html = abrir_url(url)
	html = unicode(html, 'ascii', errors='ignore')
	soup = BeautifulSoup(html)

	a = []
	categorias = soup.findAll("li", { "class" : "mainList" })
	#resultados = content.findAll("td",  { "width" : "1%" })
	for categoria in categorias:
		temp = [categoria.a["href"],"%s" % (categoria.a.img["alt"].encode('ascii', 'ignore')),categoria.a.img["src"],categoria.a["title"]] 
		a.append(temp)
	total = len(a)
	
	for url2, titulo, img, plot in a:
		titulo = cleanHtml(titulo)
		addDir(titulo,url2,27,img,True,total,plot)
	pages = soup.find('ul',{ "id" : "pagination-flickr" }).findAll('a')
	print pages
	for prox_pagina in pages:
		if prox_pagina.text == 'Next':
			addDir('Página Seguinte >>',prox_pagina['href'],26,artfolder + 'next.png')
	xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	xbmc.executebuiltin('Container.SetViewMode(500)')
	

def Listar_episodios2(url):
	print url
	html = abrir_url(url)
	html = unicode(html, 'ascii', errors='ignore')
	soup = BeautifulSoup(html)

	a = []
	categorias = soup.findAll("li", { "class" : "mainList" })
	#resultados = content.findAll("td",  { "width" : "1%" })
	for categoria in categorias:
		try:
			temp = [categoria.a["href"],"%s" % (categoria.a.img["alt"].encode('ascii', 'ignore')),categoria.a.img['src'],''] 
			a.append(temp)
		except:
			pass
	a.sort()
	total = len(a)
	
	for url2, titulo, img, plot in a:
		titulo = cleanHtml(titulo)
		addDir(titulo,url2,28,img,True,total,plot)
	try:
		pages = soup.find('ul',{ "id" : "pagination-flickr" }).findAll('a')
		for prox_pagina in pages:
			if prox_pagina.text == 'Next':
				addDir('Página Seguinte >>',prox_pagina['href'],27,artfolder + 'next.png')
	except:
		pass
	xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	xbmc.executebuiltin('Container.SetViewMode(500)')
	

def Resolve_episodio(url):
	print url
	html = abrir_url(url)
	xml_url = "http://anitube.xpg.uol.com.br/nuevo/econfig.php?key=" + re.findall(r'src="http://anitubebr.xpg.uol.com.br/embed/(.+?)"',html)[0]
	xml = abrir_url(xml_url)
	soup = BeautifulSoup(xml)
	file_url = ''
	filehd_url = ''
	image = ''
	try:
		file_url = soup.config.file.text
	except:
		pass
	try:
		filehd_url = soup.config.filehd.text
	except:
		pass
	try:
		image = soup.config.image.text
	except:
		pass
	if filehd_url:
		addLink('HD', filehd_url, image)
	if file_url:
		addLink('SD', file_url, image)
		

def Pesquisa():
	keyb = xbmc.Keyboard('', 'Pesquisar...')
	keyb.doModal()
	if (keyb.isConfirmed()):
		search = keyb.getText()
		parametro_pesquisa=urllib.quote(search)
		url = 'http://anitube.xpg.uol.com.br/search/?search_id=' + str(parametro_pesquisa)
		Listar_episodios(url)	
	
	
def Listar_categorias_series(url=series_base):
 print url
 html = abrir_url2(url)
 #html = html.encode('ascii','xmlcharrefreplace')
 soup = BeautifulSoup(html)

 a = []
 menu = soup("ul", { "class" : "SubMenu" })[0]
 #print menu
 links = menu("a")
 #resultados = content.findAll("td",  { "width" : "1%" })
 for link in links:
  if not link['href'] == '#' and not html_replace_clean(link.text.encode('ascii','xmlcharrefreplace')) == 'Pagina Inicial':
   #print link['href']
   addDirM(html_replace_clean(link.text.encode('ascii','xmlcharrefreplace')),link['href'],17,'https://copy.com/AalWGHh9t4MPy9Nr?download=1',len(links),True)
 xbmcplugin.setContent(int(sys.argv[1]), 'movies')
 xbmc.executebuiltin('Container.SetViewMode(51)')
 
 
def Listar_categorias_series_letra(url=series_base):
 print url
 html = abrir_url(url)
 #html = html.encode('ascii','xmlcharrefreplace')

 soup = BeautifulSoup(html)

 a = []
 links = soup("a", { "rel" : "nofollow" })
 #ow = open('G:\html_list\series.html', 'w')
 #ow.write(str(links))
 #ow.close()
 #print links
 #print menu
 #resultados = content.findAll("td",  { "width" : "1%" })
 for link in links:
  if len(link.text) == 1:
   #print link['href']
   addDirM('Séries com a letra: '+ html_replace_clean(link.text.encode('ascii','xmlcharrefreplace')).upper(),series_base+link['href'],17,'https://copy.com/AalWGHh9t4MPy9Nr?download=1',len(links),True)
 xbmcplugin.setContent(int(sys.argv[1]), 'movies')
 xbmc.executebuiltin('Container.SetViewMode(51)') 
 
 
def listar_series2(url):
 print url
 html = abrir_url(url)
 #html = unicode(html, 'ascii', errors='ignore')
 soup = BeautifulSoup(html)

 a = []
 categorias = soup("div", { "id" : "Conteudo" })[0]
 #print str(categorias)

 series = categorias("div", { "class" : "amazingcarousel-image" })
 for serie in series:
  #print serie
  img = serie.img['src']
  titulo = html_replace_clean(serie.img['alt'].encode('ascii','xmlcharrefreplace'))#episodio.img['alt']
  url = serie.a['href']
  #addDirM(name,url,mode,iconimage,total=0,pasta=True)
  addDir(titulo,url,18,img,len(series),True)
  #xbmcplugin.setContent(int(sys.argv[1]), 'movies')
  #xbmc.executebuiltin('Container.SetViewMode(500)')


def listar_episodios_series(url):
 #print url
 html = abrir_url(url)
 #html = unicode(html, 'ascii', errors='ignore')
 soup = BeautifulSoup(html)

 a = []
 categorias = soup("div", { "id" : "Conteudo" })[0]
 #print str(categorias)

 episodios = categorias("div", { "class" : "Episodio" })
 
 for episodio in episodios:
  img = episodio.img['src']
  titulo = html_replace_clean(episodio.img['alt'].encode('ascii','xmlcharrefreplace'))#episodio.img['alt']
  url = episodio.a['href']
  #addDir(name,url,mode,iconimage,total=0,pasta=True)
  addDirM(titulo,url,19,img,len(episodios),False)
 if len(episodios) == 0:
  addDirM('Esta temporada não tem episodios ainda...aguarde.','',0,'',0,False)
 links = soup("div", { "class" : "Temporadas" })[0]('a')
 if len(links) > 1:
    addDirM('---------------------------','',0,'',0,False)
 for link in links:
	if not link['href'] == '#':
	    addDirM("Temporada: " + link.string,link['href'],18,'',len(episodios)+1)

 xbmcplugin.setContent(int(sys.argv[1]), 'episodes')
 xbmc.executebuiltin('Container.SetViewMode(503)')
 
 
def listar_series3(url):
 print url
 html = abrir_url(url)
 #html = unicode(html, 'ascii', errors='ignore')
 soup = BeautifulSoup(html)

 a = []
 categorias = soup("div", { "id" : "Conteudo" })[0]
 #print str(categorias)

 series = categorias("div", { "class" : "amazingcarousel-image" })
 for serie in series:
  #print serie
  img = serie.img['src']
  titulo = html_replace_clean(serie.img['alt'].encode('ascii','xmlcharrefreplace'))#episodio.img['alt']
  url = serie.a['href']
  #addDir(name,url,mode,iconimage,total=0,pasta=True)
  addDir(titulo,url,18,img,len(series),True)
  #xbmcplugin.setContent(int(sys.argv[1]), 'episodes')
  #xbmc.executebuiltin('Container.SetViewMode(503)') 


def Resolve_episodio_serie(url):
	#print url
	pg = 0
	mensagemprogresso = xbmcgui.DialogProgress()
	mensagemprogresso.create('Trabalhando', 'Gerando playlist','Por favor aguarde...')
	pg += 10
	mensagemprogresso.update(pg)
	html = abrir_url(url)
	soup = BeautifulSoup(html)
	playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
	playlist.clear()
	pg += 10
	mensagemprogresso.update(pg)
	br = mechanize.Browser()
	cj = cookielib.LWPCookieJar()
	br.set_cookiejar(cj)
	br.set_handle_equiv(True)
	br.set_handle_gzip(True)
	br.set_handle_redirect(True)
	br.set_handle_referer(True)
	br.set_handle_robots(False)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
	pg += 10
	mensagemprogresso.update(pg)
	br.open(series_base)
	br.select_form(nr=0)
	br.form['senha']=base64.b64decode('MTIzNDU2')
	br.form['email']=base64.b64decode('YXJsZWlyYS5jYXN0cm9AZ21haWwuY29t')
	br.submit()
	pg += 10
	mensagemprogresso.update(pg)
	page = br.open(url).read()

	links = re.findall('src: "(.*?)"',page)
	pg += 10
	mensagemprogresso.update(pg)
	if links:
		for link in links:
		    listitem = xbmcgui.ListItem('Episodio', thumbnailImage='src')
		    listitem.setInfo('video', {'Title': 'Episodio'})
		    playlist.add(url=link, listitem=listitem, index=7)
		mensagemprogresso.update(100)
		xbmc.Player(xbmc.PLAYER_CORE_AUTO).play(playlist)
	else:
		mensagemprogresso.update(100)
		dialog = xbmcgui.Dialog()
		dialog.ok("Indisponivel", "Este ainda não esta disponivel, tente novamente em breve.") 
 

def Listar_programacao(url=filmes_base):
 print url
 html = abrir_url2(url)
 #html = html.encode('ascii','xmlcharrefreplace')
 soup = BeautifulSoup(html)

 a = []
 menu = soup("div", { "class" : "agrupador" })[0]
 #print menu
 links = menu("a")
 #resultados = content.findAll("td",  { "width" : "1%" })
 for link in links:
  if not link['href'] == '#' and not html_replace_clean(link.text.encode('ascii','xmlcharrefreplace')) == 'Pagina Inicial':
   #print link['href']
   addDir(html_replace_clean(link.text.encode('ascii','xmlcharrefreplace')),link['href'],9,'https://copy.com/9aPDiAF23J6XKems?download=1',len(links),True)
 xbmcplugin.setContent(int(sys.argv[1]), 'movies')
 xbmc.executebuiltin('Container.SetViewMode(51)') 

 
def Listar_episodios(url):
 print url
 html = abrir_url2(url)
 #html = unicode(html, 'ascii', errors='ignore')
 soup = BeautifulSoup(html)

 a = []
 categorias = soup("div", { "class" : "box_item" })[0]
 #print categorias
 episodios = categorias("div", { "class" : "peli" })
 for episodio in episodios:
  img = episodio.img['src']
  titulo = html_replace_clean(episodio.img['alt'].encode('ascii','xmlcharrefreplace'))#episodio.img['alt']
  url = episodio.a['href']
  #addDir(name,url,mode,iconimage,total=0,pasta=True)
  addDir(titulo,url,13,img,False)
 pages = soup("a",{ "class" : "nextpostslink" })
 for prox_pagina in pages:
  addDir('Próxima Página >>',prox_pagina["href"],9,artfolder + 'next.png')
  
 xbmcplugin.setContent(int(sys.argv[1]), 'movies')
 xbmc.executebuiltin('Container.SetViewMode(500)')	
	

def listar_canais(url):
      for line in urllib2.urlopen(url).readlines():
            params = line.split(',')
            try:
                  nome = params[0]
                  print 'Nome: ' + nome
                  img = params[1].replace(' rtmp','rtmp').replace(' rtsp','rtsp').replace(' http','http')
                  print 'Img: ' + img
                  rtmp = params[2].replace(' rtmp','rtmp').replace(' rtsp','rtsp').replace(' http','http')
                  print 'Link: ' + rtmp
                  addLink(nome,rtmp,img)
            except:
                  pass
      xbmc.executebuiltin("Container.SetViewMode(500)")


def filmes_armagedom(url):
	codigo_fonte = abrir_url(url)
	soup = BeautifulSoup(abrir_url(url))
	content = BeautifulSoup(soup.find("div", { "class" : "bic-miniaturas" }).prettify())
	filmes = content("div", { "class" : "bic-miniatura" })
	for filme in filmes:
		titulo = filme.a["title"].replace('Assistir ','')
		url = filme.a["href"]
		img = filme.img["src"]
		addDir(titulo.encode('utf8'),url,13,img,False,len(filmes)) 

	pagenavi = BeautifulSoup(soup.find('div', { "class" : "wp-pagenavi" }).prettify())("a", { "class" : "nextpostslink" })[0]["href"]
	addDir('Página Seguinte >>',pagenavi,33,artfolder + 'prox.png')

	xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	xbmc.executebuiltin('Container.SetViewMode(503)')


def filmes_cinefilmeshd(url):
	codigo_fonte = abrir_url(url)
	match = re.compile('<h2><a href="(.+?)" title="(.+?)">.+?</a></h2>').findall(codigo_fonte) 
	img = re.compile('<img src="(.+?)" alt=".+?" />').findall(codigo_fonte) #<div style="text-align: center;"><img alt="" border="0" src="(.+?)"

	a = [] # url titulo img
	for x in range(0, len(match)):
		temp = [match[x][0],match[x][1],img[x]]; 
		a.append(temp);
	
	total = len(a)
	for url2, titulo, img in a:
		titulo = titulo.replace('&#8211;',"-").replace('&#8217;',"'")	#Linha para corrigir caracteres especiais
		addDir(titulo,url2,13,img,False,total) # Linha que eu adicionei
		#addDirPlayer(titulo,url2,4,img,total)  #ver comentarios que fiz na funçao addDirPlayer
		
	page = re.compile("<link rel='next' href='(.+?)' />").findall(codigo_fonte)
	for prox_pagina in page:
		addDir('Página Seguinte >>',prox_pagina,35,artfolder + 'proxpagina.png')
		break


def listar_series(url):
	pagina = str(int(url.split('|')[1])+1)
	url = url.split('|')[0]

	soup = BeautifulSoup(abrir_url(url))
	content = BeautifulSoup(soup.find("div", { "class" : "bic-miniaturas" }).prettify())
	series = content("div", { "class" : "bic-miniatura" })
	codigo_fonte = abrir_url(url)
	
	total = len(series)
	for serie in series:
		titulo = serie.a['title']
		titulo = titulo.replace('&#8211;',"-").replace('&#8217;',"'").replace('Assistir ','')
		try:
			addDir(titulo.encode('utf-8'),serie.a['href'],12,serie.img['src'],True,total)
		except:
			pass

	addDir('Página Seguinte >>','http://www.armagedomfilmes.biz/?cat=21&paged='+pagina+'|'+pagina,10,artfolder + 'next.png') 


def listar_temporadas(url):

	codigo_fonte = abrir_url(url)
	soup = BeautifulSoup(abrir_url(url))
	conteudo = BeautifulSoup(soup.find("ul", { "class" : "bp-series" }).prettify())
	temporadas = conteudo("li")
	
	total = len(temporadas)
	i=1
	print total
	
	while i <= total:
		temporada = conteudo("li", { "class" : "serie"+str(i)+"-code"})
		for temp in temporada:
			img = temp.img["src"]
			titulo = str(i)+" temporada"
			try:
				addDir(titulo,url,11,img,True,total)
			except:
				pass
		i=i+1
		
		

def listar_series_f2(name,url):

	n = name.replace(' temporada','')
	
	soup = BeautifulSoup(abrir_url(url))
	content = BeautifulSoup(soup.find("li", { "class" : "serie"+n+"-code" }).prettify())
	episodios = content.findAll("a")
	print episodios[0]
	
	a = [] # url titulo img
	for episodio in episodios:
		try:
			xml = BeautifulSoup(abrir_url(episodio["href"]+'/feed'))
			title = xml.title.string.encode('utf-8').replace('Comentários sobre: Assistir ','')
			try:
				if "html" in os.path.basename(episodio["href"]):
					temp = [episodio["href"],title]
					a.append(temp)
			except:
				pass
		except:
			pass

	total = len(a)
	for url2, titulo, in a:
		titulo = titulo.replace('&#8211;',"-").replace('&#8217;',"'").replace('Assistir ','')
		addDir(titulo,url2,13,'',False,total)

		
def obtem_url_google(url):

    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    dados = urllib2.unquote(soup('script')[4].prettify()).decode('unicode-escape')
    ttsurls = re.findall(r',\["ttsurl","(.*?)"\]\s', dados)[0]
    decoded = re.findall(r',\["url_encoded_fmt_stream_map","(.*?)"\]\s',dados)[0]
    qualidade = []
    url_video = []

    urls = [l for l in decoded.split('url=') if 'mp4' in l and l.startswith('https')]
    print urls
    url_video = []
    for u in urls:
	    itags = {5:'Baixa Qualidade, 240p, FLV, 400x240',
		     17:'Baixa Qualidade, 144p, 3GP, 0x0',
		     18:'Media Qualidade, 480p, MP4, 480x360',
		     59:'Media Qualidade, 360p, MP4, 480x360',
		     22:'Alta Qualidade, 720p, MP4, 1280x720',
		     34:'Media Qualidade, 360p, FLV, 640x360',
		     35:'Standard Definition, 480p, FLV, 854x480',
		     36:'Baixa Qualidade, 240p, 3GP, 0x0',
		     37:'Alta Qualidade, 1080p, MP4, 1920x1080',
		     38:'Original Definition, MP4, 4096x3072',
		     43:'Media Qualidade, 360p, WebM, 640x360',
		     44:'Standard Definition, 480p, WebM, 854x480',
		     45:'Alta Qualidade, 720p, WebM, 1280x720',
		     46:'Alta Qualidade, 1080p, WebM, 1280x720',
		     82:'Media Qualidade 3D, 360p, MP4, 640x360',
		     84:'Alta Qualidade 3D, 720p, MP4, 1280x720',
		     100:'Media Qualidade 3D, 360p, WebM, 640x360',
		     102:'Alta Qualidade 3D, 720p, WebM, 1280x720'}
	    q = 'quality='
	    i = 'itag='
	    quality = u[u.find(q) + len(q): u.find(',', u.find(q))]
	    itag = u[u.find(i) + len(i): u.find('&', u.find(i))]
	    #print "ORG qualitys: " + quality
	    #print "ORG itag: " + itag
	    try:
		    quality = itags[int(itag)]
	    except:
		    pass
	    qualidade.append(quality)
	    url_video.append(u[:-1])
    index = 0
    index = xbmcgui.Dialog().select('Qualidade do vídeo:', qualidade)
    if index == -1: return['-','-'] # Tive que alterar esta linha para corrigir um pequeno erro
    return [url_video[index]]

	
	
def obtem_videobis(url):
	codigo_fonte = abrir_url(url)
	
	try:
		url_video = re.findall(r'file: "(.*?)"',codigo_fonte)[1]
		return [url_video,"-"]
	except:
		return ["-","-"]
		

def obtem_url_dropvideo(url):
	codigo_fonte = abrir_url(url)
	try:
		soup = BeautifulSoup(codigo_fonte)
		lista = soup.findAll('script')
		js = str(lista[9]).replace('<script>',"").replace('</script>',"")
		sUnpacked = jsunpack.unpack(js)
		print sUnpacked
		url_video = re.findall(r'var vurl2="(.*?)";', sUnpacked)
		url_video = str(url_video).replace("['","").replace("']","")
		return [url_video,"-"]
	except:
		pass
		

def obtem_neodrive(url):
	codigo_fonte = abrir_url(url)
	
	try:
		url_video = re.findall(r'vurl.=."(.*?)";',codigo_fonte)[0]
		return [url_video,"-"]
	except:
		return ["-","-"]
		

def obtem_videopw(url):
	codigo_fonte = abrir_url(url)
	
	try:
		url_video = re.findall(r'var vurl2 = "(.*?)";',codigo_fonte)[0]
		return [url_video,"-"]
	except:
		return ["-","-"]
		
		
def obtem_vidig(url):
	codigo_fonte = abrir_url(url)
	try:
		soup = BeautifulSoup(codigo_fonte)
		lista = soup.findAll('script')
		js = str(lista[9]).replace('<script>',"").replace('</script>',"")
		sUnpacked = jsunpack.unpack(js)
		print sUnpacked
		url_video = re.findall(r'var vurl2="(.*?)";', sUnpacked)
		url_video = str(url_video).replace("['","").replace("']","")
		return [url_video,"-"]
	except:
		pass
		
		
def obtem_vidzi(url):
	codigo_fonte = abrir_url(url)
	try:
		soup = BeautifulSoup(codigo_fonte)
		lista = soup.findAll('script')
		js = str(lista[9]).replace('<script>',"").replace('</script>',"")
		sUnpacked = jsunpack.unpack(js)
		print sUnpacked
		url_video = re.findall(r'var vurl2="(.*?)";', sUnpacked)
		url_video = str(url_video).replace("['","").replace("']","")
		return [url_video,"-"]
	except:
		pass		
		

def obtem_shared2(url):
	codigo_fonte = abrir_url(url)
	
	try:
		url_video = re.findall(r'src:"(.*?)"',codigo_fonte)[0]
		return [url_video,"-"]
	except:
		return ["-","-"]
		
	
def obtem_cloudzilla(url):
	codigo_fonte = abrir_url(url)
	
	try:
		url_video = re.findall(r'vurl.=."(.*?)";',codigo_fonte)[0]
		return [url_video,"-"]
	except:
		return ["-","-"]
		

def player(name,url,iconimage):
	
	try:

		dropvideo = r'src="(.*?dropvideo.*?/embed.*?)"'
		dropmega = r'src=".*?drop.*?id=(.*?)"'
		neodrive = r'src="(.*?neodrive.*?/embed.*?)"'
		neomega = r'src=".*?neodrive.*?id=(.*?)"'
		videobis = r'SRC="(.*?videobis.*?/embed.*?)"'
		vidig = r'src=".*?vidigvideo.*?/(.*?)"'
		vidzi = r'src=".*?vidzi.*?/(.*?)"'		
		videopw = r'src=".*?videopw.*?id=(.*?)"'
		shared2 = r'src=".*?shared2.*?/embed/(.*?)"'
		cloudzilla = r'cloudzilla.php.id=(.*?)"'
		cloudzilla_f = r'http://www.cloudzilla.to/share/file/(.*?)"'
		
		mensagemprogresso = xbmcgui.DialogProgress()
		mensagemprogresso.create('TRABALHANDO', 'Abrindo stream','Por favor aguarde...')
		mensagemprogresso.update(33)
		links = []
		hosts = []
		matriz = []
		codigo_fonte = abrir_url(url)
		
		try:
			links.append(re.findall(dropvideo, codigo_fonte)[0])
			hosts.append('[B][COLOR green]Dropvideo[/COLOR][/B]')
		except:
			pass
			
		try:
			links.append('http://www.dropvideo.com/embed/'+re.findall(dropmega, codigo_fonte)[0])
			hosts.append('[B][COLOR green]Dropvideo[/COLOR][/B]')
		except:
			pass
		
		try:
			links.append('http://videopw.com/e/'+re.findall(videopw, codigo_fonte)[0])
			hosts.append('[B][COLOR green]Videopw[/COLOR][/B]')
		except:
			pass

		try:
			links.append('http://vidigvideo.com/'+re.findall(vidig, codigo_fonte)[0])
			hosts.append('[B][COLOR green]Vidig[/COLOR][/B]')
		except:
			pass

		try:
			links.append('http://vidzi.tv/'+re.findall(vidzi, codigo_fonte)[0])
			hosts.append('[B][COLOR green]Vidzi[/COLOR][/B]')
		except:
			pass
			
			
		try:
			links.append('http://www.shared2.net/embed/'+re.findall(shared2, codigo_fonte)[0])
			hosts.append('shared2')
		except:
			pass						
			
		try:
			links.append(re.findall(videobis, codigo_fonte)[0])
			hosts.append('[B][COLOR green]Videobis[/COLOR][/B]')
		except:
			pass
		
		try:
			links.append(re.findall(neodrive, codigo_fonte)[0])
			hosts.append('[B][COLOR green]Neodrive[/COLOR][/B]')
		except:
			pass
		
		try:
			links.append('http://neodrive.co/embed/'+re.findall(neomega, codigo_fonte)[0])
			hosts.append('[B][COLOR green]Neodrive[/COLOR][/B]')
		except:
			pass	
			
		try:
			links.append('http://www.cloudzilla.to/embed/'+re.findall(cloudzilla,codigo_fonte)[0])
			hosts.append('CloudZilla')
		except:
			pass
		
		try:
			links.append('http://www.cloudzilla.to/embed/'+re.findall(cloudzilla_t,codigo_fonte)[0])
			hosts.append('CloudZilla(Legendado)')
		except:
			pass
			
		if not hosts:
			return
		
		index = xbmcgui.Dialog().select('Selecione um dos hosts suportados :', hosts)
		
		if index == -1:
			return
		
		url_video = links[index]
		mensagemprogresso.update(66)
		
		print 'Player url: %s' % url_video
		if 'dropvideo.com/embed' in url_video:
			matriz = obtem_url_dropvideo(url_video)
		elif 'cloudzilla' in url_video:
			matriz = obtem_cloudzilla(url_video)
		elif 'videobis' in url_video:
			matriz = obtem_videobis(url_video)
		elif 'neodrive' in url_video:
			matriz = obtem_neodrive(url_video)
		elif 'videopw' in url_video:
			matriz = obtem_videopw(url_video)
		elif 'vidig' in url_video:
			matriz = obtem_vidig(url_video)
		elif 'vidzi' in url_video:
			matriz = obtem_vidzi(url_video)			
		elif 'shared2' in url_video:
			matriz = obtem_shared2(url_video)						
		else:
			print "Falha: " + str(url_video)
		print matriz
		url = matriz[0]
		print url
		if url=='-': return
		legendas = matriz[1]
		print "Url do gdrive: " + str(url_video)
		print "Legendas: " + str(legendas)
		
		mensagemprogresso.update(100)
		mensagemprogresso.close()
		
		listitem = xbmcgui.ListItem() # name, iconImage="DefaultVideo.png", thumbnailImage="DefaultVideo.png"
		listitem.setPath(url)
		listitem.setProperty('mimetype','video/mp4')
		listitem.setProperty('IsPlayable', 'true')
		#try:
		xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
		xbmcPlayer.play(url)
		if legendas != '-':
			if 'timedtext' in legendas:
				#legenda = xmltosrt.convert(legendas)
				#try:
					import os.path
					sfile = os.path.join(xbmc.translatePath("special://temp"),'sub.srt')
					sfile_xml = os.path.join(xbmc.translatePath("special://temp"),'sub.xml')#timedtext
					sub_file_xml = open(sfile_xml,'w')
					sub_file_xml.write(urllib2.urlopen(legendas).read())
					sub_file_xml.close()
					print "Sfile.srt : " + sfile_xml
					xmltosrt.main(sfile_xml)
					xbmcPlayer.setSubtitles(sfile)
				#except:
				#	pass
			else:
				xbmcPlayer.setSubtitles(legendas)
		#except:
		#	dialog = xbmcgui.Dialog()
		#	dialog.ok(" Erro:", " Impossível abrir vídeo! ")
		#	pass
	except:
		print "erro ao abrir o video"
		print url_video
		pass		



def pesquisa_serie_sd():
	keyb = xbmc.Keyboard('', 'faca a procura') #Chama o keyboard do XBMC com a frase indicada
	keyb.doModal() #Espera ate que seja confirmada uma determinada string
	if (keyb.isConfirmed()): #Se a entrada estiver confirmada (isto e, se carregar no OK)
		search = keyb.getText() #Variavel search fica definida com o conteudo do formulario
		parametro_pesquisa=urllib.quote(search) #parametro_pesquisa faz o quote da expressao search, isto Ã©, escapa os parametros necessarios para ser incorporado num endereÃ§o url
		url = 'http://www.armagedomfilmes.biz/?s=%s&s-btn=buscar' % str(parametro_pesquisa) #nova definicao de url. str forÃ§a o parametro de pesquisa a ser uma string
		print url
		soup = BeautifulSoup(abrir_url(url))
		content = BeautifulSoup(soup.find("div", { "class" : "bic-miniaturas" }).prettify())
		series = content("div", { "class" : "bic-miniatura" })
		codigo_fonte = abrir_url(url)

		total = len(series)
		for serie in series:
			titulo = serie.a['title']
			titulo = titulo.replace('&#8211;',"-").replace('&#8217;',"'").replace('Assistir ','')
			try:
				addDir(titulo.encode('utf-8'),serie.a['href'],12,serie.img['src'],True,total)
			except:
				pass
				
				
def pesquisa_filme_armagedom():
	keyb = xbmc.Keyboard('', 'faca a procura') #Chama o keyboard do XBMC com a frase indicada
	keyb.doModal() #Espera ate que seja confirmada uma determinada string
	if (keyb.isConfirmed()): #Se a entrada estiver confirmada (isto e, se carregar no OK)
		search = keyb.getText() #Variavel search fica definida com o conteudo do formulario
		parametro_pesquisa=urllib.quote(search) #parametro_pesquisa faz o quote da expressao search, isto Ã©, escapa os parametros necessarios para ser incorporado num endereÃ§o url
		url = 'http://www.armagedomfilmes.biz/?s=%s&s-btn=buscar' % str(parametro_pesquisa) #nova definicao de url. str forÃ§a o parametro de pesquisa a ser uma string
		print url
		soup = BeautifulSoup(abrir_url(url))
		content = BeautifulSoup(soup.find("div", { "class" : "bic-miniaturas" }).prettify())
		filmes = content("div", { "class" : "bic-miniatura" })
		print filmes[0]
		for filme in filmes:
			titulo = filme.a["title"].replace('Assistir ','')
			url = filme.a["href"]
			img = filme.img["src"]
			addDir(titulo.encode('utf8'),url,13,img,False,len(filmes))				


def pesquisa_serie_hd():
	keyb = xbmc.Keyboard('', 'O que está procurando?...')
	keyb.doModal()
	if (keyb.isConfirmed()):
		search = keyb.getText()
		parametro_pesquisa=urllib.quote(search)
		url = 'http://assistirserieshd.com/busca.php?busca=' + str(parametro_pesquisa)
		listar_series2(url)
		
def pesquisa_cinefilmes(url):
	keyb = xbmc.Keyboard('', 'faca a procura') #Chama o keyboard do XBMC com a frase indicada
	keyb.doModal() #Espera ate que seja confirmada uma determinada string
	if (keyb.isConfirmed()): #Se a entrada estiver confirmada (isto e, se carregar no OK)
		search = keyb.getText() #Variavel search fica definida com o conteudo do formulario
		parametro_pesquisa=urllib.quote(search) #parametro_pesquisa faz o quote da expressao search, isto Ã©, escapa os parametros necessarios para ser incorporado num endereÃ§o url
		url = 'http://www.cinefilmeshd.com/?s=' + str(parametro_pesquisa) #nova definicao de url. str forÃ§a o parametro de pesquisa a ser uma string
		filmes_cinefilmeshd(url) #chama a funÃ§Ã£o listar_videos com o url definido em cima


def Buscar_Tv_Gravada():
	keyb = xbmc.Keyboard('', 'Digite sua busca aqui!')
	keyb.doModal()
	if (keyb.isConfirmed()):
		search = keyb.getText()
		parametro_pesquisa=urllib.quote(search)
		url = 'https://assistirnovelas.tv/buscar.php?busca=' + str(parametro_pesquisa)
		Listar_novelas(url)
		
		
	  
	  
		###################################################################################	  
	  
	  
def addDirM(name,url,mode,iconimage,total=0,pasta=True):
      u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
      liz=xbmcgui.ListItem(name,iconImage="DefaultFolder.png", thumbnailImage=iconimage)
      liz.setInfo( type="Video", infoLabels={ "Title": name} )
      liz.setProperty('fanart_image', "%s/fanart.jpg"%selfAddon.getAddonInfo("path"))
      return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=pasta,totalItems=total)	  
	  
def abrir_url(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
	return link	

def real_url(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link=response.geturl()
	response.close()
	return link
	
def addLink(name,url,iconimage):
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', fanart)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
	return ok

def addDir(name,url,mode,iconimage,pasta=True,total=1,plot=''):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', fanart)
	liz.setInfo( type="video", infoLabels={ "title": name, "plot": plot } )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=pasta,totalItems=total)
	return ok

def addDirC(name,url,mode,iconimage,pasta=True,total=1):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', fanart)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=pasta,totalItems=total)
	return ok

def addDirD(name, url, mode, iconimage, total=0, pasta=True, plot='', fanart=''):
    u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage)
    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={"Title": name, "Plot": plot})
    contextMenuItems = []
    contextMenuItems.append(('Movie Information', 'XBMC.Action(Info)'))
    liz.addContextMenuItems(contextMenuItems, replaceItems=True)
    liz.setProperty('fanart_image', fanart)
    return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=pasta, totalItems=total)	
	
	
############################################################################################################
#                                               GET PARAMS                                                 #
############################################################################################################

              
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param

      
params=get_params()
url=None
name=None
mode=None
iconimage=None


try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass

try:        
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass


print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "Iconimage: "+str(iconimage)


###############################################################################################################
#                                                   MODOS                                                     #
###############################################################################################################


if mode==None or url==None or len(url)<1:
    print ""
    menus()

elif mode==2:
	print ""
	categorias()	
	
elif mode==3: 
	print ""
	listar_canais(url)
	
elif mode==4: 
	print ""
        temporarios()
	
elif mode==5:
	print ""
	series_qualidade()
	
elif mode==6:
	print ""
	tv_ao_vivo()

elif mode==7:
	print ""
	listar_categorias()
	
elif mode==8:
	print ""
	Listar_programacao()

elif mode==9:
	print ""
	Listar_episodios(url)	
	
elif mode==10:
	listar_series(url)
	
elif mode==11:
	print ""
	listar_series_f2(name,url)

elif mode==12:
	print "Mode 12"
	listar_temporadas(url)

elif mode==13:
	print ""
	player(name,url,iconimage)

elif mode==14:
	print ""
	pesquisa_serie_sd()

elif mode==15:
	print ""
	Animacao()

elif mode==16:
    Listar_categorias_series()

elif mode==17:
    print ""
    listar_series2(url)

elif mode==18:
    print ""
    listar_episodios_series(url)

elif mode==19:
    Resolve_episodio_serie(url)

elif mode==20:
    Cine_hd(url)
	
elif mode==21:
    categorias_cine(url)

elif mode==22:
    print ""
    listar_series3(url)

elif mode==23:
    Listar_categorias_series_letra()

elif mode==24:
    filmes_hd_sd()

elif mode==25:
    Animes()

elif mode==26:
	print "Mode: 26 - Listar categorias2"
	Listar_categorias2(url)
	
elif mode==27:
	print "Mode: 27 - Listar episodios2 "
	Listar_episodios2(url)

elif mode==28:
	print "Mode: 28 - Resolve episodio"
	Resolve_episodio(url)

elif mode==29:
	print 'Mode: 29 - Pesquisa'
	Pesquisa()

elif mode==30:
	print ""
	pesquisa_serie_hd()

elif mode==31:
	print ""
	Armagedom()

elif mode==32:
	print ""
	Armagedom_categorias()

elif mode==33:
	print ""
	filmes_armagedom(url)

elif mode==34:
	print ""
	pesquisa_filme_armagedom()

elif mode==35:
	print ""
	filmes_cinefilmeshd(url)
	
elif mode==36:
	print ""
	pesquisa_cinefilmes(url)

elif mode==37:
	print ""
	series_qualidade_hd()

elif mode==38:
	print ""
	series_qualidade_sd()

elif mode==42:
	print ""
	Listar_categorias_novelas(url=novelas_base,cat=url)

elif mode==43:
	print ""
	Listar_episodios_novelas(url)

elif mode==44:
	print ""
	Resolve_episodio_novelas(url)

elif mode==45:
	print ""
	Addons()

elif mode==46:
	print ""
	Tv_Gravada()

elif mode==49:
	print ""
	series_qualidade_hd()

elif mode==50:
	print ""
	series_qualidade_sd()

elif mode==51:
	print ""
	Programas_tv()

elif mode==52:
	print ""
	Episodios_novelas(url)	
	
elif mode==53:
	print ""
	Listar_categorias_novelas2(url=novelas_base,cat=url)	

	

	
	

	


	
xbmcplugin.endOfDirectory(int(sys.argv[1]))
