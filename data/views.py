from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
# from .forms import UserLoginForm
from django.urls import reverse
from django.contrib.auth import login as auth_login,authenticate,logout as auth_logout
import datetime
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import mysql.connector as mysql
import csv
# Create your views here.

legacy_database={"host":"localhost","user":"root","password":"l00p","database":"datacollection_ddd"}
def index(request):
	return render(request,'data/index.html')

def login(request):

	usfo=AuthenticationForm(request.POST or None)
	err=None
	print(request.POST)
	if request.method=='POST':
		print("done",usfo.clean)
		# if usfo.is_valid():
			# username=usfo.cleaned_data.get('username')
			# password=usfo.cleaned_data.get('password')
		username = request.POST['username'].strip()
		password = request.POST['password']
		user=authenticate(username=username,password=password)
		print(err,user)
		if user==None:
			# raise forms.ValidationError({'bark_volume': ["Must be louder!",]})
			err="Invalid login credentials"
		if user:
			if user.is_active:
				auth_login(request,user)

				# print(request.user.name,request.user.username)
				return HttpResponseRedirect(reverse('main'))
			else:
				return HttpResponse("Your account is inactive.")
	# return render(request,'users/login.html',{'usfo':usfo,'err':err})



	# # usfo=UserLoginForm(request.POST or None)
	# err=None
	# username = request.POST['username']
	# password = request.POST['password']
	# user = authenticate(request, username=username, password=password)
	# if user is not None:
	# 	login(request, user)
	# 	HttpResponseRedirect(reverse('main'))
	# 	# Redirect to a success page.
	# else:
	# 	# Return an 'invalid login' error message.
	# 	err='Invalid login credentials'




	print(err)
	return render(request,'data/login.html',{'usfo':usfo,'err':err})


def signup(request):
        usfo=UserCreationForm(request.POST or None)
        if request.method == 'POST':
                # print(usfo.is_valid(),usfo.clean_email(),usfo.clean_password2())
                # print(usfo.clean())
                # print(usfo.data)
                # print(usfo.cleaned_data)

                if usfo.is_valid() :
                        print('doe')
                        
                        us=usfo.save(commit=False)
                        print(usfo)
                        us.set_password(usfo.clean_password2())
                        us.save()
                        auth_login(request,us,)
                        return HttpResponseRedirect(reverse('main'))
                else:
                        print(usfo.errors)

        return render(request,'data/signup.html',{'usfo':usfo})


def main(request):



	return render(request,'data/simple.html')

def query1(request):
	mydb = mysql.connect(
		host=legacy_database["host"],
		user=legacy_database["user"],passwd=legacy_database["password"],
		database=legacy_database["database"]
		)
	mycursor = mydb.cursor()
	quer=f'Select project_formn1.ProjectNumber, project_formn1.CompanyName, project_formn1.DateReceived,\
		samplen1.SampType, samplen1.ProjectNumber, samplen1.CompanyName,\
		analysisn1.analysisProjNumber, analysisn1.AnalysisType, analysisn1.CompanyName\
		from project_formn1 LEFT JOIN samplen1 ON samplen1.ProjectNumber = project_formn1.ProjectNumber\
		LEFT JOIN analysisn1 ON analysisn1.analysisProjNumber = project_formn1.ProjectNumber\
		WHERE analysisn1.CompanyName LIKE "%{ request.GET["AComany_name"] }%" OR samplen1.CompanyName like \
		"%{ request.GET["SComany_name"] }%" \
		OR project_formn1.CompanyName like "%{ request.GET["PComany_name"] }%"'
	print(quer)
	mycursor.execute(quer)
	myresult = mycursor.fetchall()
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = f'attachment; filename="query1_{str(datetime.datetime.now())}.csv"'
	writer = csv.writer(response)
	writer.writerow(('project_formn1.projectnumber','project_formn1.companyname','project_formn1.datereceived','samplen1.samptype','samplen1.projectnumber','samplen1.companyname','analysisn1.analysisprojnumber','analysisn1.analysistype','analysisn1.companyname',))


	print(len(myresult))
	for x in myresult:
		print(x) 
		writer.writerow(x)

	return response


def query1_table(request):
	mydb = mysql.connect(
		host=legacy_database["host"],
		user=legacy_database["user"],passwd=legacy_database["password"],
		database=legacy_database["database"]
		)
	mycursor = mydb.cursor()
	quer=f'Select project_formn1.ProjectNumber, project_formn1.CompanyName, project_formn1.DateReceived,\
		samplen1.SampType, samplen1.ProjectNumber, samplen1.CompanyName,\
		analysisn1.analysisProjNumber, analysisn1.AnalysisType, analysisn1.CompanyName\
		from project_formn1 LEFT JOIN samplen1 ON samplen1.ProjectNumber = project_formn1.ProjectNumber\
		LEFT JOIN analysisn1 ON analysisn1.analysisProjNumber = project_formn1.ProjectNumber\
		WHERE analysisn1.CompanyName LIKE "%{ request.GET["AComany_name"] }%" OR samplen1.CompanyName like \
		"%{ request.GET["SComany_name"] }%" \
		OR project_formn1.CompanyName like "%{ request.GET["PComany_name"] }%"'
	print(quer)
	mycursor.execute(quer)
	myresult = mycursor.fetchall()
	# response = HttpResponse(content_type='text/csv')
	# response['Content-Disposition'] = f'attachment; filename="query1_{str(datetime.datetime.now())}.csv"'
	# writer = csv.writer(response)
	# writer.writerow(('project_formn1.projectnumber','project_formn1.companyname','project_formn1.datereceived','samplen1.samptype','samplen1.projectnumber','samplen1.companyname','analysisn1.analysisprojnumber','analysisn1.analysistype','analysisn1.companyname',))
	table_data="<th>"
	table_data+="<td style='border: 2px black solid'>project_formn1.projectnumber</td>"
	table_data+="<td style='border: 2px black solid'>project_formn1.companyname</td>"
	table_data+="<td style='border: 2px black solid'>project_formn1.datereceived</td>"
	table_data+="<td style='border: 2px black solid'>samplen1.samptype</td>"
	table_data+="<td style='border: 2px black solid'>samplen1.projectnumber</td>"
	table_data+="<td style='border: 2px black solid'>samplen1.companyname</td>"
	table_data+="<td style='border: 2px black solid'>analysisn1.analysisprojnumber</td>"
	table_data+="<td style='border: 2px black solid'>analysisn1.analysistype</td>"
	table_data+="<td style='border: 2px black solid'>analysisn1.companyname</td>"
	table_data+="</th>"

	print(len(myresult))
	for x in myresult:
		print(x) 
		# writer.writerow(x)
		table_data+="<tr>"
		table_data+="<td style='border: 2px black solid'>x[0]</td>"
		table_data+="<td style='border: 2px black solid'>x[1]</td>"
		table_data+="<td style='border: 2px black solid'>x[2]</td>"
		table_data+="<td style='border: 2px black solid'>x[3]</td>"
		table_data+="<td style='border: 2px black solid'>x[4]</td>"
		table_data+="<td style='border: 2px black solid'>x[5]</td>"
		table_data+="<td style='border: 2px black solid'>x[6]</td>"
		table_data+="<td style='border: 2px black solid'>x[7]</td>"
		table_data+="<td style='border: 2px black solid'>x[8]</td>"
		table_data+="</tr>"

	table_data="<table>"+table_data+"</table>"
	return render(request,'data/table.html',{'table_data':table_data})



def query2(request):
	mydb = mysql.connect(
		host=legacy_database["host"],
		user=legacy_database["user"],passwd=legacy_database["password"],
		database=legacy_database["database"]
		)
	mycursor = mydb.cursor()
	quer=f'Select project_formn1.ProjectNumber, project_formn1.CompanyName, project_formn1.DateReceived, project_formn1.SampleTypes, project_formn1.ProjCGMP, \
samplen1.SampType, samplen1.ProjectNumber, samplen1.CompanyName, samplen1.DateReceived, \
analysisn1.analysisProjNumber, analysisn1.AnalysisType, analysisn1.CompanyName, analysisn1.MethodServiceType \
from project_formn1 LEFT JOIN samplen1 ON samplen1.ProjectNumber = project_formn1.ProjectNumber \
LEFT JOIN analysisn1 ON analysisn1.analysisProjNumber = project_formn1.ProjectNumber WHERE \
(samplen1.DateReceived BETWEEN "{ request.GET["Q2D1"] }" AND "{ request.GET["Q2D2"] }") AND \
analysisn1.CompanyName LIKE "%{ request.GET["Q2P1"] }%" \
OR samplen1.CompanyName like "%{ request.GET["Q2P2"] }%" \
OR project_formn1.CompanyName like "%{ request.GET["Q2P3"] }%"'

	print(quer)
	mycursor.execute(quer)
	myresult = mycursor.fetchall()
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = f'attachment; filename="query2_{str(datetime.datetime.now())}.csv"'
	writer = csv.writer(response)
	writer.writerow(('project_formn1.projectnumber','project_formn1.companyname','project_formn1.datereceived','project_formn1.sampletype','project_formn1.projcgmp','samplen1.samptype','samplen1.projectnumber','samplen1.companyname','samplen1.datereceive','analysisn1.analysisprojnumber','analysisn1.analysistype','analysisn1.companyname','analysisn1.methodservicetype',))


	print(len(myresult))
	for x in myresult:
		print(x) 
		writer.writerow(x)

	return response


def query2_table(request):
	mydb = mysql.connect(
		host=legacy_database["host"],
		user=legacy_database["user"],passwd=legacy_database["password"],
		database=legacy_database["database"]
		)
	mycursor = mydb.cursor()
	quer=f'Select project_formn1.ProjectNumber, project_formn1.CompanyName, project_formn1.DateReceived, project_formn1.SampleTypes, project_formn1.ProjCGMP, \
samplen1.SampType, samplen1.ProjectNumber, samplen1.CompanyName, samplen1.DateReceived, \
analysisn1.analysisProjNumber, analysisn1.AnalysisType, analysisn1.CompanyName, analysisn1.MethodServiceType \
from project_formn1 LEFT JOIN samplen1 ON samplen1.ProjectNumber = project_formn1.ProjectNumber \
LEFT JOIN analysisn1 ON analysisn1.analysisProjNumber = project_formn1.ProjectNumber WHERE \
(samplen1.DateReceived BETWEEN "{ request.GET["Q2D1"] }" AND "{ request.GET["Q2D2"] }") AND \
analysisn1.CompanyName LIKE "%{ request.GET["Q2P1"] }%" \
OR samplen1.CompanyName like "%{ request.GET["Q2P2"] }%" \
OR project_formn1.CompanyName like "%{ request.GET["Q2P3"] }%"'

	print(quer)
	mycursor.execute(quer)
	myresult = mycursor.fetchall()
	# response = HttpResponse(content_type='text/csv')
	# response['Content-Disposition'] = f'attachment; filename="query2_{str(datetime.datetime.now())}.csv"'
	# writer = csv.writer(response)
	# writer.writerow(('project_formn1.projectnumber','project_formn1.companyname','project_formn1.datereceived','project_formn1.sampletype','project_formn1.projcgmp','samplen1.samptype','samplen1.projectnumber','samplen1.companyname','samplen1.datereceive','analysisn1.analysisprojnumber','analysisn1.analysistype','analysisn1.companyname','analysisn1.methodservicetype',))

	table_data="<th>"
	table_data+="<td style='border: 2px black solid'>project_formn1.projectnumber</td>"
	table_data+="<td style='border: 2px black solid'>project_formn1.companyname</td>"
	table_data+="<td style='border: 2px black solid'>project_formn1.datereceived</td>"
	table_data+="<td style='border: 2px black solid'>project_formn1.sampletype</td>"
	table_data+="<td style='border: 2px black solid'>project_formn1.projcgmp</td>"
	table_data+="<td style='border: 2px black solid'>samplen1.samptype</td>"
	table_data+="<td style='border: 2px black solid'>samplen1.projectnumber</td>"
	table_data+="<td style='border: 2px black solid'>samplen1.companyname</td>"
	table_data+="<td style='border: 2px black solid'>samplen1.datereceive</td>"
	table_data+="<td style='border: 2px black solid'>analysisn1.analysisprojnumber</td>"
	table_data+="<td style='border: 2px black solid'>analysisn1.analysistype</td>"
	table_data+="<td style='border: 2px black solid'>analysisn1.companyname</td>"
	table_data+="<td style='border: 2px black solid'>analysisn1.methodservicetype</td>"
	table_data+="</th>"


	print(len(myresult))
	for x in myresult:
		# print(x) 
		# writer.writerow(x)
		table_data+="<tr>"
		table_data+="<td style='border: 2px black solid'>x[0]</td>"
		table_data+="<td style='border: 2px black solid'>x[1]</td>"
		table_data+="<td style='border: 2px black solid'>x[2]</td>"
		table_data+="<td style='border: 2px black solid'>x[3]</td>"
		table_data+="<td style='border: 2px black solid'>x[4]</td>"
		table_data+="<td style='border: 2px black solid'>x[5]</td>"
		table_data+="<td style='border: 2px black solid'>x[6]</td>"
		table_data+="<td style='border: 2px black solid'>x[7]</td>"
		table_data+="<td style='border: 2px black solid'>x[8]</td>"
		table_data+="<td style='border: 2px black solid'>x[9]</td>"
		table_data+="<td style='border: 2px black solid'>x[10]</td>"
		table_data+="<td style='border: 2px black solid'>x[11]</td>"
		table_data+="<td style='border: 2px black solid'>x[12]</td>"
		table_data+="<td style='border: 2px black solid'>x[13]</td>"
		table_data+="</tr>"
	table_data="<table>"+table_data+"</table>"
	return render(request,'data/table.html',{'table_data':table_data})



def query3(request):
	mydb = mysql.connect(
		host=legacy_database["host"],
		user=legacy_database["user"],passwd=legacy_database["password"],
		database=legacy_database["database"]
		)
	mycursor = mydb.cursor()
	quer=f'Select * From analysisn1 where analysisn1.AnalysisInstr LIKE "%{ request.GET["Q3P1"] }%" AND \
(analysisn1.DateReceived BETWEEN "{ request.GET["Q3D1"] }" AND "{ request.GET["Q3D2"] }") AND \
analysisn1.AnalysisAssign LIKE "%{ request.GET["Q3P1"] }%" '

# 	quer=f'Select project_formn1.ProjectNumber, project_formn1.CompanyName, project_formn1.DateReceived, project_formn1.SampleTypes, project_formn1.ProjCGMP, \
# samplen1.SampType, samplen1.ProjectNumber, samplen1.CompanyName, samplen1.DateReceived, \
# analysisn1.analysisProjNumber, analysisn1.AnalysisType, analysisn1.CompanyName, analysisn1.MethodServiceType \
# from project_formn1 LEFT JOIN samplen1 ON samplen1.ProjectNumber = project_formn1.ProjectNumber \
# LEFT JOIN analysisn1 ON analysisn1.analysisProjNumber = project_formn1.ProjectNumber WHERE \
# (samplen1.DateReceived BETWEEN "{ request.GET["Q2D1"] }" AND "{ request.GET["Q2D2"] }") AND \
# analysisn1.CompanyName LIKE "%{ request.GET["Q2P1"] }%" \
# OR samplen1.CompanyName like "%{ request.GET["Q2P2"] }%" \
# OR project_formn1.CompanyName like "%{ request.GET["Q2P3"] }%"'

	print(quer)
	mycursor.execute(quer)
	myresult = mycursor.fetchall()
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = f'attachment; filename="query3_{str(datetime.datetime.now())}.csv"'
	writer = csv.writer(response)
	writer.writerow(( 'analysisProjNumber', 'DocID', 'FamilyID', 'NoteID', 'ProjID', 'LocationID', 'AACAmt0', 'AACAmt1', 'AACAmt2', 'AACAmt3', 'AACAmt4', 'AACAmt5', 'AACAmt6', 'AACDesc0', 'AACDesc1', 'AACDesc2', 'AACDesc3', 'AACDesc4', 'AACDesc5', 'AACDesc6', 'AACQty0', 'AACQty1', 'AACQty2', 'AACQty3', 'AACQty4', 'AACQty5', 'AACQty6', 'AACTot0', 'AACTot1', 'AACTot2', 'AACTot3', 'AACTot4', 'AACTot5', 'AACTot6', 'ActionLog', 'ActionNotes', 'AMPMReceived', 'AnalysisAssign', 'AnalysisATFChrgSt', 'AnalysisCarrierUsed', 'AnalysiscGMPChrg', 'AnalysiscGMPChrgSt', 'AnalysisDEAChrgSt', 'AnalysisDept', 'AnalysisDisc', 'AnalysisDiscSt', 'AnalysisDiscStat', 'AnalysisHazChrg', 'AnalysisHazChrgSt', 'AnalysisInstr', 'AnalysisISOChrg', 'AnalysisISOChrgSt', 'AnalysisNum', 'AnalysisPrc', 'AnalysisPrcEnt', 'AnalysisPrcEntSt', 'AnalysisPrcSt', 'AnalysisPrioChrg', 'AnalysisPriority', 'AnalysisPrioSt', 'AnalysisQty', 'AnalysisQtyLab', 'AnalysisSamples', 'AnalysisSampleTypes', 'AnalysisSrvc', 'AnalysisTotal', 'AnalysisTotalwAddl', 'AnalysisType', 'AnlPVQty', 'AnlRunQty', 'AuthorDate', 'AuthorName', 'BillingCopyLab', 'BillingNotesText', 'cGMPChange', 'cGMPEnterPrc', 'CompanyName', 'ComplexProject', 'DateDue', 'DateReceived', 'DiscType', 'EditAuthors', 'EditDates', 'EditProjStatus', 'EmbeddedObjects', 'EnterDateDue', 'FamilyName', 'HazQty', 'InProjectTask', 'IsHighDEA', 'ISO', 'IsHighATF', 'ISOEnterPrc', 'LineItems', 'MethodServices', 'MethodServiceType', 'Options', 'OutSrcLocation', 'OutSrcMethod', 'OutSrcPONum', 'OutSrcTracking', 'OverridecGMP', 'OverrideISO', 'OverridePrc', 'PrelimDataCopyTo', 'PrelimDataSentBy', 'PrelimDataSentDate', 'PrelimDataSentMethod', 'PrelimDataSentTime', 'PrelimDataSentTo', 'ProjCanceled', 'ProjCancelStat', 'ProjCGMP', 'ProjDirector', 'ProjISO', 'ProjQADataRvw', 'ProjQARev', 'ProjReptWrtr', 'ProjStat', 'ProjStatus', 'ProjTechRev', 'ReptWrtrAssign', 'Revisions', 'SubAnalysisTotal', 'TechRevAssign', 'TotalBeforeDisco', 'trackLookup', 'TrackSelection', 'UniversalID', 'TurnaroundTextQuote100', 'TurnaroundTextQuote50', 'TurnaroundTextQuoteStd',))


	print(len(myresult))
	for x in myresult:
		print(x) 
		writer.writerow(x)

	return response


def query3_table(request):
	mydb = mysql.connect(
		host=legacy_database["host"],
		user=legacy_database["user"],passwd=legacy_database["password"],
		database=legacy_database["database"]
		)
	mycursor = mydb.cursor()
	quer=f'Select * From analysisn1 where analysisn1.AnalysisInstr LIKE "%{ request.GET["Q3P1"] }%" AND \
(analysisn1.DateReceived BETWEEN "{ request.GET["Q3D1"] }" AND "{ request.GET["Q3D2"] }") AND \
analysisn1.AnalysisAssign LIKE "%{ request.GET["Q3P1"] }%" '

# 	quer=f'Select project_formn1.ProjectNumber, project_formn1.CompanyName, project_formn1.DateReceived, project_formn1.SampleTypes, project_formn1.ProjCGMP, \
# samplen1.SampType, samplen1.ProjectNumber, samplen1.CompanyName, samplen1.DateReceived, \
# analysisn1.analysisProjNumber, analysisn1.AnalysisType, analysisn1.CompanyName, analysisn1.MethodServiceType \
# from project_formn1 LEFT JOIN samplen1 ON samplen1.ProjectNumber = project_formn1.ProjectNumber \
# LEFT JOIN analysisn1 ON analysisn1.analysisProjNumber = project_formn1.ProjectNumber WHERE \
# (samplen1.DateReceived BETWEEN "{ request.GET["Q2D1"] }" AND "{ request.GET["Q2D2"] }") AND \
# analysisn1.CompanyName LIKE "%{ request.GET["Q2P1"] }%" \
# OR samplen1.CompanyName like "%{ request.GET["Q2P2"] }%" \
# OR project_formn1.CompanyName like "%{ request.GET["Q2P3"] }%"'

	print(quer)
	mycursor.execute(quer)
	myresult = mycursor.fetchall()
	# response = HttpResponse(content_type='text/csv')
	# response['Content-Disposition'] = f'attachment; filename="query3_{str(datetime.datetime.now())}.csv"'
	# writer = csv.writer(response)
	# writer.writerow(( 'analysisProjNumber', 'DocID', 'FamilyID', 'NoteID', 'ProjID', 'LocationID', 'AACAmt0', 'AACAmt1', 'AACAmt2', 'AACAmt3', 'AACAmt4', 'AACAmt5', 'AACAmt6', 'AACDesc0', 'AACDesc1', 'AACDesc2', 'AACDesc3', 'AACDesc4', 'AACDesc5', 'AACDesc6', 'AACQty0', 'AACQty1', 'AACQty2', 'AACQty3', 'AACQty4', 'AACQty5', 'AACQty6', 'AACTot0', 'AACTot1', 'AACTot2', 'AACTot3', 'AACTot4', 'AACTot5', 'AACTot6', 'ActionLog', 'ActionNotes', 'AMPMReceived', 'AnalysisAssign', 'AnalysisATFChrgSt', 'AnalysisCarrierUsed', 'AnalysiscGMPChrg', 'AnalysiscGMPChrgSt', 'AnalysisDEAChrgSt', 'AnalysisDept', 'AnalysisDisc', 'AnalysisDiscSt', 'AnalysisDiscStat', 'AnalysisHazChrg', 'AnalysisHazChrgSt', 'AnalysisInstr', 'AnalysisISOChrg', 'AnalysisISOChrgSt', 'AnalysisNum', 'AnalysisPrc', 'AnalysisPrcEnt', 'AnalysisPrcEntSt', 'AnalysisPrcSt', 'AnalysisPrioChrg', 'AnalysisPriority', 'AnalysisPrioSt', 'AnalysisQty', 'AnalysisQtyLab', 'AnalysisSamples', 'AnalysisSampleTypes', 'AnalysisSrvc', 'AnalysisTotal', 'AnalysisTotalwAddl', 'AnalysisType', 'AnlPVQty', 'AnlRunQty', 'AuthorDate', 'AuthorName', 'BillingCopyLab', 'BillingNotesText', 'cGMPChange', 'cGMPEnterPrc', 'CompanyName', 'ComplexProject', 'DateDue', 'DateReceived', 'DiscType', 'EditAuthors', 'EditDates', 'EditProjStatus', 'EmbeddedObjects', 'EnterDateDue', 'FamilyName', 'HazQty', 'InProjectTask', 'IsHighDEA', 'ISO', 'IsHighATF', 'ISOEnterPrc', 'LineItems', 'MethodServices', 'MethodServiceType', 'Options', 'OutSrcLocation', 'OutSrcMethod', 'OutSrcPONum', 'OutSrcTracking', 'OverridecGMP', 'OverrideISO', 'OverridePrc', 'PrelimDataCopyTo', 'PrelimDataSentBy', 'PrelimDataSentDate', 'PrelimDataSentMethod', 'PrelimDataSentTime', 'PrelimDataSentTo', 'ProjCanceled', 'ProjCancelStat', 'ProjCGMP', 'ProjDirector', 'ProjISO', 'ProjQADataRvw', 'ProjQARev', 'ProjReptWrtr', 'ProjStat', 'ProjStatus', 'ProjTechRev', 'ReptWrtrAssign', 'Revisions', 'SubAnalysisTotal', 'TechRevAssign', 'TotalBeforeDisco', 'trackLookup', 'TrackSelection', 'UniversalID', 'TurnaroundTextQuote100', 'TurnaroundTextQuote50', 'TurnaroundTextQuoteStd',))

	table_data="<th>"
	table_data+="<td style='border: 2px black solid'>analysisProjNumber</td>"
	table_data+="<td style='border: 2px black solid'>DocID</td>"
	table_data+="<td style='border: 2px black solid'>FamilyID</td>"
	table_data+="<td style='border: 2px black solid'>NoteID</td>"
	table_data+="<td style='border: 2px black solid'>ProjID</td>"
	table_data+="<td style='border: 2px black solid'>LocationID</td>"
	table_data+="<td style='border: 2px black solid'>AACAmt0</td>"
	table_data+="<td style='border: 2px black solid'>AACAmt1</td>"
	table_data+="<td style='border: 2px black solid'>AACAmt2</td>"
	table_data+="<td style='border: 2px black solid'>AACAmt3</td>"
	table_data+="<td style='border: 2px black solid'>AACAmt4</td>"
	table_data+="<td style='border: 2px black solid'>AACAmt5</td>"
	table_data+="<td style='border: 2px black solid'>AACAmt6</td>"
	table_data+="<td style='border: 2px black solid'>AACDesc0</td>"
	table_data+="<td style='border: 2px black solid'>AACDesc1</td>"
	table_data+="<td style='border: 2px black solid'>AACDesc2</td>"
	table_data+="<td style='border: 2px black solid'>AACDesc3</td>"
	table_data+="<td style='border: 2px black solid'>AACDesc4</td>"
	table_data+="<td style='border: 2px black solid'>AACDesc5</td>"
	table_data+="<td style='border: 2px black solid'>AACDesc6</td>"
	table_data+="<td style='border: 2px black solid'>AACQty0</td>"
	table_data+="<td style='border: 2px black solid'>AACQty1</td>"
	table_data+="<td style='border: 2px black solid'>AACQty2</td>"
	table_data+="<td style='border: 2px black solid'>AACQty3</td>"
	table_data+="<td style='border: 2px black solid'>AACQty4</td>"
	table_data+="<td style='border: 2px black solid'>AACQty5</td>"
	table_data+="<td style='border: 2px black solid'>AACQty6</td>"
	table_data+="<td style='border: 2px black solid'>AACTot0</td>"
	table_data+="<td style='border: 2px black solid'>AACTot1</td>"
	table_data+="<td style='border: 2px black solid'>AACTot2</td>"
	table_data+="<td style='border: 2px black solid'>AACTot3</td>"
	table_data+="<td style='border: 2px black solid'>AACTot4</td>"
	table_data+="<td style='border: 2px black solid'>AACTot5</td>"
	table_data+="<td style='border: 2px black solid'>AACTot6</td>"
	table_data+="<td style='border: 2px black solid'>ActionLog</td>"
	table_data+="<td style='border: 2px black solid'>ActionNotes</td>"
	table_data+="<td style='border: 2px black solid'>AMPMReceived</td>"
	table_data+="<td style='border: 2px black solid'>AnalysisAssign</td>"
	table_data+="<td style='border: 2px black solid'>AnalysisATFChrgSt</td>"
	table_data+="<td style='border: 2px black solid'>AnalysisCarrierUsed</td>"
	table_data+="<td style='border: 2px black solid'>AnalysiscGMPChrg</td>"
	table_data+="<td style='border: 2px black solid'>AnalysiscGMPChrgSt</td>"
	table_data+="<td style='border: 2px black solid'>AnalysisDEAChrgSt</td>"
	table_data+="<td style='border: 2px black solid'>AnalysisDept</td>"
	table_data+="<td style='border: 2px black solid'>AnalysisDisc</td>"
	table_data+="<td style='border: 2px black solid'>AnalysisDiscSt</td>"
	table_data+="<td style='border: 2px black solid'>AnalysisDiscStat</td>"
	table_data+="<td style='border: 2px black solid'>AnalysisHazChrg</td>"
	table_data+="<td style='border: 2px black solid'>AnalysisHazChrgSt</td>"
	table_data+="<td style='border: 2px black solid'>AnalysisInstr</td>"
	table_data+="<td style='border: 2px black solid'>AnalysisISOChrg</td>"
	table_data+="<td style='border: 2px black solid'>AnalysisISOChrgSt</td>"
	table_data+="<td style='border: 2px black solid'>AnalysisNum</td>"
	table_data+="<td style='border: 2px black solid'>AnalysisPrc</td>"
	table_data+="<td style='border: 2px black solid'>AnalysisPrcEnt</td>"
	table_data+="<td style='border: 2px black solid'>AnalysisPrcEntSt</td>"
	table_data+="<td style='border: 2px black solid'>AnalysisPrcSt</td>"
	table_data+="<td style='border: 2px black solid'>AnalysisPrioChrg</td>"
	table_data+="<td style='border: 2px black solid'>AnalysisPriority</td>"
	table_data+="<td style='border: 2px black solid'>AnalysisPrioSt</td>"
	table_data+="<td style='border: 2px black solid'>AnalysisQty</td>"
	table_data+="<td style='border: 2px black solid'>AnalysisQtyLab</td>"
	table_data+="<td style='border: 2px black solid'>AnalysisSamples</td>"
	table_data+="<td style='border: 2px black solid'>AnalysisSampleTypes</td>"
	table_data+="<td style='border: 2px black solid'>AnalysisSrvc</td>"
	table_data+="<td style='border: 2px black solid'>AnalysisTotal</td>"
	table_data+="<td style='border: 2px black solid'>AnalysisTotalwAddl</td>"
	table_data+="<td style='border: 2px black solid'>AnalysisType</td>"
	table_data+="<td style='border: 2px black solid'>AnlPVQty</td>"
	table_data+="<td style='border: 2px black solid'>AnlRunQty</td>"
	table_data+="<td style='border: 2px black solid'>AuthorDate</td>"
	table_data+="<td style='border: 2px black solid'>AuthorName</td>"
	table_data+="<td style='border: 2px black solid'>BillingCopyLab</td>"
	table_data+="<td style='border: 2px black solid'>BillingNotesText</td>"
	table_data+="<td style='border: 2px black solid'>cGMPChange</td>"
	table_data+="<td style='border: 2px black solid'>cGMPEnterPrc</td>"
	table_data+="<td style='border: 2px black solid'>CompanyName</td>"
	table_data+="<td style='border: 2px black solid'>ComplexProject</td>"
	table_data+="<td style='border: 2px black solid'>DateDue</td>"
	table_data+="<td style='border: 2px black solid'>DateReceived</td>"
	table_data+="<td style='border: 2px black solid'>DiscType</td>"
	table_data+="<td style='border: 2px black solid'>EditAuthors</td>"
	table_data+="<td style='border: 2px black solid'>EditDates</td>"
	table_data+="<td style='border: 2px black solid'>EditProjStatus</td>"
	table_data+="<td style='border: 2px black solid'>EmbeddedObjects</td>"
	table_data+="<td style='border: 2px black solid'>EnterDateDue</td>"
	table_data+="<td style='border: 2px black solid'>FamilyName</td>"
	table_data+="<td style='border: 2px black solid'>HazQty</td>"
	table_data+="<td style='border: 2px black solid'>InProjectTask</td>"
	table_data+="<td style='border: 2px black solid'>IsHighDEA</td>"
	table_data+="<td style='border: 2px black solid'>ISO</td>"
	table_data+="<td style='border: 2px black solid'>IsHighATF</td>"
	table_data+="<td style='border: 2px black solid'>ISOEnterPrc</td>"
	table_data+="<td style='border: 2px black solid'>LineItems</td>"
	table_data+="<td style='border: 2px black solid'>MethodServices</td>"
	table_data+="<td style='border: 2px black solid'>MethodServiceType</td>"
	table_data+="<td style='border: 2px black solid'>Options</td>"
	table_data+="<td style='border: 2px black solid'>OutSrcLocation</td>"
	table_data+="<td style='border: 2px black solid'>OutSrcMethod</td>"
	table_data+="<td style='border: 2px black solid'>OutSrcPONum</td>"
	table_data+="<td style='border: 2px black solid'>OutSrcTracking</td>"
	table_data+="<td style='border: 2px black solid'>OverridecGMP</td>"
	table_data+="<td style='border: 2px black solid'>OverrideISO</td>"
	table_data+="<td style='border: 2px black solid'>OverridePrc</td>"
	table_data+="<td style='border: 2px black solid'>PrelimDataCopyTo</td>"
	table_data+="<td style='border: 2px black solid'>PrelimDataSentBy</td>"
	table_data+="<td style='border: 2px black solid'>PrelimDataSentDate</td>"
	table_data+="<td style='border: 2px black solid'>PrelimDataSentMethod</td>"
	table_data+="<td style='border: 2px black solid'>PrelimDataSentTime</td>"
	table_data+="<td style='border: 2px black solid'>PrelimDataSentTo</td>"
	table_data+="<td style='border: 2px black solid'>ProjCanceled</td>"
	table_data+="<td style='border: 2px black solid'>ProjCancelStat</td>"
	table_data+="<td style='border: 2px black solid'>ProjCGMP</td>"
	table_data+="<td style='border: 2px black solid'>ProjDirector</td>"
	table_data+="<td style='border: 2px black solid'>ProjISO</td>"
	table_data+="<td style='border: 2px black solid'>ProjQADataRvw</td>"
	table_data+="<td style='border: 2px black solid'>ProjQARev</td>"
	table_data+="<td style='border: 2px black solid'>ProjReptWrtr</td>"
	table_data+="<td style='border: 2px black solid'>ProjStat</td>"
	table_data+="<td style='border: 2px black solid'>ProjStatus</td>"
	table_data+="<td style='border: 2px black solid'>ProjTechRev</td>"
	table_data+="<td style='border: 2px black solid'>ReptWrtrAssign</td>"
	table_data+="<td style='border: 2px black solid'>Revisions</td>"
	table_data+="<td style='border: 2px black solid'>SubAnalysisTotal</td>"
	table_data+="<td style='border: 2px black solid'>TechRevAssign</td>"
	table_data+="<td style='border: 2px black solid'>TotalBeforeDisco</td>"
	table_data+="<td style='border: 2px black solid'>trackLookup</td>"
	table_data+="<td style='border: 2px black solid'>TrackSelection</td>"
	table_data+="<td style='border: 2px black solid'>UniversalID</td>"
	table_data+="<td style='border: 2px black solid'>TurnaroundTextQuote100</td>"
	table_data+="<td style='border: 2px black solid'>TurnaroundTextQuote50</td>"
	table_data+="<td style='border: 2px black solid'>TurnaroundTextQuoteStd</td>"

	table_data+="</th>"

	print(len(myresult))
	for x in myresult:
		# print(x) 
		# writer.writerow(x)
		table_data+="<tr>"
		for i in range(133):
			table_data+="<td style='border: 2px black solid'>x[i]</td>"
		table_data+="</tr>"


	table_data="<table>"+table_data+"</table>"
	return render(request,'data/table.html',{'table_data':table_data})
def logout(request):
	auth_logout(request)
	return HttpResponseRedirect(reverse('login'))