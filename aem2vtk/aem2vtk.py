import glob
from math import sin,cos,pi

def main():
    try:
        with open('mesh.csv') as f:
            print('reading mesh.csv')
            ele_size,element=read_aem_mesh('mesh.csv')
    except IOError:
        raise SystemExit('ERROR cannot find mesh.csv')

    out_aem_mesh_vtk_ascii(ele_size,element,'mesh.vtk')
    filelist=glob.glob('dis*.csv')
    for f in filelist:
        print('reading {}'.format(f))
        dis=read_aem_dis(f)
        write_file=f.replace('.csv','.vtk')
        out_aem_vtk_ascii(ele_size,element,dis,write_file)

    filelist=glob.glob('spr*.csv')
    for f in filelist:
        print('reading {}'.format(f))
        spr=read_aem_dis(f)
        write_file=f.replace('.csv','.vtk')
        out_aem_spr_vtk_ascii(spr,write_file)

        
def read_aem_mesh(aem_mesh_file):
    element={}
    n=0
    with open (aem_mesh_file,'r') as fo:
        for line in fo:
            if '#' in line:continue
            l=line.split(',')
            x=float(l[2])
            y=float(l[3])
            n+=1
            if n==1:vec1=[x,y]
            if n==2:vec2=[x,y]
            element[int(l[0])]={'mat_no':int(l[1]),
                                'coord':(x,y)}     
    x=abs(vec2[0]-vec1[0])
    y=abs(vec2[1]-vec1[1])
    return (x*x+y*y)**0.5,element

def read_aem_dis(aem_dis_file):
    dis={}
    with open (aem_dis_file,'r') as fo:
        for line in fo:
            if '#' in line:continue
            l=line.split(',')
            dis[int(l[0])]=list(map(float,l[1:]))
    return dis

def read_aem_spr(aem_spr_file):
    spr={}
    with open (aem_spr_file,'r') as fo:
        for line in fo:
            if '#' in line:continue
            l=line.split(',')
            spr[int(l[0])]=list(map(float,l[1:]))
    return spr

def out_aem_mesh_vtk_ascii(a,ele,outfile):
    #a=element side
    with open(outfile,'w') as vtk:
        vtk.write('# vtk DataFile Version 4.0\n')
        vtk.write('{}\n'.format('AEM_MESH'))
        vtk.write('ASCII\n')
        vtk.write('DATASET UNSTRUCTURED_GRID\n')
        vtk.write('{} {} {}\n'.format('POINTS',len(ele)*4,'double'))
        for e in ele:
            (x,y)=ele[e]['coord']
            vtk.write('{} {} {}\n'.format(x-0.5*a,y-0.5*a,0.0))
            vtk.write('{} {} {}\n'.format(x+0.5*a,y-0.5*a,0.0))
            vtk.write('{} {} {}\n'.format(x+0.5*a,y+0.5*a,0.0))
            vtk.write('{} {} {}\n'.format(x-0.5*a,y+0.5*a,0.0))
        vtk.write('\n')
        vtk.write('{} {} {}\n'.format('CELLS',len(ele),len(ele)*5))
        n=0
        for e in ele:
            vtk.write('4  {} {} {} {}\n'.format(n*4,n*4+1,n*4+2,n*4+3))
            n+=1
        vtk.write('\n')
        vtk.write('{} {}\n'.format('CELL_TYPES',len(ele)))
        for e in ele:
            vtk.write('9\n')
        vtk.write('\n')
        vtk.write('{} {}\n'.format('CELL_DATA',len(ele)))
        vtk.write('\n')
        vtk.write('SCALARS Element_ID int\n')
        vtk.write('LOOKUP_TABLE default\n')
        for e in ele:
            vtk.write('{}\n'.format(e))
        vtk.write('\n')
        vtk.write('SCALARS Material_ID int\n')
        vtk.write('LOOKUP_TABLE default\n')
        for e in ele:
            vtk.write('{}\n'.format(ele[e]['mat_no']))
        vtk.write('\n')

def out_aem_vtk_ascii(a,ele,dis,outfile):
    #a=element side
    with open(outfile,'w') as vtk:
        vtk.write('# vtk DataFile Version 4.0\n')
        vtk.write('{}\n'.format('AEM_MESH'))
        vtk.write('ASCII\n')
        vtk.write('DATASET UNSTRUCTURED_GRID\n')
        vtk.write('{} {} {}\n'.format('POINTS',len(ele)*4,'double'))
        for e in ele:
            (x,y)=ele[e]['coord']
            [dx,dy,ang]=dis[e]
            c=cos(ang*pi/180.0)
            s=sin(ang*pi/180.0)
            vtk.write('{} {} {}\n'.format(c*(x-0.5*a)-s*(y-0.5*a),
                s*(x-0.5*a)+c*(y-0.5*a),0.0))
            vtk.write('{} {} {}\n'.format(c*(x+0.5*a)-s*(y-0.5*a),
                s*(x+0.5*a)+c*(y-0.5*a),0.0))
            vtk.write('{} {} {}\n'.format(c*(x+0.5*a)-s*(y+0.5*a),
                s*(x+0.5*a)+c*(y+0.5*a),0.0))   
            vtk.write('{} {} {}\n'.format(c*(x-0.5*a)-s*(y+0.5*a),
                s*(x-0.5*a)+c*(y+0.5*a),0.0))
                
            # vtk.write('{} {} {}\n'.format(x+0.5*a,y-0.5*a,0.0))
            # vtk.write('{} {} {}\n'.format(x+0.5*a,y+0.5*a,0.0))
            # vtk.write('{} {} {}\n'.format(x-0.5*a,y+0.5*a,0.0))
        vtk.write('\n')
        vtk.write('{} {} {}\n'.format('CELLS',len(ele),len(ele)*5))
        n=0
        for e in ele:
            vtk.write('4 {} {} {} {}\n'.format(n*4,n*4+1,n*4+2,n*4+3))
            n+=1
        vtk.write('\n')
        vtk.write('{} {}\n'.format('CELL_TYPES',len(ele)))
        for e in ele:
            vtk.write('9\n')
        vtk.write('\n')
        vtk.write('{} {}\n'.format('POINT_DATA',4*len(ele)))
        vtk.write('SCALARS DUMMY_Node_ID int\n')
        vtk.write('LOOKUP_TABLE default\n')
        for e in ele:
            vtk.write('{}\n'.format(e))
            vtk.write('{}\n'.format(e))
            vtk.write('{}\n'.format(e))
            vtk.write('{}\n'.format(e))
        vtk.write('\n')
        vtk.write('VECTORS DISPLACEMENT double\n')       
        for e in ele:
            [dx,dy,ang]=dis[e]
            vtk.write('{} {} {}\n'.format(dx,dy,0.0))
            vtk.write('{} {} {}\n'.format(dx,dy,0.0))
            vtk.write('{} {} {}\n'.format(dx,dy,0.0))
            vtk.write('{} {} {}\n'.format(dx,dy,0.0))
        vtk.write('\n') 
        vtk.write('{} {}\n'.format('CELL_DATA',len(ele)))
        vtk.write('SCALARS Element_ID int\n')
        vtk.write('LOOKUP_TABLE default\n')
        for e in ele:
            vtk.write('{}\n'.format(e))
        vtk.write('\n')
        vtk.write('SCALARS Material_ID int\n')
        vtk.write('LOOKUP_TABLE default\n')
        for e in ele:
            vtk.write('{}\n'.format(ele[e]['mat_no']))
        vtk.write('\n')

def out_aem_spr_vtk_ascii(spr,outfile):
    ns=len(spr)
    with open(outfile,'w') as vtk:
        vtk.write('# vtk DataFile Version 4.0\n')
        vtk.write('{}\n'.format('AEM_SPR_MESH'))
        vtk.write('ASCII\n')
        vtk.write('DATASET UNSTRUCTURED_GRID\n')
        vtk.write('{} {} {}\n'.format('POINTS',ns*4,'double'))
        for s in spr:
            x=spr[s][1]
            y=spr[s][2]
            l=spr[s][7]
            h=spr[s][8]
            vtk.write('{} {} {}\n'.format(x-0.5*l,y-0.5*h,0.0))
            vtk.write('{} {} {}\n'.format(x+0.5*l,y-0.5*h,0.0))
            vtk.write('{} {} {}\n'.format(x+0.5*l,y+0.5*h,0.0))
            vtk.write('{} {} {}\n'.format(x-0.5*l,y+0.5*h,0.0))
        vtk.write('\n')
        vtk.write('{} {} {}\n'.format('CELLS',ns,ns*5))
        n=0
        for s in spr:
            vtk.write('4 {} {} {} {}\n'.format(n*4,n*4+1,n*4+2,n*4+3))
            n+=1
        vtk.write('\n')
        vtk.write('{} {}\n'.format('CELL_TYPES',ns))
        for s in spr:
            vtk.write('9\n')
        vtk.write('\n')
        vtk.write('{} {}\n'.format('POINT_DATA',4*ns))
        vtk.write('SCALARS SPRING_NUMBER int\n')
        vtk.write('LOOKUP_TABLE default\n')
        for s in spr:
            vtk.write('{}\n'.format(s))
            vtk.write('{}\n'.format(s))
            vtk.write('{}\n'.format(s))
            vtk.write('{}\n'.format(s))
        vtk.write('\n') 
        vtk.write('{} {}\n'.format('CELL_DATA',ns))
        vtk.write('SCALARS SPRING_NO int\n')
        vtk.write('LOOKUP_TABLE default\n')
        for s in spr:
            vtk.write('{}\n'.format(s))
        vtk.write('\n')
        vtk.write('SCALARS SPRING_MAT_NO int\n')
        vtk.write('LOOKUP_TABLE default\n')
        for s in spr:
            vtk.write('{}\n'.format(int(spr[s][0])))
        vtk.write('\n')
        vtk.write('SCALARS SPRING_NORMAL_STRESS double\n')
        vtk.write('LOOKUP_TABLE default\n')
        for s in spr:
            vtk.write('{}\n'.format(spr[s][3]))
        vtk.write('\n')
        vtk.write('SCALARS SPRING_SHEAR_STRESS double\n')
        vtk.write('LOOKUP_TABLE default\n')
        for s in spr:
            vtk.write('{}\n'.format(spr[s][4]))
        vtk.write('\n')
        vtk.write('SCALARS SPRING_NORMAL_STRAIN double\n')
        vtk.write('LOOKUP_TABLE default\n')
        for s in spr:
            vtk.write('{}\n'.format(spr[s][5]))
        vtk.write('\n')
        vtk.write('SCALARS SPRING_SHEAR_STRAIN double\n')
        vtk.write('LOOKUP_TABLE default\n')
        for s in spr:
            vtk.write('{}\n'.format(spr[s][6]))
        vtk.write('\n')
        vtk.write('SCALARS SPRING_TENSION_FAIL int\n')
        vtk.write('LOOKUP_TABLE default\n')
        for s in spr:
            vtk.write('{}\n'.format((int(spr[s][9]))))
        vtk.write('\n')

if __name__ == '__main__':
    main()