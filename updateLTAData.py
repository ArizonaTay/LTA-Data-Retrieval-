#Import module for Retrieving the Data
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import urllib.request
import os
import pandas as pd
import tabula
import datetime
import pygsheets
from oauth2client.service_account import ServiceAccountCredentials

pd.options.display.max_colwidth = 100
pd.set_option('display.max_columns', None)
#Get URL Link


folder_location = os.getcwd()+r"/Data"
directory = os.getcwd()+r"/Data"


url='https://www.lta.gov.sg/content/dam/ltagov/who_we_are/statistics_and_publications/statistics/pdf/M10-Monthly_COE_Revalidation.pdf'
r = requests.get(url, stream=True)

with open(os.path.join(folder_location,'M10-Monthly_COE_Revalidation.pdf'), 'wb') as f:
    f.write(r.content)


url = 'https://datamall.lta.gov.sg/content/datamall/en/static-data.html'
page = requests.get(url, allow_redirects=True)
soup = BeautifulSoup(page.content, 'html.parser')


# COE Revalidation File
#for link in soup.select("a[href$='Monthly_COE_Revalidation.pdf']"):
#    filename = os.path.join(folder_location,link['href'].split('/')[-1])
#    with open(filename, 'wb') as f:
#        f.write(requests.get(urljoin(url,link['href'])).content)



for link in soup.select("a[href$='Monthly_COE_Revalidation.pdf']"):
    filename = os.path.join(folder_location,link['href'].split('/')[-1])
    with open(filename, 'wb') as f:
        f.write(requests.get(urljoin(url,link['href'])).content)

    
### car transfer
for link in soup.select("a[href$='M07-Trf_by_type.pdf']"):
    filename = os.path.join(folder_location,link['href'].split('/')[-1])
    with open(filename, 'wb') as f:
        f.write(requests.get(urljoin(url,link['href'])).content)

#Dereg COE
for link in soup.select("a[href$='M05-Dereg_by_Quota.pdf']"):
    filename = os.path.join(folder_location,link['href'].split('/')[-1])
    with open(filename, 'wb') as f:
        f.write(requests.get(urljoin(url,link['href'])).content)


#new Reg
for link in soup.select("a[href$='M02-New_Reg_by_Quota.pdf']"):
    filename = os.path.join(folder_location,link['href'].split('/')[-1])
    with open(filename, 'wb') as f:
        f.write(requests.get(urljoin(url,link['href'])).content)

        
#car population
for link in soup.select("a[href$='M06-Vehs_by_Type.pdf']"):
    filename = os.path.join(folder_location,link['href'].split('/')[-1])
    with open(filename, 'wb') as f:
        f.write(requests.get(urljoin(url,link['href'])).content)

#Open Market Share Google Sheet
#export_df = pd.read_csv(directory+r'/marketShare.csv')
gc = pygsheets.authorize()
sh = gc.open('market Share')
wk1 = sh[0]
rows = wk1.rows


#Vehicle Transfer
###########################################################################
path = directory+r'/M07-Trf_by_type.pdf'
df = tabula.read_pdf(path, stream=True, pages = '1')
month = (datetime.date.today() - datetime.timedelta(days=30)).strftime('%m')
year = (datetime.date.today() - datetime.timedelta(days=30)).strftime('%Y')
date = year+ str(month) + "02"
transfer = df[0].get(["Unnamed: 3"])
transfer = transfer['Unnamed: 3'].iloc[[len(transfer)-1]].to_string(index=False).replace(",", "")
#export_df.loc[export_df['Date'] == int(date), 'Vehicle Transfer'] = transfer

#Dereg
#############################################################################
path = directory+r'/M05-Dereg_by_Quota.pdf'
df = tabula.read_pdf(path, stream=True, pages = '1')
dereg = df[0].get(["Unnamed: 2"])
dereg = dereg['Unnamed: 2'].iloc[[len(dereg)-1]].to_string(index=False).replace(",", "")

dereg2 = df[0].get(["Unnamed: 3"])
dereg2 = dereg2['Unnamed: 3'].iloc[[len(dereg2)-1]].to_string(index=False).replace(",", "")
dereg = int(dereg) + int(dereg2)
#export_df.loc[export_df['Date'] == int(date), 'Dereg'] = dereg 

#Car Population
#############################################################################
path = directory+r'/M06-Vehs_by_Type.pdf'
df = tabula.read_pdf(path, stream=True, pages = '1')
population = df[0].get(["Unnamed: 2"])
population = population['Unnamed: 2'].iloc[[len(population)-1]].to_string(index=False).replace(",", "")
population2 = df[0].get(["Unnamed: 3"])
population2 = population2['Unnamed: 3'].iloc[[len(population2)-1]].to_string(index=False).replace(",", "")
population = int(population2) + int(population)

population3 = df[0].get(["Unnamed: 2"])
population3 = population3['Unnamed: 2'].iloc[[len(population3)-2]].to_string(index=False).replace(",", "")
population4 = df[0].get(["Unnamed: 3"])
population4 = population4['Unnamed: 3'].iloc[[len(population4)-2]].to_string(index=False).replace(",", "")
popdiff  = int(population) - int(population3) - int(population4)
#export_df.loc[export_df['Date'] == int(date), 'Population'] = population
#export_df.loc[export_df['Date'] == int(date), 'Population Diff'] = popdiff


#New Reg
#############################################################################
path = directory+r'/M02-New_Reg_by_Quota.pdf'
df = tabula.read_pdf(path, stream=True, pages = '1')
newReg = df[0].get(["Unnamed: 2"])
newReg = newReg['Unnamed: 2'].iloc[[len(newReg)-1]].to_string(index=False).replace(",", "")
newReg2 = df[0].get(["Unnamed: 3"])
newReg2 = newReg2['Unnamed: 3'].iloc[[len(newReg2)-1]].to_string(index=False).replace(",", "")
newReg = int(newReg) + int(newReg2)
#export_df.loc[export_df['Date'] == int(date), 'New Reg'] = newReg


#COE Revalidation
#############################################################################
path = directory+r'/M10-Monthly_COE_Revalidation.pdf'
df = tabula.read_pdf(path, stream=True, pages = '1')

revad = df[0].get(["Category A"])
revad = revad['Category A'].iloc[[len(revad)-1]].to_string(index=False).replace(",", "")

revad = int(revad.split(" ")[0] + revad.split(" ")[1]) + int(revad.split(" ")[2] + revad.split(" ")[3])

revad2 = df[0].get(["Category B"])
revad2 = revad2['Category B'].iloc[[len(revad2)-1]].to_string(index=False).replace(",", "")
revad2 = int(revad2.split(" ")[0] + revad2.split(" ")[1]) + int(revad2.split(" ")[2] + revad2.split(" ")[3])
Total = revad2 + revad

date = year+ str(int(month)-1) + "02"
#export_df.loc[export_df['Date'] == int(date), 'Total Revalidation'] = Total




update = ((datetime.datetime.now().year - 2019)* 12) + datetime.datetime.now().month 
wk1.update_row(update ,[newReg], 9)
wk1.update_row(update ,[ transfer, dereg, population, popdiff], 11)

update = (((datetime.datetime.now().year - 2019)* 12) + datetime.datetime.now().month) - 1
wk1.update_row(update ,[Total], 10)

#export_df.to_csv(directory+r'/marketShare.csv', index = False)   
os.remove(folder_location+ '/' + 'M02-New_Reg_by_Quota.pdf')
os.remove(folder_location+ '/' + 'M05-Dereg_by_Quota.pdf')
os.remove(folder_location+ '/' + 'M07-Trf_by_type.pdf')
os.remove(folder_location+ '/' + 'M06-Vehs_by_Type.pdf')
os.remove(folder_location+ '/' + 'M10-Monthly_COE_Revalidation.pdf')
os.remove(folder_location+ '/' + 'Monthly_COE_Revalidation.pdf')

print("Done")
input('Press ENTER to exit')

