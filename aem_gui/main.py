# -*- coding: utf-8 -*-
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from aemWindow import Ui_MainWindow,Ui_Dialog_AddBlock,Ui_Dialog_AddSteel
from AEM import AEMmodel
import sys
import vtk
import numpy as np
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import logging

log = logging.getLogger(__name__)

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self,win_w,win_h):
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.setWindowTitle("AEM GUI")
        self.setWindowIcon(QIcon('PreStruct.ico'))
        self.BlockDlg=AddBlockDlg()
        self.SteelDlg=AddSteelDlg()
        self.AEMmodel=AEMmodel()

        self.DisplayMode='Simple'

        #fix window dimensions
        self.win_w=win_w
        self.win_h=win_h
        self.setFixedSize(int(0.9*win_w),int(0.9*win_h))
        self.verticalLayoutWidget.setGeometry(QRect(int(0.11*win_w), 10, int(0.8*win_w), int(0.9*win_h)))
        self.menubar.setGeometry(QRect(0, 0, 700, 22))
        self.splitter.setGeometry(QRect(11, 10, int(0.1*win_w), int(0.25*win_h)))

        # assign push button 
        self.pushButton_block.pressed.connect(self.OpenAddElementBlockDlg)
        self.pushButton_bc.pressed.connect(self.OpenAddBoundaryDlg)
        self.pushButton_steel.pressed.connect(self.OpenAddSteelDlg)

        #checkbox
        self.checkBox_eleno.stateChanged.connect(lambda:self.btnstate(self.checkBox_eleno))
        self.checkBox_steel.stateChanged.connect(lambda:self.btnstate(self.checkBox_steel))
        self.checkBox_bc.stateChanged.connect(lambda:self.btnstate(self.checkBox_bc))
        self.checkBox_load.stateChanged.connect(lambda:self.btnstate(self.checkBox_load))

        self.renderer = vtk.vtkRenderer()
        self.frame = QFrame()
        self.renWinInteract = QVTKRenderWindowInteractor(self.frame)  
        self.verticalLayout.addWidget(self.renWinInteract)    
        self.renWin=self.renWinInteract.GetRenderWindow()
        self.renWin.SetSize(200,100)
        self.renWin.AddRenderer(self.renderer)   

        interactor = vtk.vtkInteractorStyleImage()
        self.renWinInteract.SetInteractorStyle(interactor)   
        
        self.renWinInteract.Initialize()

    def OpenAddElementBlockDlg(self):
        w=self.win_w
        h=self.win_h
        self.BlockDlg.resize(int(0.4*w),int(0.2*h))
        self.BlockDlg.ui.formLayoutWidget.setGeometry(QRect(20, 20,int(0.4*w), int(0.2*h)))
        try:
            self.BlockDlg.ui.pushButton.clicked.disconnect()
        except:
            pass
        self.BlockDlg.ui.pushButton.clicked.connect(self.AddElementBlock)
        # self.BlockDlg.ui.pushButton.clicked.disconnect()
        self.BlockDlg.show()
      
    def AddElementBlock(self): 
        x0=float(self.BlockDlg.ui.Xcoord.text())
        y0=float(self.BlockDlg.ui.Ycoord.text())
        nx=int(self.BlockDlg.ui.nBlockX.text())
        ny=int(self.BlockDlg.ui.nBlockY.text())
        #add points
        self.AEMmodel.add_element_block([x0,y0,0.0],[nx,ny,1])
        self.RenderAEMmodel()
        self.renderer.ResetCamera()
        self.BlockDlg.close()

    def OpenAddSteelDlg(self):
        w=self.win_w
        h=self.win_h
        self.SteelDlg.resize(int(0.4*w),int(0.2*h))
        self.SteelDlg.ui.formLayoutWidget.setGeometry(QRect(20, 20,int(0.4*w), int(0.2*h)))
        self.SteelDlg.ui.pushButton.clicked.connect(lambda: self.AddSteel(self.SteelDlg))
        self.SteelDlg.exec()

    def AddSteel(self,dlg): 
        x0=float(self.SteelDlg.ui.InitXcoord.text())
        y0=float(self.SteelDlg.ui.InitYcoord.text())
        xf=float(self.SteelDlg.ui.FinXcoord.text())
        yf=float(self.SteelDlg.ui.FinYcoord.text())
        Ey=float(self.SteelDlg.ui.Young.text())
        fy=float(self.SteelDlg.ui.Yield.text())
        d=float(self.SteelDlg.ui.Dia.text())
        #add points
        self.AEMmodel.add_steel([x0,y0,xf,yf],Ey,fy,d)
        if 'Steel' not in self.DisplayMode:
            self.DisplayMode=self.DisplayMode+'Steel'
        self.RenderAEMmodel()
        self.renderer.ResetCamera()
        dlg.close()

    def RenderAEMmodel(self):
        self.renWin.RemoveRenderer(self.renderer)
        self.renderer = vtk.vtkRenderer()
        
        points_free = vtk.vtkPoints()
        points_fix = vtk.vtkPoints()
        uGrid_free = vtk.vtkUnstructuredGrid()
        uGrid_fix = vtk.vtkUnstructuredGrid()
        for e in self.AEMmodel.Elements:
            for crd in self.AEMmodel.Elements[e]['edge_coord']:
                if crd[2]==0.0:
                    if self.AEMmodel.Elements[e]['dof']=='free':
                        points_free.InsertNextPoint([crd[0],crd[1],0.0])
                    else:
                        points_fix.InsertNextPoint([crd[0],crd[1],0.0])
                else:
                    if self.AEMmodel.Elements[e]['dof']=='free':
                        points_free.InsertNextPoint([crd[0],crd[1],-self.AEMmodel.Elements[e]['thickness']])
                    else:
                        points_fix.InsertNextPoint([crd[0],crd[1],-self.AEMmodel.Elements[e]['thickness']])
            uGrid_free.SetPoints(points_free)
            uGrid_fix.SetPoints(points_fix)
            
        nn=0
        for e in self.AEMmodel.Elements:
            if self.AEMmodel.Elements[e]['dof']=='fix':continue
            hexa=vtk.vtkHexahedron ()
            for (i,n) in enumerate(range(nn,nn+8)):hexa.GetPointIds().SetId(i,n)
            nn+=8
            uGrid_free.InsertNextCell(hexa.GetCellType(), hexa.GetPointIds())
        nn=0
        for e in self.AEMmodel.Elements:
            if self.AEMmodel.Elements[e]['dof']=='free':continue
            hexa=vtk.vtkHexahedron ()
            for (i,n) in enumerate(range(nn,nn+8)):hexa.GetPointIds().SetId(i,n)
            nn+=8
            uGrid_fix.InsertNextCell(hexa.GetCellType(), hexa.GetPointIds())


        # create actor and mapper
        actor_fix = vtk.vtkActor()
        actor_free= vtk.vtkActor()
        mapper_fix = vtk.vtkDataSetMapper()
        mapper_free = vtk.vtkDataSetMapper()
        mapper_fix.SetInputData(uGrid_fix)
        mapper_free.SetInputData(uGrid_free)
        color=vtk.vtkNamedColors()


        actor_fix.SetMapper(mapper_fix)
        actor_fix.GetProperty().EdgeVisibilityOn()
        if 'Boundary' in self.DisplayMode:
            actor_fix.GetProperty().SetColor(color.GetColor3ub('Blue'))
        else:
            actor_fix.GetProperty().SetColor(color.GetColor3ub('Ivory'))

        actor_free.SetMapper(mapper_free)
        actor_free.GetProperty().EdgeVisibilityOn()
        actor_free.GetProperty().SetColor(color.GetColor3ub('Ivory'))
        self.renderer.AddActor(actor_fix)
        self.renderer.AddActor(actor_free)   


        #add steel actor
        if 'Steel' in self.DisplayMode:
            pts = vtk.vtkPoints()          
            lines = vtk.vtkCellArray()
            linesPolyData = vtk.vtkPolyData()
            for s in self.AEMmodel.Steel:
                [x0,y0,xf,yf]=self.AEMmodel.Steel[s]['coord']
                pts.InsertNextPoint([x0,y0,0.01])
                pts.InsertNextPoint([xf,yf,0.01])
            ni=0
            for s in self.AEMmodel.Steel:
                sline = vtk.vtkLine()
                sline.GetPointIds().SetId(0,ni)
                sline.GetPointIds().SetId(1,ni+1) 
                ni+=2
                lines.InsertNextCell(sline)
            
            linesPolyData.SetPoints(pts)
            linesPolyData.SetLines(lines)
            mapper_steel = vtk.vtkPolyDataMapper()
            mapper_steel.SetInputData(linesPolyData)
            actor_steel = vtk.vtkActor()
            actor_steel.SetMapper(mapper_steel)
            actor_steel.GetProperty().SetColor(color.GetColor3ub('Red'))
            self.renderer.AddActor(actor_steel)
        
        #add steel actor
        if 'ElementNo' in self.DisplayMode:
                esize=self.AEMmodel.ElementSize
                for e in self.AEMmodel.Elements:
                    eid='{}'.format(self.AEMmodel.Elements[e]['id'])
                    c=self.AEMmodel.Elements[e]['centre']
                    XText = vtk.vtkVectorText()
                    XText.SetText(eid)
                    XTextMapper = vtk.vtkPolyDataMapper()
                    XTextMapper.SetInputConnection(XText.GetOutputPort())
                    XActor = vtk.vtkFollower()
                    XActor.SetMapper(XTextMapper)
                    XActor.SetScale(0.25*esize,0.25*esize,0.25*esize)

                    XActor.SetPosition(c[0]-0.25*esize,c[1]-0.25*esize,c[2]+0.25*esize)
                    XActor.GetProperty().SetColor(color.GetColor3ub('Green'))
                    self.renderer.AddActor(XActor)            


        interactor = vtk.vtkInteractorStyleImage()
        self.renWinInteract.SetInteractorStyle(interactor)
        self.renWin.AddRenderer(self.renderer)
        self.renWin.Render()

    def OpenAddBoundaryDlg(self):
        self.style = vtk.vtkInteractorStyleRubberBand2D()
        self.position=[0.0,0.0,0.0,0.0]
        self.statusbar.showMessage('Select Boundary Elements')

        self.style.area_picker = vtk.vtkRenderedAreaPicker()
        self.style.AddObserver("LeftButtonReleaseEvent", self.leftButtonReleaseEvent)
        self.style.SetDefaultRenderer(self.renderer)
        self.renWinInteract.SetInteractorStyle(self.style) 
        self.renWinInteract.SetPicker(self.style.area_picker)
    
    def GetInputText(self):
        return self.text()   

    def leftButtonReleaseEvent(self, obj, event):
        self.style.OnLeftButtonUp()
        position=(self.style.GetStartPosition()[0],self.style.GetStartPosition()[1],
                        self.style.GetEndPosition()[0],self.style.GetEndPosition()[1])
        coord=vtk.vtkCoordinate()
        coord.SetCoordinateSystemToDisplay()
        coord.SetValue(position[0], position[1], 0)
        wcoord=coord.GetComputedWorldValue(self.renderer) 
        coord.SetValue(position[2], position[3], 0)
        wcoord=wcoord+coord.GetComputedWorldValue(self.renderer)
        self.AEMmodel.add_boundary(wcoord,'fix')
        if 'Boundary' not in self.DisplayMode:
                self.DisplayMode=self.DisplayMode+'Boundary'
        self.RenderAEMmodel()
        self.statusbar.showMessage('')

    def btnstate(self,b):
        if b.text() == "Element Number":
            if b.isChecked() == True:
                if 'ElementNo' not in self.DisplayMode:
                        self.DisplayMode=self.DisplayMode+'ElementNo'
                self.RenderAEMmodel()
            else:
                if 'ElementNo' in self.DisplayMode:
                        self.DisplayMode=self.DisplayMode.replace('ElementNo','')
                self.RenderAEMmodel()

        if b.text() == "Steel Rod":
            if b.isChecked() == True:
                if 'Steel' not in self.DisplayMode:
                        self.DisplayMode=self.DisplayMode+'Steel'
                self.RenderAEMmodel()
            else:
                if 'Steel' in self.DisplayMode:
                        self.DisplayMode=self.DisplayMode.replace('Steel','')
                self.RenderAEMmodel()
        
        if b.text() == "Boundary Condition":
            if b.isChecked() == True:
                if 'Boundary' not in self.DisplayMode:
                        self.DisplayMode=self.DisplayMode+'Boundary'
                self.RenderAEMmodel()
            else:
                if 'Boundary' in self.DisplayMode:
                        self.DisplayMode=self.DisplayMode.replace('Boundary','')
                self.RenderAEMmodel()

        if b.text() == "Loading":
            if b.isChecked() == True:
                if 'Loading' not in self.DisplayMode:
                        self.DisplayMode=self.DisplayMode+'Loading'
                self.RenderAEMmodel()
            else:
                if 'Loading' in self.DisplayMode:
                        self.DisplayMode=self.DisplayMode.replace('Loading','')
                self.RenderAEMmodel()

    def GetDisplayCoordinate(self,loc):
        coord=vtk.vtkCoordinate()
        coord.SetCoordinateSystemToWorld()
        coord.SetValue(loc[0], loc[1], loc[2])
        return coord.GetComputedDisplayValue(self.renderer) 


class AddBlockDlg(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_Dialog_AddBlock()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)

class AddSteelDlg(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_Dialog_AddSteel()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)

#####Extra###### 
class MouseInteractorHighLightActorSingle(vtk.vtkInteractorStyleTrackballCamera):

    def __init__(self, parent=None):
        self.AddObserver("LeftButtonPressEvent", self.leftButtonPressEvent)
        self.LastPickedActor = None
        self.LastPickedProperty = vtk.vtkProperty()

    def leftButtonPressEvent(self, obj, event):
        clickPos = self.GetInteractor().GetEventPosition()
        picker = vtk.vtkCellPicker()
        picker.Pick(clickPos[0], clickPos[1], 0, self.GetDefaultRenderer())
        print (picker.GetCellId())
        return



if (__name__ == '__main__'):
    logging.basicConfig(level=logging.DEBUG)
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    size = screen.size()
    mainWindow = MainWindow(size.width(), size.height())
    mainWindow.show()
    sys.exit(app.exec_())
