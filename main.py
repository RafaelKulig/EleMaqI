from dataclasses import dataclass
import re

@dataclass
class Eixo():
    comprimento:float=None
    apoio:dict=None
    
    def info(self):
        print(f"Distância: {self.comprimento}")
        print(f"Apoios:",end="")
        print([i for i in self.apoio.items()])

@dataclass
class Momento():
    distancia:float=None
    intensidade:list=None
    plano:str=None
    
    def info(self):
        print(f"Distância: {self.distancia}")
        print(f"Intensidade: {self.intensidade}")
        print(f"Plano: {self.plano}")

@dataclass
class Força:
    distancia:float = None
    intensidade:float = None
    angulo:list = None
    plano:str = None

    def info(self):
        print(f"Distância: {self.distancia}")
        print(f"Módulo: {self.intensidade}")
        print(f"Angulo: {self.angulo}")
        print(f"Plano: {self.plano}")
    
@dataclass
class Apoio:
    distancia:float=None
    eixo: str=None
    tipo: str=None
    reacao: dict={}

    def info(self):
        print(f"Distância: {self.distancia}")
        print(f"Eixo: {self.eixo}")
        print(f"Tipo: {self.tipo}")


def _ValidadeType(d_type:object):
    types={int:'número inteiro',
           float: 'número real',
           str:'texto'}
    while True:    
        data=input()
        try:
            data=d_type(data)
            return data
        except:
            print(f"Insira um {types[d_type]}\n>>>",end="")

def ListarForças():
    dictForças={}
    

    print("Insira a quantidade de forças aplicadas\n>>>",end="")
    qtd_Forças=_ValidadeType(int)

    for i in range(qtd_Forças):
        print("Insira a distância da força ao ponto inicial\n>>>",end="")
        distancia=_ValidadeType(float)
        print("Insira o valor absoluto da força\n>>>",end="")
        intensidade=_ValidadeType(float)
        print(f"Insira o plano da força {i+1}\n\t\'xz\' ou \'zx\' : Radial\n\t\'xy\' ou \'yx\' : Superior \n\t\'zy\' ou \'yz\' : Axial\n>>>",end="")
        while True:
            plano=input()
            match plano:
                case 'xy'|'yx':
                    print("Insira o ângulo da força aplicada em graus em relação a 'x'\n>>>",end="")
                    angulo=[a:=_ValidadeType(float),90-a,0]
                    break
                case 'zx'|'xz':
                    print("Insira o ângulo da força aplicada em graus em relação a 'x'\n>>>",end="")
                    angulo=[a:=_ValidadeType(float),0,90-a]
                    break
                case 'zy'|'yz':
                    print("Insira o ângulo da força aplicada em graus em relação a 'z'\n>>>",end="")
                    angulo=[0,90-a,a:=_ValidadeType(float)]
                    break
                case 'xyz'|'xzy'|'yxz'|'yzx'|'zyx'|'zxy':
                    print("Insira o ângulo da força aplicada em graus em relação a 'x'\n>>>",end="")
                    angulo[0]=_ValidadeType(float)
                    print("Insira o ângulo da força aplicada em graus em relação a 'y'\n>>>",end="")
                    angulo[1]=_ValidadeType(float)
                    print("Insira o ângulo da força aplicada em graus em relação a 'z'\n>>>",end="")
                    angulo[2]=_ValidadeType(float)
                    break
                case _:
                    print('Plano não identificado. Por favor escolha o(s) plano(s) com base em \'xyz\'')
        
        dictForças.update({str(i):Força(distancia,intensidade,angulo,plano)})

def DimEixo():
    objEixo=Eixo()  
    print("Insira o comprimento do eixo\n>>>",end="")
    objEixo.comprimento=_ValidadeType(float)
    print("Insira a quantidade de apoios\n>>>",end="")
    objEixo.apoio={}
    for i in range(_ValidadeType(int)):
        print(f"Insira a distância do apoio {i+1}\n>>>",end="")
        objEixo.apoio[str(i)]=[_ValidadeType(float)]
        print("Insira o tipo de apoio\n\tApoio: 1\n\tMancal: 2\n\tEngaste: 3\n>>>",end="")
        objEixo.apoio[str(i)].append(_ValidadeType(int))

def DimMomentos():
  
    print("Insira a quantidade de momentos aplicados\n>>>",end="")
    qtd_Momentos=_ValidadeType(int)
    dictMomentos={}

    for i in range(qtd_Momentos):
        print("Insira a distância do momento\n>>>",end="")
        distancia=_ValidadeType(float)
        print("Insira a intensidade do momento (Negativo para horário e positivo para anti-horário)\n>>>",end="")
        intensidade=_ValidadeType(float)
        print("Insira o eixo do momento\n>>>",end="")
        while True:
            plano=input()
            match plano:
                case 'z':
                    intensidade=[0,0,intensidade]
                    break
                case 'y':
                    intensidade=[0,intensidade,0]
                    break
                case 'x':
                    intensidade=[intensidade,0,0]
                    break
                case _:
                    print('Plano não identificado. Por favor escolha o(s) plano(s) com base em \'xyz\'')
    dictMomentos.update({str(i):Momento(distancia,intensidade,plano)})

def Apoios():
    print("Insira a quantidade de apoios\n>>>",end="")
    qtd_Apoios=_ValidadeType(int)
    dictApoios={}

    for i in range(qtd_Apoios):
        print(f"Insira a distância do apoio {i+1}\n>>>",end="")
        Distancia_apoio=_ValidadeType(float)
        print(f"Insira o tipo do apoio {i+1}\n\t1-Móvel\n\t2-Fixo\n\t3-Engaste>>>",end="")
        while True:
            match apoio:=input():
                case 1|2|3:
                    break
                case _:
                    print("Apoio não identificado, tente novamente\n>>>")
        print(f"Insira o eixo em que o apoio {i+1} está\n>>>",end="")
        while True:
            match eixo:=input():
                case 'x'|'y'|'z':
                    break
                case _:
                    print("Eixo inválido, tente novamente\n>>>")
        
    dictApoios.update({str(i):Apoio(Distancia_apoio,eixo,apoio)})
