import matplotlib.pyplot as plt 
from osgeo import gdal 
from mpl_toolkits.basemap import Basemap 
import numpy as np
from numpy import linspace 
from numpy import meshgrid 
import matplotlib.patheffects as path_effects
import datetime as dt
import matplotlib
from datetime import datetime
from datetime import date
import scipy.ndimage as ndimage
import matplotlib.image as image
import csv
#import wget
import matplotlib.patheffects as path_effects
plt.rcParams['axes.xmargin'] = 0
print('\n\nPROGRAMA GFS CHUVA 15 DIAS\nMeteorologista: Lucas A. F. Coelho')

now = datetime.now()
hora= now.strftime("%H")
minutos= now.strftime("%M")
dia= now.strftime("%d")
#dia='27'
mes= now.strftime("%m")
ano= now.strftime("%Y")

rodada = '12'

print('\n\nInício do processo:', dia,'/',mes,'/',ano,' ',hora,':',minutos,'\n\n')

if int(rodada) == 12:
   z=['015','039','063','087','111','135','159','183','375']


if int(rodada) == 6:
   z=['000','021','045','069','093','117','141','165','357']

grib0 = gdal.Open('gfs.t'+rodada+'z.pgrb2.0p25.f'+z[0]+'.txt')  
grib1 = gdal.Open('gfs.t'+rodada+'z.pgrb2.0p25.f'+z[1]+'.txt')  
grib2 = gdal.Open('gfs.t'+rodada+'z.pgrb2.0p25.f'+z[2]+'.txt')  
grib3 = gdal.Open('gfs.t'+rodada+'z.pgrb2.0p25.f'+z[3]+'.txt')  
grib4 = gdal.Open('gfs.t'+rodada+'z.pgrb2.0p25.f'+z[4]+'.txt')  
grib5 = gdal.Open('gfs.t'+rodada+'z.pgrb2.0p25.f'+z[5]+'.txt')  
grib6 = gdal.Open('gfs.t'+rodada+'z.pgrb2.0p25.f'+z[6]+'.txt')  
grib7 = gdal.Open('gfs.t'+rodada+'z.pgrb2.0p25.f'+z[7]+'.txt')  
grib8 = gdal.Open('gfs.t'+rodada+'z.pgrb2.0p25.f'+z[8]+'.txt')  

       
extent = [-90, -40, -20,10]
min_lon = extent[0]; max_lon = extent[2]; min_lat = extent[1]; max_lat = extent[3]

print('Montando arquivo Grib 0')
grib0 = gdal.Translate('subsected_grib.grb', grib0, projWin = [min_lon + 359.9, max_lat + 0.25, max_lon + 360.5, min_lat -0.1])    
print('Montando arquivo Grib 1')
grib1 = gdal.Translate('subsected_grib.grb', grib1, projWin = [min_lon + 359.9, max_lat + 0.25, max_lon + 360.5, min_lat -0.1])    
print('Montando arquivo Grib 2')
grib2 = gdal.Translate('subsected_grib.grb', grib2, projWin = [min_lon + 359.9, max_lat + 0.25, max_lon + 360.5, min_lat -0.1])    
print('Montando arquivo Grib 3')
grib3 = gdal.Translate('subsected_grib.grb', grib3, projWin = [min_lon + 359.9, max_lat + 0.25, max_lon + 360.5, min_lat -0.1])    
print('Montando arquivo Grib 4')
grib4 = gdal.Translate('subsected_grib.grb', grib4, projWin = [min_lon + 359.9, max_lat + 0.25, max_lon + 360.5, min_lat -0.1])    
print('Montando arquivo Grib 5')
grib5 = gdal.Translate('subsected_grib.grb', grib5, projWin = [min_lon + 359.9, max_lat + 0.25, max_lon + 360.5, min_lat -0.1])    
print('Montando arquivo Grib 6')
grib6 = gdal.Translate('subsected_grib.grb', grib6, projWin = [min_lon + 359.9, max_lat + 0.25, max_lon + 360.5, min_lat -0.1])    
print('Montando arquivo Grib 7')
grib7 = gdal.Translate('subsected_grib.grb', grib7, projWin = [min_lon + 359.9, max_lat + 0.25, max_lon + 360.5, min_lat -0.1])    
print('Montando arquivo Grib 8')
grib8 = gdal.Translate('subsected_grib.grb', grib8, projWin = [min_lon + 359.9, max_lat + 0.25, max_lon + 360.5, min_lat -0.1])  

varnumber = 597

data_inicial=dt.datetime(int(ano),int(mes),int(dia))

print('\n\n3. Montando figuras\n\n')

for j in range(2):
    for i in range(10):
        fig = plt.figure(figsize=(11,11))
        ax = fig.add_subplot(111)
        if j ==0:
           m = Basemap(llcrnrlon=np.min(-90), llcrnrlat=np.min(-40), urcrnrlon=np.max(-20), urcrnrlat=10)
        if j ==1:
           m = Basemap(llcrnrlon=np.min(-64), llcrnrlat=np.min(-36), urcrnrlon=np.max(-41), urcrnrlat=-20)
        m.readshapefile('/Users/lucasfumagalli/shapefile/BRUFE250GC_SIR','BRUFE250GC_SIR',linewidth=.7,color='#606060')
        m.readshapefile('/Users/lucasfumagalli/shapefile/ne_10m_admin_0_countries','ne_10m_admin_0_countries',linewidth=.7,color='#303030')
        m.drawparallels(np.arange( -90., 90.,5.),labels=[1,0,0,0],fontsize=8,linewidth=0.0,  dashes=[4, 2], color='grey')
        m.drawmeridians(np.arange(-180.,180.,5.),labels=[0,0,0,1],fontsize=8,linewidth=0.0,  dashes=[4, 2], color='grey')     
      #  m.bluemarble()
    
        if i ==0: gribi = grib0; gribf = grib1
        if i ==1: gribi = grib1; gribf = grib2
        if i ==2: gribi = grib2; gribf = grib3
        if i ==3: gribi = grib3; gribf = grib4
        if i ==4: gribi = grib4; gribf = grib5
        if i ==5: gribi = grib5; gribf = grib6
        if i ==6: gribi = grib6; gribf = grib7
        if i ==7: gribi = grib0; gribf = grib7
        if i ==8: gribi = grib7; gribf = grib8
        if i ==9: gribi = grib0; gribf = grib8                                    
    
    
        if i < 7:  
           data0=data_inicial+dt.timedelta(hours=9+int(z[i]))
           data1=data_inicial+dt.timedelta(hours=9+int(z[i+1]))
        if i == 7:
           data0=data_inicial+dt.timedelta(hours=9+int(z[0]))
           data1=data_inicial+dt.timedelta(hours=9+int(z[7])) 
        if i == 8:
           data0=data_inicial+dt.timedelta(hours=9+int(z[7]))
           data1=data_inicial+dt.timedelta(hours=9+int(z[8])) 
        if i == 9:
           data0=data_inicial+dt.timedelta(hours=9+int(z[0]))
           data1=data_inicial+dt.timedelta(hours=9+int(z[8]))      
        
        dia0= data0.strftime("%d")
        mes0= data0.strftime("%m")
        ano0= data0.strftime("%Y")
    
        dia1= data1.strftime("%d")
        mes1= data1.strftime("%m")
        ano1= data1.strftime("%Y")
    
        chuvai = gribi.GetRasterBand(varnumber)
        chuvai = chuvai.ReadAsArray() 
        chuvaf = gribf.GetRasterBand(varnumber)
        chuvaf = chuvaf.ReadAsArray()       
       
        chuva = chuvaf-chuvai     
       
        if i < 7:
           plt.title('GFS-FV3: Precipitação total: '+str(dia0)+'/'+str(mes0)+'/'+str(ano0)+' (mm)',fontweight='bold',fontsize=9,loc='left', va='center')    
        if i >= 7:
           plt.title('GFS-FV3: Precipitação total entre: '+str(dia0)+'/'+str(mes0)+'/'+str(ano0)+' - '+str(dia1)+'/'+str(mes1)+'/'+str(ano1)+' (mm)',fontweight='bold',fontsize=9,loc='left', va='center')    
    
        x = linspace(min_lon, max_lon, chuva.shape[1])
        y = linspace(max_lat, min_lat, chuva.shape[0])
        x, y = m(*np.meshgrid(x, y))   
    
        precc = ['#FFFFFF','#BEBEBE','#A5A5A5','#969696','#828282',
        '#B4F0FA','#96D2FA','#78B9FA','#3C96F5','#1E6EEB','#1464D2',
        '#0FA00F','#28BE28','#50F050','#73F06E','#B4FAAA','#FFFAAA',
        '#FFE878','#FFC03C','#FFA000','#FF6000','#FF3200','#E11400',
        '#C00000','#6C0500','#870000','#643B32','#643232']
    
        levelstp=[0,.5,1,1.5,2,2.5,5,7.5,10,13,16,20,25,30,35,40,50,60,70,80,90,100,125,150,175,200,250,500,3000]



        cores = ['#88D025','#28BE0A','#19A60D','#1C785F','#258EC4','#14A7E1','#11D6ED','#5E9ADE','#825FEC','#9536BF',
    '#992259','#C41C33','#E84125','#FB6E19','#F39121','#FFCC22']
       
        levels=[0.5,10,20,30,40,50,60,70,80,90,100,125,150,200,300,1000]
    
        plotA = plt.contourf(x, y, chuva, colors=precc, levels=levelstp)     
    
            
        x = linspace(min_lon, max_lon, chuva.shape[1])
        y = linspace(max_lat, min_lat, chuva.shape[0])
        xx, yy = np.meshgrid(x, y)     
        if j ==0: 
           filecsv = 'gfs.csv'
           nome='BR'
           txtplt=plt.text(-89.6,-38.1, 'Modelo GFS-FV3\nVAR: 597; dx, dy = 28km\nAtualizado em '+str(dia)+'/'+str(mes)+'/'+str(ano)+' '+str(hora)+':'+str(minutos)+'\nMeteorologista Lucas A. F. Coelho', ha= 'left', va='center', color='k',fontsize=7,zorder=200)    
           
        if j ==1:
           filecsv = 'gfsSUL.csv'
           nome='SBR'
           txtplt=plt.text(-63.9,-35.9, 'Modelo GFS-FV3\nVAR: 597; dx, dy = 28km\nAtualizado em '+str(dia)+'/'+str(mes)+'/'+str(ano)+' '+str(hora)+':'+str(minutos)+'\nMeteorologista Lucas A. F. Coelho', ha= 'left', va='bottom', color='k',fontsize=7,zorder=200)               
           
        Latitude,Longitude = [],[]
        with open(''+str(filecsv)+'') as csvfile:
            reader = csv.DictReader(csvfile,delimiter=',')
            for datai in reader:
                Latitude.append(float(datai['LAT']))
                Longitude.append(float(datai['LON']))
    
        xj, yj = m(Longitude, Latitude)            
     
        xk = linspace(min_lon, max_lon, chuva.shape[1])
        yk = linspace(max_lat, min_lat, chuva.shape[0])
    
     
        for j in range(0,len(Latitude)):
            latslons = [Latitude[j], Longitude[j]]                               
            plot = {'lat': latslons[0], 'lon': latslons[1]}        
     
            lat_idx = np.abs(yk - plot['lat']).argmin()  
            lon_idx = np.abs(xk - plot['lon']).argmin()    
            if chuva[lat_idx, lon_idx] > 0.1:      
               txtplt=plt.text(xj[j],yj[j], 
               ''+'{:.1f}'.format(chuva[lat_idx, lon_idx])+'',
               color='k',va='center', ha='center', fontsize=7.5,zorder=12) 
        
        fig.text(0.9,0.785,'✆ (45) 32225180\n', fontsize=9, fontweight='bold', color='#3EE45C',ha='right', va='center')    
        fig.text(0.9,0.785,'\n✉ lucasfumagalli@gmail.com', fontsize=9, fontweight='bold', color='#EA4335',ha='right', va='center')     
    

        
        cax = fig.add_axes([0.9024, 0.2185, 0.02, 0.5532])
        fig.colorbar(plotA, shrink=.6, cax=cax) 
        if i < 7:
           plt.savefig(''+str(nome)+'_'+str(ano0)+'_'+str(mes0)+'_'+str(dia0)+'.png',bbox_inches='tight', dpi=500, transparent=False)              
        if i >= 7:
           plt.savefig(''+str(nome)+'_'+str(ano0)+'_'+str(mes0)+'_'+str(dia0)+'__'+str(ano1)+'_'+str(mes1)+'_'+str(dia1)+'.png',bbox_inches='tight', dpi=500, transparent=False)
        plt.clf()
        plt.close()       

print('\n\n4. Arquivos salvos\n\n')
