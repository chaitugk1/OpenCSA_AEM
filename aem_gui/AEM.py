# -*- coding: utf-8 -*-
import numpy

class AEMmodel:
    def __init__(self):
        self.ElementSize=1.0
        self.ElementCount=0
        self.BoundaryIndex=0
        self.ElementIndex=0
        self.SteelIndex=0
        self.Elements={}
        self.Boundary={}
        self.Load={}
        self.Steel={}
        self.ElementBlocks={}
        self.Material={}

        self.Boundary['fix']=[]

    def add_element_block(self,init_point,div):
        ds=self.ElementSize
        [xi,yi,zi]=map(float,init_point)
        x=[xi+ds*i for i in range(div[0]+1)]*((div[1]+1)*(div[2]+1))
        y=[]
        z=[]
        for i in range(div[1]+1):
            y=y+[yi+ds*i for j in range(div[0]+1)]
        y=y*(div[1]+1)
        for i in range(div[2]+1):
            z=z+[zi+i*ds]*((div[0]+1)*(div[1]+1))
        yadd=div[0]+1
        zadd=(div[0]+1)*(div[1]+1)
        ne=0
        ecount=self.ElementIndex
        for ze in range(div[2]):
            for ye in range(div[1]):
                for xe in range(div[0]):
                    ecount+=1
                    ne=xe+(ye*(div[0]+1))+(ze*((div[0]+1)*(div[1]+1)))
                    edge_nodes=(ne,ne+1,ne+yadd+1,ne+yadd,ne+zadd,ne+1+zadd,ne+yadd+1+zadd,ne+yadd+zadd)
                    c=[]
                    for n in edge_nodes:c.append([x[n],y[n],z[n]])
                    centre=[0.5*(x[ne]+x[ne+yadd+1]),0.5*(y[ne]+y[ne+yadd+1]),
                            0.5*(z[ne]+z[ne+yadd+1])]
                    self.Elements[ecount]={'edge_coord':c,'material':0,'thickness':1.0,'centre':centre,
                                            'id':ecount,'dof':'free',
                                            'displacement':[0.0,0.0,0.0],'rotation':[0.0,0.0,0.0]}
        self.ElementIndex=self.ElementIndex+div[0]*div[1]*div[2]

    def add_boundary(self,rect,bdtype):
        for e in self.Elements:
            xc,yc,zc=self.Elements[e]['centre']
            if (((xc>rect[0] and xc<rect[3]) and (yc>rect[1] and yc<rect[4])) or
                ((xc<rect[0] and xc>rect[3]) and (yc<rect[1] and yc>rect[4])) or 
                ((xc<rect[0] and xc>rect[3]) and (yc>rect[1] and yc<rect[4])) or 
                ((xc>rect[0] and xc<rect[3]) and (yc<rect[1] and yc>rect[4]))):
                self.Boundary[bdtype].append(e)     
                self.Elements[e]['dof']=bdtype  
                self.BoundaryIndex+=1

    def add_steel(self,coord,Ey,fy,d):
        self.Steel[self.SteelIndex]={'coord':coord,'Ey':Ey,'fy':fy,
                                'area':3.14159*0.25*d*d,
                                'dia':d}
        self.SteelIndex+=1