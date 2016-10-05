# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 15:23:59 2016

@author: isidoro
"""
class ConfParameters:
    
    def __init__ (self, dictionary):
        self.cabecera_ranking_individual = dictionary.pop("cabecera_ranking_individual")
        self.cabecera_ranking_clubes = dictionary.pop("cabecera_ranking_clubes")
        self.cabecera_grupos_cerrados = dictionary.pop("cabecera_grupos_cerrados")
        self.carreras = dictionary.pop("carreras")
        self.divisiones = dictionary.pop("divisiones")
        self.division_honor = dictionary.pop("division_honor")
        self.tipos_organizador = dictionary.pop("tipos_organizador")
        self.licencias = dictionary.pop("licencias")
        self.tipos_categoria_ranking_clubes = dictionary.pop("tipos_categoria_ranking_clubes")
        self.fecha_actual = dictionary.pop("fecha_actual")[0]
        self.temporada_actual = dictionary.pop("temporada_actual")[0]
        self.puntos_penalizacion = float(dictionary.pop("puntos_penalizacion")[0])
        self.puntos_ganador_nac = float(dictionary.pop("puntos_ganador_nac")[0])
        self.puntos_ganador_inter = float(dictionary.pop("puntos_ganador_inter")[0])
        self.puntos_ganador_inter_aux = float(dictionary.pop("puntos_ganador_inter_aux")[0])
        self.puntos_fuera_categoria = float(dictionary.pop("puntos_fuera_categoria")[0])
        self.num_carreras_total = int(dictionary.pop("num_carreras_total")[0])
        self.num_carreras_total_elite = int(dictionary.pop("num_carreras_total_elite")[0])
        self.num_carreras_media = int(dictionary.pop("num_carreras_media")[0])
        self.num_carreras_media_elite = int(dictionary.pop("num_carreras_media_elite")[0])
        self.num_carreras_organizador = int(dictionary.pop("num_carreras_organizador")[0])
        self.coeficiente_clubes = float(dictionary.pop("coeficiente_clubes")[0])
        self.num_trofeos = int(dictionary.pop("num_trofeos")[0])
        self.minimo_elite = float(dictionary.pop("minimo_elite")[0])
        self.minimo_21A = float(dictionary.pop("minimo_21A")[0])
        self.minimo_21Aaux = float(dictionary.pop("minimo_21Aaux")[0])
        self.minimo_21B = float(dictionary.pop("minimo_21B")[0])
        self.minimo_20 = float(dictionary.pop("minimo_20")[0])
        self.minimo_20aux = float(dictionary.pop("minimo_20aux")[0])
        self.coef_elite = float(dictionary.pop("coef_elite")[0])
        self.coef_20a = float(dictionary.pop("coef_20a")[0])
        self.coef_35a = float(dictionary.pop("coef_35a")[0])
        self.coef_18a = float(dictionary.pop("coef_18a")[0])
        self.coef_21a = float(dictionary.pop("coef_21a")[0])
        self.coef_40 = float(dictionary.pop("coef_40")[0])
        self.coef_16 = float(dictionary.pop("coef_16")[0])
        self.coef_45 = float(dictionary.pop("coef_45")[0])
        self.coef_50 = float(dictionary.pop("coef_50")[0])
        self.coef_12 = float(dictionary.pop("coef_12")[0])
        self.coef_14 = float(dictionary.pop("coef_14")[0])
        self.coef_21b = float(dictionary.pop("coef_21b")[0])
        self.coef_55 = float(dictionary.pop("coef_55")[0])
        self.coef_60 = float(dictionary.pop("coef_60")[0])
        self.coef_65 = float(dictionary.pop("coef_65")[0])
        self.coef_70 = float(dictionary.pop("coef_70")[0])
        self.coef_1820b = float(dictionary.pop("coef_1820b")[0])
        self.coef_35b = float(dictionary.pop("coef_35b")[0])
        self.num_max_corredores = dictionary.pop("num_max_corredores")
        self.opcion_calculo_m1 = dictionary.pop("opcion_calculo_m1")
        self.opcion_ranking_individual = dictionary.pop("opcion_ranking_individual")
        #extra parameters in case of need
        self.parametro1 = dictionary.pop("parametro1")
        self.parametro2 = dictionary.pop("parametro2")
        self.parametro3 = dictionary.pop("parametro3")