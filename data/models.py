# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# class Analysis(models.Model):
#     analysisprojnumber = models.CharField(db_column='analysisProjNumber', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     docid = models.CharField(db_column='DocID', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     familyid = models.CharField(db_column='FamilyID', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     noteid = models.CharField(db_column='NoteID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     projid = models.CharField(db_column='ProjID', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     aacamt0 = models.CharField(db_column='AACAmt0', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacamt1 = models.CharField(db_column='AACAmt1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacamt2 = models.CharField(db_column='AACAmt2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacamt3 = models.CharField(db_column='AACAmt3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacamt4 = models.CharField(db_column='AACAmt4', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacamt5 = models.CharField(db_column='AACAmt5', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacamt6 = models.CharField(db_column='AACAmt6', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacdesc0 = models.CharField(db_column='AACDesc0', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     aacdesc1 = models.CharField(db_column='AACDesc1', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     aacdesc2 = models.CharField(db_column='AACDesc2', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     aacdesc3 = models.CharField(db_column='AACDesc3', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     aacdesc4 = models.CharField(db_column='AACDesc4', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     aacdesc5 = models.CharField(db_column='AACDesc5', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     aacdesc6 = models.CharField(db_column='AACDesc6', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     aacqty0 = models.CharField(db_column='AACQty0', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacqty1 = models.CharField(db_column='AACQty1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacqty2 = models.CharField(db_column='AACQty2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacqty3 = models.CharField(db_column='AACQty3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacqty4 = models.CharField(db_column='AACQty4', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacqty5 = models.CharField(db_column='AACQty5', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacqty6 = models.CharField(db_column='AACQty6', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aactot0 = models.CharField(db_column='AACTot0', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aactot1 = models.CharField(db_column='AACTot1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aactot2 = models.CharField(db_column='AACTot2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aactot3 = models.CharField(db_column='AACTot3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aactot4 = models.CharField(db_column='AACTot4', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aactot5 = models.CharField(db_column='AACTot5', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aactot6 = models.CharField(db_column='AACTot6', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     actionlog = models.TextField(db_column='ActionLog', blank=True, null=True)  # Field name made lowercase.
#     actionnotes = models.TextField(db_column='ActionNotes', blank=True, null=True)  # Field name made lowercase.
#     ampmreceived = models.CharField(db_column='AMPMReceived', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     analysisassign = models.TextField(db_column='AnalysisAssign', blank=True, null=True)  # Field name made lowercase.
#     analysisatfchrgst = models.TextField(db_column='AnalysisATFChrgSt', blank=True, null=True)  # Field name made lowercase.
#     analysiscarrierused = models.TextField(db_column='AnalysisCarrierUsed', blank=True, null=True)  # Field name made lowercase.
#     analysiscgmpchrg = models.TextField(db_column='AnalysiscGMPChrg', blank=True, null=True)  # Field name made lowercase.
#     analysiscgmpchrgst = models.TextField(db_column='AnalysiscGMPChrgSt', blank=True, null=True)  # Field name made lowercase.
#     analysisdeachrgst = models.TextField(db_column='AnalysisDEAChrgSt', blank=True, null=True)  # Field name made lowercase.
#     analysisdept = models.TextField(db_column='AnalysisDept', blank=True, null=True)  # Field name made lowercase.
#     analysisdisc = models.TextField(db_column='AnalysisDisc', blank=True, null=True)  # Field name made lowercase.
#     analysisdiscst = models.TextField(db_column='AnalysisDiscSt', blank=True, null=True)  # Field name made lowercase.
#     analysisdiscstat = models.TextField(db_column='AnalysisDiscStat', blank=True, null=True)  # Field name made lowercase.
#     analysishazchrg = models.TextField(db_column='AnalysisHazChrg', blank=True, null=True)  # Field name made lowercase.
#     analysishazchrgst = models.TextField(db_column='AnalysisHazChrgSt', blank=True, null=True)  # Field name made lowercase.
#     analysisinstr = models.TextField(db_column='AnalysisInstr', blank=True, null=True)  # Field name made lowercase.
#     analysisisochrg = models.TextField(db_column='AnalysisISOChrg', blank=True, null=True)  # Field name made lowercase.
#     analysisisochrgst = models.TextField(db_column='AnalysisISOChrgSt', blank=True, null=True)  # Field name made lowercase.
#     analysisnum = models.TextField(db_column='AnalysisNum', blank=True, null=True)  # Field name made lowercase.
#     analysisprc = models.TextField(db_column='AnalysisPrc', blank=True, null=True)  # Field name made lowercase.
#     analysisprcent = models.TextField(db_column='AnalysisPrcEnt', blank=True, null=True)  # Field name made lowercase.
#     analysisprcentst = models.TextField(db_column='AnalysisPrcEntSt', blank=True, null=True)  # Field name made lowercase.
#     analysisprcst = models.TextField(db_column='AnalysisPrcSt', blank=True, null=True)  # Field name made lowercase.
#     analysispriochrg = models.TextField(db_column='AnalysisPrioChrg', blank=True, null=True)  # Field name made lowercase.
#     analysispriority = models.TextField(db_column='AnalysisPriority', blank=True, null=True)  # Field name made lowercase.
#     analysispriost = models.TextField(db_column='AnalysisPrioSt', blank=True, null=True)  # Field name made lowercase.
#     analysisqty = models.TextField(db_column='AnalysisQty', blank=True, null=True)  # Field name made lowercase.
#     analysisqtylab = models.TextField(db_column='AnalysisQtyLab', blank=True, null=True)  # Field name made lowercase.
#     analysissamples = models.TextField(db_column='AnalysisSamples', blank=True, null=True)  # Field name made lowercase.
#     analysissampletypes = models.TextField(db_column='AnalysisSampleTypes', blank=True, null=True)  # Field name made lowercase.
#     analysissrvc = models.TextField(db_column='AnalysisSrvc', blank=True, null=True)  # Field name made lowercase.
#     analysisstandardrun = models.TextField(db_column='AnalysisStandardRun', blank=True, null=True)  # Field name made lowercase.
#     analysistotal = models.TextField(db_column='AnalysisTotal', blank=True, null=True)  # Field name made lowercase.
#     analysistotalwaddl = models.TextField(db_column='AnalysisTotalwAddl', blank=True, null=True)  # Field name made lowercase.
#     analysistype = models.TextField(db_column='AnalysisType', blank=True, null=True)  # Field name made lowercase.
#     anlpvqty = models.TextField(db_column='AnlPVQty', blank=True, null=True)  # Field name made lowercase.
#     anlrunqty = models.TextField(db_column='AnlRunQty', blank=True, null=True)  # Field name made lowercase.
#     authordate = models.TextField(db_column='AuthorDate', blank=True, null=True)  # Field name made lowercase.
#     authorname = models.TextField(db_column='AuthorName', blank=True, null=True)  # Field name made lowercase.
#     authors = models.TextField(db_column='Authors', blank=True, null=True)  # Field name made lowercase.
#     billingcopylab = models.TextField(db_column='BillingCopyLab', blank=True, null=True)  # Field name made lowercase.
#     billingnotes = models.TextField(db_column='BillingNotes', blank=True, null=True)  # Field name made lowercase.
#     billingnotestext = models.TextField(db_column='BillingNotesText', blank=True, null=True)  # Field name made lowercase.
#     cgmpchange = models.TextField(db_column='cGMPChange', blank=True, null=True)  # Field name made lowercase.
#     cgmpenterprc = models.TextField(db_column='cGMPEnterPrc', blank=True, null=True)  # Field name made lowercase.
#     companyname = models.TextField(db_column='CompanyName', blank=True, null=True)  # Field name made lowercase.
#     complexproject = models.TextField(db_column='ComplexProject', blank=True, null=True)  # Field name made lowercase.
#     created = models.TextField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
#     datedue = models.TextField(db_column='DateDue', blank=True, null=True)  # Field name made lowercase.
#     datereceived = models.TextField(db_column='DateReceived', blank=True, null=True)  # Field name made lowercase.
#     disctype = models.TextField(db_column='DiscType', blank=True, null=True)  # Field name made lowercase.
#     editauthors = models.TextField(db_column='EditAuthors', blank=True, null=True)  # Field name made lowercase.
#     editdates = models.TextField(db_column='EditDates', blank=True, null=True)  # Field name made lowercase.
#     editprojstatus = models.TextField(db_column='EditProjStatus', blank=True, null=True)  # Field name made lowercase.
#     embeddedobjects = models.TextField(db_column='EmbeddedObjects', blank=True, null=True)  # Field name made lowercase.
#     enterdatedue = models.TextField(db_column='EnterDateDue', blank=True, null=True)  # Field name made lowercase.
#     familyname = models.TextField(db_column='FamilyName', blank=True, null=True)  # Field name made lowercase.
#     hazqty = models.TextField(db_column='HazQty', blank=True, null=True)  # Field name made lowercase.
#     holddata = models.TextField(db_column='HoldData', blank=True, null=True)  # Field name made lowercase.
#     inprojecttask = models.TextField(db_column='InProjectTask', blank=True, null=True)  # Field name made lowercase.
#     invfamilyid = models.TextField(db_column='InvFamilyID', blank=True, null=True)  # Field name made lowercase.
#     invfamilyname = models.TextField(db_column='InvFamilyName', blank=True, null=True)  # Field name made lowercase.
#     ishighdea = models.TextField(db_column='IsHighDEA', blank=True, null=True)  # Field name made lowercase.
#     iso = models.TextField(db_column='ISO', blank=True, null=True)  # Field name made lowercase.
#     ishighatf = models.TextField(db_column='IsHighATF', blank=True, null=True)  # Field name made lowercase.
#     isoenterprc = models.TextField(db_column='ISOEnterPrc', blank=True, null=True)  # Field name made lowercase.
#     lastaccessed = models.TextField(db_column='LastAccessed', blank=True, null=True)  # Field name made lowercase.
#     lastmodified = models.TextField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.
#     lineitems = models.TextField(db_column='LineItems', blank=True, null=True)  # Field name made lowercase.
#     locationid = models.TextField(db_column='LocationID', blank=True, null=True)  # Field name made lowercase.
#     methodservices = models.TextField(db_column='MethodServices', blank=True, null=True)  # Field name made lowercase.
#     methodservicetype = models.TextField(db_column='MethodServiceType', blank=True, null=True)  # Field name made lowercase.
#     options = models.TextField(db_column='Options', blank=True, null=True)  # Field name made lowercase.
#     outsrclocation = models.TextField(db_column='OutSrcLocation', blank=True, null=True)  # Field name made lowercase.
#     outsrcmethod = models.TextField(db_column='OutSrcMethod', blank=True, null=True)  # Field name made lowercase.
#     outsrcponum = models.TextField(db_column='OutSrcPONum', blank=True, null=True)  # Field name made lowercase.
#     outsrctracking = models.TextField(db_column='OutSrcTracking', blank=True, null=True)  # Field name made lowercase.
#     overridecgmp = models.TextField(db_column='OverridecGMP', blank=True, null=True)  # Field name made lowercase.
#     overrideiso = models.TextField(db_column='OverrideISO', blank=True, null=True)  # Field name made lowercase.
#     overrideprc = models.TextField(db_column='OverridePrc', blank=True, null=True)  # Field name made lowercase.
#     prelimdatacopyto = models.TextField(db_column='PrelimDataCopyTo', blank=True, null=True)  # Field name made lowercase.
#     prelimdatasentby = models.TextField(db_column='PrelimDataSentBy', blank=True, null=True)  # Field name made lowercase.
#     prelimdatasentdate = models.TextField(db_column='PrelimDataSentDate', blank=True, null=True)  # Field name made lowercase.
#     prelimdatasentmethod = models.TextField(db_column='PrelimDataSentMethod', blank=True, null=True)  # Field name made lowercase.
#     prelimdatasenttime = models.TextField(db_column='PrelimDataSentTime', blank=True, null=True)  # Field name made lowercase.
#     prelimdatasentto = models.TextField(db_column='PrelimDataSentTo', blank=True, null=True)  # Field name made lowercase.
#     projcanceled = models.TextField(db_column='ProjCanceled', blank=True, null=True)  # Field name made lowercase.
#     projcancelstat = models.TextField(db_column='ProjCancelStat', blank=True, null=True)  # Field name made lowercase.
#     projcgmp = models.TextField(db_column='ProjCGMP', blank=True, null=True)  # Field name made lowercase.
#     projdirector = models.TextField(db_column='ProjDirector', blank=True, null=True)  # Field name made lowercase.
#     projevent = models.TextField(db_column='ProjEvent', blank=True, null=True)  # Field name made lowercase.
#     projiso = models.TextField(db_column='ProjISO', blank=True, null=True)  # Field name made lowercase.
#     projqadatarvw = models.TextField(db_column='ProjQADataRvw', blank=True, null=True)  # Field name made lowercase.
#     projqarev = models.TextField(db_column='ProjQARev', blank=True, null=True)  # Field name made lowercase.
#     projreptwrtr = models.TextField(db_column='ProjReptWrtr', blank=True, null=True)  # Field name made lowercase.
#     projstat = models.TextField(db_column='ProjStat', blank=True, null=True)  # Field name made lowercase.
#     projstatus = models.TextField(db_column='ProjStatus', blank=True, null=True)  # Field name made lowercase.
#     projtechrev = models.TextField(db_column='ProjTechRev', blank=True, null=True)  # Field name made lowercase.
#     reptwrtrassign = models.TextField(db_column='ReptWrtrAssign', blank=True, null=True)  # Field name made lowercase.
#     revisions = models.TextField(db_column='Revisions', blank=True, null=True)  # Field name made lowercase.
#     subanalysistotal = models.TextField(db_column='SubAnalysisTotal', blank=True, null=True)  # Field name made lowercase.
#     techrevassign = models.TextField(db_column='TechRevAssign', blank=True, null=True)  # Field name made lowercase.
#     totalbeforedisco = models.TextField(db_column='TotalBeforeDisco', blank=True, null=True)  # Field name made lowercase.
#     tracklookup = models.TextField(db_column='trackLookup', blank=True, null=True)  # Field name made lowercase.
#     trackselection = models.TextField(db_column='TrackSelection', blank=True, null=True)  # Field name made lowercase.
#     universalid = models.TextField(db_column='UniversalID', blank=True, null=True)  # Field name made lowercase.
#     updatedby = models.TextField(db_column='UpdatedBy', blank=True, null=True)  # Field name made lowercase.
#     validateevent = models.TextField(db_column='ValidateEvent', blank=True, null=True)  # Field name made lowercase.
#     validatenow = models.TextField(db_column='ValidateNow', blank=True, null=True)  # Field name made lowercase.
#     turnaroundtextquote100 = models.TextField(db_column='TurnaroundTextQuote100', blank=True, null=True)  # Field name made lowercase.
#     turnaroundtextquote50 = models.TextField(db_column='TurnaroundTextQuote50', blank=True, null=True)  # Field name made lowercase.
#     turnaroundtextquotestd = models.TextField(db_column='TurnaroundTextQuoteStd', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         db_table = 'analysis'


# class Analysisarch(models.Model):
#     analysisprojnumber = models.CharField(db_column='analysisProjNumber', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     docid = models.CharField(db_column='DocID', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     familyid = models.CharField(db_column='FamilyID', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     noteid = models.CharField(db_column='NoteID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     projid = models.CharField(db_column='ProjID', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     aacamt0 = models.CharField(db_column='AACAmt0', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacamt1 = models.CharField(db_column='AACAmt1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacamt2 = models.CharField(db_column='AACAmt2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacamt3 = models.CharField(db_column='AACAmt3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacamt4 = models.CharField(db_column='AACAmt4', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacamt5 = models.CharField(db_column='AACAmt5', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacamt6 = models.CharField(db_column='AACAmt6', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacdesc0 = models.CharField(db_column='AACDesc0', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     aacdesc1 = models.CharField(db_column='AACDesc1', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     aacdesc2 = models.CharField(db_column='AACDesc2', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     aacdesc3 = models.CharField(db_column='AACDesc3', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     aacdesc4 = models.CharField(db_column='AACDesc4', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     aacdesc5 = models.CharField(db_column='AACDesc5', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     aacdesc6 = models.CharField(db_column='AACDesc6', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     aacqty0 = models.CharField(db_column='AACQty0', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacqty1 = models.CharField(db_column='AACQty1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacqty2 = models.CharField(db_column='AACQty2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacqty3 = models.CharField(db_column='AACQty3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacqty4 = models.CharField(db_column='AACQty4', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacqty5 = models.CharField(db_column='AACQty5', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacqty6 = models.CharField(db_column='AACQty6', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aactot0 = models.CharField(db_column='AACTot0', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aactot1 = models.CharField(db_column='AACTot1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aactot2 = models.CharField(db_column='AACTot2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aactot3 = models.CharField(db_column='AACTot3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aactot4 = models.CharField(db_column='AACTot4', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aactot5 = models.CharField(db_column='AACTot5', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aactot6 = models.CharField(db_column='AACTot6', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     actionlog = models.TextField(db_column='ActionLog', blank=True, null=True)  # Field name made lowercase.
#     actionnotes = models.TextField(db_column='ActionNotes', blank=True, null=True)  # Field name made lowercase.
#     ampmreceived = models.CharField(db_column='AMPMReceived', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     analysisassign = models.TextField(db_column='AnalysisAssign', blank=True, null=True)  # Field name made lowercase.
#     analysisatfchrgst = models.TextField(db_column='AnalysisATFChrgSt', blank=True, null=True)  # Field name made lowercase.
#     analysiscarrierused = models.TextField(db_column='AnalysisCarrierUsed', blank=True, null=True)  # Field name made lowercase.
#     analysiscgmpchrg = models.TextField(db_column='AnalysiscGMPChrg', blank=True, null=True)  # Field name made lowercase.
#     analysiscgmpchrgst = models.TextField(db_column='AnalysiscGMPChrgSt', blank=True, null=True)  # Field name made lowercase.
#     analysisdeachrgst = models.TextField(db_column='AnalysisDEAChrgSt', blank=True, null=True)  # Field name made lowercase.
#     analysisdept = models.TextField(db_column='AnalysisDept', blank=True, null=True)  # Field name made lowercase.
#     analysisdisc = models.TextField(db_column='AnalysisDisc', blank=True, null=True)  # Field name made lowercase.
#     analysisdiscst = models.TextField(db_column='AnalysisDiscSt', blank=True, null=True)  # Field name made lowercase.
#     analysisdiscstat = models.TextField(db_column='AnalysisDiscStat', blank=True, null=True)  # Field name made lowercase.
#     analysishazchrg = models.TextField(db_column='AnalysisHazChrg', blank=True, null=True)  # Field name made lowercase.
#     analysishazchrgst = models.TextField(db_column='AnalysisHazChrgSt', blank=True, null=True)  # Field name made lowercase.
#     analysisinstr = models.TextField(db_column='AnalysisInstr', blank=True, null=True)  # Field name made lowercase.
#     analysisisochrg = models.TextField(db_column='AnalysisISOChrg', blank=True, null=True)  # Field name made lowercase.
#     analysisisochrgst = models.TextField(db_column='AnalysisISOChrgSt', blank=True, null=True)  # Field name made lowercase.
#     analysisnum = models.TextField(db_column='AnalysisNum', blank=True, null=True)  # Field name made lowercase.
#     analysisprc = models.TextField(db_column='AnalysisPrc', blank=True, null=True)  # Field name made lowercase.
#     analysisprcent = models.TextField(db_column='AnalysisPrcEnt', blank=True, null=True)  # Field name made lowercase.
#     analysisprcentst = models.TextField(db_column='AnalysisPrcEntSt', blank=True, null=True)  # Field name made lowercase.
#     analysisprcst = models.TextField(db_column='AnalysisPrcSt', blank=True, null=True)  # Field name made lowercase.
#     analysispriochrg = models.TextField(db_column='AnalysisPrioChrg', blank=True, null=True)  # Field name made lowercase.
#     analysispriority = models.TextField(db_column='AnalysisPriority', blank=True, null=True)  # Field name made lowercase.
#     analysispriost = models.TextField(db_column='AnalysisPrioSt', blank=True, null=True)  # Field name made lowercase.
#     analysisqty = models.TextField(db_column='AnalysisQty', blank=True, null=True)  # Field name made lowercase.
#     analysisqtylab = models.TextField(db_column='AnalysisQtyLab', blank=True, null=True)  # Field name made lowercase.
#     analysissamples = models.TextField(db_column='AnalysisSamples', blank=True, null=True)  # Field name made lowercase.
#     analysissampletypes = models.TextField(db_column='AnalysisSampleTypes', blank=True, null=True)  # Field name made lowercase.
#     analysissrvc = models.TextField(db_column='AnalysisSrvc', blank=True, null=True)  # Field name made lowercase.
#     analysisstandardrun = models.TextField(db_column='AnalysisStandardRun', blank=True, null=True)  # Field name made lowercase.
#     analysistotal = models.TextField(db_column='AnalysisTotal', blank=True, null=True)  # Field name made lowercase.
#     analysistotalwaddl = models.TextField(db_column='AnalysisTotalwAddl', blank=True, null=True)  # Field name made lowercase.
#     analysistype = models.TextField(db_column='AnalysisType', blank=True, null=True)  # Field name made lowercase.
#     anlpvqty = models.TextField(db_column='AnlPVQty', blank=True, null=True)  # Field name made lowercase.
#     anlrunqty = models.TextField(db_column='AnlRunQty', blank=True, null=True)  # Field name made lowercase.
#     authordate = models.TextField(db_column='AuthorDate', blank=True, null=True)  # Field name made lowercase.
#     authorname = models.TextField(db_column='AuthorName', blank=True, null=True)  # Field name made lowercase.
#     authors = models.TextField(db_column='Authors', blank=True, null=True)  # Field name made lowercase.
#     billingcopylab = models.TextField(db_column='BillingCopyLab', blank=True, null=True)  # Field name made lowercase.
#     billingnotes = models.TextField(db_column='BillingNotes', blank=True, null=True)  # Field name made lowercase.
#     billingnotestext = models.TextField(db_column='BillingNotesText', blank=True, null=True)  # Field name made lowercase.
#     cgmpchange = models.TextField(db_column='cGMPChange', blank=True, null=True)  # Field name made lowercase.
#     cgmpenterprc = models.TextField(db_column='cGMPEnterPrc', blank=True, null=True)  # Field name made lowercase.
#     companyname = models.TextField(db_column='CompanyName', blank=True, null=True)  # Field name made lowercase.
#     complexproject = models.TextField(db_column='ComplexProject', blank=True, null=True)  # Field name made lowercase.
#     created = models.TextField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
#     datedue = models.TextField(db_column='DateDue', blank=True, null=True)  # Field name made lowercase.
#     datereceived = models.TextField(db_column='DateReceived', blank=True, null=True)  # Field name made lowercase.
#     disctype = models.TextField(db_column='DiscType', blank=True, null=True)  # Field name made lowercase.
#     editauthors = models.TextField(db_column='EditAuthors', blank=True, null=True)  # Field name made lowercase.
#     editdates = models.TextField(db_column='EditDates', blank=True, null=True)  # Field name made lowercase.
#     editprojstatus = models.TextField(db_column='EditProjStatus', blank=True, null=True)  # Field name made lowercase.
#     embeddedobjects = models.TextField(db_column='EmbeddedObjects', blank=True, null=True)  # Field name made lowercase.
#     enterdatedue = models.TextField(db_column='EnterDateDue', blank=True, null=True)  # Field name made lowercase.
#     familyname = models.TextField(db_column='FamilyName', blank=True, null=True)  # Field name made lowercase.
#     hazqty = models.TextField(db_column='HazQty', blank=True, null=True)  # Field name made lowercase.
#     holddata = models.TextField(db_column='HoldData', blank=True, null=True)  # Field name made lowercase.
#     inprojecttask = models.TextField(db_column='InProjectTask', blank=True, null=True)  # Field name made lowercase.
#     invfamilyid = models.TextField(db_column='InvFamilyID', blank=True, null=True)  # Field name made lowercase.
#     invfamilyname = models.TextField(db_column='InvFamilyName', blank=True, null=True)  # Field name made lowercase.
#     ishighdea = models.TextField(db_column='IsHighDEA', blank=True, null=True)  # Field name made lowercase.
#     iso = models.TextField(db_column='ISO', blank=True, null=True)  # Field name made lowercase.
#     ishighatf = models.TextField(db_column='IsHighATF', blank=True, null=True)  # Field name made lowercase.
#     isoenterprc = models.TextField(db_column='ISOEnterPrc', blank=True, null=True)  # Field name made lowercase.
#     lastaccessed = models.TextField(db_column='LastAccessed', blank=True, null=True)  # Field name made lowercase.
#     lastmodified = models.TextField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.
#     lineitems = models.TextField(db_column='LineItems', blank=True, null=True)  # Field name made lowercase.
#     locationid = models.TextField(db_column='LocationID', blank=True, null=True)  # Field name made lowercase.
#     methodservices = models.TextField(db_column='MethodServices', blank=True, null=True)  # Field name made lowercase.
#     methodservicetype = models.TextField(db_column='MethodServiceType', blank=True, null=True)  # Field name made lowercase.
#     options = models.TextField(db_column='Options', blank=True, null=True)  # Field name made lowercase.
#     outsrclocation = models.TextField(db_column='OutSrcLocation', blank=True, null=True)  # Field name made lowercase.
#     outsrcmethod = models.TextField(db_column='OutSrcMethod', blank=True, null=True)  # Field name made lowercase.
#     outsrcponum = models.TextField(db_column='OutSrcPONum', blank=True, null=True)  # Field name made lowercase.
#     outsrctracking = models.TextField(db_column='OutSrcTracking', blank=True, null=True)  # Field name made lowercase.
#     overridecgmp = models.TextField(db_column='OverridecGMP', blank=True, null=True)  # Field name made lowercase.
#     overrideiso = models.TextField(db_column='OverrideISO', blank=True, null=True)  # Field name made lowercase.
#     overrideprc = models.TextField(db_column='OverridePrc', blank=True, null=True)  # Field name made lowercase.
#     prelimdatacopyto = models.TextField(db_column='PrelimDataCopyTo', blank=True, null=True)  # Field name made lowercase.
#     prelimdatasentby = models.TextField(db_column='PrelimDataSentBy', blank=True, null=True)  # Field name made lowercase.
#     prelimdatasentdate = models.TextField(db_column='PrelimDataSentDate', blank=True, null=True)  # Field name made lowercase.
#     prelimdatasentmethod = models.TextField(db_column='PrelimDataSentMethod', blank=True, null=True)  # Field name made lowercase.
#     prelimdatasenttime = models.TextField(db_column='PrelimDataSentTime', blank=True, null=True)  # Field name made lowercase.
#     prelimdatasentto = models.TextField(db_column='PrelimDataSentTo', blank=True, null=True)  # Field name made lowercase.
#     projcanceled = models.TextField(db_column='ProjCanceled', blank=True, null=True)  # Field name made lowercase.
#     projcancelstat = models.TextField(db_column='ProjCancelStat', blank=True, null=True)  # Field name made lowercase.
#     projcgmp = models.TextField(db_column='ProjCGMP', blank=True, null=True)  # Field name made lowercase.
#     projdirector = models.TextField(db_column='ProjDirector', blank=True, null=True)  # Field name made lowercase.
#     projevent = models.TextField(db_column='ProjEvent', blank=True, null=True)  # Field name made lowercase.
#     projiso = models.TextField(db_column='ProjISO', blank=True, null=True)  # Field name made lowercase.
#     projqadatarvw = models.TextField(db_column='ProjQADataRvw', blank=True, null=True)  # Field name made lowercase.
#     projqarev = models.TextField(db_column='ProjQARev', blank=True, null=True)  # Field name made lowercase.
#     projreptwrtr = models.TextField(db_column='ProjReptWrtr', blank=True, null=True)  # Field name made lowercase.
#     projstat = models.TextField(db_column='ProjStat', blank=True, null=True)  # Field name made lowercase.
#     projstatus = models.TextField(db_column='ProjStatus', blank=True, null=True)  # Field name made lowercase.
#     projtechrev = models.TextField(db_column='ProjTechRev', blank=True, null=True)  # Field name made lowercase.
#     reptwrtrassign = models.TextField(db_column='ReptWrtrAssign', blank=True, null=True)  # Field name made lowercase.
#     revisions = models.TextField(db_column='Revisions', blank=True, null=True)  # Field name made lowercase.
#     subanalysistotal = models.TextField(db_column='SubAnalysisTotal', blank=True, null=True)  # Field name made lowercase.
#     techrevassign = models.TextField(db_column='TechRevAssign', blank=True, null=True)  # Field name made lowercase.
#     totalbeforedisco = models.TextField(db_column='TotalBeforeDisco', blank=True, null=True)  # Field name made lowercase.
#     tracklookup = models.TextField(db_column='trackLookup', blank=True, null=True)  # Field name made lowercase.
#     trackselection = models.TextField(db_column='TrackSelection', blank=True, null=True)  # Field name made lowercase.
#     universalid = models.TextField(db_column='UniversalID', blank=True, null=True)  # Field name made lowercase.
#     updatedby = models.TextField(db_column='UpdatedBy', blank=True, null=True)  # Field name made lowercase.
#     validateevent = models.TextField(db_column='ValidateEvent', blank=True, null=True)  # Field name made lowercase.
#     validatenow = models.TextField(db_column='ValidateNow', blank=True, null=True)  # Field name made lowercase.
#     turnaroundtextquote100 = models.TextField(db_column='TurnaroundTextQuote100', blank=True, null=True)  # Field name made lowercase.
#     turnaroundtextquote50 = models.TextField(db_column='TurnaroundTextQuote50', blank=True, null=True)  # Field name made lowercase.
#     turnaroundtextquotestd = models.TextField(db_column='TurnaroundTextQuoteStd', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         db_table = 'analysisarch'


# class Analysisn1(models.Model):
#     analysisprojnumber = models.CharField(db_column='analysisProjNumber', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     docid = models.CharField(db_column='DocID', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     familyid = models.CharField(db_column='FamilyID', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     noteid = models.CharField(db_column='NoteID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     projid = models.CharField(db_column='ProjID', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     locationid = models.CharField(db_column='LocationID', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     aacamt0 = models.CharField(db_column='AACAmt0', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacamt1 = models.CharField(db_column='AACAmt1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacamt2 = models.CharField(db_column='AACAmt2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacamt3 = models.CharField(db_column='AACAmt3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacamt4 = models.CharField(db_column='AACAmt4', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacamt5 = models.CharField(db_column='AACAmt5', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacamt6 = models.CharField(db_column='AACAmt6', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacdesc0 = models.CharField(db_column='AACDesc0', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     aacdesc1 = models.CharField(db_column='AACDesc1', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     aacdesc2 = models.CharField(db_column='AACDesc2', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     aacdesc3 = models.CharField(db_column='AACDesc3', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     aacdesc4 = models.CharField(db_column='AACDesc4', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     aacdesc5 = models.CharField(db_column='AACDesc5', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     aacdesc6 = models.CharField(db_column='AACDesc6', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     aacqty0 = models.CharField(db_column='AACQty0', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacqty1 = models.CharField(db_column='AACQty1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacqty2 = models.CharField(db_column='AACQty2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacqty3 = models.CharField(db_column='AACQty3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacqty4 = models.CharField(db_column='AACQty4', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacqty5 = models.CharField(db_column='AACQty5', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aacqty6 = models.CharField(db_column='AACQty6', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aactot0 = models.CharField(db_column='AACTot0', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aactot1 = models.CharField(db_column='AACTot1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aactot2 = models.CharField(db_column='AACTot2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aactot3 = models.CharField(db_column='AACTot3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aactot4 = models.CharField(db_column='AACTot4', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aactot5 = models.CharField(db_column='AACTot5', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aactot6 = models.CharField(db_column='AACTot6', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     actionlog = models.TextField(db_column='ActionLog', blank=True, null=True)  # Field name made lowercase.
#     actionnotes = models.TextField(db_column='ActionNotes', blank=True, null=True)  # Field name made lowercase.
#     ampmreceived = models.CharField(db_column='AMPMReceived', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     analysisassign = models.CharField(db_column='AnalysisAssign', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     analysisatfchrgst = models.CharField(db_column='AnalysisATFChrgSt', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     analysiscarrierused = models.CharField(db_column='AnalysisCarrierUsed', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     analysiscgmpchrg = models.CharField(db_column='AnalysiscGMPChrg', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     analysiscgmpchrgst = models.CharField(db_column='AnalysiscGMPChrgSt', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     analysisdeachrgst = models.CharField(db_column='AnalysisDEAChrgSt', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     analysisdept = models.CharField(db_column='AnalysisDept', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     analysisdisc = models.CharField(db_column='AnalysisDisc', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     analysisdiscst = models.CharField(db_column='AnalysisDiscSt', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     analysisdiscstat = models.CharField(db_column='AnalysisDiscStat', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     analysishazchrg = models.CharField(db_column='AnalysisHazChrg', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     analysishazchrgst = models.CharField(db_column='AnalysisHazChrgSt', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     analysisinstr = models.TextField(db_column='AnalysisInstr', blank=True, null=True)  # Field name made lowercase.
#     analysisisochrg = models.CharField(db_column='AnalysisISOChrg', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     analysisisochrgst = models.CharField(db_column='AnalysisISOChrgSt', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     analysisnum = models.CharField(db_column='AnalysisNum', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     analysisprc = models.CharField(db_column='AnalysisPrc', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     analysisprcent = models.CharField(db_column='AnalysisPrcEnt', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     analysisprcentst = models.CharField(db_column='AnalysisPrcEntSt', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     analysisprcst = models.CharField(db_column='AnalysisPrcSt', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     analysispriochrg = models.CharField(db_column='AnalysisPrioChrg', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     analysispriority = models.CharField(db_column='AnalysisPriority', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     analysispriost = models.CharField(db_column='AnalysisPrioSt', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     analysisqty = models.CharField(db_column='AnalysisQty', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     analysisqtylab = models.CharField(db_column='AnalysisQtyLab', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     analysissamples = models.TextField(db_column='AnalysisSamples', blank=True, null=True)  # Field name made lowercase.
#     analysissampletypes = models.TextField(db_column='AnalysisSampleTypes', blank=True, null=True)  # Field name made lowercase.
#     analysissrvc = models.CharField(db_column='AnalysisSrvc', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     analysistotal = models.CharField(db_column='AnalysisTotal', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     analysistotalwaddl = models.CharField(db_column='AnalysisTotalwAddl', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     analysistype = models.CharField(db_column='AnalysisType', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     anlpvqty = models.CharField(db_column='AnlPVQty', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     anlrunqty = models.CharField(db_column='AnlRunQty', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     authordate = models.CharField(db_column='AuthorDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     authorname = models.CharField(db_column='AuthorName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     billingcopylab = models.CharField(db_column='BillingCopyLab', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     billingnotestext = models.TextField(db_column='BillingNotesText', blank=True, null=True)  # Field name made lowercase.
#     cgmpchange = models.CharField(db_column='cGMPChange', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     cgmpenterprc = models.CharField(db_column='cGMPEnterPrc', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     companyname = models.CharField(db_column='CompanyName', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     complexproject = models.CharField(db_column='ComplexProject', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     datedue = models.CharField(db_column='DateDue', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     datereceived = models.CharField(db_column='DateReceived', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     disctype = models.CharField(db_column='DiscType', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     editauthors = models.CharField(db_column='EditAuthors', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     editdates = models.CharField(db_column='EditDates', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editprojstatus = models.CharField(db_column='EditProjStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     embeddedobjects = models.TextField(db_column='EmbeddedObjects', blank=True, null=True)  # Field name made lowercase.
#     enterdatedue = models.CharField(db_column='EnterDateDue', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     familyname = models.CharField(db_column='FamilyName', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     hazqty = models.CharField(db_column='HazQty', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     inprojecttask = models.CharField(db_column='InProjectTask', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     ishighdea = models.CharField(db_column='IsHighDEA', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     iso = models.CharField(db_column='ISO', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     ishighatf = models.CharField(db_column='IsHighATF', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     isoenterprc = models.CharField(db_column='ISOEnterPrc', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     lineitems = models.CharField(db_column='LineItems', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     methodservices = models.CharField(db_column='MethodServices', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     methodservicetype = models.CharField(db_column='MethodServiceType', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     options = models.CharField(db_column='Options', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     outsrclocation = models.CharField(db_column='OutSrcLocation', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     outsrcmethod = models.CharField(db_column='OutSrcMethod', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     outsrcponum = models.CharField(db_column='OutSrcPONum', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     outsrctracking = models.CharField(db_column='OutSrcTracking', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     overridecgmp = models.CharField(db_column='OverridecGMP', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     overrideiso = models.CharField(db_column='OverrideISO', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     overrideprc = models.CharField(db_column='OverridePrc', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     prelimdatacopyto = models.CharField(db_column='PrelimDataCopyTo', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     prelimdatasentby = models.CharField(db_column='PrelimDataSentBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     prelimdatasentdate = models.CharField(db_column='PrelimDataSentDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     prelimdatasentmethod = models.CharField(db_column='PrelimDataSentMethod', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     prelimdatasenttime = models.CharField(db_column='PrelimDataSentTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     prelimdatasentto = models.CharField(db_column='PrelimDataSentTo', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     projcanceled = models.CharField(db_column='ProjCanceled', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     projcancelstat = models.CharField(db_column='ProjCancelStat', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     projcgmp = models.CharField(db_column='ProjCGMP', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     projdirector = models.CharField(db_column='ProjDirector', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     projiso = models.CharField(db_column='ProjISO', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     projqadatarvw = models.CharField(db_column='ProjQADataRvw', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     projqarev = models.CharField(db_column='ProjQARev', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     projreptwrtr = models.CharField(db_column='ProjReptWrtr', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     projstat = models.CharField(db_column='ProjStat', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     projstatus = models.CharField(db_column='ProjStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     projtechrev = models.CharField(db_column='ProjTechRev', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     reptwrtrassign = models.CharField(db_column='ReptWrtrAssign', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     revisions = models.CharField(db_column='Revisions', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     subanalysistotal = models.CharField(db_column='SubAnalysisTotal', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     techrevassign = models.CharField(db_column='TechRevAssign', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     totalbeforedisco = models.CharField(db_column='TotalBeforeDisco', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     tracklookup = models.CharField(db_column='trackLookup', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     trackselection = models.CharField(db_column='TrackSelection', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     universalid = models.CharField(db_column='UniversalID', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     turnaroundtextquote100 = models.TextField(db_column='TurnaroundTextQuote100', blank=True, null=True)  # Field name made lowercase.
#     turnaroundtextquote50 = models.TextField(db_column='TurnaroundTextQuote50', blank=True, null=True)  # Field name made lowercase.
#     turnaroundtextquotestd = models.TextField(db_column='TurnaroundTextQuoteStd', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         db_table = 'analysisn1'


# class Contacts(models.Model):
#     personid = models.CharField(db_column='PersonID', primary_key=True, max_length=50)  # Field name made lowercase.
#     companyid = models.CharField(db_column='CompanyID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     activitycomments = models.TextField(db_column='ActivityComments', blank=True, null=True)  # Field name made lowercase.
#     assistant = models.TextField(db_column='Assistant', blank=True, null=True)  # Field name made lowercase.
#     assistantphonenumber = models.TextField(db_column='AssistantPhoneNumber', blank=True, null=True)  # Field name made lowercase.
#     authordate = models.TextField(db_column='AuthorDate', blank=True, null=True)  # Field name made lowercase.
#     authorname = models.TextField(db_column='AuthorName', blank=True, null=True)  # Field name made lowercase.
#     authors = models.TextField(db_column='Authors', blank=True, null=True)  # Field name made lowercase.
#     carphonenumber = models.TextField(db_column='CarPhoneNumber', blank=True, null=True)  # Field name made lowercase.
#     city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.
#     comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
#     companyacctexec = models.TextField(db_column='CompanyAcctExec', blank=True, null=True)  # Field name made lowercase.
#     companyacctstatus = models.TextField(db_column='CompanyAcctStatus', blank=True, null=True)  # Field name made lowercase.
#     companyacctteam = models.TextField(db_column='CompanyAcctTeam', blank=True, null=True)  # Field name made lowercase.
#     companyindustry = models.TextField(db_column='CompanyIndustry', blank=True, null=True)  # Field name made lowercase.
#     companyname = models.TextField(db_column='CompanyName', blank=True, null=True)  # Field name made lowercase.
#     companynumber = models.TextField(db_column='CompanyNumber', blank=True, null=True)  # Field name made lowercase.
#     companyparent = models.TextField(db_column='CompanyParent', blank=True, null=True)  # Field name made lowercase.
#     companyphonenumber = models.TextField(db_column='CompanyPhoneNumber', blank=True, null=True)  # Field name made lowercase.
#     companyterritory = models.TextField(db_column='CompanyTerritory', blank=True, null=True)  # Field name made lowercase.
#     companytype = models.TextField(db_column='CompanyType', blank=True, null=True)  # Field name made lowercase.
#     country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase.
#     department = models.TextField(db_column='Department', blank=True, null=True)  # Field name made lowercase.
#     division = models.TextField(db_column='Division', blank=True, null=True)  # Field name made lowercase.
#     dob = models.TextField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
#     editauthors = models.TextField(db_column='EditAuthors', blank=True, null=True)  # Field name made lowercase.
#     editcount = models.TextField(db_column='EditCount', blank=True, null=True)  # Field name made lowercase.
#     editdatename = models.TextField(db_column='EditDateName', blank=True, null=True)  # Field name made lowercase.
#     editdates = models.TextField(db_column='EditDates', blank=True, null=True)  # Field name made lowercase.
#     edited = models.TextField(db_column='Edited', blank=True, null=True)  # Field name made lowercase.
#     editnames = models.TextField(db_column='EditNames', blank=True, null=True)  # Field name made lowercase.
#     familyid = models.TextField(db_column='FamilyID', blank=True, null=True)  # Field name made lowercase.
#     familyname = models.TextField(db_column='FamilyName', blank=True, null=True)  # Field name made lowercase.
#     firstmphone = models.TextField(db_column='FirstMPhone', blank=True, null=True)  # Field name made lowercase.
#     firstname = models.TextField(db_column='FirstName', blank=True, null=True)  # Field name made lowercase.
#     fullname = models.TextField(db_column='FullName', blank=True, null=True)  # Field name made lowercase.
#     homecarphonenumber = models.TextField(db_column='HomeCarPhoneNumber', blank=True, null=True)  # Field name made lowercase.
#     homecellphonenumber = models.TextField(db_column='HomeCellPhoneNumber', blank=True, null=True)  # Field name made lowercase.
#     homefaxphonenumber = models.TextField(db_column='HomeFAXPhoneNumber', blank=True, null=True)  # Field name made lowercase.
#     industrycode = models.TextField(db_column='IndustryCode', blank=True, null=True)  # Field name made lowercase.
#     interest = models.TextField(db_column='Interest', blank=True, null=True)  # Field name made lowercase.
#     jobtitle = models.TextField(db_column='JobTitle', blank=True, null=True)  # Field name made lowercase.
#     labelname = models.TextField(db_column='LabelName', blank=True, null=True)  # Field name made lowercase.
#     lastaccessed = models.TextField(db_column='LastAccessed', blank=True, null=True)  # Field name made lowercase.
#     lastmodified = models.TextField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.
#     lastmphone = models.TextField(db_column='LastMPhone', blank=True, null=True)  # Field name made lowercase.
#     lastname = models.TextField(db_column='LastName', blank=True, null=True)  # Field name made lowercase.
#     location = models.TextField(db_column='Location', blank=True, null=True)  # Field name made lowercase.
#     mailaddress = models.TextField(db_column='MailAddress', blank=True, null=True)  # Field name made lowercase.
#     maildomain = models.TextField(db_column='MailDomain', blank=True, null=True)  # Field name made lowercase.
#     mailinglist = models.TextField(db_column='MailingList', blank=True, null=True)  # Field name made lowercase.
#     mailname = models.TextField(db_column='MailName', blank=True, null=True)  # Field name made lowercase.
#     mailsystem = models.TextField(db_column='MailSystem', blank=True, null=True)  # Field name made lowercase.
#     manager = models.TextField(db_column='Manager', blank=True, null=True)  # Field name made lowercase.
#     middleinitial = models.TextField(db_column='MiddleInitial', blank=True, null=True)  # Field name made lowercase.
#     nickname = models.TextField(db_column='NickName', blank=True, null=True)  # Field name made lowercase.
#     office800phonenumber = models.TextField(db_column='Office800PhoneNumber', blank=True, null=True)  # Field name made lowercase.
#     officeaddress1 = models.TextField(db_column='OfficeAddress1', blank=True, null=True)  # Field name made lowercase.
#     officeaddress2 = models.TextField(db_column='OfficeAddress2', blank=True, null=True)  # Field name made lowercase.
#     officecity = models.TextField(db_column='OfficeCity', blank=True, null=True)  # Field name made lowercase.
#     officecountry = models.TextField(db_column='OfficeCountry', blank=True, null=True)  # Field name made lowercase.
#     officefaxphonenumber = models.TextField(db_column='OfficeFAXPhoneNumber', blank=True, null=True)  # Field name made lowercase.
#     officephonenumber = models.TextField(db_column='OfficePhoneNumber', blank=True, null=True)  # Field name made lowercase.
#     officestate = models.TextField(db_column='OfficeState', blank=True, null=True)  # Field name made lowercase.
#     officezip = models.TextField(db_column='OfficeZip', blank=True, null=True)  # Field name made lowercase.
#     omailaddress1 = models.TextField(db_column='OMailAddress1', blank=True, null=True)  # Field name made lowercase.
#     omailaddress2 = models.TextField(db_column='OMailAddress2', blank=True, null=True)  # Field name made lowercase.
#     omailcity = models.TextField(db_column='OMailCity', blank=True, null=True)  # Field name made lowercase.
#     omailcountry = models.TextField(db_column='OMailCountry', blank=True, null=True)  # Field name made lowercase.
#     omailstate = models.TextField(db_column='OMailState', blank=True, null=True)  # Field name made lowercase.
#     omailzip = models.TextField(db_column='OMailZip', blank=True, null=True)  # Field name made lowercase.
#     owners = models.TextField(db_column='Owners', blank=True, null=True)  # Field name made lowercase.
#     pagerphonenumber = models.TextField(db_column='PagerPhoneNumber', blank=True, null=True)  # Field name made lowercase.
#     person800phonenumber = models.TextField(db_column='Person800PhoneNumber', blank=True, null=True)  # Field name made lowercase.
#     personaddress1 = models.TextField(db_column='PersonAddress1', blank=True, null=True)  # Field name made lowercase.
#     personaddress2 = models.TextField(db_column='PersonAddress2', blank=True, null=True)  # Field name made lowercase.
#     personcity = models.TextField(db_column='PersonCity', blank=True, null=True)  # Field name made lowercase.
#     personcountry = models.TextField(db_column='PersonCountry', blank=True, null=True)  # Field name made lowercase.
#     personfaxphonenumber = models.TextField(db_column='PersonFAXPhoneNumber', blank=True, null=True)  # Field name made lowercase.
#     personnamelfm = models.TextField(db_column='PersonNameLFM', blank=True, null=True)  # Field name made lowercase.
#     personphonenumber = models.TextField(db_column='PersonPhoneNumber', blank=True, null=True)  # Field name made lowercase.
#     personstate = models.TextField(db_column='PersonState', blank=True, null=True)  # Field name made lowercase.
#     personzip = models.TextField(db_column='PersonZip', blank=True, null=True)  # Field name made lowercase.
#     phonenumber = models.TextField(db_column='PhoneNumber', blank=True, null=True)  # Field name made lowercase.
#     pmailaddress1 = models.TextField(db_column='PMailAddress1', blank=True, null=True)  # Field name made lowercase.
#     pmailaddress2 = models.TextField(db_column='PMailAddress2', blank=True, null=True)  # Field name made lowercase.
#     pmailcity = models.TextField(db_column='PMailCity', blank=True, null=True)  # Field name made lowercase.
#     pmailcountry = models.TextField(db_column='PMailCountry', blank=True, null=True)  # Field name made lowercase.
#     pmailstate = models.TextField(db_column='PMailState', blank=True, null=True)  # Field name made lowercase.
#     prefobjrepid = models.TextField(db_column='PrefObjRepID', blank=True, null=True)  # Field name made lowercase.
#     referralsource = models.TextField(db_column='ReferralSource', blank=True, null=True)  # Field name made lowercase.
#     referredby = models.TextField(db_column='ReferredBy', blank=True, null=True)  # Field name made lowercase.
#     rel = models.TextField(db_column='Rel', blank=True, null=True)  # Field name made lowercase.
#     relationships = models.TextField(db_column='Relationships', blank=True, null=True)  # Field name made lowercase.
#     responsibility = models.TextField(db_column='Responsibility', blank=True, null=True)  # Field name made lowercase.
#     salutation = models.TextField(db_column='Salutation', blank=True, null=True)  # Field name made lowercase.
#     state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase.
#     status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
#     streetaddress = models.TextField(db_column='StreetAddress', blank=True, null=True)  # Field name made lowercase.
#     type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
#     universalid = models.TextField(db_column='UniversalID', blank=True, null=True)  # Field name made lowercase.
#     usernamelist = models.TextField(db_column='UserNameList', blank=True, null=True)  # Field name made lowercase.
#     usernameslist_1 = models.TextField(db_column='UserNamesList_1', blank=True, null=True)  # Field name made lowercase.
#     zip = models.TextField(db_column='Zip', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         db_table = 'contacts'


# class Contactsn1(models.Model):
#     personid = models.CharField(db_column='PersonID', primary_key=True, max_length=50)  # Field name made lowercase.
#     companyid = models.CharField(db_column='CompanyID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     familyid = models.CharField(db_column='FamilyID', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     activitycomments = models.TextField(db_column='ActivityComments', blank=True, null=True)  # Field name made lowercase.
#     assistant = models.CharField(db_column='Assistant', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     assistantphonenumber = models.CharField(db_column='AssistantPhoneNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     carphonenumber = models.CharField(db_column='CarPhoneNumber', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     city = models.CharField(db_column='City', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     companyacctstatus = models.CharField(db_column='CompanyAcctStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     companyparent = models.CharField(db_column='CompanyParent', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     companyphonenumber = models.CharField(db_column='CompanyPhoneNumber', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     country = models.CharField(db_column='Country', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     department = models.CharField(db_column='Department', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     division = models.CharField(db_column='Division', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     dob = models.CharField(db_column='DOB', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     familyname = models.TextField(db_column='FamilyName', blank=True, null=True)  # Field name made lowercase.
#     homecellphonenumber = models.CharField(db_column='HomeCellPhoneNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     office800phonenumber = models.TextField(db_column='Office800PhoneNumber', blank=True, null=True)  # Field name made lowercase.
#     firstmphone = models.CharField(db_column='FirstMPhone', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     firstname = models.CharField(db_column='FirstName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     fullname = models.TextField(db_column='FullName', blank=True, null=True)  # Field name made lowercase.
#     homecarphonenumber = models.CharField(db_column='HomeCarPhoneNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     homefaxphonenumber = models.CharField(db_column='HomeFAXPhoneNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     interest = models.CharField(db_column='Interest', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     jobtitle = models.CharField(db_column='JobTitle', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     labelname = models.CharField(db_column='LabelName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     lastmphone = models.CharField(db_column='LastMPhone', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     lastname = models.CharField(db_column='LastName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     mailaddress = models.TextField(db_column='MailAddress', blank=True, null=True)  # Field name made lowercase.
#     maildomain = models.CharField(db_column='MailDomain', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     mailinglist = models.TextField(db_column='MailingList', blank=True, null=True)  # Field name made lowercase.
#     mailname = models.TextField(db_column='MailName', blank=True, null=True)  # Field name made lowercase.
#     mailsystem = models.CharField(db_column='MailSystem', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     manager = models.CharField(db_column='Manager', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     middleinitial = models.CharField(db_column='MiddleInitial', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     nickname = models.CharField(db_column='NickName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     officeaddress1 = models.TextField(db_column='OfficeAddress1', blank=True, null=True)  # Field name made lowercase.
#     officeaddress2 = models.CharField(db_column='OfficeAddress2', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     officecity = models.CharField(db_column='OfficeCity', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     officecountry = models.CharField(db_column='OfficeCountry', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     officefaxphonenumber = models.CharField(db_column='OfficeFAXPhoneNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     officephonenumber = models.CharField(db_column='OfficePhoneNumber', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     officestate = models.CharField(db_column='OfficeState', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     officezip = models.CharField(db_column='OfficeZip', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     omailaddress1 = models.CharField(db_column='OMailAddress1', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     omailaddress2 = models.CharField(db_column='OMailAddress2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     omailcity = models.CharField(db_column='OMailCity', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     omailcountry = models.CharField(db_column='OMailCountry', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     omailstate = models.CharField(db_column='OMailState', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     omailzip = models.CharField(db_column='OMailZip', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     owners = models.CharField(db_column='Owners', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     pagerphonenumber = models.CharField(db_column='PagerPhoneNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     person800phonenumber = models.CharField(db_column='Person800PhoneNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     personaddress1 = models.CharField(db_column='PersonAddress1', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     personaddress2 = models.CharField(db_column='PersonAddress2', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     personcity = models.CharField(db_column='PersonCity', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     personcountry = models.CharField(db_column='PersonCountry', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     personfaxphonenumber = models.CharField(db_column='PersonFAXPhoneNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     personnamelfm = models.CharField(db_column='PersonNameLFM', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     personphonenumber = models.CharField(db_column='PersonPhoneNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     personstate = models.CharField(db_column='PersonState', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     personzip = models.CharField(db_column='PersonZip', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     phonenumber = models.CharField(db_column='PhoneNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     pmailaddress1 = models.CharField(db_column='PMailAddress1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     pmailaddress2 = models.CharField(db_column='PMailAddress2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     pmailcity = models.CharField(db_column='PMailCity', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     pmailcountry = models.CharField(db_column='PMailCountry', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     pmailstate = models.CharField(db_column='PMailState', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     prefobjrepid = models.TextField(db_column='PrefObjRepID', blank=True, null=True)  # Field name made lowercase.
#     referralsource = models.CharField(db_column='ReferralSource', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     referredby = models.CharField(db_column='ReferredBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     rel = models.CharField(db_column='Rel', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     relationships = models.CharField(db_column='Relationships', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     responsibility = models.CharField(db_column='Responsibility', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     salutation = models.CharField(db_column='Salutation', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     state = models.CharField(db_column='State', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     streetaddress = models.CharField(db_column='StreetAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     type = models.CharField(db_column='Type', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     universalid = models.CharField(db_column='UniversalID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     zip = models.CharField(db_column='Zip', max_length=25, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         db_table = 'contactsn1'


# class InvoiceBilling(models.Model):
#     projectnumber = models.TextField(db_column='ProjectNumber', blank=True, null=True)  # Field name made lowercase.
#     projid = models.CharField(db_column='ProjID', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     acctnotes = models.TextField(db_column='AcctNotes', blank=True, null=True)  # Field name made lowercase.
#     address1 = models.TextField(db_column='Address1', blank=True, null=True)  # Field name made lowercase.
#     address2 = models.TextField(db_column='Address2', blank=True, null=True)  # Field name made lowercase.
#     analysiscomments = models.TextField(db_column='AnalysisComments', blank=True, null=True)  # Field name made lowercase.
#     authordate = models.TextField(db_column='AuthorDate', blank=True, null=True)  # Field name made lowercase.
#     authorname = models.TextField(db_column='AuthorName', blank=True, null=True)  # Field name made lowercase.
#     authors = models.TextField(db_column='Authors', blank=True, null=True)  # Field name made lowercase.
#     billedyn = models.TextField(db_column='BilledYN', blank=True, null=True)  # Field name made lowercase.
#     billingnotes = models.TextField(db_column='BillingNotes', blank=True, null=True)  # Field name made lowercase.
#     city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.
#     companyname = models.TextField(blank=True, null=True)
#     contactname = models.TextField(db_column='ContactName', blank=True, null=True)  # Field name made lowercase.
#     contactnumber = models.TextField(db_column='ContactNumber', blank=True, null=True)  # Field name made lowercase.
#     country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase.
#     created = models.TextField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
#     datedue = models.TextField(db_column='DateDue', blank=True, null=True)  # Field name made lowercase.
#     datereceived = models.TextField(db_column='DateReceived', blank=True, null=True)  # Field name made lowercase.
#     docid = models.TextField(db_column='DocID', blank=True, null=True)  # Field name made lowercase.
#     editauthors = models.TextField(db_column='EditAuthors', blank=True, null=True)  # Field name made lowercase.
#     editdates = models.TextField(db_column='EditDates', blank=True, null=True)  # Field name made lowercase.
#     email = models.TextField(db_column='EMail', blank=True, null=True)  # Field name made lowercase.
#     embeddedobjects = models.TextField(db_column='EmbeddedObjects', blank=True, null=True)  # Field name made lowercase.
#     familyid = models.TextField(db_column='FamilyID', blank=True, null=True)  # Field name made lowercase.
#     familyname = models.TextField(db_column='FamilyName', blank=True, null=True)  # Field name made lowercase.
#     familynotes = models.TextField(db_column='FamilyNotes', blank=True, null=True)  # Field name made lowercase.
#     fax = models.TextField(db_column='Fax', blank=True, null=True)  # Field name made lowercase.
#     hasmissedopportunity = models.TextField(db_column='HasMissedOpportunity', blank=True, null=True)  # Field name made lowercase.
#     invamt = models.TextField(db_column='InvAmt', blank=True, null=True)  # Field name made lowercase.
#     invcity = models.TextField(db_column='InvCity', blank=True, null=True)  # Field name made lowercase.
#     invcompanyname = models.TextField(db_column='InvCompanyName', blank=True, null=True)  # Field name made lowercase.
#     invcountry = models.TextField(db_column='InvCountry', blank=True, null=True)  # Field name made lowercase.
#     invdate = models.TextField(db_column='InvDate', blank=True, null=True)  # Field name made lowercase.
#     invdesc = models.TextField(db_column='InvDesc', blank=True, null=True)  # Field name made lowercase.
#     invdisc = models.TextField(db_column='InvDisc', blank=True, null=True)  # Field name made lowercase.
#     invfamilyid = models.TextField(db_column='InvFamilyID', blank=True, null=True)  # Field name made lowercase.
#     invfamilyname = models.TextField(db_column='InvFamilyName', blank=True, null=True)  # Field name made lowercase.
#     invlocationid = models.TextField(db_column='InvLocationID', blank=True, null=True)  # Field name made lowercase.
#     invoicedate = models.TextField(db_column='InvoiceDate', blank=True, null=True)  # Field name made lowercase.
#     invpersonid = models.TextField(db_column='InvPersonID', blank=True, null=True)  # Field name made lowercase.
#     invqty = models.TextField(db_column='InvQty', blank=True, null=True)  # Field name made lowercase.
#     invrate = models.TextField(db_column='InvRate', blank=True, null=True)  # Field name made lowercase.
#     invstate = models.TextField(db_column='InvState', blank=True, null=True)  # Field name made lowercase.
#     invtotal = models.TextField(db_column='InvTotal', blank=True, null=True)  # Field name made lowercase.
#     lastaccessed = models.TextField(db_column='LastAccessed', blank=True, null=True)  # Field name made lowercase.
#     lastmodified = models.TextField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.
#     locationid = models.TextField(db_column='LocationID', blank=True, null=True)  # Field name made lowercase.
#     misscategory = models.TextField(db_column='MissCategory', blank=True, null=True)  # Field name made lowercase.
#     missdescription = models.TextField(db_column='MissDescription', blank=True, null=True)  # Field name made lowercase.
#     missestimate = models.TextField(db_column='MissEstimate', blank=True, null=True)  # Field name made lowercase.
#     misslineitems = models.TextField(db_column='MissLineItems', blank=True, null=True)  # Field name made lowercase.
#     note1_desc = models.TextField(db_column='Note1_Desc', blank=True, null=True)  # Field name made lowercase.
#     note1_name = models.TextField(db_column='Note1_Name', blank=True, null=True)  # Field name made lowercase.
#     note2_desc = models.TextField(db_column='Note2_Desc', blank=True, null=True)  # Field name made lowercase.
#     note2_name = models.TextField(db_column='Note2_Name', blank=True, null=True)  # Field name made lowercase.
#     note3_desc = models.TextField(db_column='Note3_Desc', blank=True, null=True)  # Field name made lowercase.
#     note3_name = models.TextField(db_column='Note3_Name', blank=True, null=True)  # Field name made lowercase.
#     note4_desc = models.TextField(db_column='Note4_Desc', blank=True, null=True)  # Field name made lowercase.
#     note4_name = models.TextField(db_column='Note4_Name', blank=True, null=True)  # Field name made lowercase.
#     note5_desc = models.TextField(db_column='Note5_Desc', blank=True, null=True)  # Field name made lowercase.
#     note5_name = models.TextField(db_column='Note5_Name', blank=True, null=True)  # Field name made lowercase.
#     note6_desc = models.TextField(db_column='Note6_Desc', blank=True, null=True)  # Field name made lowercase.
#     note6_name = models.TextField(db_column='Note6_Name', blank=True, null=True)  # Field name made lowercase.
#     noteid = models.TextField(db_column='NoteID', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_1 = models.TextField(db_column='Notes_Text_Loc_1', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_2 = models.TextField(db_column='Notes_Text_Loc_2', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_3 = models.TextField(db_column='Notes_Text_Loc_3', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_4 = models.TextField(db_column='Notes_Text_Loc_4', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_5 = models.TextField(db_column='Notes_Text_Loc_5', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_6 = models.TextField(db_column='Notes_Text_Loc_6', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_archive = models.TextField(db_column='Notes_Text_Loc_Archive', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_historical = models.TextField(db_column='Notes_Text_Loc_Historical', blank=True, null=True)  # Field name made lowercase.
#     notes_text_org_1 = models.TextField(db_column='Notes_Text_Org_1', blank=True, null=True)  # Field name made lowercase.
#     notes_text_org_2 = models.TextField(db_column='Notes_Text_Org_2', blank=True, null=True)  # Field name made lowercase.
#     notes_text_org_3 = models.TextField(db_column='Notes_Text_Org_3', blank=True, null=True)  # Field name made lowercase.
#     notes_text_org_4 = models.TextField(db_column='Notes_Text_Org_4', blank=True, null=True)  # Field name made lowercase.
#     notes_text_org_5 = models.TextField(db_column='Notes_Text_Org_5', blank=True, null=True)  # Field name made lowercase.
#     notes_text_org_6 = models.TextField(db_column='Notes_Text_Org_6', blank=True, null=True)  # Field name made lowercase.
#     notes_text_org_archive = models.TextField(db_column='Notes_Text_Org_Archive', blank=True, null=True)  # Field name made lowercase.
#     notes_text_org_historical = models.TextField(db_column='Notes_Text_Org_Historical', blank=True, null=True)  # Field name made lowercase.
#     personid = models.CharField(db_column='PersonID', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     ponumber = models.TextField(db_column='PONumber', blank=True, null=True)  # Field name made lowercase.
#     prelimdatasentdate = models.TextField(db_column='PrelimDataSentDate', blank=True, null=True)  # Field name made lowercase.
#     projassgn = models.TextField(db_column='PROJASSGN', blank=True, null=True)  # Field name made lowercase.
#     projdirector = models.TextField(db_column='ProjDirector', blank=True, null=True)  # Field name made lowercase.
#     projectcomments = models.TextField(db_column='ProjectComments', blank=True, null=True)  # Field name made lowercase.
#     projevent = models.TextField(db_column='ProjEvent', blank=True, null=True)  # Field name made lowercase.
#     projsource = models.TextField(db_column='ProjSource', blank=True, null=True)  # Field name made lowercase.
#     projstatus = models.TextField(db_column='ProjStatus', blank=True, null=True)  # Field name made lowercase.
#     quote = models.TextField(db_column='Quote', blank=True, null=True)  # Field name made lowercase.
#     rptshipsentdate = models.TextField(db_column='RptShipSentDate', blank=True, null=True)  # Field name made lowercase.
#     sampcount = models.TextField(db_column='SAMPCOUNT', blank=True, null=True)  # Field name made lowercase.
#     samplecomments = models.TextField(db_column='SampleComments', blank=True, null=True)  # Field name made lowercase.
#     sampletypes = models.TextField(db_column='SampleTypes', blank=True, null=True)  # Field name made lowercase.
#     specialtermsinvoice = models.TextField(db_column='SpecialTermsInvoice', blank=True, null=True)  # Field name made lowercase.
#     specialtermsreport = models.TextField(db_column='SpecialTermsReport', blank=True, null=True)  # Field name made lowercase.
#     state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase.
#     universalid = models.CharField(db_column='UniversalID', max_length=50, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         db_table = 'invoice_billing'


# class InvoiceBillingarch(models.Model):
#     projectnumber = models.TextField(db_column='ProjectNumber', blank=True, null=True)  # Field name made lowercase.
#     projid = models.CharField(db_column='ProjID', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     acctnotes = models.TextField(db_column='AcctNotes', blank=True, null=True)  # Field name made lowercase.
#     address1 = models.TextField(db_column='Address1', blank=True, null=True)  # Field name made lowercase.
#     address2 = models.TextField(db_column='Address2', blank=True, null=True)  # Field name made lowercase.
#     analysiscomments = models.TextField(db_column='AnalysisComments', blank=True, null=True)  # Field name made lowercase.
#     authordate = models.TextField(db_column='AuthorDate', blank=True, null=True)  # Field name made lowercase.
#     authorname = models.TextField(db_column='AuthorName', blank=True, null=True)  # Field name made lowercase.
#     authors = models.TextField(db_column='Authors', blank=True, null=True)  # Field name made lowercase.
#     billedyn = models.TextField(db_column='BilledYN', blank=True, null=True)  # Field name made lowercase.
#     billingnotes = models.TextField(db_column='BillingNotes', blank=True, null=True)  # Field name made lowercase.
#     city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.
#     companyname = models.TextField(blank=True, null=True)
#     contactname = models.TextField(db_column='ContactName', blank=True, null=True)  # Field name made lowercase.
#     contactnumber = models.TextField(db_column='ContactNumber', blank=True, null=True)  # Field name made lowercase.
#     country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase.
#     created = models.TextField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
#     datedue = models.TextField(db_column='DateDue', blank=True, null=True)  # Field name made lowercase.
#     datereceived = models.TextField(db_column='DateReceived', blank=True, null=True)  # Field name made lowercase.
#     docid = models.TextField(db_column='DocID', blank=True, null=True)  # Field name made lowercase.
#     editauthors = models.TextField(db_column='EditAuthors', blank=True, null=True)  # Field name made lowercase.
#     editdates = models.TextField(db_column='EditDates', blank=True, null=True)  # Field name made lowercase.
#     email = models.TextField(db_column='EMail', blank=True, null=True)  # Field name made lowercase.
#     embeddedobjects = models.TextField(db_column='EmbeddedObjects', blank=True, null=True)  # Field name made lowercase.
#     familyid = models.TextField(db_column='FamilyID', blank=True, null=True)  # Field name made lowercase.
#     familyname = models.TextField(db_column='FamilyName', blank=True, null=True)  # Field name made lowercase.
#     familynotes = models.TextField(db_column='FamilyNotes', blank=True, null=True)  # Field name made lowercase.
#     fax = models.TextField(db_column='Fax', blank=True, null=True)  # Field name made lowercase.
#     hasmissedopportunity = models.TextField(db_column='HasMissedOpportunity', blank=True, null=True)  # Field name made lowercase.
#     invamt = models.TextField(db_column='InvAmt', blank=True, null=True)  # Field name made lowercase.
#     invcity = models.TextField(db_column='InvCity', blank=True, null=True)  # Field name made lowercase.
#     invcompanyname = models.TextField(db_column='InvCompanyName', blank=True, null=True)  # Field name made lowercase.
#     invcountry = models.TextField(db_column='InvCountry', blank=True, null=True)  # Field name made lowercase.
#     invdate = models.TextField(db_column='InvDate', blank=True, null=True)  # Field name made lowercase.
#     invdesc = models.TextField(db_column='InvDesc', blank=True, null=True)  # Field name made lowercase.
#     invdisc = models.TextField(db_column='InvDisc', blank=True, null=True)  # Field name made lowercase.
#     invfamilyid = models.TextField(db_column='InvFamilyID', blank=True, null=True)  # Field name made lowercase.
#     invfamilyname = models.TextField(db_column='InvFamilyName', blank=True, null=True)  # Field name made lowercase.
#     invlocationid = models.TextField(db_column='InvLocationID', blank=True, null=True)  # Field name made lowercase.
#     invoicedate = models.TextField(db_column='InvoiceDate', blank=True, null=True)  # Field name made lowercase.
#     invpersonid = models.TextField(db_column='InvPersonID', blank=True, null=True)  # Field name made lowercase.
#     invqty = models.TextField(db_column='InvQty', blank=True, null=True)  # Field name made lowercase.
#     invrate = models.TextField(db_column='InvRate', blank=True, null=True)  # Field name made lowercase.
#     invstate = models.TextField(db_column='InvState', blank=True, null=True)  # Field name made lowercase.
#     invtotal = models.TextField(db_column='InvTotal', blank=True, null=True)  # Field name made lowercase.
#     lastaccessed = models.TextField(db_column='LastAccessed', blank=True, null=True)  # Field name made lowercase.
#     lastmodified = models.TextField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.
#     locationid = models.TextField(db_column='LocationID', blank=True, null=True)  # Field name made lowercase.
#     misscategory = models.TextField(db_column='MissCategory', blank=True, null=True)  # Field name made lowercase.
#     missdescription = models.TextField(db_column='MissDescription', blank=True, null=True)  # Field name made lowercase.
#     missestimate = models.TextField(db_column='MissEstimate', blank=True, null=True)  # Field name made lowercase.
#     misslineitems = models.TextField(db_column='MissLineItems', blank=True, null=True)  # Field name made lowercase.
#     note1_desc = models.TextField(db_column='Note1_Desc', blank=True, null=True)  # Field name made lowercase.
#     note1_name = models.TextField(db_column='Note1_Name', blank=True, null=True)  # Field name made lowercase.
#     note2_desc = models.TextField(db_column='Note2_Desc', blank=True, null=True)  # Field name made lowercase.
#     note2_name = models.TextField(db_column='Note2_Name', blank=True, null=True)  # Field name made lowercase.
#     note3_desc = models.TextField(db_column='Note3_Desc', blank=True, null=True)  # Field name made lowercase.
#     note3_name = models.TextField(db_column='Note3_Name', blank=True, null=True)  # Field name made lowercase.
#     note4_desc = models.TextField(db_column='Note4_Desc', blank=True, null=True)  # Field name made lowercase.
#     note4_name = models.TextField(db_column='Note4_Name', blank=True, null=True)  # Field name made lowercase.
#     note5_desc = models.TextField(db_column='Note5_Desc', blank=True, null=True)  # Field name made lowercase.
#     note5_name = models.TextField(db_column='Note5_Name', blank=True, null=True)  # Field name made lowercase.
#     note6_desc = models.TextField(db_column='Note6_Desc', blank=True, null=True)  # Field name made lowercase.
#     note6_name = models.TextField(db_column='Note6_Name', blank=True, null=True)  # Field name made lowercase.
#     noteid = models.TextField(db_column='NoteID', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_1 = models.TextField(db_column='Notes_Text_Loc_1', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_2 = models.TextField(db_column='Notes_Text_Loc_2', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_3 = models.TextField(db_column='Notes_Text_Loc_3', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_4 = models.TextField(db_column='Notes_Text_Loc_4', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_5 = models.TextField(db_column='Notes_Text_Loc_5', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_6 = models.TextField(db_column='Notes_Text_Loc_6', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_archive = models.TextField(db_column='Notes_Text_Loc_Archive', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_historical = models.TextField(db_column='Notes_Text_Loc_Historical', blank=True, null=True)  # Field name made lowercase.
#     notes_text_org_1 = models.TextField(db_column='Notes_Text_Org_1', blank=True, null=True)  # Field name made lowercase.
#     notes_text_org_2 = models.TextField(db_column='Notes_Text_Org_2', blank=True, null=True)  # Field name made lowercase.
#     notes_text_org_3 = models.TextField(db_column='Notes_Text_Org_3', blank=True, null=True)  # Field name made lowercase.
#     notes_text_org_4 = models.TextField(db_column='Notes_Text_Org_4', blank=True, null=True)  # Field name made lowercase.
#     notes_text_org_5 = models.TextField(db_column='Notes_Text_Org_5', blank=True, null=True)  # Field name made lowercase.
#     notes_text_org_6 = models.TextField(db_column='Notes_Text_Org_6', blank=True, null=True)  # Field name made lowercase.
#     notes_text_org_archive = models.TextField(db_column='Notes_Text_Org_Archive', blank=True, null=True)  # Field name made lowercase.
#     notes_text_org_historical = models.TextField(db_column='Notes_Text_Org_Historical', blank=True, null=True)  # Field name made lowercase.
#     personid = models.CharField(db_column='PersonID', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     ponumber = models.TextField(db_column='PONumber', blank=True, null=True)  # Field name made lowercase.
#     prelimdatasentdate = models.TextField(db_column='PrelimDataSentDate', blank=True, null=True)  # Field name made lowercase.
#     projassgn = models.TextField(db_column='PROJASSGN', blank=True, null=True)  # Field name made lowercase.
#     projdirector = models.TextField(db_column='ProjDirector', blank=True, null=True)  # Field name made lowercase.
#     projectcomments = models.TextField(db_column='ProjectComments', blank=True, null=True)  # Field name made lowercase.
#     projevent = models.TextField(db_column='ProjEvent', blank=True, null=True)  # Field name made lowercase.
#     projsource = models.TextField(db_column='ProjSource', blank=True, null=True)  # Field name made lowercase.
#     projstatus = models.TextField(db_column='ProjStatus', blank=True, null=True)  # Field name made lowercase.
#     quote = models.TextField(db_column='Quote', blank=True, null=True)  # Field name made lowercase.
#     rptshipsentdate = models.TextField(db_column='RptShipSentDate', blank=True, null=True)  # Field name made lowercase.
#     sampcount = models.TextField(db_column='SAMPCOUNT', blank=True, null=True)  # Field name made lowercase.
#     samplecomments = models.TextField(db_column='SampleComments', blank=True, null=True)  # Field name made lowercase.
#     sampletypes = models.TextField(db_column='SampleTypes', blank=True, null=True)  # Field name made lowercase.
#     specialtermsinvoice = models.TextField(db_column='SpecialTermsInvoice', blank=True, null=True)  # Field name made lowercase.
#     specialtermsreport = models.TextField(db_column='SpecialTermsReport', blank=True, null=True)  # Field name made lowercase.
#     state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase.
#     universalid = models.CharField(db_column='UniversalID', max_length=50, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         db_table = 'invoice_billingarch'


# class InvoiceBillingn1(models.Model):
#     projectnumber = models.CharField(db_column='ProjectNumber', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     projid = models.CharField(db_column='ProjID', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     acctnotes = models.TextField(db_column='AcctNotes', blank=True, null=True)  # Field name made lowercase.
#     address1 = models.CharField(db_column='Address1', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     address2 = models.CharField(db_column='Address2', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     authordate = models.CharField(db_column='AuthorDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     authorname = models.CharField(db_column='AuthorName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     authors = models.CharField(db_column='Authors', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     billedyn = models.CharField(db_column='BilledYN', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     city = models.CharField(db_column='City', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     companyname = models.CharField(max_length=100, blank=True, null=True)
#     contactname = models.CharField(db_column='ContactName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     contactnumber = models.CharField(db_column='ContactNumber', max_length=60, blank=True, null=True)  # Field name made lowercase.
#     country = models.CharField(db_column='Country', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     datedue = models.CharField(db_column='DateDue', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     datereceived = models.CharField(db_column='DateReceived', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     docid = models.CharField(db_column='DocID', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     email = models.CharField(db_column='EMail', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     embeddedobjects = models.TextField(db_column='EmbeddedObjects', blank=True, null=True)  # Field name made lowercase.
#     familyid = models.CharField(db_column='FamilyID', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     familyname = models.CharField(db_column='FamilyName', max_length=125, blank=True, null=True)  # Field name made lowercase.
#     fax = models.CharField(db_column='Fax', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     hasmissedopportunity = models.CharField(db_column='HasMissedOpportunity', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     invamt = models.CharField(db_column='InvAmt', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     invcity = models.CharField(db_column='InvCity', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     invcompanyname = models.CharField(db_column='InvCompanyName', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     invcountry = models.CharField(db_column='InvCountry', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     invdate = models.CharField(db_column='InvDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     invdisc = models.CharField(db_column='InvDisc', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     invfamilyid = models.CharField(db_column='InvFamilyID', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     invdesc = models.TextField(db_column='InvDesc', blank=True, null=True)  # Field name made lowercase.
#     invfamilyname = models.CharField(db_column='InvFamilyName', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     invlocationid = models.CharField(db_column='InvLocationID', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     invoicedate = models.CharField(db_column='InvoiceDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     invpersonid = models.CharField(db_column='InvPersonID', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     invqty = models.CharField(db_column='InvQty', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     invrate = models.CharField(db_column='InvRate', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     invstate = models.CharField(db_column='InvState', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     invtotal = models.CharField(db_column='InvTotal', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     locationid = models.CharField(db_column='LocationID', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     misscategory = models.CharField(db_column='MissCategory', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     missdescription = models.TextField(db_column='MissDescription', blank=True, null=True)  # Field name made lowercase.
#     missestimate = models.CharField(db_column='MissEstimate', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     misslineitems = models.TextField(db_column='MissLineItems', blank=True, null=True)  # Field name made lowercase.
#     note1_desc = models.CharField(db_column='Note1_Desc', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     note1_name = models.CharField(db_column='Note1_Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     note2_desc = models.CharField(db_column='Note2_Desc', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     note2_name = models.CharField(db_column='Note2_Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     note3_desc = models.CharField(db_column='Note3_Desc', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     note3_name = models.CharField(db_column='Note3_Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     note4_desc = models.CharField(db_column='Note4_Desc', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     note4_name = models.CharField(db_column='Note4_Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     note5_desc = models.CharField(db_column='Note5_Desc', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     note5_name = models.CharField(db_column='Note5_Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     note6_desc = models.CharField(db_column='Note6_Desc', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     note6_name = models.CharField(db_column='Note6_Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     noteid = models.CharField(db_column='NoteID', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_1 = models.TextField(db_column='Notes_Text_Loc_1', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_2 = models.TextField(db_column='Notes_Text_Loc_2', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_3 = models.TextField(db_column='Notes_Text_Loc_3', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_4 = models.TextField(db_column='Notes_Text_Loc_4', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_5 = models.TextField(db_column='Notes_Text_Loc_5', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_6 = models.TextField(db_column='Notes_Text_Loc_6', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_archive = models.TextField(db_column='Notes_Text_Loc_Archive', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_historical = models.TextField(db_column='Notes_Text_Loc_Historical', blank=True, null=True)  # Field name made lowercase.
#     notes_text_org_1 = models.TextField(db_column='Notes_Text_Org_1', blank=True, null=True)  # Field name made lowercase.
#     notes_text_org_2 = models.TextField(db_column='Notes_Text_Org_2', blank=True, null=True)  # Field name made lowercase.
#     notes_text_org_3 = models.TextField(db_column='Notes_Text_Org_3', blank=True, null=True)  # Field name made lowercase.
#     notes_text_org_4 = models.TextField(db_column='Notes_Text_Org_4', blank=True, null=True)  # Field name made lowercase.
#     notes_text_org_5 = models.TextField(db_column='Notes_Text_Org_5', blank=True, null=True)  # Field name made lowercase.
#     notes_text_org_6 = models.TextField(db_column='Notes_Text_Org_6', blank=True, null=True)  # Field name made lowercase.
#     notes_text_org_archive = models.TextField(db_column='Notes_Text_Org_Archive', blank=True, null=True)  # Field name made lowercase.
#     notes_text_org_historical = models.TextField(db_column='Notes_Text_Org_Historical', blank=True, null=True)  # Field name made lowercase.
#     personid = models.CharField(db_column='PersonID', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     ponumber = models.CharField(db_column='PONumber', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     prelimdatasentdate = models.CharField(db_column='PrelimDataSentDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     projassgn = models.CharField(db_column='PROJASSGN', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     projdirector = models.CharField(db_column='ProjDirector', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     projstatus = models.CharField(db_column='ProjStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     quote = models.CharField(db_column='Quote', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     rptshipsentdate = models.CharField(db_column='RptShipSentDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     sampcount = models.CharField(db_column='SAMPCOUNT', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     sampletypes = models.TextField(db_column='SampleTypes', blank=True, null=True)  # Field name made lowercase.
#     state = models.CharField(db_column='State', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     universalid = models.CharField(db_column='UniversalID', max_length=50, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         db_table = 'invoice_billingn1'


# class Locations(models.Model):
#     companyid = models.CharField(db_column='CompanyID', primary_key=True, max_length=50)  # Field name made lowercase.
#     familyid = models.CharField(db_column='FamilyID', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     personid = models.CharField(db_column='PersonID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     parentid = models.CharField(db_column='ParentID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     prevfamilyid = models.CharField(db_column='PrevFamilyID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     abbbillingnotes = models.TextField(db_column='AbbBillingNotes', blank=True, null=True)  # Field name made lowercase.
#     affiliates1 = models.TextField(db_column='Affiliates1', blank=True, null=True)  # Field name made lowercase.
#     affiliates2 = models.TextField(db_column='Affiliates2', blank=True, null=True)  # Field name made lowercase.
#     affiliatessummaryinfo1 = models.TextField(db_column='AffiliatesSummaryInfo1', blank=True, null=True)  # Field name made lowercase.
#     affiliatessummaryinfo2 = models.TextField(db_column='AffiliatesSummaryInfo2', blank=True, null=True)  # Field name made lowercase.
#     agreementdate = models.TextField(db_column='AgreementDate', blank=True, null=True)  # Field name made lowercase.
#     authordate = models.TextField(db_column='AuthorDate', blank=True, null=True)  # Field name made lowercase.
#     authorname = models.TextField(db_column='AuthorName', blank=True, null=True)  # Field name made lowercase.
#     authors = models.TextField(db_column='Authors', blank=True, null=True)  # Field name made lowercase.
#     avg_invoice = models.TextField(blank=True, null=True)
#     billingnotes = models.TextField(db_column='BillingNotes', blank=True, null=True)  # Field name made lowercase.
#     city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.
#     cofein = models.TextField(db_column='coFEIN', blank=True, null=True)  # Field name made lowercase.
#     comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
#     companyacctexec = models.TextField(db_column='CompanyAcctExec', blank=True, null=True)  # Field name made lowercase.
#     companyacctteam = models.TextField(db_column='CompanyAcctTeam', blank=True, null=True)  # Field name made lowercase.
#     companyclass = models.TextField(db_column='CompanyClass', blank=True, null=True)  # Field name made lowercase.
#     companycounty = models.TextField(db_column='CompanyCounty', blank=True, null=True)  # Field name made lowercase.
#     companycredit = models.TextField(db_column='CompanyCredit', blank=True, null=True)  # Field name made lowercase.
#     companydiscount = models.TextField(db_column='CompanyDiscount', blank=True, null=True)  # Field name made lowercase.
#     companyempl = models.TextField(db_column='CompanyEmpl', blank=True, null=True)  # Field name made lowercase.
#     companyindustry = models.TextField(db_column='CompanyIndustry', blank=True, null=True)  # Field name made lowercase.
#     companyinsagree = models.TextField(db_column='CompanyInsAgree', blank=True, null=True)  # Field name made lowercase.
#     companylat = models.TextField(db_column='CompanyLat', blank=True, null=True)  # Field name made lowercase.
#     companylong = models.TextField(db_column='CompanyLong', blank=True, null=True)  # Field name made lowercase.
#     companymphone = models.TextField(db_column='CompanyMPhone', blank=True, null=True)  # Field name made lowercase.
#     companyname = models.TextField(db_column='CompanyName', blank=True, null=True)  # Field name made lowercase.
#     companynamecheck = models.TextField(db_column='CompanyNameCheck', blank=True, null=True)  # Field name made lowercase.
#     companynumber = models.TextField(db_column='CompanyNumber', blank=True, null=True)  # Field name made lowercase.
#     companysales = models.TextField(db_column='CompanySales', blank=True, null=True)  # Field name made lowercase.
#     companysearch = models.TextField(db_column='CompanySearch', blank=True, null=True)  # Field name made lowercase.
#     companysic = models.TextField(db_column='CompanySIC', blank=True, null=True)  # Field name made lowercase.
#     companyterritory = models.TextField(db_column='CompanyTerritory', blank=True, null=True)  # Field name made lowercase.
#     companytype = models.TextField(db_column='CompanyType', blank=True, null=True)  # Field name made lowercase.
#     companyurl = models.TextField(db_column='CompanyURL', blank=True, null=True)  # Field name made lowercase.
#     companyyears = models.TextField(db_column='CompanyYears', blank=True, null=True)  # Field name made lowercase.
#     count_invoice = models.TextField(blank=True, null=True)
#     count_quotes = models.TextField(blank=True, null=True)
#     country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase.
#     created = models.TextField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
#     duns = models.TextField(db_column='DUNS', blank=True, null=True)  # Field name made lowercase.
#     editauthors = models.TextField(db_column='EditAuthors', blank=True, null=True)  # Field name made lowercase.
#     editcount = models.TextField(db_column='EditCount', blank=True, null=True)  # Field name made lowercase.
#     editdatename = models.TextField(db_column='EditDateName', blank=True, null=True)  # Field name made lowercase.
#     editdates = models.TextField(db_column='EditDates', blank=True, null=True)  # Field name made lowercase.
#     edited = models.TextField(db_column='Edited', blank=True, null=True)  # Field name made lowercase.
#     editnames = models.TextField(db_column='EditNames', blank=True, null=True)  # Field name made lowercase.
#     edits = models.TextField(db_column='Edits', blank=True, null=True)  # Field name made lowercase.
#     familyjoindate = models.TextField(db_column='FamilyJoinDate', blank=True, null=True)  # Field name made lowercase.
#     familyname = models.TextField(db_column='FamilyName', blank=True, null=True)  # Field name made lowercase.
#     familynotes = models.TextField(db_column='FamilyNotes', blank=True, null=True)  # Field name made lowercase.
#     first_invoice = models.TextField(blank=True, null=True)
#     gap_invoice = models.TextField(blank=True, null=True)
#     hasfamilydefinition = models.TextField(db_column='HasFamilyDefinition', blank=True, null=True)  # Field name made lowercase.
#     historicalnotes = models.TextField(db_column='HistoricalNotes', blank=True, null=True)  # Field name made lowercase.
#     industrycode = models.TextField(db_column='IndustryCode', blank=True, null=True)  # Field name made lowercase.
#     last_invoice = models.TextField(blank=True, null=True)
#     lastaccessed = models.TextField(db_column='LastAccessed', blank=True, null=True)  # Field name made lowercase.
#     lastmodified = models.TextField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.
#     lineitems = models.TextField(blank=True, null=True)
#     litigationsampletext = models.TextField(db_column='LitigationSampleText', blank=True, null=True)  # Field name made lowercase.
#     litigationsampletypes = models.TextField(db_column='LitigationSampleTypes', blank=True, null=True)  # Field name made lowercase.
#     location = models.TextField(db_column='Location', blank=True, null=True)  # Field name made lowercase.
#     mailaddress1 = models.TextField(db_column='MailAddress1', blank=True, null=True)  # Field name made lowercase.
#     mailaddress2 = models.TextField(db_column='MailAddress2', blank=True, null=True)  # Field name made lowercase.
#     mailcity = models.TextField(db_column='MailCity', blank=True, null=True)  # Field name made lowercase.
#     mailcountry = models.TextField(db_column='MailCountry', blank=True, null=True)  # Field name made lowercase.
#     mailstate = models.TextField(db_column='MailState', blank=True, null=True)  # Field name made lowercase.
#     mailzip = models.TextField(db_column='MailZip', blank=True, null=True)  # Field name made lowercase.
#     note1_desc = models.TextField(db_column='Note1_Desc', blank=True, null=True)  # Field name made lowercase.
#     office800phonenumber = models.TextField(db_column='Office800PhoneNumber', blank=True, null=True)  # Field name made lowercase.
#     officeaddress1 = models.TextField(db_column='OfficeAddress1', blank=True, null=True)  # Field name made lowercase.
#     officeaddress2 = models.TextField(db_column='OfficeAddress2', blank=True, null=True)  # Field name made lowercase.
#     officefaxphonenumber = models.TextField(db_column='OfficeFAXPhoneNumber', blank=True, null=True)  # Field name made lowercase.
#     officephonenumber = models.TextField(db_column='OfficePhoneNumber', blank=True, null=True)  # Field name made lowercase.
#     othernames = models.TextField(db_column='OtherNames', blank=True, null=True)  # Field name made lowercase.
#     othernamesmphone = models.TextField(db_column='OtherNamesMPhone', blank=True, null=True)  # Field name made lowercase.
#     paymentterms = models.TextField(db_column='PaymentTerms', blank=True, null=True)  # Field name made lowercase.
#     prefobjrepid = models.TextField(db_column='PrefObjRepID', blank=True, null=True)  # Field name made lowercase.
#     prelimdatarvw = models.TextField(db_column='PrelimDataRvw', blank=True, null=True)  # Field name made lowercase.
#     prevfamilyjoindate = models.TextField(db_column='PrevFamilyJoinDate', blank=True, null=True)  # Field name made lowercase.
#     referralsource = models.TextField(db_column='ReferralSource', blank=True, null=True)  # Field name made lowercase.
#     referredby = models.TextField(db_column='ReferredBy', blank=True, null=True)  # Field name made lowercase.
#     rel = models.TextField(db_column='Rel', blank=True, null=True)  # Field name made lowercase.
#     sendhardcopyrpt = models.TextField(db_column='SendHardCopyRpt', blank=True, null=True)  # Field name made lowercase.
#     state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase.
#     surchargedesc = models.TextField(db_column='SurchargeDesc', blank=True, null=True)  # Field name made lowercase.
#     surchargeprice = models.TextField(db_column='SurchargePrice', blank=True, null=True)  # Field name made lowercase.
#     type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
#     universalid = models.CharField(db_column='UniversalID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     usernamelist = models.TextField(db_column='UserNameList', blank=True, null=True)  # Field name made lowercase.
#     zip = models.CharField(db_column='Zip', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     note1_name = models.TextField(db_column='Note1_Name', blank=True, null=True)  # Field name made lowercase.
#     note2_desc = models.TextField(db_column='Note2_Desc', blank=True, null=True)  # Field name made lowercase.
#     note2_name = models.TextField(db_column='Note2_Name', blank=True, null=True)  # Field name made lowercase.
#     note3_desc = models.TextField(db_column='Note3_Desc', blank=True, null=True)  # Field name made lowercase.
#     note3_name = models.TextField(db_column='Note3_Name', blank=True, null=True)  # Field name made lowercase.
#     note4_desc = models.TextField(db_column='Note4_Desc', blank=True, null=True)  # Field name made lowercase.
#     note4_name = models.TextField(db_column='Note4_Name', blank=True, null=True)  # Field name made lowercase.
#     note5_desc = models.TextField(db_column='Note5_Desc', blank=True, null=True)  # Field name made lowercase.
#     note5_name = models.TextField(db_column='Note5_Name', blank=True, null=True)  # Field name made lowercase.
#     note6_desc = models.TextField(db_column='Note6_Desc', blank=True, null=True)  # Field name made lowercase.
#     note6_name = models.TextField(db_column='Note6_Name', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         db_table = 'locations'


# class Locationsn1(models.Model):
#     companyid = models.CharField(db_column='CompanyID', primary_key=True, max_length=25)  # Field name made lowercase.
#     familyid = models.CharField(db_column='FamilyID', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     personid = models.CharField(db_column='PersonID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     parentid = models.CharField(db_column='ParentID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     prevfamilyid = models.CharField(db_column='PrevFamilyID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     abbbillingnotes = models.TextField(db_column='AbbBillingNotes', blank=True, null=True)  # Field name made lowercase.
#     agreementdate = models.TextField(db_column='AgreementDate', blank=True, null=True)  # Field name made lowercase.
#     avg_invoice = models.CharField(max_length=50, blank=True, null=True)
#     billingnotes = models.TextField(db_column='BillingNotes', blank=True, null=True)  # Field name made lowercase.
#     city = models.CharField(db_column='City', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     cofein = models.CharField(db_column='coFEIN', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     companyacctexec = models.CharField(db_column='CompanyAcctExec', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     companyacctteam = models.CharField(db_column='CompanyAcctTeam', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     companyclass = models.TextField(db_column='CompanyClass', blank=True, null=True)  # Field name made lowercase.
#     companycounty = models.TextField(db_column='CompanyCounty', blank=True, null=True)  # Field name made lowercase.
#     companycredit = models.CharField(db_column='CompanyCredit', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     companydiscount = models.CharField(db_column='CompanyDiscount', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     companyempl = models.CharField(db_column='CompanyEmpl', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     companyindustry = models.CharField(db_column='CompanyIndustry', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     companyinsagree = models.CharField(db_column='CompanyInsAgree', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     companylat = models.TextField(db_column='CompanyLat', blank=True, null=True)  # Field name made lowercase.
#     companylong = models.TextField(db_column='CompanyLong', blank=True, null=True)  # Field name made lowercase.
#     companymphone = models.CharField(db_column='CompanyMPhone', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     companyname = models.CharField(db_column='CompanyName', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     companynamecheck = models.TextField(db_column='CompanyNameCheck', blank=True, null=True)  # Field name made lowercase.
#     companynumber = models.TextField(db_column='CompanyNumber', blank=True, null=True)  # Field name made lowercase.
#     companysales = models.CharField(db_column='CompanySales', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     companysearch = models.TextField(db_column='CompanySearch', blank=True, null=True)  # Field name made lowercase.
#     companysic = models.TextField(db_column='CompanySIC', blank=True, null=True)  # Field name made lowercase.
#     companyterritory = models.TextField(db_column='CompanyTerritory', blank=True, null=True)  # Field name made lowercase.
#     companytype = models.CharField(db_column='CompanyType', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     companyurl = models.CharField(db_column='CompanyURL', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     companyyears = models.CharField(db_column='CompanyYears', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     count_invoice = models.CharField(max_length=10, blank=True, null=True)
#     count_quotes = models.CharField(max_length=10, blank=True, null=True)
#     country = models.CharField(db_column='Country', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     created = models.CharField(db_column='Created', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     duns = models.CharField(db_column='DUNS', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     familyjoindate = models.TextField(db_column='FamilyJoinDate', blank=True, null=True)  # Field name made lowercase.
#     familyname = models.TextField(db_column='FamilyName', blank=True, null=True)  # Field name made lowercase.
#     familynotes = models.TextField(db_column='FamilyNotes', blank=True, null=True)  # Field name made lowercase.
#     first_invoice = models.TextField(blank=True, null=True)
#     gap_invoice = models.CharField(max_length=15, blank=True, null=True)
#     industrycode = models.CharField(db_column='IndustryCode', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     last_invoice = models.TextField(blank=True, null=True)
#     lastaccessed = models.TextField(db_column='LastAccessed', blank=True, null=True)  # Field name made lowercase.
#     lastmodified = models.TextField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.
#     lineitems = models.TextField(blank=True, null=True)
#     litigationsampletext = models.TextField(db_column='LitigationSampleText', blank=True, null=True)  # Field name made lowercase.
#     litigationsampletypes = models.TextField(db_column='LitigationSampleTypes', blank=True, null=True)  # Field name made lowercase.
#     location = models.CharField(db_column='Location', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     mailaddress1 = models.TextField(db_column='MailAddress1', blank=True, null=True)  # Field name made lowercase.
#     mailaddress2 = models.CharField(db_column='MailAddress2', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     mailcity = models.CharField(db_column='MailCity', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     mailcountry = models.CharField(db_column='MailCountry', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     mailstate = models.CharField(db_column='MailState', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     mailzip = models.CharField(db_column='MailZip', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     office800phonenumber = models.CharField(db_column='Office800PhoneNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     officeaddress1 = models.TextField(db_column='OfficeAddress1', blank=True, null=True)  # Field name made lowercase.
#     officeaddress2 = models.TextField(db_column='OfficeAddress2', blank=True, null=True)  # Field name made lowercase.
#     officefaxphonenumber = models.CharField(db_column='OfficeFAXPhoneNumber', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     officephonenumber = models.CharField(db_column='OfficePhoneNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     othernames = models.TextField(db_column='OtherNames', blank=True, null=True)  # Field name made lowercase.
#     othernamesmphone = models.CharField(db_column='OtherNamesMPhone', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     paymentterms = models.CharField(db_column='PaymentTerms', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     prefobjrepid = models.TextField(db_column='PrefObjRepID', blank=True, null=True)  # Field name made lowercase.
#     prelimdatarvw = models.CharField(db_column='PrelimDataRvw', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     prevfamilyjoindate = models.TextField(db_column='PrevFamilyJoinDate', blank=True, null=True)  # Field name made lowercase.
#     referralsource = models.CharField(db_column='ReferralSource', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     referredby = models.CharField(db_column='ReferredBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     rel = models.CharField(db_column='Rel', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     sendhardcopyrpt = models.CharField(db_column='SendHardCopyRpt', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     state = models.CharField(db_column='State', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     surchargedesc = models.TextField(db_column='SurchargeDesc', blank=True, null=True)  # Field name made lowercase.
#     surchargeprice = models.TextField(db_column='SurchargePrice', blank=True, null=True)  # Field name made lowercase.
#     type = models.CharField(db_column='Type', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     universalid = models.CharField(db_column='UniversalID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     usernamelist = models.TextField(db_column='UserNameList', blank=True, null=True)  # Field name made lowercase.
#     zip = models.CharField(db_column='Zip', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     note1_desc = models.TextField(db_column='Note1_Desc', blank=True, null=True)  # Field name made lowercase.
#     note1_name = models.TextField(db_column='Note1_Name', blank=True, null=True)  # Field name made lowercase.
#     note2_desc = models.TextField(db_column='Note2_Desc', blank=True, null=True)  # Field name made lowercase.
#     note2_name = models.TextField(db_column='Note2_Name', blank=True, null=True)  # Field name made lowercase.
#     note3_desc = models.TextField(db_column='Note3_Desc', blank=True, null=True)  # Field name made lowercase.
#     note3_name = models.TextField(db_column='Note3_Name', blank=True, null=True)  # Field name made lowercase.
#     note4_desc = models.TextField(db_column='Note4_Desc', blank=True, null=True)  # Field name made lowercase.
#     note4_name = models.TextField(db_column='Note4_Name', blank=True, null=True)  # Field name made lowercase.
#     note5_desc = models.TextField(db_column='Note5_Desc', blank=True, null=True)  # Field name made lowercase.
#     note5_name = models.TextField(db_column='Note5_Name', blank=True, null=True)  # Field name made lowercase.
#     note6_desc = models.TextField(db_column='Note6_Desc', blank=True, null=True)  # Field name made lowercase.
#     note6_name = models.TextField(db_column='Note6_Name', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         db_table = 'locationsn1'


# class OrgFamily(models.Model):
#     familyid = models.CharField(db_column='FamilyID', primary_key=True, max_length=50)  # Field name made lowercase.
#     personid = models.CharField(db_column='PersonID', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     companyid = models.CharField(db_column='CompanyID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     affiliates = models.TextField(db_column='Affiliates', blank=True, null=True)  # Field name made lowercase.
#     affiliates1 = models.TextField(db_column='Affiliates1', blank=True, null=True)  # Field name made lowercase.
#     affiliates2 = models.TextField(db_column='Affiliates2', blank=True, null=True)  # Field name made lowercase.
#     affiliatessummaryinfo1 = models.TextField(db_column='AffiliatesSummaryInfo1', blank=True, null=True)  # Field name made lowercase.
#     affiliatessummaryinfo2 = models.TextField(db_column='AffiliatesSummaryInfo2', blank=True, null=True)  # Field name made lowercase.
#     agreementdate = models.TextField(db_column='AgreementDate', blank=True, null=True)  # Field name made lowercase.
#     authordate = models.TextField(db_column='AuthorDate', blank=True, null=True)  # Field name made lowercase.
#     authorname = models.TextField(db_column='AuthorName', blank=True, null=True)  # Field name made lowercase.
#     autocreateonly = models.TextField(db_column='AutoCreateOnly', blank=True, null=True)  # Field name made lowercase.
#     avg_invoice = models.TextField(blank=True, null=True)
#     billingnotes = models.TextField(db_column='BillingNotes', blank=True, null=True)  # Field name made lowercase.
#     city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.
#     companycredit = models.TextField(db_column='CompanyCredit', blank=True, null=True)  # Field name made lowercase.
#     companydiscount = models.TextField(db_column='CompanyDiscount', blank=True, null=True)  # Field name made lowercase.
#     companyindustry = models.TextField(db_column='CompanyIndustry', blank=True, null=True)  # Field name made lowercase.
#     companyinsagree = models.TextField(db_column='CompanyInsAgree', blank=True, null=True)  # Field name made lowercase.
#     companytype = models.TextField(db_column='CompanyType', blank=True, null=True)  # Field name made lowercase.
#     companyurl = models.TextField(db_column='CompanyURL', blank=True, null=True)  # Field name made lowercase.
#     count_invoice = models.TextField(blank=True, null=True)
#     count_quotes = models.TextField(blank=True, null=True)
#     country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase.
#     created = models.TextField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
#     editauthors = models.TextField(db_column='EditAuthors', blank=True, null=True)  # Field name made lowercase.
#     editcount = models.TextField(db_column='EditCount', blank=True, null=True)  # Field name made lowercase.
#     editdatename = models.TextField(db_column='EditDateName', blank=True, null=True)  # Field name made lowercase.
#     editdates = models.TextField(db_column='EditDates', blank=True, null=True)  # Field name made lowercase.
#     edited = models.TextField(db_column='Edited', blank=True, null=True)  # Field name made lowercase.
#     editnames = models.TextField(db_column='EditNames', blank=True, null=True)  # Field name made lowercase.
#     edits = models.TextField(db_column='Edits', blank=True, null=True)  # Field name made lowercase.
#     familyname = models.TextField(db_column='FamilyName', blank=True, null=True)  # Field name made lowercase.
#     familynamemphone = models.TextField(db_column='FamilyNameMPhone', blank=True, null=True)  # Field name made lowercase.
#     familynotes = models.TextField(db_column='FamilyNotes', blank=True, null=True)  # Field name made lowercase.
#     first_invoice = models.TextField(blank=True, null=True)
#     gap_invoice = models.TextField(blank=True, null=True)
#     historicalnotes = models.TextField(db_column='HistoricalNotes', blank=True, null=True)  # Field name made lowercase.
#     industrycode = models.TextField(db_column='IndustryCode', blank=True, null=True)  # Field name made lowercase.
#     last_invoice = models.TextField(blank=True, null=True)
#     lastaccessed = models.TextField(db_column='LastAccessed', blank=True, null=True)  # Field name made lowercase.
#     lastmodified = models.TextField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.
#     lineitems = models.TextField(blank=True, null=True)
#     mailaddress1 = models.TextField(db_column='MailAddress1', blank=True, null=True)  # Field name made lowercase.
#     mailaddress2 = models.TextField(db_column='MailAddress2', blank=True, null=True)  # Field name made lowercase.
#     mailcity = models.TextField(db_column='MailCity', blank=True, null=True)  # Field name made lowercase.
#     mailcountry = models.TextField(db_column='MailCountry', blank=True, null=True)  # Field name made lowercase.
#     mailstate = models.TextField(db_column='MailState', blank=True, null=True)  # Field name made lowercase.
#     mailzip = models.TextField(db_column='MailZip', blank=True, null=True)  # Field name made lowercase.
#     note1_text = models.TextField(db_column='Note1_Text', blank=True, null=True)  # Field name made lowercase.
#     note2_text = models.TextField(db_column='Note2_Text', blank=True, null=True)  # Field name made lowercase.
#     note3_text = models.TextField(db_column='Note3_Text', blank=True, null=True)  # Field name made lowercase.
#     note4_text = models.TextField(db_column='Note4_Text', blank=True, null=True)  # Field name made lowercase.
#     note5_text = models.TextField(db_column='Note5_Text', blank=True, null=True)  # Field name made lowercase.
#     note6_text = models.TextField(db_column='Note6_Text', blank=True, null=True)  # Field name made lowercase.
#     office800phonenumber = models.TextField(db_column='Office800PhoneNumber', blank=True, null=True)  # Field name made lowercase.
#     officeaddress1 = models.TextField(db_column='OfficeAddress1', blank=True, null=True)  # Field name made lowercase.
#     officeaddress2 = models.TextField(db_column='OfficeAddress2', blank=True, null=True)  # Field name made lowercase.
#     officefaxphonenumber = models.TextField(db_column='OfficeFAXPhoneNumber', blank=True, null=True)  # Field name made lowercase.
#     officephonenumber = models.TextField(db_column='OfficePhoneNumber', blank=True, null=True)  # Field name made lowercase.
#     orgfein = models.TextField(db_column='orgFEIN', blank=True, null=True)  # Field name made lowercase.
#     paymentterms = models.TextField(db_column='PaymentTerms', blank=True, null=True)  # Field name made lowercase.
#     prefobjrepid = models.TextField(db_column='PrefObjRepID', blank=True, null=True)  # Field name made lowercase.
#     prelimdatarvw = models.TextField(db_column='PrelimDataRvw', blank=True, null=True)  # Field name made lowercase.
#     prevmembers = models.TextField(db_column='PrevMembers', blank=True, null=True)  # Field name made lowercase.
#     referralsource = models.TextField(db_column='ReferralSource', blank=True, null=True)  # Field name made lowercase.
#     referredby = models.TextField(db_column='ReferredBy', blank=True, null=True)  # Field name made lowercase.
#     rel = models.TextField(db_column='Rel', blank=True, null=True)  # Field name made lowercase.
#     sendhardcopyrpt = models.TextField(db_column='SendHardCopyRpt', blank=True, null=True)  # Field name made lowercase.
#     state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase.
#     surchargedesc = models.TextField(db_column='SurchargeDesc', blank=True, null=True)  # Field name made lowercase.
#     surchargeprice = models.TextField(db_column='SurchargePrice', blank=True, null=True)  # Field name made lowercase.
#     type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
#     universalid = models.CharField(db_column='UniversalID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     usernamelist = models.TextField(db_column='UserNameList', blank=True, null=True)  # Field name made lowercase.
#     usernameslist_1 = models.TextField(db_column='UserNamesList_1', blank=True, null=True)  # Field name made lowercase.
#     zip = models.CharField(db_column='Zip', max_length=25, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         db_table = 'org_family'


# class ProjectForm(models.Model):
#     projectnumber = models.CharField(db_column='ProjectNumber', primary_key=True, max_length=45)  # Field name made lowercase.
#     noteid = models.CharField(db_column='NoteID', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     universalid = models.CharField(db_column='UniversalID', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     acctnotes = models.TextField(db_column='AcctNotes', blank=True, null=True)  # Field name made lowercase.
#     actionlog = models.TextField(db_column='ActionLog', blank=True, null=True)  # Field name made lowercase.
#     actionnotes = models.TextField(db_column='ActionNotes', blank=True, null=True)  # Field name made lowercase.
#     addquotenotes = models.TextField(db_column='AddQuoteNotes', blank=True, null=True)  # Field name made lowercase.
#     created = models.TextField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
#     lastaccessed = models.TextField(db_column='LastAccessed', blank=True, null=True)  # Field name made lowercase.
#     lastmodified = models.TextField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.
#     address1 = models.TextField(db_column='Address1', blank=True, null=True)  # Field name made lowercase.
#     address2 = models.TextField(db_column='Address2', blank=True, null=True)  # Field name made lowercase.
#     ampmreceived = models.TextField(db_column='AMPMReceived', blank=True, null=True)  # Field name made lowercase.
#     analysiscomments = models.TextField(db_column='AnalysisComments', blank=True, null=True)  # Field name made lowercase.
#     analysisqty = models.TextField(db_column='AnalysisQty', blank=True, null=True)  # Field name made lowercase.
#     analysistypes = models.TextField(db_column='AnalysisTypes', blank=True, null=True)  # Field name made lowercase.
#     authordate = models.TextField(db_column='AuthorDate', blank=True, null=True)  # Field name made lowercase.
#     authorname = models.TextField(db_column='AuthorName', blank=True, null=True)  # Field name made lowercase.
#     authors = models.TextField(db_column='Authors', blank=True, null=True)  # Field name made lowercase.
#     autoemailed = models.TextField(db_column='AutoEmailed', blank=True, null=True)  # Field name made lowercase.
#     city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.
#     clientwaitreason = models.TextField(db_column='ClientWaitReason', blank=True, null=True)  # Field name made lowercase.
#     companyfirstproj = models.TextField(db_column='CompanyFirstProj', blank=True, null=True)  # Field name made lowercase.
#     companyname = models.TextField(db_column='CompanyName', blank=True, null=True)  # Field name made lowercase.
#     complexproject = models.TextField(db_column='ComplexProject', blank=True, null=True)  # Field name made lowercase.
#     contactname = models.TextField(db_column='ContactName', blank=True, null=True)  # Field name made lowercase.
#     contactnumber = models.TextField(db_column='ContactNumber', blank=True, null=True)  # Field name made lowercase.
#     country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase.
#     custcriteria = models.TextField(db_column='CustCriteria', blank=True, null=True)  # Field name made lowercase.
#     customcharge = models.TextField(db_column='CustomCharge', blank=True, null=True)  # Field name made lowercase.
#     customdescription = models.TextField(db_column='CustomDescription', blank=True, null=True)  # Field name made lowercase.
#     customreturncharge = models.TextField(db_column='CustomReturnCharge', blank=True, null=True)  # Field name made lowercase.
#     custtype = models.TextField(db_column='CustType', blank=True, null=True)  # Field name made lowercase.
#     dangerousgoods = models.TextField(db_column='DangerousGoods', blank=True, null=True)  # Field name made lowercase.
#     datedue = models.TextField(db_column='DateDue', blank=True, null=True)  # Field name made lowercase.
#     datereceived = models.TextField(db_column='DateReceived', blank=True, null=True)  # Field name made lowercase.
#     datercvd = models.CharField(db_column='DateRcvd', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     editauthors = models.TextField(db_column='EditAuthors', blank=True, null=True)  # Field name made lowercase.
#     editdates = models.TextField(db_column='EditDates', blank=True, null=True)  # Field name made lowercase.
#     editprojstatus = models.TextField(db_column='EditProjStatus', blank=True, null=True)  # Field name made lowercase.
#     email = models.TextField(db_column='EMail', blank=True, null=True)  # Field name made lowercase.
#     enterdatedue = models.TextField(db_column='EnterDateDue', blank=True, null=True)  # Field name made lowercase.
#     enterprojectnumber = models.TextField(db_column='EnterProjectNumber', blank=True, null=True)  # Field name made lowercase.
#     familyid = models.TextField(db_column='FamilyID', blank=True, null=True)  # Field name made lowercase.
#     familyname = models.TextField(db_column='FamilyName', blank=True, null=True)  # Field name made lowercase.
#     fax = models.TextField(db_column='Fax', blank=True, null=True)  # Field name made lowercase.
#     firstprojlookup = models.TextField(db_column='FirstProjLookup', blank=True, null=True)  # Field name made lowercase.
#     holddata = models.TextField(db_column='HoldData', blank=True, null=True)  # Field name made lowercase.
#     holddatafollowup = models.TextField(db_column='HoldDataFollowup', blank=True, null=True)  # Field name made lowercase.
#     indraftdate = models.TextField(db_column='InDraftDate', blank=True, null=True)  # Field name made lowercase.
#     industrycode = models.TextField(db_column='IndustryCode', blank=True, null=True)  # Field name made lowercase.
#     inprojecttask = models.TextField(db_column='InProjectTask', blank=True, null=True)  # Field name made lowercase.
#     invaddress1 = models.TextField(db_column='InvAddress1', blank=True, null=True)  # Field name made lowercase.
#     invaddress2 = models.TextField(db_column='InvAddress2', blank=True, null=True)  # Field name made lowercase.
#     invcity = models.TextField(db_column='InvCity', blank=True, null=True)  # Field name made lowercase.
#     invcompanyname = models.TextField(db_column='InvCompanyName', blank=True, null=True)  # Field name made lowercase.
#     invcontactname = models.TextField(db_column='InvContactName', blank=True, null=True)  # Field name made lowercase.
#     invcountry = models.TextField(db_column='InvCountry', blank=True, null=True)  # Field name made lowercase.
#     invemail = models.TextField(db_column='InvEMail', blank=True, null=True)  # Field name made lowercase.
#     invfamilyid = models.TextField(db_column='InvFamilyID', blank=True, null=True)  # Field name made lowercase.
#     pohardcopy = models.TextField(db_column='POHardCopy', blank=True, null=True)  # Field name made lowercase.
#     ponumber = models.CharField(db_column='PONumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     invfamilyname = models.TextField(db_column='InvFamilyName', blank=True, null=True)  # Field name made lowercase.
#     invfax = models.TextField(db_column='InvFax', blank=True, null=True)  # Field name made lowercase.
#     invlocationid = models.TextField(db_column='InvLocationID', blank=True, null=True)  # Field name made lowercase.
#     invpersonid = models.TextField(db_column='InvPersonID', blank=True, null=True)  # Field name made lowercase.
#     invphone = models.TextField(db_column='InvPhone', blank=True, null=True)  # Field name made lowercase.
#     invstate = models.TextField(db_column='InvState', blank=True, null=True)  # Field name made lowercase.
#     invzip = models.TextField(db_column='InvZip', blank=True, null=True)  # Field name made lowercase.
#     locationid = models.TextField(db_column='LocationID', blank=True, null=True)  # Field name made lowercase.
#     methodservices = models.TextField(db_column='MethodServices', blank=True, null=True)  # Field name made lowercase.
#     methodservicetype = models.TextField(db_column='MethodServiceType', blank=True, null=True)  # Field name made lowercase.
#     msquoteallow = models.TextField(db_column='MSQuoteAllow', blank=True, null=True)  # Field name made lowercase.
#     needshardcopyrpt = models.TextField(db_column='NeedsHardCopyRpt', blank=True, null=True)  # Field name made lowercase.
#     overridecredithold = models.TextField(db_column='OverrideCreditHold', blank=True, null=True)  # Field name made lowercase.
#     personid = models.CharField(db_column='PersonID', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     projcanceled = models.TextField(db_column='ProjCanceled', blank=True, null=True)  # Field name made lowercase.
#     projcgmp = models.CharField(db_column='ProjCGMP', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     projdirector = models.TextField(db_column='ProjDirector', blank=True, null=True)  # Field name made lowercase.
#     projevent = models.TextField(db_column='ProjEvent', blank=True, null=True)  # Field name made lowercase.
#     projid = models.CharField(db_column='ProjID', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     projiso = models.CharField(db_column='ProjISO', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     projlitigation = models.TextField(db_column='ProjLitigation', blank=True, null=True)  # Field name made lowercase.
#     projpofollowup = models.TextField(db_column='ProjPOFollowup', blank=True, null=True)  # Field name made lowercase.
#     projpriority = models.CharField(db_column='ProjPriority', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     projqadatarvw = models.TextField(db_column='ProjQADataRvw', blank=True, null=True)  # Field name made lowercase.
#     projqadiscrepancy = models.TextField(db_column='ProjQADiscrepancy', blank=True, null=True)  # Field name made lowercase.
#     projqarev = models.TextField(db_column='ProjQARev', blank=True, null=True)  # Field name made lowercase.
#     projreptwrtr = models.TextField(db_column='ProjReptWrtr', blank=True, null=True)  # Field name made lowercase.
#     projsource = models.TextField(db_column='ProjSource', blank=True, null=True)  # Field name made lowercase.
#     projstatus = models.TextField(db_column='ProjStatus', blank=True, null=True)  # Field name made lowercase.
#     projtechrev = models.TextField(db_column='ProjTechRev', blank=True, null=True)  # Field name made lowercase.
#     protocolperson = models.TextField(db_column='ProtocolPerson', blank=True, null=True)  # Field name made lowercase.
#     quote = models.TextField(db_column='Quote', blank=True, null=True)  # Field name made lowercase.
#     reporttracking = models.TextField(db_column='ReportTracking', blank=True, null=True)  # Field name made lowercase.
#     returnreason = models.TextField(db_column='ReturnReason', blank=True, null=True)  # Field name made lowercase.
#     returnshipfrom = models.TextField(db_column='ReturnShipFrom', blank=True, null=True)  # Field name made lowercase.
#     returnshipmethod = models.TextField(db_column='ReturnShipMethod', blank=True, null=True)  # Field name made lowercase.
#     returnshipsentdate = models.TextField(db_column='ReturnShipSentDate', blank=True, null=True)  # Field name made lowercase.
#     returntracking = models.TextField(db_column='ReturnTracking', blank=True, null=True)  # Field name made lowercase.
#     rptcontactname = models.TextField(db_column='RptContactName', blank=True, null=True)  # Field name made lowercase.
#     rptdigby = models.TextField(db_column='RptDigBy', blank=True, null=True)  # Field name made lowercase.
#     rptdigsenddate = models.TextField(db_column='RptDigSendDate', blank=True, null=True)  # Field name made lowercase.
#     rptdigsendtime = models.TextField(db_column='RptDigSendTime', blank=True, null=True)  # Field name made lowercase.
#     rptdigsent = models.TextField(db_column='RptDigSent', blank=True, null=True)  # Field name made lowercase.
#     rptdigto = models.TextField(db_column='RptDigTo', blank=True, null=True)  # Field name made lowercase.
#     rpthardcopysent = models.TextField(db_column='RptHardCopySent', blank=True, null=True)  # Field name made lowercase.
#     rptlocationid = models.TextField(db_column='RptLocationID', blank=True, null=True)  # Field name made lowercase.
#     rptpersonid = models.TextField(db_column='RptPersonID', blank=True, null=True)  # Field name made lowercase.
#     rptshipfrom = models.TextField(db_column='RptShipFrom', blank=True, null=True)  # Field name made lowercase.
#     rptshipmethod = models.TextField(db_column='RptShipMethod', blank=True, null=True)  # Field name made lowercase.
#     rptshipsentdate = models.TextField(db_column='RptShipSentDate', blank=True, null=True)  # Field name made lowercase.
#     rptshipsenttime = models.TextField(db_column='RptShipSentTime', blank=True, null=True)  # Field name made lowercase.
#     sampdeascheds = models.TextField(db_column='SampDEAScheds', blank=True, null=True)  # Field name made lowercase.
#     samplecomments = models.TextField(db_column='SampleComments', blank=True, null=True)  # Field name made lowercase.
#     sampleqty = models.TextField(db_column='SampleQty', blank=True, null=True)  # Field name made lowercase.
#     samplesdea = models.TextField(db_column='SamplesDEA', blank=True, null=True)  # Field name made lowercase.
#     sampleshaz = models.TextField(db_column='SamplesHaz', blank=True, null=True)  # Field name made lowercase.
#     samplestorage = models.TextField(db_column='SampleStorage', blank=True, null=True)  # Field name made lowercase.
#     sampletypes = models.TextField(db_column='SampleTypes', blank=True, null=True)  # Field name made lowercase.
#     sampreturn = models.TextField(db_column='SampReturn', blank=True, null=True)  # Field name made lowercase.
#     state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase.
#     trackselection = models.TextField(db_column='TrackSelection', blank=True, null=True)  # Field name made lowercase.
#     validatenow = models.TextField(db_column='ValidateNow', blank=True, null=True)  # Field name made lowercase.
#     zip = models.TextField(db_column='Zip', blank=True, null=True)  # Field name made lowercase.
#     affiliates1 = models.TextField(db_column='Affiliates1', blank=True, null=True)  # Field name made lowercase.
#     affiliates2 = models.TextField(db_column='Affiliates2', blank=True, null=True)  # Field name made lowercase.
#     affiliatessummaryinfo1 = models.TextField(db_column='AffiliatesSummaryInfo1', blank=True, null=True)  # Field name made lowercase.
#     affiliatessummaryinfo2 = models.TextField(db_column='AffiliatesSummaryInfo2', blank=True, null=True)  # Field name made lowercase.
#     note1_desc = models.TextField(db_column='Note1_Desc', blank=True, null=True)  # Field name made lowercase.
#     note1_name = models.TextField(db_column='Note1_Name', blank=True, null=True)  # Field name made lowercase.
#     note2_desc = models.TextField(db_column='Note2_Desc', blank=True, null=True)  # Field name made lowercase.
#     note2_name = models.TextField(db_column='Note2_Name', blank=True, null=True)  # Field name made lowercase.
#     note3_desc = models.TextField(db_column='Note3_Desc', blank=True, null=True)  # Field name made lowercase.
#     note3_name = models.TextField(db_column='Note3_Name', blank=True, null=True)  # Field name made lowercase.
#     note4_desc = models.TextField(db_column='Note4_Desc', blank=True, null=True)  # Field name made lowercase.
#     note4_name = models.TextField(db_column='Note4_Name', blank=True, null=True)  # Field name made lowercase.
#     note5_desc = models.TextField(db_column='Note5_Desc', blank=True, null=True)  # Field name made lowercase.
#     note5_name = models.TextField(db_column='Note5_Name', blank=True, null=True)  # Field name made lowercase.
#     note6_desc = models.TextField(db_column='Note6_Desc', blank=True, null=True)  # Field name made lowercase.
#     note6_name = models.TextField(db_column='Note6_Name', blank=True, null=True)  # Field name made lowercase.
#     partlyhiddenservices = models.TextField(db_column='PartlyHiddenServices', blank=True, null=True)  # Field name made lowercase.
#     partlyhiddenservices_quotes = models.TextField(db_column='PartlyHiddenServices_Quotes', blank=True, null=True)  # Field name made lowercase.
#     prefobjrepid = models.TextField(db_column='PrefObjRepID', blank=True, null=True)  # Field name made lowercase.
#     projnum_digits = models.TextField(db_column='ProjNum_Digits', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         db_table = 'project_form'


# class ProjectFormarch(models.Model):
#     projectnumber = models.CharField(db_column='ProjectNumber', primary_key=True, max_length=45)  # Field name made lowercase.
#     noteid = models.CharField(db_column='NoteID', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     universalid = models.CharField(db_column='UniversalID', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     acctnotes = models.TextField(db_column='AcctNotes', blank=True, null=True)  # Field name made lowercase.
#     actionlog = models.TextField(db_column='ActionLog', blank=True, null=True)  # Field name made lowercase.
#     actionnotes = models.TextField(db_column='ActionNotes', blank=True, null=True)  # Field name made lowercase.
#     addquotenotes = models.TextField(db_column='AddQuoteNotes', blank=True, null=True)  # Field name made lowercase.
#     created = models.TextField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
#     lastaccessed = models.TextField(db_column='LastAccessed', blank=True, null=True)  # Field name made lowercase.
#     lastmodified = models.TextField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.
#     address1 = models.TextField(db_column='Address1', blank=True, null=True)  # Field name made lowercase.
#     address2 = models.TextField(db_column='Address2', blank=True, null=True)  # Field name made lowercase.
#     ampmreceived = models.TextField(db_column='AMPMReceived', blank=True, null=True)  # Field name made lowercase.
#     analysiscomments = models.TextField(db_column='AnalysisComments', blank=True, null=True)  # Field name made lowercase.
#     analysisqty = models.TextField(db_column='AnalysisQty', blank=True, null=True)  # Field name made lowercase.
#     analysistypes = models.TextField(db_column='AnalysisTypes', blank=True, null=True)  # Field name made lowercase.
#     authordate = models.TextField(db_column='AuthorDate', blank=True, null=True)  # Field name made lowercase.
#     authorname = models.TextField(db_column='AuthorName', blank=True, null=True)  # Field name made lowercase.
#     authors = models.TextField(db_column='Authors', blank=True, null=True)  # Field name made lowercase.
#     autoemailed = models.TextField(db_column='AutoEmailed', blank=True, null=True)  # Field name made lowercase.
#     city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.
#     clientwaitreason = models.TextField(db_column='ClientWaitReason', blank=True, null=True)  # Field name made lowercase.
#     companyfirstproj = models.TextField(db_column='CompanyFirstProj', blank=True, null=True)  # Field name made lowercase.
#     companyname = models.TextField(db_column='CompanyName', blank=True, null=True)  # Field name made lowercase.
#     complexproject = models.TextField(db_column='ComplexProject', blank=True, null=True)  # Field name made lowercase.
#     contactname = models.TextField(db_column='ContactName', blank=True, null=True)  # Field name made lowercase.
#     contactnumber = models.TextField(db_column='ContactNumber', blank=True, null=True)  # Field name made lowercase.
#     country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase.
#     custcriteria = models.TextField(db_column='CustCriteria', blank=True, null=True)  # Field name made lowercase.
#     customcharge = models.TextField(db_column='CustomCharge', blank=True, null=True)  # Field name made lowercase.
#     customdescription = models.TextField(db_column='CustomDescription', blank=True, null=True)  # Field name made lowercase.
#     customreturncharge = models.TextField(db_column='CustomReturnCharge', blank=True, null=True)  # Field name made lowercase.
#     custtype = models.TextField(db_column='CustType', blank=True, null=True)  # Field name made lowercase.
#     dangerousgoods = models.TextField(db_column='DangerousGoods', blank=True, null=True)  # Field name made lowercase.
#     datedue = models.TextField(db_column='DateDue', blank=True, null=True)  # Field name made lowercase.
#     datereceived = models.TextField(db_column='DateReceived', blank=True, null=True)  # Field name made lowercase.
#     editauthors = models.TextField(db_column='EditAuthors', blank=True, null=True)  # Field name made lowercase.
#     editdates = models.TextField(db_column='EditDates', blank=True, null=True)  # Field name made lowercase.
#     editprojstatus = models.TextField(db_column='EditProjStatus', blank=True, null=True)  # Field name made lowercase.
#     email = models.TextField(db_column='EMail', blank=True, null=True)  # Field name made lowercase.
#     enterdatedue = models.TextField(db_column='EnterDateDue', blank=True, null=True)  # Field name made lowercase.
#     enterprojectnumber = models.TextField(db_column='EnterProjectNumber', blank=True, null=True)  # Field name made lowercase.
#     familyid = models.TextField(db_column='FamilyID', blank=True, null=True)  # Field name made lowercase.
#     familyname = models.TextField(db_column='FamilyName', blank=True, null=True)  # Field name made lowercase.
#     fax = models.TextField(db_column='Fax', blank=True, null=True)  # Field name made lowercase.
#     firstprojlookup = models.TextField(db_column='FirstProjLookup', blank=True, null=True)  # Field name made lowercase.
#     holddata = models.TextField(db_column='HoldData', blank=True, null=True)  # Field name made lowercase.
#     holddatafollowup = models.TextField(db_column='HoldDataFollowup', blank=True, null=True)  # Field name made lowercase.
#     indraftdate = models.TextField(db_column='InDraftDate', blank=True, null=True)  # Field name made lowercase.
#     industrycode = models.TextField(db_column='IndustryCode', blank=True, null=True)  # Field name made lowercase.
#     inprojecttask = models.TextField(db_column='InProjectTask', blank=True, null=True)  # Field name made lowercase.
#     invaddress1 = models.TextField(db_column='InvAddress1', blank=True, null=True)  # Field name made lowercase.
#     invaddress2 = models.TextField(db_column='InvAddress2', blank=True, null=True)  # Field name made lowercase.
#     invcity = models.TextField(db_column='InvCity', blank=True, null=True)  # Field name made lowercase.
#     invcompanyname = models.TextField(db_column='InvCompanyName', blank=True, null=True)  # Field name made lowercase.
#     invcontactname = models.TextField(db_column='InvContactName', blank=True, null=True)  # Field name made lowercase.
#     invcountry = models.TextField(db_column='InvCountry', blank=True, null=True)  # Field name made lowercase.
#     invemail = models.TextField(db_column='InvEMail', blank=True, null=True)  # Field name made lowercase.
#     invfamilyid = models.TextField(db_column='InvFamilyID', blank=True, null=True)  # Field name made lowercase.
#     pohardcopy = models.TextField(db_column='POHardCopy', blank=True, null=True)  # Field name made lowercase.
#     ponumber = models.CharField(db_column='PONumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     invfamilyname = models.TextField(db_column='InvFamilyName', blank=True, null=True)  # Field name made lowercase.
#     invfax = models.TextField(db_column='InvFax', blank=True, null=True)  # Field name made lowercase.
#     invlocationid = models.TextField(db_column='InvLocationID', blank=True, null=True)  # Field name made lowercase.
#     invpersonid = models.TextField(db_column='InvPersonID', blank=True, null=True)  # Field name made lowercase.
#     invphone = models.TextField(db_column='InvPhone', blank=True, null=True)  # Field name made lowercase.
#     invstate = models.TextField(db_column='InvState', blank=True, null=True)  # Field name made lowercase.
#     invzip = models.TextField(db_column='InvZip', blank=True, null=True)  # Field name made lowercase.
#     locationid = models.TextField(db_column='LocationID', blank=True, null=True)  # Field name made lowercase.
#     methodservices = models.TextField(db_column='MethodServices', blank=True, null=True)  # Field name made lowercase.
#     methodservicetype = models.TextField(db_column='MethodServiceType', blank=True, null=True)  # Field name made lowercase.
#     msquoteallow = models.TextField(db_column='MSQuoteAllow', blank=True, null=True)  # Field name made lowercase.
#     needshardcopyrpt = models.TextField(db_column='NeedsHardCopyRpt', blank=True, null=True)  # Field name made lowercase.
#     overridecredithold = models.TextField(db_column='OverrideCreditHold', blank=True, null=True)  # Field name made lowercase.
#     personid = models.CharField(db_column='PersonID', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     projcanceled = models.TextField(db_column='ProjCanceled', blank=True, null=True)  # Field name made lowercase.
#     projcgmp = models.CharField(db_column='ProjCGMP', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     projdirector = models.TextField(db_column='ProjDirector', blank=True, null=True)  # Field name made lowercase.
#     projevent = models.TextField(db_column='ProjEvent', blank=True, null=True)  # Field name made lowercase.
#     projid = models.CharField(db_column='ProjID', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     projiso = models.CharField(db_column='ProjISO', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     projlitigation = models.TextField(db_column='ProjLitigation', blank=True, null=True)  # Field name made lowercase.
#     projpofollowup = models.TextField(db_column='ProjPOFollowup', blank=True, null=True)  # Field name made lowercase.
#     projpriority = models.CharField(db_column='ProjPriority', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     projqadatarvw = models.TextField(db_column='ProjQADataRvw', blank=True, null=True)  # Field name made lowercase.
#     projqadiscrepancy = models.TextField(db_column='ProjQADiscrepancy', blank=True, null=True)  # Field name made lowercase.
#     projqarev = models.TextField(db_column='ProjQARev', blank=True, null=True)  # Field name made lowercase.
#     projreptwrtr = models.TextField(db_column='ProjReptWrtr', blank=True, null=True)  # Field name made lowercase.
#     projsource = models.TextField(db_column='ProjSource', blank=True, null=True)  # Field name made lowercase.
#     projstatus = models.TextField(db_column='ProjStatus', blank=True, null=True)  # Field name made lowercase.
#     projtechrev = models.TextField(db_column='ProjTechRev', blank=True, null=True)  # Field name made lowercase.
#     protocolperson = models.TextField(db_column='ProtocolPerson', blank=True, null=True)  # Field name made lowercase.
#     quote = models.TextField(db_column='Quote', blank=True, null=True)  # Field name made lowercase.
#     reporttracking = models.TextField(db_column='ReportTracking', blank=True, null=True)  # Field name made lowercase.
#     returnreason = models.TextField(db_column='ReturnReason', blank=True, null=True)  # Field name made lowercase.
#     returnshipfrom = models.TextField(db_column='ReturnShipFrom', blank=True, null=True)  # Field name made lowercase.
#     returnshipmethod = models.TextField(db_column='ReturnShipMethod', blank=True, null=True)  # Field name made lowercase.
#     returnshipsentdate = models.TextField(db_column='ReturnShipSentDate', blank=True, null=True)  # Field name made lowercase.
#     returntracking = models.TextField(db_column='ReturnTracking', blank=True, null=True)  # Field name made lowercase.
#     rptcontactname = models.TextField(db_column='RptContactName', blank=True, null=True)  # Field name made lowercase.
#     rptdigby = models.TextField(db_column='RptDigBy', blank=True, null=True)  # Field name made lowercase.
#     rptdigsenddate = models.TextField(db_column='RptDigSendDate', blank=True, null=True)  # Field name made lowercase.
#     rptdigsendtime = models.TextField(db_column='RptDigSendTime', blank=True, null=True)  # Field name made lowercase.
#     rptdigsent = models.TextField(db_column='RptDigSent', blank=True, null=True)  # Field name made lowercase.
#     rptdigto = models.TextField(db_column='RptDigTo', blank=True, null=True)  # Field name made lowercase.
#     rpthardcopysent = models.TextField(db_column='RptHardCopySent', blank=True, null=True)  # Field name made lowercase.
#     rptlocationid = models.TextField(db_column='RptLocationID', blank=True, null=True)  # Field name made lowercase.
#     rptpersonid = models.TextField(db_column='RptPersonID', blank=True, null=True)  # Field name made lowercase.
#     rptshipfrom = models.TextField(db_column='RptShipFrom', blank=True, null=True)  # Field name made lowercase.
#     rptshipmethod = models.TextField(db_column='RptShipMethod', blank=True, null=True)  # Field name made lowercase.
#     rptshipsentdate = models.TextField(db_column='RptShipSentDate', blank=True, null=True)  # Field name made lowercase.
#     rptshipsenttime = models.TextField(db_column='RptShipSentTime', blank=True, null=True)  # Field name made lowercase.
#     sampdeascheds = models.TextField(db_column='SampDEAScheds', blank=True, null=True)  # Field name made lowercase.
#     samplecomments = models.TextField(db_column='SampleComments', blank=True, null=True)  # Field name made lowercase.
#     sampleqty = models.TextField(db_column='SampleQty', blank=True, null=True)  # Field name made lowercase.
#     samplesdea = models.TextField(db_column='SamplesDEA', blank=True, null=True)  # Field name made lowercase.
#     sampleshaz = models.TextField(db_column='SamplesHaz', blank=True, null=True)  # Field name made lowercase.
#     samplestorage = models.TextField(db_column='SampleStorage', blank=True, null=True)  # Field name made lowercase.
#     sampletypes = models.TextField(db_column='SampleTypes', blank=True, null=True)  # Field name made lowercase.
#     sampreturn = models.TextField(db_column='SampReturn', blank=True, null=True)  # Field name made lowercase.
#     state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase.
#     trackselection = models.TextField(db_column='TrackSelection', blank=True, null=True)  # Field name made lowercase.
#     validatenow = models.TextField(db_column='ValidateNow', blank=True, null=True)  # Field name made lowercase.
#     zip = models.TextField(db_column='Zip', blank=True, null=True)  # Field name made lowercase.
#     affiliates1 = models.TextField(db_column='Affiliates1', blank=True, null=True)  # Field name made lowercase.
#     affiliates2 = models.TextField(db_column='Affiliates2', blank=True, null=True)  # Field name made lowercase.
#     affiliatessummaryinfo1 = models.TextField(db_column='AffiliatesSummaryInfo1', blank=True, null=True)  # Field name made lowercase.
#     affiliatessummaryinfo2 = models.TextField(db_column='AffiliatesSummaryInfo2', blank=True, null=True)  # Field name made lowercase.
#     note1_desc = models.TextField(db_column='Note1_Desc', blank=True, null=True)  # Field name made lowercase.
#     note1_name = models.TextField(db_column='Note1_Name', blank=True, null=True)  # Field name made lowercase.
#     note2_desc = models.TextField(db_column='Note2_Desc', blank=True, null=True)  # Field name made lowercase.
#     note2_name = models.TextField(db_column='Note2_Name', blank=True, null=True)  # Field name made lowercase.
#     note3_desc = models.TextField(db_column='Note3_Desc', blank=True, null=True)  # Field name made lowercase.
#     note3_name = models.TextField(db_column='Note3_Name', blank=True, null=True)  # Field name made lowercase.
#     note4_desc = models.TextField(db_column='Note4_Desc', blank=True, null=True)  # Field name made lowercase.
#     note4_name = models.TextField(db_column='Note4_Name', blank=True, null=True)  # Field name made lowercase.
#     note5_desc = models.TextField(db_column='Note5_Desc', blank=True, null=True)  # Field name made lowercase.
#     note5_name = models.TextField(db_column='Note5_Name', blank=True, null=True)  # Field name made lowercase.
#     note6_desc = models.TextField(db_column='Note6_Desc', blank=True, null=True)  # Field name made lowercase.
#     note6_name = models.TextField(db_column='Note6_Name', blank=True, null=True)  # Field name made lowercase.
#     partlyhiddenservices = models.TextField(db_column='PartlyHiddenServices', blank=True, null=True)  # Field name made lowercase.
#     partlyhiddenservices_quotes = models.TextField(db_column='PartlyHiddenServices_Quotes', blank=True, null=True)  # Field name made lowercase.
#     prefobjrepid = models.TextField(db_column='PrefObjRepID', blank=True, null=True)  # Field name made lowercase.
#     projnum_digits = models.TextField(db_column='ProjNum_Digits', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         db_table = 'project_formarch'


# class ProjectFormn1(models.Model):
#     projectnumber = models.CharField(db_column='ProjectNumber', primary_key=True, max_length=35)  # Field name made lowercase.
#     familyid = models.CharField(db_column='FamilyID', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     locationid = models.CharField(db_column='LocationID', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     personid = models.CharField(db_column='PersonID', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     universalid = models.CharField(db_column='UniversalID', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     address1 = models.CharField(db_column='Address1', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     address2 = models.CharField(db_column='Address2', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     ampmreceived = models.CharField(db_column='AMPMReceived', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     analysisqty = models.CharField(db_column='AnalysisQty', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     analysistypes = models.CharField(db_column='AnalysisTypes', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     authordate = models.CharField(db_column='AuthorDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     authorname = models.CharField(db_column='AuthorName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     autoemailed = models.CharField(db_column='AutoEmailed', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     city = models.CharField(db_column='City', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     clientwaitreason = models.CharField(db_column='ClientWaitReason', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     companyfirstproj = models.CharField(db_column='CompanyFirstProj', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     companyname = models.CharField(db_column='CompanyName', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     complexproject = models.CharField(db_column='ComplexProject', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     contactname = models.CharField(db_column='ContactName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     contactnumber = models.CharField(db_column='ContactNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     country = models.CharField(db_column='Country', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     custcriteria = models.CharField(db_column='CustCriteria', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     customcharge = models.CharField(db_column='CustomCharge', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     customdescription = models.TextField(db_column='CustomDescription', blank=True, null=True)  # Field name made lowercase.
#     customreturncharge = models.CharField(db_column='CustomReturnCharge', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     custtype = models.CharField(db_column='CustType', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     dangerousgoods = models.CharField(db_column='DangerousGoods', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     datedue = models.CharField(db_column='DateDue', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     datereceived = models.CharField(db_column='DateReceived', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     datercvd = models.CharField(db_column='DateRcvd', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     email = models.CharField(db_column='EMail', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     enterdatedue = models.CharField(db_column='EnterDateDue', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     enterprojectnumber = models.CharField(db_column='EnterProjectNumber', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     familyname = models.CharField(db_column='FamilyName', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     fax = models.CharField(db_column='Fax', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     firstprojlookup = models.CharField(db_column='FirstProjLookup', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     holddata = models.CharField(db_column='HoldData', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     holddatafollowup = models.CharField(db_column='HoldDataFollowup', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     indraftdate = models.CharField(db_column='InDraftDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     industrycode = models.CharField(db_column='IndustryCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     inprojecttask = models.CharField(db_column='InProjectTask', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     invaddress1 = models.CharField(db_column='InvAddress1', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     invaddress2 = models.CharField(db_column='InvAddress2', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     invcity = models.CharField(db_column='InvCity', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     invcompanyname = models.CharField(db_column='InvCompanyName', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     invcontactname = models.CharField(db_column='InvContactName', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     invcountry = models.CharField(db_column='InvCountry', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     invemail = models.CharField(db_column='InvEMail', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     invfamilyid = models.CharField(db_column='InvFamilyID', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     invfamilyname = models.CharField(db_column='InvFamilyName', max_length=70, blank=True, null=True)  # Field name made lowercase.
#     invfax = models.CharField(db_column='InvFax', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     invlocationid = models.CharField(db_column='InvLocationID', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     invpersonid = models.CharField(db_column='InvPersonID', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     invphone = models.CharField(db_column='InvPhone', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     invstate = models.CharField(db_column='InvState', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     invzip = models.CharField(db_column='InvZip', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     methodservices = models.CharField(db_column='MethodServices', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     methodservicetype = models.CharField(db_column='MethodServiceType', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     msquoteallow = models.CharField(db_column='MSQuoteAllow', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     needshardcopyrpt = models.CharField(db_column='NeedsHardCopyRpt', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     note1_desc = models.TextField(db_column='Note1_Desc', blank=True, null=True)  # Field name made lowercase.
#     note1_name = models.TextField(db_column='Note1_Name', blank=True, null=True)  # Field name made lowercase.
#     note2_desc = models.TextField(db_column='Note2_Desc', blank=True, null=True)  # Field name made lowercase.
#     note2_name = models.TextField(db_column='Note2_Name', blank=True, null=True)  # Field name made lowercase.
#     note3_desc = models.TextField(db_column='Note3_Desc', blank=True, null=True)  # Field name made lowercase.
#     note3_name = models.TextField(db_column='Note3_Name', blank=True, null=True)  # Field name made lowercase.
#     note4_desc = models.TextField(db_column='Note4_Desc', blank=True, null=True)  # Field name made lowercase.
#     note4_name = models.TextField(db_column='Note4_Name', blank=True, null=True)  # Field name made lowercase.
#     note5_desc = models.TextField(db_column='Note5_Desc', blank=True, null=True)  # Field name made lowercase.
#     note5_name = models.TextField(db_column='Note5_Name', blank=True, null=True)  # Field name made lowercase.
#     note6_desc = models.TextField(db_column='Note6_Desc', blank=True, null=True)  # Field name made lowercase.
#     note6_name = models.TextField(db_column='Note6_Name', blank=True, null=True)  # Field name made lowercase.
#     overridecredithold = models.TextField(db_column='OverrideCreditHold', blank=True, null=True)  # Field name made lowercase.
#     projcanceled = models.CharField(db_column='ProjCanceled', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     projcgmp = models.CharField(db_column='ProjCGMP', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     projdirector = models.CharField(db_column='ProjDirector', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     projevent = models.CharField(db_column='ProjEvent', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     projid = models.CharField(db_column='ProjID', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     projiso = models.CharField(db_column='ProjISO', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     projlitigation = models.CharField(db_column='ProjLitigation', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     projpofollowup = models.CharField(db_column='ProjPOFollowup', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     projpriority = models.CharField(db_column='ProjPriority', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     projqadatarvw = models.CharField(db_column='ProjQADataRvw', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     projqadiscrepancy = models.CharField(db_column='ProjQADiscrepancy', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     projqarev = models.CharField(db_column='ProjQARev', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     projreptwrtr = models.CharField(db_column='ProjReptWrtr', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     projsource = models.CharField(db_column='ProjSource', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     projstatus = models.CharField(db_column='ProjStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     projtechrev = models.CharField(db_column='ProjTechRev', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     protocolperson = models.CharField(db_column='ProtocolPerson', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     pohardcopy = models.CharField(db_column='POHardCopy', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     ponumber = models.CharField(db_column='PONumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     quote = models.CharField(db_column='Quote', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     reporttracking = models.CharField(db_column='ReportTracking', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     returnreason = models.CharField(db_column='ReturnReason', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     returnshipfrom = models.CharField(db_column='ReturnShipFrom', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     returnshipmethod = models.CharField(db_column='ReturnShipMethod', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     returnshipsentdate = models.CharField(db_column='ReturnShipSentDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     returntracking = models.CharField(db_column='ReturnTracking', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     rptcontactname = models.CharField(db_column='RptContactName', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     rptdigby = models.CharField(db_column='RptDigBy', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     rptdigsenddate = models.CharField(db_column='RptDigSendDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     rptdigsendtime = models.CharField(db_column='RptDigSendTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     rptdigsent = models.CharField(db_column='RptDigSent', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     rptdigto = models.TextField(db_column='RptDigTo', blank=True, null=True)  # Field name made lowercase.
#     rpthardcopysent = models.CharField(db_column='RptHardCopySent', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     rptlocationid = models.CharField(db_column='RptLocationID', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     rptpersonid = models.CharField(db_column='RptPersonID', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     rptshipfrom = models.CharField(db_column='RptShipFrom', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     rptshipmethod = models.CharField(db_column='RptShipMethod', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     rptshipsentdate = models.CharField(db_column='RptShipSentDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     rptshipsenttime = models.CharField(db_column='RptShipSentTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     sampdeascheds = models.CharField(db_column='SampDEAScheds', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     sampleqty = models.CharField(db_column='SampleQty', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     samplesdea = models.CharField(db_column='SamplesDEA', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     sampleshaz = models.CharField(db_column='SamplesHaz', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     samplestorage = models.CharField(db_column='SampleStorage', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     sampletypes = models.TextField(db_column='SampleTypes', blank=True, null=True)  # Field name made lowercase.
#     sampreturn = models.CharField(db_column='SampReturn', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     state = models.CharField(db_column='State', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     trackselection = models.CharField(db_column='TrackSelection', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     zip = models.CharField(db_column='Zip', max_length=30, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         db_table = 'project_formn1'


# class Projformdata(models.Model):
#     projectnumber = models.CharField(db_column='ProjectNumber', primary_key=True, max_length=45)  # Field name made lowercase.
#     noteid = models.CharField(db_column='NoteID', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     universalid = models.CharField(db_column='UniversalID', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     acctnotes = models.TextField(db_column='AcctNotes', blank=True, null=True)  # Field name made lowercase.
#     actionlog = models.TextField(db_column='ActionLog', blank=True, null=True)  # Field name made lowercase.
#     actionnotes = models.TextField(db_column='ActionNotes', blank=True, null=True)  # Field name made lowercase.
#     addquotenotes = models.TextField(db_column='AddQuoteNotes', blank=True, null=True)  # Field name made lowercase.
#     created = models.TextField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
#     lastaccessed = models.TextField(db_column='LastAccessed', blank=True, null=True)  # Field name made lowercase.
#     lastmodified = models.TextField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.
#     address1 = models.TextField(db_column='Address1', blank=True, null=True)  # Field name made lowercase.
#     address2 = models.TextField(db_column='Address2', blank=True, null=True)  # Field name made lowercase.
#     ampmreceived = models.TextField(db_column='AMPMReceived', blank=True, null=True)  # Field name made lowercase.
#     analysiscomments = models.TextField(db_column='AnalysisComments', blank=True, null=True)  # Field name made lowercase.
#     analysisqty = models.IntegerField(db_column='AnalysisQty', blank=True, null=True)  # Field name made lowercase.
#     analysistypes = models.TextField(db_column='AnalysisTypes', blank=True, null=True)  # Field name made lowercase.
#     authordate = models.DateTimeField(db_column='AuthorDate', blank=True, null=True)  # Field name made lowercase.
#     authorname = models.TextField(db_column='AuthorName', blank=True, null=True)  # Field name made lowercase.
#     authors = models.TextField(db_column='Authors', blank=True, null=True)  # Field name made lowercase.
#     autoemailed = models.TextField(db_column='AutoEmailed', blank=True, null=True)  # Field name made lowercase.
#     city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.
#     clientwaitreason = models.TextField(db_column='ClientWaitReason', blank=True, null=True)  # Field name made lowercase.
#     companyfirstproj = models.TextField(db_column='CompanyFirstProj', blank=True, null=True)  # Field name made lowercase.
#     companyname = models.TextField(db_column='CompanyName', blank=True, null=True)  # Field name made lowercase.
#     complexproject = models.TextField(db_column='ComplexProject', blank=True, null=True)  # Field name made lowercase.
#     contactname = models.TextField(db_column='ContactName', blank=True, null=True)  # Field name made lowercase.
#     contactnumber = models.TextField(db_column='ContactNumber', blank=True, null=True)  # Field name made lowercase.
#     country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase.
#     custcriteria = models.TextField(db_column='CustCriteria', blank=True, null=True)  # Field name made lowercase.
#     customcharge = models.TextField(db_column='CustomCharge', blank=True, null=True)  # Field name made lowercase.
#     customdescription = models.TextField(db_column='CustomDescription', blank=True, null=True)  # Field name made lowercase.
#     customreturncharge = models.TextField(db_column='CustomReturnCharge', blank=True, null=True)  # Field name made lowercase.
#     custtype = models.TextField(db_column='CustType', blank=True, null=True)  # Field name made lowercase.
#     dangerousgoods = models.TextField(db_column='DangerousGoods', blank=True, null=True)  # Field name made lowercase.
#     datedue = models.DateTimeField(db_column='DateDue', blank=True, null=True)  # Field name made lowercase.
#     datereceived = models.DateTimeField(db_column='DateReceived', blank=True, null=True)  # Field name made lowercase.
#     datercvd = models.DateTimeField(db_column='DateRcvd', blank=True, null=True)  # Field name made lowercase.
#     editauthors = models.TextField(db_column='EditAuthors', blank=True, null=True)  # Field name made lowercase.
#     editdates = models.DateTimeField(db_column='EditDates', blank=True, null=True)  # Field name made lowercase.
#     editprojstatus = models.TextField(db_column='EditProjStatus', blank=True, null=True)  # Field name made lowercase.
#     email = models.TextField(db_column='EMail', blank=True, null=True)  # Field name made lowercase.
#     enterdatedue = models.DateTimeField(db_column='EnterDateDue', blank=True, null=True)  # Field name made lowercase.
#     enterprojectnumber = models.TextField(db_column='EnterProjectNumber', blank=True, null=True)  # Field name made lowercase.
#     familyid = models.TextField(db_column='FamilyID', blank=True, null=True)  # Field name made lowercase.
#     familyname = models.TextField(db_column='FamilyName', blank=True, null=True)  # Field name made lowercase.
#     fax = models.TextField(db_column='Fax', blank=True, null=True)  # Field name made lowercase.
#     firstprojlookup = models.TextField(db_column='FirstProjLookup', blank=True, null=True)  # Field name made lowercase.
#     holddata = models.TextField(db_column='HoldData', blank=True, null=True)  # Field name made lowercase.
#     holddatafollowup = models.TextField(db_column='HoldDataFollowup', blank=True, null=True)  # Field name made lowercase.
#     indraftdate = models.TextField(db_column='InDraftDate', blank=True, null=True)  # Field name made lowercase.
#     industrycode = models.TextField(db_column='IndustryCode', blank=True, null=True)  # Field name made lowercase.
#     inprojecttask = models.TextField(db_column='InProjectTask', blank=True, null=True)  # Field name made lowercase.
#     invaddress1 = models.TextField(db_column='InvAddress1', blank=True, null=True)  # Field name made lowercase.
#     invaddress2 = models.TextField(db_column='InvAddress2', blank=True, null=True)  # Field name made lowercase.
#     invcity = models.TextField(db_column='InvCity', blank=True, null=True)  # Field name made lowercase.
#     invcompanyname = models.TextField(db_column='InvCompanyName', blank=True, null=True)  # Field name made lowercase.
#     invcontactname = models.TextField(db_column='InvContactName', blank=True, null=True)  # Field name made lowercase.
#     invcountry = models.TextField(db_column='InvCountry', blank=True, null=True)  # Field name made lowercase.
#     invemail = models.TextField(db_column='InvEMail', blank=True, null=True)  # Field name made lowercase.
#     invfamilyid = models.TextField(db_column='InvFamilyID', blank=True, null=True)  # Field name made lowercase.
#     pohardcopy = models.TextField(db_column='POHardCopy', blank=True, null=True)  # Field name made lowercase.
#     ponumber = models.CharField(db_column='PONumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     invfamilyname = models.TextField(db_column='InvFamilyName', blank=True, null=True)  # Field name made lowercase.
#     invfax = models.TextField(db_column='InvFax', blank=True, null=True)  # Field name made lowercase.
#     invlocationid = models.TextField(db_column='InvLocationID', blank=True, null=True)  # Field name made lowercase.
#     invpersonid = models.TextField(db_column='InvPersonID', blank=True, null=True)  # Field name made lowercase.
#     invphone = models.TextField(db_column='InvPhone', blank=True, null=True)  # Field name made lowercase.
#     invstate = models.TextField(db_column='InvState', blank=True, null=True)  # Field name made lowercase.
#     invzip = models.TextField(db_column='InvZip', blank=True, null=True)  # Field name made lowercase.
#     locationid = models.TextField(db_column='LocationID', blank=True, null=True)  # Field name made lowercase.
#     methodservices = models.TextField(db_column='MethodServices', blank=True, null=True)  # Field name made lowercase.
#     methodservicetype = models.TextField(db_column='MethodServiceType', blank=True, null=True)  # Field name made lowercase.
#     msquoteallow = models.TextField(db_column='MSQuoteAllow', blank=True, null=True)  # Field name made lowercase.
#     needshardcopyrpt = models.TextField(db_column='NeedsHardCopyRpt', blank=True, null=True)  # Field name made lowercase.
#     overridecredithold = models.TextField(db_column='OverrideCreditHold', blank=True, null=True)  # Field name made lowercase.
#     personid = models.CharField(db_column='PersonID', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     projcanceled = models.TextField(db_column='ProjCanceled', blank=True, null=True)  # Field name made lowercase.
#     projcgmp = models.CharField(db_column='ProjCGMP', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     projdirector = models.TextField(db_column='ProjDirector', blank=True, null=True)  # Field name made lowercase.
#     projevent = models.TextField(db_column='ProjEvent', blank=True, null=True)  # Field name made lowercase.
#     projid = models.CharField(db_column='ProjID', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     projiso = models.CharField(db_column='ProjISO', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     projlitigation = models.TextField(db_column='ProjLitigation', blank=True, null=True)  # Field name made lowercase.
#     projpofollowup = models.TextField(db_column='ProjPOFollowup', blank=True, null=True)  # Field name made lowercase.
#     projpriority = models.CharField(db_column='ProjPriority', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     projqadatarvw = models.TextField(db_column='ProjQADataRvw', blank=True, null=True)  # Field name made lowercase.
#     projqadiscrepancy = models.TextField(db_column='ProjQADiscrepancy', blank=True, null=True)  # Field name made lowercase.
#     projqarev = models.TextField(db_column='ProjQARev', blank=True, null=True)  # Field name made lowercase.
#     projreptwrtr = models.TextField(db_column='ProjReptWrtr', blank=True, null=True)  # Field name made lowercase.
#     projsource = models.TextField(db_column='ProjSource', blank=True, null=True)  # Field name made lowercase.
#     projstatus = models.TextField(db_column='ProjStatus', blank=True, null=True)  # Field name made lowercase.
#     projtechrev = models.TextField(db_column='ProjTechRev', blank=True, null=True)  # Field name made lowercase.
#     protocolperson = models.TextField(db_column='ProtocolPerson', blank=True, null=True)  # Field name made lowercase.
#     quote = models.TextField(db_column='Quote', blank=True, null=True)  # Field name made lowercase.
#     reporttracking = models.TextField(db_column='ReportTracking', blank=True, null=True)  # Field name made lowercase.
#     returnreason = models.TextField(db_column='ReturnReason', blank=True, null=True)  # Field name made lowercase.
#     returnshipfrom = models.TextField(db_column='ReturnShipFrom', blank=True, null=True)  # Field name made lowercase.
#     returnshipmethod = models.TextField(db_column='ReturnShipMethod', blank=True, null=True)  # Field name made lowercase.
#     returnshipsentdate = models.DateTimeField(db_column='ReturnShipSentDate', blank=True, null=True)  # Field name made lowercase.
#     returntracking = models.TextField(db_column='ReturnTracking', blank=True, null=True)  # Field name made lowercase.
#     rptcontactname = models.TextField(db_column='RptContactName', blank=True, null=True)  # Field name made lowercase.
#     rptdigby = models.TextField(db_column='RptDigBy', blank=True, null=True)  # Field name made lowercase.
#     rptdigsenddate = models.DateTimeField(db_column='RptDigSendDate', blank=True, null=True)  # Field name made lowercase.
#     rptdigsendtime = models.DateTimeField(db_column='RptDigSendTime', blank=True, null=True)  # Field name made lowercase.
#     rptdigsent = models.TextField(db_column='RptDigSent', blank=True, null=True)  # Field name made lowercase.
#     rptdigto = models.TextField(db_column='RptDigTo', blank=True, null=True)  # Field name made lowercase.
#     rpthardcopysent = models.TextField(db_column='RptHardCopySent', blank=True, null=True)  # Field name made lowercase.
#     rptlocationid = models.TextField(db_column='RptLocationID', blank=True, null=True)  # Field name made lowercase.
#     rptpersonid = models.TextField(db_column='RptPersonID', blank=True, null=True)  # Field name made lowercase.
#     rptshipfrom = models.TextField(db_column='RptShipFrom', blank=True, null=True)  # Field name made lowercase.
#     rptshipmethod = models.TextField(db_column='RptShipMethod', blank=True, null=True)  # Field name made lowercase.
#     rptshipsentdate = models.DateTimeField(db_column='RptShipSentDate', blank=True, null=True)  # Field name made lowercase.
#     rptshipsenttime = models.DateTimeField(db_column='RptShipSentTime', blank=True, null=True)  # Field name made lowercase.
#     sampdeascheds = models.TextField(db_column='SampDEAScheds', blank=True, null=True)  # Field name made lowercase.
#     samplecomments = models.TextField(db_column='SampleComments', blank=True, null=True)  # Field name made lowercase.
#     sampleqty = models.TextField(db_column='SampleQty', blank=True, null=True)  # Field name made lowercase.
#     samplesdea = models.TextField(db_column='SamplesDEA', blank=True, null=True)  # Field name made lowercase.
#     sampleshaz = models.TextField(db_column='SamplesHaz', blank=True, null=True)  # Field name made lowercase.
#     samplestorage = models.TextField(db_column='SampleStorage', blank=True, null=True)  # Field name made lowercase.
#     sampletypes = models.TextField(db_column='SampleTypes', blank=True, null=True)  # Field name made lowercase.
#     sampreturn = models.TextField(db_column='SampReturn', blank=True, null=True)  # Field name made lowercase.
#     state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase.
#     trackselection = models.TextField(db_column='TrackSelection', blank=True, null=True)  # Field name made lowercase.
#     validatenow = models.TextField(db_column='ValidateNow', blank=True, null=True)  # Field name made lowercase.
#     zip = models.TextField(db_column='Zip', blank=True, null=True)  # Field name made lowercase.
#     affiliates1 = models.TextField(db_column='Affiliates1', blank=True, null=True)  # Field name made lowercase.
#     affiliates2 = models.TextField(db_column='Affiliates2', blank=True, null=True)  # Field name made lowercase.
#     affiliatessummaryinfo1 = models.TextField(db_column='AffiliatesSummaryInfo1', blank=True, null=True)  # Field name made lowercase.
#     affiliatessummaryinfo2 = models.TextField(db_column='AffiliatesSummaryInfo2', blank=True, null=True)  # Field name made lowercase.
#     note1_desc = models.TextField(db_column='Note1_Desc', blank=True, null=True)  # Field name made lowercase.
#     note1_name = models.TextField(db_column='Note1_Name', blank=True, null=True)  # Field name made lowercase.
#     note2_desc = models.TextField(db_column='Note2_Desc', blank=True, null=True)  # Field name made lowercase.
#     note2_name = models.TextField(db_column='Note2_Name', blank=True, null=True)  # Field name made lowercase.
#     note3_desc = models.TextField(db_column='Note3_Desc', blank=True, null=True)  # Field name made lowercase.
#     note3_name = models.TextField(db_column='Note3_Name', blank=True, null=True)  # Field name made lowercase.
#     note4_desc = models.TextField(db_column='Note4_Desc', blank=True, null=True)  # Field name made lowercase.
#     note4_name = models.TextField(db_column='Note4_Name', blank=True, null=True)  # Field name made lowercase.
#     note5_desc = models.TextField(db_column='Note5_Desc', blank=True, null=True)  # Field name made lowercase.
#     note5_name = models.TextField(db_column='Note5_Name', blank=True, null=True)  # Field name made lowercase.
#     note6_desc = models.TextField(db_column='Note6_Desc', blank=True, null=True)  # Field name made lowercase.
#     note6_name = models.TextField(db_column='Note6_Name', blank=True, null=True)  # Field name made lowercase.
#     partlyhiddenservices = models.TextField(db_column='PartlyHiddenServices', blank=True, null=True)  # Field name made lowercase.
#     partlyhiddenservices_quotes = models.TextField(db_column='PartlyHiddenServices_Quotes', blank=True, null=True)  # Field name made lowercase.
#     prefobjrepid = models.TextField(db_column='PrefObjRepID', blank=True, null=True)  # Field name made lowercase.
#     projnum_digits = models.TextField(db_column='ProjNum_Digits', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         db_table = 'projformdata'


# class Quoteanalysis(models.Model):
#     quotenumber = models.CharField(db_column='QuoteNumber', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     aacamt0 = models.TextField(db_column='AACAmt0', blank=True, null=True)  # Field name made lowercase.
#     aacamt1 = models.TextField(db_column='AACAmt1', blank=True, null=True)  # Field name made lowercase.
#     aacamt2 = models.TextField(db_column='AACAmt2', blank=True, null=True)  # Field name made lowercase.
#     aacamt3 = models.TextField(db_column='AACAmt3', blank=True, null=True)  # Field name made lowercase.
#     aacamt4 = models.TextField(db_column='AACAmt4', blank=True, null=True)  # Field name made lowercase.
#     aacamt5 = models.TextField(db_column='AACAmt5', blank=True, null=True)  # Field name made lowercase.
#     aacamt6 = models.TextField(db_column='AACAmt6', blank=True, null=True)  # Field name made lowercase.
#     aacdesc0 = models.TextField(db_column='AACDesc0', blank=True, null=True)  # Field name made lowercase.
#     aacdesc1 = models.TextField(db_column='AACDesc1', blank=True, null=True)  # Field name made lowercase.
#     aacdesc2 = models.TextField(db_column='AACDesc2', blank=True, null=True)  # Field name made lowercase.
#     aacdesc3 = models.TextField(db_column='AACDesc3', blank=True, null=True)  # Field name made lowercase.
#     aacdesc4 = models.TextField(db_column='AACDesc4', blank=True, null=True)  # Field name made lowercase.
#     aacdesc5 = models.TextField(db_column='AACDesc5', blank=True, null=True)  # Field name made lowercase.
#     aacdesc6 = models.TextField(db_column='AACDesc6', blank=True, null=True)  # Field name made lowercase.
#     aacqty0 = models.TextField(db_column='AACQty0', blank=True, null=True)  # Field name made lowercase.
#     aacqty1 = models.TextField(db_column='AACQty1', blank=True, null=True)  # Field name made lowercase.
#     aacqty2 = models.TextField(db_column='AACQty2', blank=True, null=True)  # Field name made lowercase.
#     aacqty3 = models.TextField(db_column='AACQty3', blank=True, null=True)  # Field name made lowercase.
#     aacqty4 = models.TextField(db_column='AACQty4', blank=True, null=True)  # Field name made lowercase.
#     aacqty5 = models.TextField(db_column='AACQty5', blank=True, null=True)  # Field name made lowercase.
#     aacqty6 = models.TextField(db_column='AACQty6', blank=True, null=True)  # Field name made lowercase.
#     aactot0 = models.TextField(db_column='AACTot0', blank=True, null=True)  # Field name made lowercase.
#     aactot1 = models.TextField(db_column='AACTot1', blank=True, null=True)  # Field name made lowercase.
#     aactot2 = models.TextField(db_column='AACTot2', blank=True, null=True)  # Field name made lowercase.
#     aactot3 = models.TextField(db_column='AACTot3', blank=True, null=True)  # Field name made lowercase.
#     aactot4 = models.TextField(db_column='AACTot4', blank=True, null=True)  # Field name made lowercase.
#     aactot5 = models.TextField(db_column='AACTot5', blank=True, null=True)  # Field name made lowercase.
#     aactot6 = models.TextField(db_column='AACTot6', blank=True, null=True)  # Field name made lowercase.
#     actionlog = models.TextField(db_column='ActionLog', blank=True, null=True)  # Field name made lowercase.
#     actionnotes = models.TextField(db_column='ActionNotes', blank=True, null=True)  # Field name made lowercase.
#     ampmreceived = models.TextField(db_column='AMPMReceived', blank=True, null=True)  # Field name made lowercase.
#     analysisatfchrgst = models.TextField(db_column='AnalysisATFChrgSt', blank=True, null=True)  # Field name made lowercase.
#     analysiscarrierused = models.TextField(db_column='AnalysisCarrierUsed', blank=True, null=True)  # Field name made lowercase.
#     analysiscgmpchrg = models.TextField(db_column='AnalysiscGMPChrg', blank=True, null=True)  # Field name made lowercase.
#     analysiscgmpchrgst = models.TextField(db_column='AnalysiscGMPChrgSt', blank=True, null=True)  # Field name made lowercase.
#     analysisdeachrgst = models.TextField(db_column='AnalysisDEAChrgSt', blank=True, null=True)  # Field name made lowercase.
#     analysisdept = models.TextField(db_column='AnalysisDept', blank=True, null=True)  # Field name made lowercase.
#     analysisdisc = models.TextField(db_column='AnalysisDisc', blank=True, null=True)  # Field name made lowercase.
#     analysisdiscst = models.TextField(db_column='AnalysisDiscSt', blank=True, null=True)  # Field name made lowercase.
#     analysisdiscstat = models.TextField(db_column='AnalysisDiscStat', blank=True, null=True)  # Field name made lowercase.
#     analysishazchrg = models.TextField(db_column='AnalysisHazChrg', blank=True, null=True)  # Field name made lowercase.
#     analysishazchrgst = models.TextField(db_column='AnalysisHazChrgSt', blank=True, null=True)  # Field name made lowercase.
#     analysisinstr = models.TextField(db_column='AnalysisInstr', blank=True, null=True)  # Field name made lowercase.
#     analysisisochrg = models.TextField(db_column='AnalysisISOChrg', blank=True, null=True)  # Field name made lowercase.
#     analysisisochrgst = models.TextField(db_column='AnalysisISOChrgSt', blank=True, null=True)  # Field name made lowercase.
#     analysisnum = models.TextField(db_column='AnalysisNum', blank=True, null=True)  # Field name made lowercase.
#     analysisprc = models.TextField(db_column='AnalysisPrc', blank=True, null=True)  # Field name made lowercase.
#     analysisprcent = models.TextField(db_column='AnalysisPrcEnt', blank=True, null=True)  # Field name made lowercase.
#     analysisprcentst = models.TextField(db_column='AnalysisPrcEntSt', blank=True, null=True)  # Field name made lowercase.
#     analysisprcst = models.TextField(db_column='AnalysisPrcSt', blank=True, null=True)  # Field name made lowercase.
#     analysispriochrg = models.TextField(db_column='AnalysisPrioChrg', blank=True, null=True)  # Field name made lowercase.
#     analysispriority = models.TextField(db_column='AnalysisPriority', blank=True, null=True)  # Field name made lowercase.
#     analysispriost = models.TextField(db_column='AnalysisPrioSt', blank=True, null=True)  # Field name made lowercase.
#     analysisqty = models.TextField(db_column='AnalysisQty', blank=True, null=True)  # Field name made lowercase.
#     analysissrvc = models.TextField(db_column='AnalysisSrvc', blank=True, null=True)  # Field name made lowercase.
#     analysisstandardrun = models.TextField(db_column='AnalysisStandardRun', blank=True, null=True)  # Field name made lowercase.
#     analysistotal = models.TextField(db_column='AnalysisTotal', blank=True, null=True)  # Field name made lowercase.
#     analysistotalwaddl = models.TextField(db_column='AnalysisTotalwAddl', blank=True, null=True)  # Field name made lowercase.
#     analysistype = models.TextField(db_column='AnalysisType', blank=True, null=True)  # Field name made lowercase.
#     anlpvqty = models.TextField(db_column='AnlPVQty', blank=True, null=True)  # Field name made lowercase.
#     atfqty = models.TextField(db_column='ATFQty', blank=True, null=True)  # Field name made lowercase.
#     atfyn = models.TextField(db_column='ATFYN', blank=True, null=True)  # Field name made lowercase.
#     authordate = models.TextField(db_column='AuthorDate', blank=True, null=True)  # Field name made lowercase.
#     authorname = models.TextField(db_column='AuthorName', blank=True, null=True)  # Field name made lowercase.
#     authors = models.TextField(db_column='Authors', blank=True, null=True)  # Field name made lowercase.
#     billingnotestext = models.TextField(db_column='BillingNotesText', blank=True, null=True)  # Field name made lowercase.
#     cgmpchange = models.TextField(db_column='cGMPChange', blank=True, null=True)  # Field name made lowercase.
#     cgmpenterprc = models.TextField(db_column='cGMPEnterPrc', blank=True, null=True)  # Field name made lowercase.
#     comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
#     companyname = models.TextField(db_column='CompanyName', blank=True, null=True)  # Field name made lowercase.
#     created = models.TextField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
#     customdesc = models.TextField(db_column='CustomDesc', blank=True, null=True)  # Field name made lowercase.
#     custommsdesc = models.TextField(db_column='CustomMSDesc', blank=True, null=True)  # Field name made lowercase.
#     customunitname = models.TextField(db_column='CustomUnitName', blank=True, null=True)  # Field name made lowercase.
#     customunitqty = models.TextField(db_column='CustomUnitQty', blank=True, null=True)  # Field name made lowercase.
#     datedue = models.TextField(db_column='DateDue', blank=True, null=True)  # Field name made lowercase.
#     datereceived = models.TextField(db_column='DateReceived', blank=True, null=True)  # Field name made lowercase.
#     deaqty = models.TextField(db_column='DEAQty', blank=True, null=True)  # Field name made lowercase.
#     deayn = models.TextField(db_column='DEAYN', blank=True, null=True)  # Field name made lowercase.
#     disctype = models.TextField(db_column='DiscType', blank=True, null=True)  # Field name made lowercase.
#     docid = models.TextField(db_column='DocID', blank=True, null=True)  # Field name made lowercase.
#     editauthors = models.TextField(db_column='EditAuthors', blank=True, null=True)  # Field name made lowercase.
#     editdates = models.TextField(db_column='EditDates', blank=True, null=True)  # Field name made lowercase.
#     editdatename = models.TextField(db_column='EditDateName', blank=True, null=True)  # Field name made lowercase.
#     editprojstatus = models.TextField(db_column='EditProjStatus', blank=True, null=True)  # Field name made lowercase.
#     embeddedobjects = models.TextField(db_column='EmbeddedObjects', blank=True, null=True)  # Field name made lowercase.
#     enterdatedue = models.TextField(db_column='EnterDateDue', blank=True, null=True)  # Field name made lowercase.
#     familyid = models.TextField(db_column='FamilyID', blank=True, null=True)  # Field name made lowercase.
#     familyid_1 = models.TextField(db_column='FamilyID_1', blank=True, null=True)  # Field name made lowercase.
#     familyname = models.TextField(db_column='FamilyName', blank=True, null=True)  # Field name made lowercase.
#     familyname_1 = models.TextField(db_column='FamilyName_1', blank=True, null=True)  # Field name made lowercase.
#     finalize = models.TextField(db_column='Finalize', blank=True, null=True)  # Field name made lowercase.
#     finalizeddate = models.TextField(db_column='FinalizedDate', blank=True, null=True)  # Field name made lowercase.
#     hasatfsamples = models.TextField(db_column='HasATFSamples', blank=True, null=True)  # Field name made lowercase.
#     hasdeasamples = models.TextField(db_column='HasDEASamples', blank=True, null=True)  # Field name made lowercase.
#     hiddenservices_quotes = models.TextField(db_column='HiddenServices_Quotes', blank=True, null=True)  # Field name made lowercase.
#     inprojecttask = models.TextField(db_column='InProjectTask', blank=True, null=True)  # Field name made lowercase.
#     invfamilyid = models.TextField(db_column='InvFamilyID', blank=True, null=True)  # Field name made lowercase.
#     invfamilyname = models.TextField(db_column='InvFamilyName', blank=True, null=True)  # Field name made lowercase.
#     ishighatf = models.TextField(db_column='IsHighATF', blank=True, null=True)  # Field name made lowercase.
#     ishighdea = models.TextField(db_column='IsHighDEA', blank=True, null=True)  # Field name made lowercase.
#     iso = models.TextField(db_column='ISO', blank=True, null=True)  # Field name made lowercase.
#     isoenterprc = models.TextField(db_column='ISOEnterPrc', blank=True, null=True)  # Field name made lowercase.
#     lastaccessed = models.TextField(db_column='LastAccessed', blank=True, null=True)  # Field name made lowercase.
#     lastmodified = models.TextField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.
#     linedescription = models.TextField(db_column='lineDescription', blank=True, null=True)  # Field name made lowercase.
#     lineitems = models.TextField(db_column='LineItems', blank=True, null=True)  # Field name made lowercase.
#     locationid = models.TextField(db_column='LocationID', blank=True, null=True)  # Field name made lowercase.
#     methodservices = models.TextField(db_column='MethodServices', blank=True, null=True)  # Field name made lowercase.
#     noteid = models.TextField(db_column='NoteID', blank=True, null=True)  # Field name made lowercase.
#     note1_desc = models.TextField(db_column='Note1_Desc', blank=True, null=True)  # Field name made lowercase.
#     note1_name = models.TextField(db_column='Note1_Name', blank=True, null=True)  # Field name made lowercase.
#     note2_desc = models.TextField(db_column='Note2_Desc', blank=True, null=True)  # Field name made lowercase.
#     note2_name = models.TextField(db_column='Note2_Name', blank=True, null=True)  # Field name made lowercase.
#     note3_desc = models.TextField(db_column='Note3_Desc', blank=True, null=True)  # Field name made lowercase.
#     note3_name = models.TextField(db_column='Note3_Name', blank=True, null=True)  # Field name made lowercase.
#     note4_desc = models.TextField(db_column='Note4_Desc', blank=True, null=True)  # Field name made lowercase.
#     note4_name = models.TextField(db_column='Note4_Name', blank=True, null=True)  # Field name made lowercase.
#     note5_desc = models.TextField(db_column='Note5_Desc', blank=True, null=True)  # Field name made lowercase.
#     note5_name = models.TextField(db_column='Note5_Name', blank=True, null=True)  # Field name made lowercase.
#     note6_desc = models.TextField(db_column='Note6_Desc', blank=True, null=True)  # Field name made lowercase.
#     note6_name = models.TextField(db_column='Note6_Name', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_1 = models.TextField(db_column='Notes_Text_Loc_1', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_2 = models.TextField(db_column='Notes_Text_Loc_2', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_3 = models.TextField(db_column='Notes_Text_Loc_3', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_4 = models.TextField(db_column='Notes_Text_Loc_4', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_5 = models.TextField(db_column='Notes_Text_Loc_5', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_6 = models.TextField(db_column='Notes_Text_Loc_6', blank=True, null=True)  # Field name made lowercase.
#     notes_text_org_archive = models.TextField(db_column='Notes_Text_Org_Archive', blank=True, null=True)  # Field name made lowercase.
#     notes_text_org_historical = models.TextField(db_column='Notes_Text_Org_Historical', blank=True, null=True)  # Field name made lowercase.
#     overridecgmp = models.TextField(db_column='OverridecGMP', blank=True, null=True)  # Field name made lowercase.
#     overrideiso = models.TextField(db_column='OverrideISO', blank=True, null=True)  # Field name made lowercase.
#     overrideprc = models.TextField(db_column='OverridePrc', blank=True, null=True)  # Field name made lowercase.
#     priceagentrun = models.TextField(db_column='PriceAgentRun', blank=True, null=True)  # Field name made lowercase.
#     projcgmp = models.TextField(db_column='ProjCGMP', blank=True, null=True)  # Field name made lowercase.
#     projid = models.CharField(db_column='ProjID', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     projiso = models.TextField(db_column='ProjISO', blank=True, null=True)  # Field name made lowercase.
#     partlyhiddenservices = models.TextField(db_column='PartlyHiddenServices', blank=True, null=True)  # Field name made lowercase.
#     partlyhiddenservices_quotes = models.TextField(db_column='PartlyHiddenServices_Quotes', blank=True, null=True)  # Field name made lowercase.
#     prefobjrepid = models.TextField(db_column='PrefObjRepID', blank=True, null=True)  # Field name made lowercase.
#     projnum_digits = models.TextField(db_column='ProjNum_Digits', blank=True, null=True)  # Field name made lowercase.
#     runqty = models.TextField(db_column='RunQty', blank=True, null=True)  # Field name made lowercase.
#     sampqty = models.TextField(db_column='SampQty', blank=True, null=True)  # Field name made lowercase.
#     subanalysistotal = models.TextField(db_column='SubAnalysisTotal', blank=True, null=True)  # Field name made lowercase.
#     totalbeforedisco = models.TextField(db_column='TotalBeforeDisco', blank=True, null=True)  # Field name made lowercase.
#     turnaroundtext = models.TextField(db_column='TurnaroundText', blank=True, null=True)  # Field name made lowercase.
#     turnaroundtextquote100 = models.TextField(db_column='TurnaroundTextQuote100', blank=True, null=True)  # Field name made lowercase.
#     turnaroundtextquote50 = models.TextField(db_column='TurnaroundTextQuote50', blank=True, null=True)  # Field name made lowercase.
#     turnaroundtextquotestd = models.TextField(db_column='TurnaroundTextQuoteStd', blank=True, null=True)  # Field name made lowercase.
#     usecustomdesc = models.TextField(db_column='UseCustomDesc', blank=True, null=True)  # Field name made lowercase.
#     usecustomunits = models.TextField(db_column='UseCustomUnits', blank=True, null=True)  # Field name made lowercase.
#     universalid = models.CharField(db_column='UniversalID', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     validateevent = models.TextField(db_column='ValidateEvent', blank=True, null=True)  # Field name made lowercase.
#     validatenow = models.TextField(db_column='ValidateNow', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         db_table = 'quoteanalysis'


# class Quoteanalysisarch(models.Model):
#     quotenumber = models.CharField(db_column='QuoteNumber', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     aacamt0 = models.TextField(db_column='AACAmt0', blank=True, null=True)  # Field name made lowercase.
#     aacamt1 = models.TextField(db_column='AACAmt1', blank=True, null=True)  # Field name made lowercase.
#     aacamt2 = models.TextField(db_column='AACAmt2', blank=True, null=True)  # Field name made lowercase.
#     aacamt3 = models.TextField(db_column='AACAmt3', blank=True, null=True)  # Field name made lowercase.
#     aacamt4 = models.TextField(db_column='AACAmt4', blank=True, null=True)  # Field name made lowercase.
#     aacamt5 = models.TextField(db_column='AACAmt5', blank=True, null=True)  # Field name made lowercase.
#     aacamt6 = models.TextField(db_column='AACAmt6', blank=True, null=True)  # Field name made lowercase.
#     aacdesc0 = models.TextField(db_column='AACDesc0', blank=True, null=True)  # Field name made lowercase.
#     aacdesc1 = models.TextField(db_column='AACDesc1', blank=True, null=True)  # Field name made lowercase.
#     aacdesc2 = models.TextField(db_column='AACDesc2', blank=True, null=True)  # Field name made lowercase.
#     aacdesc3 = models.TextField(db_column='AACDesc3', blank=True, null=True)  # Field name made lowercase.
#     aacdesc4 = models.TextField(db_column='AACDesc4', blank=True, null=True)  # Field name made lowercase.
#     aacdesc5 = models.TextField(db_column='AACDesc5', blank=True, null=True)  # Field name made lowercase.
#     aacdesc6 = models.TextField(db_column='AACDesc6', blank=True, null=True)  # Field name made lowercase.
#     aacqty0 = models.TextField(db_column='AACQty0', blank=True, null=True)  # Field name made lowercase.
#     aacqty1 = models.TextField(db_column='AACQty1', blank=True, null=True)  # Field name made lowercase.
#     aacqty2 = models.TextField(db_column='AACQty2', blank=True, null=True)  # Field name made lowercase.
#     aacqty3 = models.TextField(db_column='AACQty3', blank=True, null=True)  # Field name made lowercase.
#     aacqty4 = models.TextField(db_column='AACQty4', blank=True, null=True)  # Field name made lowercase.
#     aacqty5 = models.TextField(db_column='AACQty5', blank=True, null=True)  # Field name made lowercase.
#     aacqty6 = models.TextField(db_column='AACQty6', blank=True, null=True)  # Field name made lowercase.
#     aactot0 = models.TextField(db_column='AACTot0', blank=True, null=True)  # Field name made lowercase.
#     aactot1 = models.TextField(db_column='AACTot1', blank=True, null=True)  # Field name made lowercase.
#     aactot2 = models.TextField(db_column='AACTot2', blank=True, null=True)  # Field name made lowercase.
#     aactot3 = models.TextField(db_column='AACTot3', blank=True, null=True)  # Field name made lowercase.
#     aactot4 = models.TextField(db_column='AACTot4', blank=True, null=True)  # Field name made lowercase.
#     aactot5 = models.TextField(db_column='AACTot5', blank=True, null=True)  # Field name made lowercase.
#     aactot6 = models.TextField(db_column='AACTot6', blank=True, null=True)  # Field name made lowercase.
#     actionlog = models.TextField(db_column='ActionLog', blank=True, null=True)  # Field name made lowercase.
#     actionnotes = models.TextField(db_column='ActionNotes', blank=True, null=True)  # Field name made lowercase.
#     ampmreceived = models.TextField(db_column='AMPMReceived', blank=True, null=True)  # Field name made lowercase.
#     analysisatfchrgst = models.TextField(db_column='AnalysisATFChrgSt', blank=True, null=True)  # Field name made lowercase.
#     analysiscarrierused = models.TextField(db_column='AnalysisCarrierUsed', blank=True, null=True)  # Field name made lowercase.
#     analysiscgmpchrg = models.TextField(db_column='AnalysiscGMPChrg', blank=True, null=True)  # Field name made lowercase.
#     analysiscgmpchrgst = models.TextField(db_column='AnalysiscGMPChrgSt', blank=True, null=True)  # Field name made lowercase.
#     analysisdeachrgst = models.TextField(db_column='AnalysisDEAChrgSt', blank=True, null=True)  # Field name made lowercase.
#     analysisdept = models.TextField(db_column='AnalysisDept', blank=True, null=True)  # Field name made lowercase.
#     analysisdisc = models.TextField(db_column='AnalysisDisc', blank=True, null=True)  # Field name made lowercase.
#     analysisdiscst = models.TextField(db_column='AnalysisDiscSt', blank=True, null=True)  # Field name made lowercase.
#     analysisdiscstat = models.TextField(db_column='AnalysisDiscStat', blank=True, null=True)  # Field name made lowercase.
#     analysishazchrg = models.TextField(db_column='AnalysisHazChrg', blank=True, null=True)  # Field name made lowercase.
#     analysishazchrgst = models.TextField(db_column='AnalysisHazChrgSt', blank=True, null=True)  # Field name made lowercase.
#     analysisinstr = models.TextField(db_column='AnalysisInstr', blank=True, null=True)  # Field name made lowercase.
#     analysisisochrg = models.TextField(db_column='AnalysisISOChrg', blank=True, null=True)  # Field name made lowercase.
#     analysisisochrgst = models.TextField(db_column='AnalysisISOChrgSt', blank=True, null=True)  # Field name made lowercase.
#     analysisnum = models.TextField(db_column='AnalysisNum', blank=True, null=True)  # Field name made lowercase.
#     analysisprc = models.TextField(db_column='AnalysisPrc', blank=True, null=True)  # Field name made lowercase.
#     analysisprcent = models.TextField(db_column='AnalysisPrcEnt', blank=True, null=True)  # Field name made lowercase.
#     analysisprcentst = models.TextField(db_column='AnalysisPrcEntSt', blank=True, null=True)  # Field name made lowercase.
#     analysisprcst = models.TextField(db_column='AnalysisPrcSt', blank=True, null=True)  # Field name made lowercase.
#     analysispriochrg = models.TextField(db_column='AnalysisPrioChrg', blank=True, null=True)  # Field name made lowercase.
#     analysispriority = models.TextField(db_column='AnalysisPriority', blank=True, null=True)  # Field name made lowercase.
#     analysispriost = models.TextField(db_column='AnalysisPrioSt', blank=True, null=True)  # Field name made lowercase.
#     analysisqty = models.TextField(db_column='AnalysisQty', blank=True, null=True)  # Field name made lowercase.
#     analysissrvc = models.TextField(db_column='AnalysisSrvc', blank=True, null=True)  # Field name made lowercase.
#     analysisstandardrun = models.TextField(db_column='AnalysisStandardRun', blank=True, null=True)  # Field name made lowercase.
#     analysistotal = models.TextField(db_column='AnalysisTotal', blank=True, null=True)  # Field name made lowercase.
#     analysistotalwaddl = models.TextField(db_column='AnalysisTotalwAddl', blank=True, null=True)  # Field name made lowercase.
#     analysistype = models.TextField(db_column='AnalysisType', blank=True, null=True)  # Field name made lowercase.
#     anlpvqty = models.TextField(db_column='AnlPVQty', blank=True, null=True)  # Field name made lowercase.
#     atfqty = models.TextField(db_column='ATFQty', blank=True, null=True)  # Field name made lowercase.
#     atfyn = models.TextField(db_column='ATFYN', blank=True, null=True)  # Field name made lowercase.
#     authordate = models.TextField(db_column='AuthorDate', blank=True, null=True)  # Field name made lowercase.
#     authorname = models.TextField(db_column='AuthorName', blank=True, null=True)  # Field name made lowercase.
#     authors = models.TextField(db_column='Authors', blank=True, null=True)  # Field name made lowercase.
#     billingnotestext = models.TextField(db_column='BillingNotesText', blank=True, null=True)  # Field name made lowercase.
#     cgmpchange = models.TextField(db_column='cGMPChange', blank=True, null=True)  # Field name made lowercase.
#     cgmpenterprc = models.TextField(db_column='cGMPEnterPrc', blank=True, null=True)  # Field name made lowercase.
#     comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
#     companyname = models.TextField(db_column='CompanyName', blank=True, null=True)  # Field name made lowercase.
#     created = models.TextField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
#     customdesc = models.TextField(db_column='CustomDesc', blank=True, null=True)  # Field name made lowercase.
#     custommsdesc = models.TextField(db_column='CustomMSDesc', blank=True, null=True)  # Field name made lowercase.
#     customunitname = models.TextField(db_column='CustomUnitName', blank=True, null=True)  # Field name made lowercase.
#     customunitqty = models.TextField(db_column='CustomUnitQty', blank=True, null=True)  # Field name made lowercase.
#     datedue = models.TextField(db_column='DateDue', blank=True, null=True)  # Field name made lowercase.
#     datereceived = models.TextField(db_column='DateReceived', blank=True, null=True)  # Field name made lowercase.
#     deaqty = models.TextField(db_column='DEAQty', blank=True, null=True)  # Field name made lowercase.
#     deayn = models.TextField(db_column='DEAYN', blank=True, null=True)  # Field name made lowercase.
#     disctype = models.TextField(db_column='DiscType', blank=True, null=True)  # Field name made lowercase.
#     docid = models.TextField(db_column='DocID', blank=True, null=True)  # Field name made lowercase.
#     editauthors = models.TextField(db_column='EditAuthors', blank=True, null=True)  # Field name made lowercase.
#     editdates = models.TextField(db_column='EditDates', blank=True, null=True)  # Field name made lowercase.
#     editdatename = models.TextField(db_column='EditDateName', blank=True, null=True)  # Field name made lowercase.
#     editprojstatus = models.TextField(db_column='EditProjStatus', blank=True, null=True)  # Field name made lowercase.
#     embeddedobjects = models.TextField(db_column='EmbeddedObjects', blank=True, null=True)  # Field name made lowercase.
#     enterdatedue = models.TextField(db_column='EnterDateDue', blank=True, null=True)  # Field name made lowercase.
#     familyid = models.TextField(db_column='FamilyID', blank=True, null=True)  # Field name made lowercase.
#     familyid_1 = models.TextField(db_column='FamilyID_1', blank=True, null=True)  # Field name made lowercase.
#     familyname = models.TextField(db_column='FamilyName', blank=True, null=True)  # Field name made lowercase.
#     familyname_1 = models.TextField(db_column='FamilyName_1', blank=True, null=True)  # Field name made lowercase.
#     finalize = models.TextField(db_column='Finalize', blank=True, null=True)  # Field name made lowercase.
#     finalizeddate = models.TextField(db_column='FinalizedDate', blank=True, null=True)  # Field name made lowercase.
#     hasatfsamples = models.TextField(db_column='HasATFSamples', blank=True, null=True)  # Field name made lowercase.
#     hasdeasamples = models.TextField(db_column='HasDEASamples', blank=True, null=True)  # Field name made lowercase.
#     hiddenservices_quotes = models.TextField(db_column='HiddenServices_Quotes', blank=True, null=True)  # Field name made lowercase.
#     inprojecttask = models.TextField(db_column='InProjectTask', blank=True, null=True)  # Field name made lowercase.
#     invfamilyid = models.TextField(db_column='InvFamilyID', blank=True, null=True)  # Field name made lowercase.
#     invfamilyname = models.TextField(db_column='InvFamilyName', blank=True, null=True)  # Field name made lowercase.
#     ishighatf = models.TextField(db_column='IsHighATF', blank=True, null=True)  # Field name made lowercase.
#     ishighdea = models.TextField(db_column='IsHighDEA', blank=True, null=True)  # Field name made lowercase.
#     iso = models.TextField(db_column='ISO', blank=True, null=True)  # Field name made lowercase.
#     isoenterprc = models.TextField(db_column='ISOEnterPrc', blank=True, null=True)  # Field name made lowercase.
#     lastaccessed = models.TextField(db_column='LastAccessed', blank=True, null=True)  # Field name made lowercase.
#     lastmodified = models.TextField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.
#     linedescription = models.TextField(db_column='lineDescription', blank=True, null=True)  # Field name made lowercase.
#     lineitems = models.TextField(db_column='LineItems', blank=True, null=True)  # Field name made lowercase.
#     locationid = models.TextField(db_column='LocationID', blank=True, null=True)  # Field name made lowercase.
#     methodservices = models.TextField(db_column='MethodServices', blank=True, null=True)  # Field name made lowercase.
#     noteid = models.TextField(db_column='NoteID', blank=True, null=True)  # Field name made lowercase.
#     note1_desc = models.TextField(db_column='Note1_Desc', blank=True, null=True)  # Field name made lowercase.
#     note1_name = models.TextField(db_column='Note1_Name', blank=True, null=True)  # Field name made lowercase.
#     note2_desc = models.TextField(db_column='Note2_Desc', blank=True, null=True)  # Field name made lowercase.
#     note2_name = models.TextField(db_column='Note2_Name', blank=True, null=True)  # Field name made lowercase.
#     note3_desc = models.TextField(db_column='Note3_Desc', blank=True, null=True)  # Field name made lowercase.
#     note3_name = models.TextField(db_column='Note3_Name', blank=True, null=True)  # Field name made lowercase.
#     note4_desc = models.TextField(db_column='Note4_Desc', blank=True, null=True)  # Field name made lowercase.
#     note4_name = models.TextField(db_column='Note4_Name', blank=True, null=True)  # Field name made lowercase.
#     note5_desc = models.TextField(db_column='Note5_Desc', blank=True, null=True)  # Field name made lowercase.
#     note5_name = models.TextField(db_column='Note5_Name', blank=True, null=True)  # Field name made lowercase.
#     note6_desc = models.TextField(db_column='Note6_Desc', blank=True, null=True)  # Field name made lowercase.
#     note6_name = models.TextField(db_column='Note6_Name', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_1 = models.TextField(db_column='Notes_Text_Loc_1', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_2 = models.TextField(db_column='Notes_Text_Loc_2', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_3 = models.TextField(db_column='Notes_Text_Loc_3', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_4 = models.TextField(db_column='Notes_Text_Loc_4', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_5 = models.TextField(db_column='Notes_Text_Loc_5', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_6 = models.TextField(db_column='Notes_Text_Loc_6', blank=True, null=True)  # Field name made lowercase.
#     notes_text_org_archive = models.TextField(db_column='Notes_Text_Org_Archive', blank=True, null=True)  # Field name made lowercase.
#     notes_text_org_historical = models.TextField(db_column='Notes_Text_Org_Historical', blank=True, null=True)  # Field name made lowercase.
#     overridecgmp = models.TextField(db_column='OverridecGMP', blank=True, null=True)  # Field name made lowercase.
#     overrideiso = models.TextField(db_column='OverrideISO', blank=True, null=True)  # Field name made lowercase.
#     overrideprc = models.TextField(db_column='OverridePrc', blank=True, null=True)  # Field name made lowercase.
#     priceagentrun = models.TextField(db_column='PriceAgentRun', blank=True, null=True)  # Field name made lowercase.
#     projcgmp = models.TextField(db_column='ProjCGMP', blank=True, null=True)  # Field name made lowercase.
#     projid = models.CharField(db_column='ProjID', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     projiso = models.TextField(db_column='ProjISO', blank=True, null=True)  # Field name made lowercase.
#     partlyhiddenservices = models.TextField(db_column='PartlyHiddenServices', blank=True, null=True)  # Field name made lowercase.
#     partlyhiddenservices_quotes = models.TextField(db_column='PartlyHiddenServices_Quotes', blank=True, null=True)  # Field name made lowercase.
#     prefobjrepid = models.TextField(db_column='PrefObjRepID', blank=True, null=True)  # Field name made lowercase.
#     projnum_digits = models.TextField(db_column='ProjNum_Digits', blank=True, null=True)  # Field name made lowercase.
#     runqty = models.TextField(db_column='RunQty', blank=True, null=True)  # Field name made lowercase.
#     sampqty = models.TextField(db_column='SampQty', blank=True, null=True)  # Field name made lowercase.
#     subanalysistotal = models.TextField(db_column='SubAnalysisTotal', blank=True, null=True)  # Field name made lowercase.
#     totalbeforedisco = models.TextField(db_column='TotalBeforeDisco', blank=True, null=True)  # Field name made lowercase.
#     turnaroundtext = models.TextField(db_column='TurnaroundText', blank=True, null=True)  # Field name made lowercase.
#     turnaroundtextquote100 = models.TextField(db_column='TurnaroundTextQuote100', blank=True, null=True)  # Field name made lowercase.
#     turnaroundtextquote50 = models.TextField(db_column='TurnaroundTextQuote50', blank=True, null=True)  # Field name made lowercase.
#     turnaroundtextquotestd = models.TextField(db_column='TurnaroundTextQuoteStd', blank=True, null=True)  # Field name made lowercase.
#     usecustomdesc = models.TextField(db_column='UseCustomDesc', blank=True, null=True)  # Field name made lowercase.
#     usecustomunits = models.TextField(db_column='UseCustomUnits', blank=True, null=True)  # Field name made lowercase.
#     universalid = models.CharField(db_column='UniversalID', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     validateevent = models.TextField(db_column='ValidateEvent', blank=True, null=True)  # Field name made lowercase.
#     validatenow = models.TextField(db_column='ValidateNow', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         db_table = 'quoteanalysisarch'


# class Quoteanalysisn1(models.Model):
#     quotenumber = models.CharField(db_column='QuoteNumber', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     projid = models.CharField(db_column='ProjID', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     actionlog = models.TextField(db_column='ActionLog', blank=True, null=True)  # Field name made lowercase.
#     actionnotes = models.TextField(db_column='ActionNotes', blank=True, null=True)  # Field name made lowercase.
#     ampmreceived = models.CharField(db_column='AMPMReceived', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     analysisatfchrgst = models.CharField(db_column='AnalysisATFChrgSt', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     analysiscarrierused = models.CharField(db_column='AnalysisCarrierUsed', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     analysiscgmpchrg = models.CharField(db_column='AnalysiscGMPChrg', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     analysiscgmpchrgst = models.CharField(db_column='AnalysiscGMPChrgSt', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     analysisdeachrgst = models.CharField(db_column='AnalysisDEAChrgSt', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     analysisdept = models.CharField(db_column='AnalysisDept', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     analysisdisc = models.CharField(db_column='AnalysisDisc', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     analysisdiscst = models.CharField(db_column='AnalysisDiscSt', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     analysisdiscstat = models.CharField(db_column='AnalysisDiscStat', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     analysishazchrg = models.CharField(db_column='AnalysisHazChrg', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     analysishazchrgst = models.CharField(db_column='AnalysisHazChrgSt', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     analysisinstr = models.CharField(db_column='AnalysisInstr', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     analysisisochrg = models.CharField(db_column='AnalysisISOChrg', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     analysisisochrgst = models.CharField(db_column='AnalysisISOChrgSt', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     analysisnum = models.CharField(db_column='AnalysisNum', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     analysisprc = models.CharField(db_column='AnalysisPrc', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     analysisprcent = models.CharField(db_column='AnalysisPrcEnt', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     analysisprcentst = models.CharField(db_column='AnalysisPrcEntSt', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     analysisprcst = models.CharField(db_column='AnalysisPrcSt', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     analysispriochrg = models.CharField(db_column='AnalysisPrioChrg', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     analysispriority = models.CharField(db_column='AnalysisPriority', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     analysispriost = models.CharField(db_column='AnalysisPrioSt', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     analysisqty = models.CharField(db_column='AnalysisQty', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     analysissrvc = models.CharField(db_column='AnalysisSrvc', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     analysisstandardrun = models.CharField(db_column='AnalysisStandardRun', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     analysistotal = models.CharField(db_column='AnalysisTotal', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     analysistotalwaddl = models.CharField(db_column='AnalysisTotalwAddl', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     analysistype = models.CharField(db_column='AnalysisType', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     anlpvqty = models.CharField(db_column='AnlPVQty', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     atfqty = models.CharField(db_column='ATFQty', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     atfyn = models.CharField(db_column='ATFYN', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     authordate = models.CharField(db_column='AuthorDate', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     authorname = models.CharField(db_column='AuthorName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     billingnotestext = models.TextField(db_column='BillingNotesText', blank=True, null=True)  # Field name made lowercase.
#     cgmpchange = models.CharField(db_column='cGMPChange', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     cgmpenterprc = models.CharField(db_column='cGMPEnterPrc', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
#     companyname = models.CharField(db_column='CompanyName', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     customdesc = models.TextField(db_column='CustomDesc', blank=True, null=True)  # Field name made lowercase.
#     custommsdesc = models.TextField(db_column='CustomMSDesc', blank=True, null=True)  # Field name made lowercase.
#     customunitname = models.CharField(db_column='CustomUnitName', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     customunitqty = models.CharField(db_column='CustomUnitQty', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     datedue = models.CharField(db_column='DateDue', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     datereceived = models.CharField(db_column='DateReceived', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     deaqty = models.CharField(db_column='DEAQty', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     deayn = models.CharField(db_column='DEAYN', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     disctype = models.CharField(db_column='DiscType', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     docid = models.CharField(db_column='DocID', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     enterdatedue = models.CharField(db_column='EnterDateDue', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     familyid = models.CharField(db_column='FamilyID', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     familyid_1 = models.CharField(db_column='FamilyID_1', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     familyname = models.CharField(db_column='FamilyName', max_length=125, blank=True, null=True)  # Field name made lowercase.
#     familyname_1 = models.CharField(db_column='FamilyName_1', max_length=125, blank=True, null=True)  # Field name made lowercase.
#     finalize = models.CharField(db_column='Finalize', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     finalizeddate = models.CharField(db_column='FinalizedDate', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     hasatfsamples = models.CharField(db_column='HasATFSamples', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     hasdeasamples = models.CharField(db_column='HasDEASamples', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     hiddenservices_quotes = models.CharField(db_column='HiddenServices_Quotes', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     inprojecttask = models.CharField(db_column='InProjectTask', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     invfamilyid = models.CharField(db_column='InvFamilyID', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     invfamilyname = models.CharField(db_column='InvFamilyName', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     ishighatf = models.CharField(db_column='IsHighATF', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     ishighdea = models.CharField(db_column='IsHighDEA', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     iso = models.CharField(db_column='ISO', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     isoenterprc = models.CharField(db_column='ISOEnterPrc', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     linedescription = models.TextField(db_column='lineDescription', blank=True, null=True)  # Field name made lowercase.
#     lineitems = models.CharField(db_column='LineItems', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     locationid = models.CharField(db_column='LocationID', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     methodservices = models.CharField(db_column='MethodServices', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     noteid = models.CharField(db_column='NoteID', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     overridecgmp = models.CharField(db_column='OverridecGMP', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     overrideiso = models.CharField(db_column='OverrideISO', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     overrideprc = models.CharField(db_column='OverridePrc', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     projcgmp = models.CharField(db_column='ProjCGMP', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     projiso = models.CharField(db_column='ProjISO', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     partlyhiddenservices = models.CharField(db_column='PartlyHiddenServices', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     partlyhiddenservices_quotes = models.CharField(db_column='PartlyHiddenServices_Quotes', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     prefobjrepid = models.CharField(db_column='PrefObjRepID', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     projnum_digits = models.CharField(db_column='ProjNum_Digits', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     runqty = models.CharField(db_column='RunQty', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     sampqty = models.CharField(db_column='SampQty', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     subanalysistotal = models.CharField(db_column='SubAnalysisTotal', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     totalbeforedisco = models.CharField(db_column='TotalBeforeDisco', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     turnaroundtext = models.CharField(db_column='TurnaroundText', max_length=125, blank=True, null=True)  # Field name made lowercase.
#     turnaroundtextquote100 = models.CharField(db_column='TurnaroundTextQuote100', max_length=125, blank=True, null=True)  # Field name made lowercase.
#     turnaroundtextquote50 = models.TextField(db_column='TurnaroundTextQuote50', blank=True, null=True)  # Field name made lowercase.
#     turnaroundtextquotestd = models.TextField(db_column='TurnaroundTextQuoteStd', blank=True, null=True)  # Field name made lowercase.
#     usecustomdesc = models.TextField(db_column='UseCustomDesc', blank=True, null=True)  # Field name made lowercase.
#     usecustomunits = models.CharField(db_column='UseCustomUnits', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     universalid = models.CharField(db_column='UniversalID', max_length=35, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         db_table = 'quoteanalysisn1'


# class Quotebuilder(models.Model):
#     quotebuildernumber = models.CharField(db_column='QuoteBuilderNumber', primary_key=True, max_length=75)  # Field name made lowercase.
#     actionlog = models.TextField(db_column='ActionLog', blank=True, null=True)  # Field name made lowercase.
#     actionnotes = models.TextField(db_column='ActionNotes', blank=True, null=True)  # Field name made lowercase.
#     addltextselect = models.TextField(db_column='AddlTextSelect', blank=True, null=True)  # Field name made lowercase.
#     address1 = models.TextField(db_column='Address1', blank=True, null=True)  # Field name made lowercase.
#     address2 = models.TextField(db_column='Address2', blank=True, null=True)  # Field name made lowercase.
#     affiliates1 = models.TextField(db_column='Affiliates1', blank=True, null=True)  # Field name made lowercase.
#     affiliates2 = models.TextField(db_column='Affiliates2', blank=True, null=True)  # Field name made lowercase.
#     affiliatessummaryinfo1 = models.TextField(db_column='AffiliatesSummaryInfo1', blank=True, null=True)  # Field name made lowercase.
#     affiliatessummaryinfo2 = models.TextField(db_column='AffiliatesSummaryInfo2', blank=True, null=True)  # Field name made lowercase.
#     alldeaqty = models.TextField(db_column='AllDEAQty', blank=True, null=True)  # Field name made lowercase.
#     alldeaschedule = models.TextField(db_column='AllDEASchedule', blank=True, null=True)  # Field name made lowercase.
#     alldeayn = models.TextField(db_column='AllDEAYN', blank=True, null=True)  # Field name made lowercase.
#     ampmreceived = models.TextField(db_column='AMPMReceived', blank=True, null=True)  # Field name made lowercase.
#     analysisqty = models.TextField(db_column='AnalysisQty', blank=True, null=True)  # Field name made lowercase.
#     analysistypes = models.TextField(db_column='AnalysisTypes', blank=True, null=True)  # Field name made lowercase.
#     assocproj = models.TextField(db_column='AssocProj', blank=True, null=True)  # Field name made lowercase.
#     assocproj1 = models.TextField(db_column='AssocProj1', blank=True, null=True)  # Field name made lowercase.
#     atfsampleqty = models.TextField(db_column='ATFSampleQty', blank=True, null=True)  # Field name made lowercase.
#     authordate = models.TextField(db_column='AuthorDate', blank=True, null=True)  # Field name made lowercase.
#     authorname = models.TextField(db_column='AuthorName', blank=True, null=True)  # Field name made lowercase.
#     authors = models.TextField(db_column='Authors', blank=True, null=True)  # Field name made lowercase.
#     blocktextchoices = models.TextField(db_column='BlockTextChoices', blank=True, null=True)  # Field name made lowercase.
#     city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.
#     comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.
#     companyname = models.TextField(db_column='CompanyName', blank=True, null=True)  # Field name made lowercase.
#     completepayterms = models.TextField(db_column='CompletePayTerms', blank=True, null=True)  # Field name made lowercase.
#     contactname = models.TextField(db_column='ContactName', blank=True, null=True)  # Field name made lowercase.
#     contactnumber = models.TextField(db_column='ContactNumber', blank=True, null=True)  # Field name made lowercase.
#     country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase.
#     created = models.TextField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
#     customcharge = models.TextField(db_column='CustomCharge', blank=True, null=True)  # Field name made lowercase.
#     customdescription = models.TextField(db_column='CustomDescription', blank=True, null=True)  # Field name made lowercase.
#     customreturncharge = models.TextField(db_column='CustomReturnCharge', blank=True, null=True)  # Field name made lowercase.
#     datedue = models.TextField(db_column='DateDue', blank=True, null=True)  # Field name made lowercase.
#     datereceived = models.TextField(db_column='DateReceived', blank=True, null=True)  # Field name made lowercase.
#     discountnotes = models.TextField(db_column='DiscountNotes', blank=True, null=True)  # Field name made lowercase.
#     editauthors = models.TextField(db_column='EditAuthors', blank=True, null=True)  # Field name made lowercase.
#     editdates = models.TextField(db_column='EditDates', blank=True, null=True)  # Field name made lowercase.
#     editdatename = models.TextField(db_column='EditDateName', blank=True, null=True)  # Field name made lowercase.
#     edited = models.TextField(db_column='Edited', blank=True, null=True)  # Field name made lowercase.
#     editprojstatus = models.TextField(db_column='EditProjStatus', blank=True, null=True)  # Field name made lowercase.
#     email = models.TextField(db_column='EMail', blank=True, null=True)  # Field name made lowercase.
#     embeddedobjects = models.TextField(db_column='EmbeddedObjects', blank=True, null=True)  # Field name made lowercase.
#     enterdatedue = models.TextField(db_column='EnterDateDue', blank=True, null=True)  # Field name made lowercase.
#     enterquotenumber = models.TextField(db_column='EnterQuoteNumber', blank=True, null=True)  # Field name made lowercase.
#     excelquotefilepath = models.TextField(db_column='ExcelQuoteFilePath', blank=True, null=True)  # Field name made lowercase.
#     familyid = models.CharField(db_column='FamilyID', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     familyname = models.TextField(db_column='FamilyName', blank=True, null=True)  # Field name made lowercase.
#     favorited = models.TextField(db_column='Favorited', blank=True, null=True)  # Field name made lowercase.
#     fax = models.TextField(db_column='Fax', blank=True, null=True)  # Field name made lowercase.
#     finalize = models.TextField(db_column='Finalize', blank=True, null=True)  # Field name made lowercase.
#     finalizeddate = models.TextField(db_column='FinalizedDate', blank=True, null=True)  # Field name made lowercase.
#     finalpayterms = models.TextField(db_column='FinalPayTerms', blank=True, null=True)  # Field name made lowercase.
#     hazsampleqty = models.TextField(db_column='HazSampleQty', blank=True, null=True)  # Field name made lowercase.
#     hiddenservices = models.TextField(db_column='HiddenServices', blank=True, null=True)  # Field name made lowercase.
#     hiddenservices_quotes = models.TextField(db_column='HiddenServices_Quotes', blank=True, null=True)  # Field name made lowercase.
#     inactive = models.TextField(db_column='Inactive', blank=True, null=True)  # Field name made lowercase.
#     inhousequote = models.TextField(db_column='InhouseQuote', blank=True, null=True)  # Field name made lowercase.
#     invaddress1 = models.TextField(db_column='InvAddress1', blank=True, null=True)  # Field name made lowercase.
#     invaddress2 = models.TextField(db_column='InvAddress2', blank=True, null=True)  # Field name made lowercase.
#     invcity = models.TextField(db_column='InvCity', blank=True, null=True)  # Field name made lowercase.
#     invcompanyname = models.TextField(db_column='InvCompanyName', blank=True, null=True)  # Field name made lowercase.
#     invcontactname = models.TextField(db_column='InvContactName', blank=True, null=True)  # Field name made lowercase.
#     invcountry = models.TextField(db_column='InvCountry', blank=True, null=True)  # Field name made lowercase.
#     invemail = models.TextField(db_column='InvEMail', blank=True, null=True)  # Field name made lowercase.
#     invfamilyid = models.TextField(db_column='InvFamilyID', blank=True, null=True)  # Field name made lowercase.
#     invfamilyname = models.TextField(db_column='InvFamilyName', blank=True, null=True)  # Field name made lowercase.
#     invfax = models.TextField(db_column='InvFax', blank=True, null=True)  # Field name made lowercase.
#     invlocationid = models.TextField(db_column='InvLocationID', blank=True, null=True)  # Field name made lowercase.
#     invpersonid = models.TextField(db_column='InvPersonID', blank=True, null=True)  # Field name made lowercase.
#     invphone = models.TextField(db_column='InvPhone', blank=True, null=True)  # Field name made lowercase.
#     invstate = models.TextField(db_column='InvState', blank=True, null=True)  # Field name made lowercase.
#     invzip = models.TextField(db_column='InvZip', blank=True, null=True)  # Field name made lowercase.
#     iso = models.TextField(db_column='ISO', blank=True, null=True)  # Field name made lowercase.
#     lastaccessed = models.TextField(db_column='LastAccessed', blank=True, null=True)  # Field name made lowercase.
#     lastmodified = models.TextField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.
#     locationid = models.TextField(db_column='LocationID', blank=True, null=True)  # Field name made lowercase.
#     methodservices = models.TextField(db_column='MethodServices', blank=True, null=True)  # Field name made lowercase.
#     methodservicetype = models.TextField(db_column='MethodServiceType', blank=True, null=True)  # Field name made lowercase.
#     note1_desc = models.TextField(db_column='Note1_Desc', blank=True, null=True)  # Field name made lowercase.
#     note1_name = models.TextField(db_column='Note1_Name', blank=True, null=True)  # Field name made lowercase.
#     note2_desc = models.TextField(db_column='Note2_Desc', blank=True, null=True)  # Field name made lowercase.
#     note2_name = models.TextField(db_column='Note2_Name', blank=True, null=True)  # Field name made lowercase.
#     note3_desc = models.TextField(db_column='Note3_Desc', blank=True, null=True)  # Field name made lowercase.
#     note3_name = models.TextField(db_column='Note3_Name', blank=True, null=True)  # Field name made lowercase.
#     note4_desc = models.TextField(db_column='Note4_Desc', blank=True, null=True)  # Field name made lowercase.
#     note4_name = models.TextField(db_column='Note4_Name', blank=True, null=True)  # Field name made lowercase.
#     note5_desc = models.TextField(db_column='Note5_Desc', blank=True, null=True)  # Field name made lowercase.
#     note5_name = models.TextField(db_column='Note5_Name', blank=True, null=True)  # Field name made lowercase.
#     note6_desc = models.TextField(db_column='Note6_Desc', blank=True, null=True)  # Field name made lowercase.
#     note6_name = models.TextField(db_column='Note6_Name', blank=True, null=True)  # Field name made lowercase.
#     noteid = models.TextField(db_column='NoteID', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_archive = models.TextField(db_column='Notes_Text_Loc_Archive', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_historical = models.TextField(db_column='Notes_Text_Loc_Historical', blank=True, null=True)  # Field name made lowercase.
#     paymentterms = models.TextField(db_column='PaymentTerms', blank=True, null=True)  # Field name made lowercase.
#     personid = models.CharField(db_column='PersonID', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     prepayterms = models.TextField(db_column='PrepayTerms', blank=True, null=True)  # Field name made lowercase.
#     pricequotenotes = models.TextField(db_column='PriceQuoteNotes', blank=True, null=True)  # Field name made lowercase.
#     projcgmp = models.TextField(db_column='ProjCGMP', blank=True, null=True)  # Field name made lowercase.
#     projid = models.CharField(db_column='ProjID', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     projiso = models.TextField(db_column='ProjISO', blank=True, null=True)  # Field name made lowercase.
#     projpriority = models.TextField(db_column='ProjPriority', blank=True, null=True)  # Field name made lowercase.
#     protocolperson = models.TextField(db_column='ProtocolPerson', blank=True, null=True)  # Field name made lowercase.
#     partlyhiddenservices = models.TextField(db_column='PartlyHiddenServices', blank=True, null=True)  # Field name made lowercase.
#     partlyhiddenservices_quotes = models.TextField(db_column='PartlyHiddenServices_Quotes', blank=True, null=True)  # Field name made lowercase.
#     prefobjrepid = models.TextField(db_column='PrefObjRepID', blank=True, null=True)  # Field name made lowercase.
#     projnum_digits = models.TextField(db_column='ProjNum_Digits', blank=True, null=True)  # Field name made lowercase.
#     quotecompanyname = models.TextField(db_column='QuoteCompanyName', blank=True, null=True)  # Field name made lowercase.
#     quotedate = models.TextField(db_column='QuoteDate', blank=True, null=True)  # Field name made lowercase.
#     returnreason = models.TextField(db_column='ReturnReason', blank=True, null=True)  # Field name made lowercase.
#     rptlocationid = models.TextField(db_column='RptLocationID', blank=True, null=True)  # Field name made lowercase.
#     rptpersonid = models.TextField(db_column='RptPersonID', blank=True, null=True)  # Field name made lowercase.
#     salesperson = models.TextField(db_column='SalesPerson', blank=True, null=True)  # Field name made lowercase.
#     sampleqty = models.TextField(db_column='SampleQty', blank=True, null=True)  # Field name made lowercase.
#     samplesatfyn = models.TextField(db_column='SamplesATFYN', blank=True, null=True)  # Field name made lowercase.
#     samplesdea = models.TextField(db_column='SamplesDEA', blank=True, null=True)  # Field name made lowercase.
#     sampleshaz = models.TextField(db_column='SamplesHaz', blank=True, null=True)  # Field name made lowercase.
#     sampleshazyn = models.TextField(db_column='SamplesHazYN', blank=True, null=True)  # Field name made lowercase.
#     sampletypes = models.TextField(db_column='SampleTypes', blank=True, null=True)  # Field name made lowercase.
#     sampreturn = models.TextField(db_column='SampReturn', blank=True, null=True)  # Field name made lowercase.
#     state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase.
#     turnaroundtext = models.TextField(db_column='TurnaroundText', blank=True, null=True)  # Field name made lowercase.
#     turnaroundtextquote = models.TextField(db_column='TURNAROUNDTEXTQUOTE', blank=True, null=True)  # Field name made lowercase.
#     turnaroundtextquote100 = models.TextField(db_column='TurnaroundTextQuote100', blank=True, null=True)  # Field name made lowercase.
#     turnaroundtextquote50 = models.TextField(db_column='TurnaroundTextQuote50', blank=True, null=True)  # Field name made lowercase.
#     turnaroundtextquotestd = models.TextField(db_column='TurnaroundTextQuoteStd', blank=True, null=True)  # Field name made lowercase.
#     universalid = models.TextField(db_column='UniversalID', blank=True, null=True)  # Field name made lowercase.
#     validatenow = models.TextField(db_column='ValidateNow', blank=True, null=True)  # Field name made lowercase.
#     zip = models.TextField(db_column='Zip', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         db_table = 'quotebuilder'


# class Quotebuilderarch(models.Model):
#     quotebuildernumber = models.CharField(db_column='QuoteBuilderNumber', primary_key=True, max_length=75)  # Field name made lowercase.
#     actionlog = models.TextField(db_column='ActionLog', blank=True, null=True)  # Field name made lowercase.
#     actionnotes = models.TextField(db_column='ActionNotes', blank=True, null=True)  # Field name made lowercase.
#     addltextselect = models.TextField(db_column='AddlTextSelect', blank=True, null=True)  # Field name made lowercase.
#     address1 = models.TextField(db_column='Address1', blank=True, null=True)  # Field name made lowercase.
#     address2 = models.TextField(db_column='Address2', blank=True, null=True)  # Field name made lowercase.
#     affiliates1 = models.TextField(db_column='Affiliates1', blank=True, null=True)  # Field name made lowercase.
#     affiliates2 = models.TextField(db_column='Affiliates2', blank=True, null=True)  # Field name made lowercase.
#     affiliatessummaryinfo1 = models.TextField(db_column='AffiliatesSummaryInfo1', blank=True, null=True)  # Field name made lowercase.
#     affiliatessummaryinfo2 = models.TextField(db_column='AffiliatesSummaryInfo2', blank=True, null=True)  # Field name made lowercase.
#     alldeaqty = models.TextField(db_column='AllDEAQty', blank=True, null=True)  # Field name made lowercase.
#     alldeaschedule = models.TextField(db_column='AllDEASchedule', blank=True, null=True)  # Field name made lowercase.
#     alldeayn = models.TextField(db_column='AllDEAYN', blank=True, null=True)  # Field name made lowercase.
#     ampmreceived = models.TextField(db_column='AMPMReceived', blank=True, null=True)  # Field name made lowercase.
#     analysisqty = models.TextField(db_column='AnalysisQty', blank=True, null=True)  # Field name made lowercase.
#     analysistypes = models.TextField(db_column='AnalysisTypes', blank=True, null=True)  # Field name made lowercase.
#     assocproj = models.TextField(db_column='AssocProj', blank=True, null=True)  # Field name made lowercase.
#     assocproj1 = models.TextField(db_column='AssocProj1', blank=True, null=True)  # Field name made lowercase.
#     atfsampleqty = models.TextField(db_column='ATFSampleQty', blank=True, null=True)  # Field name made lowercase.
#     authordate = models.TextField(db_column='AuthorDate', blank=True, null=True)  # Field name made lowercase.
#     authorname = models.TextField(db_column='AuthorName', blank=True, null=True)  # Field name made lowercase.
#     authors = models.TextField(db_column='Authors', blank=True, null=True)  # Field name made lowercase.
#     blocktextchoices = models.TextField(db_column='BlockTextChoices', blank=True, null=True)  # Field name made lowercase.
#     city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.
#     comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.
#     companyname = models.TextField(db_column='CompanyName', blank=True, null=True)  # Field name made lowercase.
#     completepayterms = models.TextField(db_column='CompletePayTerms', blank=True, null=True)  # Field name made lowercase.
#     contactname = models.TextField(db_column='ContactName', blank=True, null=True)  # Field name made lowercase.
#     contactnumber = models.TextField(db_column='ContactNumber', blank=True, null=True)  # Field name made lowercase.
#     country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase.
#     created = models.TextField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
#     customcharge = models.TextField(db_column='CustomCharge', blank=True, null=True)  # Field name made lowercase.
#     customdescription = models.TextField(db_column='CustomDescription', blank=True, null=True)  # Field name made lowercase.
#     customreturncharge = models.TextField(db_column='CustomReturnCharge', blank=True, null=True)  # Field name made lowercase.
#     datedue = models.TextField(db_column='DateDue', blank=True, null=True)  # Field name made lowercase.
#     datereceived = models.TextField(db_column='DateReceived', blank=True, null=True)  # Field name made lowercase.
#     discountnotes = models.TextField(db_column='DiscountNotes', blank=True, null=True)  # Field name made lowercase.
#     editauthors = models.TextField(db_column='EditAuthors', blank=True, null=True)  # Field name made lowercase.
#     editdates = models.TextField(db_column='EditDates', blank=True, null=True)  # Field name made lowercase.
#     editdatename = models.TextField(db_column='EditDateName', blank=True, null=True)  # Field name made lowercase.
#     edited = models.TextField(db_column='Edited', blank=True, null=True)  # Field name made lowercase.
#     editprojstatus = models.TextField(db_column='EditProjStatus', blank=True, null=True)  # Field name made lowercase.
#     email = models.TextField(db_column='EMail', blank=True, null=True)  # Field name made lowercase.
#     embeddedobjects = models.TextField(db_column='EmbeddedObjects', blank=True, null=True)  # Field name made lowercase.
#     enterdatedue = models.TextField(db_column='EnterDateDue', blank=True, null=True)  # Field name made lowercase.
#     enterquotenumber = models.TextField(db_column='EnterQuoteNumber', blank=True, null=True)  # Field name made lowercase.
#     excelquotefilepath = models.TextField(db_column='ExcelQuoteFilePath', blank=True, null=True)  # Field name made lowercase.
#     familyid = models.CharField(db_column='FamilyID', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     familyname = models.TextField(db_column='FamilyName', blank=True, null=True)  # Field name made lowercase.
#     favorited = models.TextField(db_column='Favorited', blank=True, null=True)  # Field name made lowercase.
#     fax = models.TextField(db_column='Fax', blank=True, null=True)  # Field name made lowercase.
#     finalize = models.TextField(db_column='Finalize', blank=True, null=True)  # Field name made lowercase.
#     finalizeddate = models.TextField(db_column='FinalizedDate', blank=True, null=True)  # Field name made lowercase.
#     finalpayterms = models.TextField(db_column='FinalPayTerms', blank=True, null=True)  # Field name made lowercase.
#     hazsampleqty = models.TextField(db_column='HazSampleQty', blank=True, null=True)  # Field name made lowercase.
#     hiddenservices = models.TextField(db_column='HiddenServices', blank=True, null=True)  # Field name made lowercase.
#     hiddenservices_quotes = models.TextField(db_column='HiddenServices_Quotes', blank=True, null=True)  # Field name made lowercase.
#     inactive = models.TextField(db_column='Inactive', blank=True, null=True)  # Field name made lowercase.
#     inhousequote = models.TextField(db_column='InhouseQuote', blank=True, null=True)  # Field name made lowercase.
#     invaddress1 = models.TextField(db_column='InvAddress1', blank=True, null=True)  # Field name made lowercase.
#     invaddress2 = models.TextField(db_column='InvAddress2', blank=True, null=True)  # Field name made lowercase.
#     invcity = models.TextField(db_column='InvCity', blank=True, null=True)  # Field name made lowercase.
#     invcompanyname = models.TextField(db_column='InvCompanyName', blank=True, null=True)  # Field name made lowercase.
#     invcontactname = models.TextField(db_column='InvContactName', blank=True, null=True)  # Field name made lowercase.
#     invcountry = models.TextField(db_column='InvCountry', blank=True, null=True)  # Field name made lowercase.
#     invemail = models.TextField(db_column='InvEMail', blank=True, null=True)  # Field name made lowercase.
#     invfamilyid = models.TextField(db_column='InvFamilyID', blank=True, null=True)  # Field name made lowercase.
#     invfamilyname = models.TextField(db_column='InvFamilyName', blank=True, null=True)  # Field name made lowercase.
#     invfax = models.TextField(db_column='InvFax', blank=True, null=True)  # Field name made lowercase.
#     invlocationid = models.TextField(db_column='InvLocationID', blank=True, null=True)  # Field name made lowercase.
#     invpersonid = models.TextField(db_column='InvPersonID', blank=True, null=True)  # Field name made lowercase.
#     invphone = models.TextField(db_column='InvPhone', blank=True, null=True)  # Field name made lowercase.
#     invstate = models.TextField(db_column='InvState', blank=True, null=True)  # Field name made lowercase.
#     invzip = models.TextField(db_column='InvZip', blank=True, null=True)  # Field name made lowercase.
#     iso = models.TextField(db_column='ISO', blank=True, null=True)  # Field name made lowercase.
#     lastaccessed = models.TextField(db_column='LastAccessed', blank=True, null=True)  # Field name made lowercase.
#     lastmodified = models.TextField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.
#     locationid = models.TextField(db_column='LocationID', blank=True, null=True)  # Field name made lowercase.
#     methodservices = models.TextField(db_column='MethodServices', blank=True, null=True)  # Field name made lowercase.
#     methodservicetype = models.TextField(db_column='MethodServiceType', blank=True, null=True)  # Field name made lowercase.
#     note1_desc = models.TextField(db_column='Note1_Desc', blank=True, null=True)  # Field name made lowercase.
#     note1_name = models.TextField(db_column='Note1_Name', blank=True, null=True)  # Field name made lowercase.
#     note2_desc = models.TextField(db_column='Note2_Desc', blank=True, null=True)  # Field name made lowercase.
#     note2_name = models.TextField(db_column='Note2_Name', blank=True, null=True)  # Field name made lowercase.
#     note3_desc = models.TextField(db_column='Note3_Desc', blank=True, null=True)  # Field name made lowercase.
#     note3_name = models.TextField(db_column='Note3_Name', blank=True, null=True)  # Field name made lowercase.
#     note4_desc = models.TextField(db_column='Note4_Desc', blank=True, null=True)  # Field name made lowercase.
#     note4_name = models.TextField(db_column='Note4_Name', blank=True, null=True)  # Field name made lowercase.
#     note5_desc = models.TextField(db_column='Note5_Desc', blank=True, null=True)  # Field name made lowercase.
#     note5_name = models.TextField(db_column='Note5_Name', blank=True, null=True)  # Field name made lowercase.
#     note6_desc = models.TextField(db_column='Note6_Desc', blank=True, null=True)  # Field name made lowercase.
#     note6_name = models.TextField(db_column='Note6_Name', blank=True, null=True)  # Field name made lowercase.
#     noteid = models.TextField(db_column='NoteID', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_archive = models.TextField(db_column='Notes_Text_Loc_Archive', blank=True, null=True)  # Field name made lowercase.
#     notes_text_loc_historical = models.TextField(db_column='Notes_Text_Loc_Historical', blank=True, null=True)  # Field name made lowercase.
#     paymentterms = models.TextField(db_column='PaymentTerms', blank=True, null=True)  # Field name made lowercase.
#     personid = models.CharField(db_column='PersonID', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     prepayterms = models.TextField(db_column='PrepayTerms', blank=True, null=True)  # Field name made lowercase.
#     pricequotenotes = models.TextField(db_column='PriceQuoteNotes', blank=True, null=True)  # Field name made lowercase.
#     projcgmp = models.TextField(db_column='ProjCGMP', blank=True, null=True)  # Field name made lowercase.
#     projid = models.CharField(db_column='ProjID', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     projiso = models.TextField(db_column='ProjISO', blank=True, null=True)  # Field name made lowercase.
#     projpriority = models.TextField(db_column='ProjPriority', blank=True, null=True)  # Field name made lowercase.
#     protocolperson = models.TextField(db_column='ProtocolPerson', blank=True, null=True)  # Field name made lowercase.
#     partlyhiddenservices = models.TextField(db_column='PartlyHiddenServices', blank=True, null=True)  # Field name made lowercase.
#     partlyhiddenservices_quotes = models.TextField(db_column='PartlyHiddenServices_Quotes', blank=True, null=True)  # Field name made lowercase.
#     prefobjrepid = models.TextField(db_column='PrefObjRepID', blank=True, null=True)  # Field name made lowercase.
#     projnum_digits = models.TextField(db_column='ProjNum_Digits', blank=True, null=True)  # Field name made lowercase.
#     quotecompanyname = models.TextField(db_column='QuoteCompanyName', blank=True, null=True)  # Field name made lowercase.
#     quotedate = models.TextField(db_column='QuoteDate', blank=True, null=True)  # Field name made lowercase.
#     returnreason = models.TextField(db_column='ReturnReason', blank=True, null=True)  # Field name made lowercase.
#     rptlocationid = models.TextField(db_column='RptLocationID', blank=True, null=True)  # Field name made lowercase.
#     rptpersonid = models.TextField(db_column='RptPersonID', blank=True, null=True)  # Field name made lowercase.
#     salesperson = models.TextField(db_column='SalesPerson', blank=True, null=True)  # Field name made lowercase.
#     sampleqty = models.TextField(db_column='SampleQty', blank=True, null=True)  # Field name made lowercase.
#     samplesatfyn = models.TextField(db_column='SamplesATFYN', blank=True, null=True)  # Field name made lowercase.
#     samplesdea = models.TextField(db_column='SamplesDEA', blank=True, null=True)  # Field name made lowercase.
#     sampleshaz = models.TextField(db_column='SamplesHaz', blank=True, null=True)  # Field name made lowercase.
#     sampleshazyn = models.TextField(db_column='SamplesHazYN', blank=True, null=True)  # Field name made lowercase.
#     sampletypes = models.TextField(db_column='SampleTypes', blank=True, null=True)  # Field name made lowercase.
#     sampreturn = models.TextField(db_column='SampReturn', blank=True, null=True)  # Field name made lowercase.
#     state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase.
#     turnaroundtext = models.TextField(db_column='TurnaroundText', blank=True, null=True)  # Field name made lowercase.
#     turnaroundtextquote = models.TextField(db_column='TURNAROUNDTEXTQUOTE', blank=True, null=True)  # Field name made lowercase.
#     turnaroundtextquote100 = models.TextField(db_column='TurnaroundTextQuote100', blank=True, null=True)  # Field name made lowercase.
#     turnaroundtextquote50 = models.TextField(db_column='TurnaroundTextQuote50', blank=True, null=True)  # Field name made lowercase.
#     turnaroundtextquotestd = models.TextField(db_column='TurnaroundTextQuoteStd', blank=True, null=True)  # Field name made lowercase.
#     universalid = models.TextField(db_column='UniversalID', blank=True, null=True)  # Field name made lowercase.
#     validatenow = models.TextField(db_column='ValidateNow', blank=True, null=True)  # Field name made lowercase.
#     zip = models.TextField(db_column='Zip', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         db_table = 'quotebuilderarch'


# class Quotebuildern1(models.Model):
#     quotebuildernumber = models.CharField(db_column='QuoteBuilderNumber', primary_key=True, max_length=15)  # Field name made lowercase.
#     actionlog = models.TextField(db_column='ActionLog', blank=True, null=True)  # Field name made lowercase.
#     addltextselect = models.TextField(db_column='AddlTextSelect', blank=True, null=True)  # Field name made lowercase.
#     address1 = models.CharField(db_column='Address1', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     address2 = models.CharField(db_column='Address2', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     alldeaqty = models.CharField(db_column='AllDEAQty', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     alldeaschedule = models.CharField(db_column='AllDEASchedule', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     alldeayn = models.CharField(db_column='AllDEAYN', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     ampmreceived = models.CharField(db_column='AMPMReceived', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     analysisqty = models.CharField(db_column='AnalysisQty', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     analysistypes = models.CharField(db_column='AnalysisTypes', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     assocproj = models.CharField(db_column='AssocProj', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     assocproj1 = models.CharField(db_column='AssocProj1', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     atfsampleqty = models.CharField(db_column='ATFSampleQty', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     authordate = models.CharField(db_column='AuthorDate', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     authorname = models.CharField(db_column='AuthorName', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     city = models.CharField(db_column='City', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.
#     companyname = models.CharField(db_column='CompanyName', max_length=105, blank=True, null=True)  # Field name made lowercase.
#     completepayterms = models.TextField(db_column='CompletePayTerms', blank=True, null=True)  # Field name made lowercase.
#     contactname = models.CharField(db_column='ContactName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     contactnumber = models.CharField(db_column='ContactNumber', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     country = models.CharField(db_column='Country', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     customcharge = models.CharField(db_column='CustomCharge', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     customdescription = models.TextField(db_column='CustomDescription', blank=True, null=True)  # Field name made lowercase.
#     customreturncharge = models.CharField(db_column='CustomReturnCharge', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     datedue = models.CharField(db_column='DateDue', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     datereceived = models.CharField(db_column='DateReceived', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     discountnotes = models.TextField(db_column='DiscountNotes', blank=True, null=True)  # Field name made lowercase.
#     email = models.CharField(db_column='EMail', max_length=105, blank=True, null=True)  # Field name made lowercase.
#     enterdatedue = models.CharField(db_column='EnterDateDue', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     excelquotefilepath = models.TextField(db_column='ExcelQuoteFilePath', blank=True, null=True)  # Field name made lowercase.
#     familyid = models.CharField(db_column='FamilyID', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     familyname = models.CharField(db_column='FamilyName', max_length=135, blank=True, null=True)  # Field name made lowercase.
#     fax = models.CharField(db_column='Fax', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     finalizeddate = models.CharField(db_column='FinalizedDate', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     finalpayterms = models.CharField(db_column='FinalPayTerms', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     hazsampleqty = models.CharField(db_column='HazSampleQty', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     inactive = models.CharField(db_column='Inactive', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     inhousequote = models.CharField(db_column='InhouseQuote', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     invaddress1 = models.CharField(db_column='InvAddress1', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     invaddress2 = models.CharField(db_column='InvAddress2', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     invcity = models.CharField(db_column='InvCity', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     invcompanyname = models.CharField(db_column='InvCompanyName', max_length=105, blank=True, null=True)  # Field name made lowercase.
#     invcontactname = models.CharField(db_column='InvContactName', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     invcountry = models.CharField(db_column='InvCountry', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     invemail = models.CharField(db_column='InvEMail', max_length=55, blank=True, null=True)  # Field name made lowercase.
#     invfamilyid = models.CharField(db_column='InvFamilyID', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     invfamilyname = models.CharField(db_column='InvFamilyName', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     invfax = models.CharField(db_column='InvFax', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     invlocationid = models.CharField(db_column='InvLocationID', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     invpersonid = models.CharField(db_column='InvPersonID', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     invphone = models.CharField(db_column='InvPhone', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     invstate = models.CharField(db_column='InvState', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     invzip = models.CharField(db_column='InvZip', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     iso = models.CharField(db_column='ISO', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     locationid = models.CharField(db_column='LocationID', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     methodservices = models.CharField(db_column='MethodServices', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     methodservicetype = models.CharField(db_column='MethodServiceType', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     noteid = models.CharField(db_column='NoteID', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     paymentterms = models.CharField(db_column='PaymentTerms', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     personid = models.CharField(db_column='PersonID', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     prepayterms = models.CharField(db_column='PrepayTerms', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     pricequotenotes = models.TextField(db_column='PriceQuoteNotes', blank=True, null=True)  # Field name made lowercase.
#     projcgmp = models.CharField(db_column='ProjCGMP', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     projid = models.CharField(db_column='ProjID', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     projiso = models.CharField(db_column='ProjISO', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     projpriority = models.CharField(db_column='ProjPriority', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     protocolperson = models.CharField(db_column='ProtocolPerson', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     quotecompanyname = models.CharField(db_column='QuoteCompanyName', max_length=105, blank=True, null=True)  # Field name made lowercase.
#     quotedate = models.CharField(db_column='QuoteDate', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     returnreason = models.CharField(db_column='ReturnReason', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     rptlocationid = models.CharField(db_column='RptLocationID', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     rptpersonid = models.CharField(db_column='RptPersonID', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     salesperson = models.CharField(db_column='SalesPerson', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     sampleqty = models.CharField(db_column='SampleQty', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     samplesatfyn = models.CharField(db_column='SamplesATFYN', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     samplesdea = models.CharField(db_column='SamplesDEA', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     sampleshaz = models.CharField(db_column='SamplesHaz', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     sampleshazyn = models.CharField(db_column='SamplesHazYN', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     sampletypes = models.CharField(db_column='SampleTypes', max_length=105, blank=True, null=True)  # Field name made lowercase.
#     sampreturn = models.CharField(db_column='SampReturn', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     state = models.CharField(db_column='State', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     universalid = models.CharField(db_column='UniversalID', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     zip = models.CharField(db_column='Zip', max_length=35, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         db_table = 'quotebuildern1'


# class Quoteinvoice(models.Model):
#     alldeaqty = models.IntegerField(db_column='AllDEAQty', blank=True, null=True)  # Field name made lowercase.
#     analysiscomments = models.CharField(db_column='AnalysisComments', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     analysisqty = models.IntegerField(db_column='AnalysisQty', blank=True, null=True)  # Field name made lowercase.
#     analysistypes = models.CharField(db_column='AnalysisTypes', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     atfsampleqty = models.IntegerField(db_column='ATFSampleQty', blank=True, null=True)  # Field name made lowercase.
#     authordate = models.CharField(db_column='AuthorDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     authorname = models.CharField(db_column='AuthorName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     authors = models.CharField(db_column='Authors', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     billedyn = models.CharField(db_column='BilledYN', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     billingnotes = models.CharField(db_column='BillingNotes', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     comments = models.CharField(db_column='Comments', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     contactnumber = models.CharField(db_column='ContactNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     created = models.DateTimeField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
#     datedue = models.DateTimeField(db_column='DateDue', blank=True, null=True)  # Field name made lowercase.
#     discountnotes = models.CharField(db_column='DiscountNotes', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     docid = models.CharField(db_column='DocID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editauthors = models.CharField(db_column='EditAuthors', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdates = models.DateTimeField(db_column='EditDates', blank=True, null=True)  # Field name made lowercase.
#     email = models.CharField(db_column='EMail', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     embeddedobjects = models.TextField(db_column='EmbeddedObjects', blank=True, null=True)  # Field name made lowercase.
#     familyid = models.CharField(db_column='FamilyID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     familyname = models.CharField(db_column='FamilyName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     fax = models.CharField(db_column='Fax', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     finalize = models.CharField(db_column='Finalize', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     finalizeddate = models.DateTimeField(db_column='FinalizedDate', blank=True, null=True)  # Field name made lowercase.
#     form = models.CharField(db_column='Form', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     hazsampleqty = models.IntegerField(db_column='HazSampleQty', blank=True, null=True)  # Field name made lowercase.
#     invamt = models.IntegerField(db_column='InvAmt', blank=True, null=True)  # Field name made lowercase.
#     invdate = models.DateTimeField(db_column='InvDate', blank=True, null=True)  # Field name made lowercase.
#     invdesc = models.CharField(db_column='InvDesc', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     invdisc = models.CharField(db_column='InvDisc', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     invfamilyid = models.CharField(db_column='InvFamilyID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     invfamilyname = models.CharField(db_column='InvFamilyName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     invlocationid = models.CharField(db_column='InvLocationID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     invoicenum = models.CharField(db_column='InvoiceNum', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     invpersonid = models.CharField(db_column='InvPersonID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     invqty = models.IntegerField(db_column='InvQty', blank=True, null=True)  # Field name made lowercase.
#     invrate = models.CharField(db_column='InvRate', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     invtotal = models.CharField(db_column='InvTotal', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     lastaccessed = models.DateTimeField(db_column='LastAccessed', blank=True, null=True)  # Field name made lowercase.
#     lastmodified = models.DateTimeField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.
#     locationid = models.CharField(db_column='LocationID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     noteid = models.CharField(db_column='NoteID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     personid = models.CharField(db_column='PersonID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     pricequotenotes = models.CharField(db_column='PriceQuoteNotes', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     projectcomments = models.CharField(db_column='ProjectComments', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     projid = models.CharField(db_column='ProjID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     quoteanalysispriority = models.CharField(db_column='QuoteAnalysisPriority', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     quoteanlruns = models.CharField(db_column='QuoteAnlRuns', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     quoteanlsamps = models.CharField(db_column='QuoteAnlSamps', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     quotecompanyname = models.CharField(db_column='QuoteCompanyName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     quoteinvoicenumber = models.CharField(db_column='QuoteInvoiceNumber', primary_key=True, max_length=50)  # Field name made lowercase.
#     rptlocationid = models.CharField(db_column='RptLocationID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     rptpersonid = models.CharField(db_column='RptPersonID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     sampcount = models.CharField(db_column='SampCount', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     sampletypes = models.CharField(db_column='SampleTypes', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     universalid = models.CharField(db_column='UniversalID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     affiliates1 = models.CharField(db_column='Affiliates1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     affiliates2 = models.CharField(db_column='Affiliates2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     affiliatessummaryinfo1 = models.CharField(db_column='AffiliatesSummaryInfo1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     affiliatessummaryinfo2 = models.CharField(db_column='AffiliatesSummaryInfo2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appactivity = models.CharField(db_column='AppActivity', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appanalytics = models.CharField(db_column='AppAnalytics', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appbidproc = models.CharField(db_column='AppBidProc', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appcontact = models.CharField(db_column='AppContact', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appdeareg = models.CharField(db_column='AppDEAReg', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appdir = models.CharField(db_column='AppDir', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appdir2 = models.CharField(db_column='AppDir2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appprojectwkfl = models.CharField(db_column='AppProjectWkfl', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appsaleopp = models.CharField(db_column='AppSaleOpp', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appsalesmkt = models.CharField(db_column='AppSalesMkt', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appserver = models.CharField(db_column='AppServer', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appservices = models.CharField(db_column='AppServices', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appsyspref = models.CharField(db_column='AppSysPref', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     apptestmethods = models.CharField(db_column='AppTestMethods', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appthisdb = models.CharField(db_column='AppThisDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     colorcoding = models.CharField(db_column='ColorCoding', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdatename = models.CharField(db_column='EditDateName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     edited = models.CharField(db_column='Edited', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     formulachecker = models.CharField(db_column='FormulaChecker', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     hiddenservices = models.CharField(db_column='HiddenServices', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     hiddenservices_quotes = models.CharField(db_column='HiddenServices_Quotes', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     note1_desc = models.CharField(db_column='Note1_Desc', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     note1_name = models.CharField(db_column='Note1_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     note2_desc = models.CharField(db_column='Note2_Desc', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     note2_name = models.CharField(db_column='Note2_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     note3_desc = models.CharField(db_column='Note3_Desc', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     note3_name = models.CharField(db_column='Note3_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     note4_desc = models.CharField(db_column='Note4_Desc', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     note4_name = models.CharField(db_column='Note4_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     note5_desc = models.CharField(db_column='Note5_Desc', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     note5_name = models.CharField(db_column='Note5_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     note6_desc = models.CharField(db_column='Note6_Desc', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     note6_name = models.CharField(db_column='Note6_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     partlyhiddenservices = models.CharField(db_column='PartlyHiddenServices', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     partlyhiddenservices_quotes = models.CharField(db_column='PartlyHiddenServices_Quotes', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     prefobjrepid = models.CharField(db_column='PrefObjRepID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     projnum_digits = models.CharField(db_column='ProjNum_Digits', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     systemname = models.CharField(db_column='SystemName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     versionchangehistory = models.CharField(db_column='VersionChangeHistory', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     workflowchangehistory = models.CharField(db_column='WorkflowChangeHistory', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     workflowrevisionnumber = models.CharField(db_column='WorkflowRevisionNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     digit_count = models.CharField(db_column='DIGIT_COUNT', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editprojstatus = models.CharField(db_column='EditProjStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     locationinfo = models.CharField(db_column='LocationInfo', max_length=50, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         db_table = 'quoteinvoice'


# class Quoteinvoicearch(models.Model):
#     alldeaqty = models.IntegerField(db_column='AllDEAQty', blank=True, null=True)  # Field name made lowercase.
#     analysiscomments = models.CharField(db_column='AnalysisComments', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     analysisqty = models.IntegerField(db_column='AnalysisQty', blank=True, null=True)  # Field name made lowercase.
#     analysistypes = models.CharField(db_column='AnalysisTypes', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     atfsampleqty = models.IntegerField(db_column='ATFSampleQty', blank=True, null=True)  # Field name made lowercase.
#     authordate = models.CharField(db_column='AuthorDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     authorname = models.CharField(db_column='AuthorName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     authors = models.CharField(db_column='Authors', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     billedyn = models.CharField(db_column='BilledYN', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     billingnotes = models.CharField(db_column='BillingNotes', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     comments = models.CharField(db_column='Comments', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     contactnumber = models.CharField(db_column='ContactNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     created = models.DateTimeField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
#     datedue = models.DateTimeField(db_column='DateDue', blank=True, null=True)  # Field name made lowercase.
#     discountnotes = models.CharField(db_column='DiscountNotes', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     docid = models.CharField(db_column='DocID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editauthors = models.CharField(db_column='EditAuthors', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdates = models.DateTimeField(db_column='EditDates', blank=True, null=True)  # Field name made lowercase.
#     email = models.CharField(db_column='EMail', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     embeddedobjects = models.TextField(db_column='EmbeddedObjects', blank=True, null=True)  # Field name made lowercase.
#     familyid = models.CharField(db_column='FamilyID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     familyname = models.CharField(db_column='FamilyName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     fax = models.CharField(db_column='Fax', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     finalize = models.CharField(db_column='Finalize', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     finalizeddate = models.DateTimeField(db_column='FinalizedDate', blank=True, null=True)  # Field name made lowercase.
#     form = models.CharField(db_column='Form', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     hazsampleqty = models.IntegerField(db_column='HazSampleQty', blank=True, null=True)  # Field name made lowercase.
#     invamt = models.IntegerField(db_column='InvAmt', blank=True, null=True)  # Field name made lowercase.
#     invdate = models.DateTimeField(db_column='InvDate', blank=True, null=True)  # Field name made lowercase.
#     invdesc = models.CharField(db_column='InvDesc', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     invdisc = models.CharField(db_column='InvDisc', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     invfamilyid = models.CharField(db_column='InvFamilyID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     invfamilyname = models.CharField(db_column='InvFamilyName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     invlocationid = models.CharField(db_column='InvLocationID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     invoicenum = models.CharField(db_column='InvoiceNum', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     invpersonid = models.CharField(db_column='InvPersonID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     invqty = models.IntegerField(db_column='InvQty', blank=True, null=True)  # Field name made lowercase.
#     invrate = models.CharField(db_column='InvRate', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     invtotal = models.CharField(db_column='InvTotal', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     lastaccessed = models.DateTimeField(db_column='LastAccessed', blank=True, null=True)  # Field name made lowercase.
#     lastmodified = models.DateTimeField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.
#     locationid = models.CharField(db_column='LocationID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     noteid = models.CharField(db_column='NoteID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     personid = models.CharField(db_column='PersonID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     pricequotenotes = models.CharField(db_column='PriceQuoteNotes', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     projectcomments = models.CharField(db_column='ProjectComments', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     projid = models.CharField(db_column='ProjID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     quoteanalysispriority = models.CharField(db_column='QuoteAnalysisPriority', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     quoteanlruns = models.CharField(db_column='QuoteAnlRuns', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     quoteanlsamps = models.CharField(db_column='QuoteAnlSamps', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     quotecompanyname = models.CharField(db_column='QuoteCompanyName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     quoteinvoicenumber = models.CharField(db_column='QuoteInvoiceNumber', primary_key=True, max_length=50)  # Field name made lowercase.
#     rptlocationid = models.CharField(db_column='RptLocationID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     rptpersonid = models.CharField(db_column='RptPersonID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     sampcount = models.CharField(db_column='SampCount', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     sampletypes = models.CharField(db_column='SampleTypes', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     universalid = models.CharField(db_column='UniversalID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     affiliates1 = models.CharField(db_column='Affiliates1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     affiliates2 = models.CharField(db_column='Affiliates2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     affiliatessummaryinfo1 = models.CharField(db_column='AffiliatesSummaryInfo1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     affiliatessummaryinfo2 = models.CharField(db_column='AffiliatesSummaryInfo2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appactivity = models.CharField(db_column='AppActivity', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appanalytics = models.CharField(db_column='AppAnalytics', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appbidproc = models.CharField(db_column='AppBidProc', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appcontact = models.CharField(db_column='AppContact', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appdeareg = models.CharField(db_column='AppDEAReg', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appdir = models.CharField(db_column='AppDir', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appdir2 = models.CharField(db_column='AppDir2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appprojectwkfl = models.CharField(db_column='AppProjectWkfl', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appsaleopp = models.CharField(db_column='AppSaleOpp', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appsalesmkt = models.CharField(db_column='AppSalesMkt', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appserver = models.CharField(db_column='AppServer', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appservices = models.CharField(db_column='AppServices', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appsyspref = models.CharField(db_column='AppSysPref', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     apptestmethods = models.CharField(db_column='AppTestMethods', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appthisdb = models.CharField(db_column='AppThisDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     colorcoding = models.CharField(db_column='ColorCoding', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdatename = models.CharField(db_column='EditDateName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     edited = models.CharField(db_column='Edited', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     formulachecker = models.CharField(db_column='FormulaChecker', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     hiddenservices = models.CharField(db_column='HiddenServices', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     hiddenservices_quotes = models.CharField(db_column='HiddenServices_Quotes', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     note1_desc = models.CharField(db_column='Note1_Desc', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     note1_name = models.CharField(db_column='Note1_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     note2_desc = models.CharField(db_column='Note2_Desc', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     note2_name = models.CharField(db_column='Note2_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     note3_desc = models.CharField(db_column='Note3_Desc', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     note3_name = models.CharField(db_column='Note3_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     note4_desc = models.CharField(db_column='Note4_Desc', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     note4_name = models.CharField(db_column='Note4_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     note5_desc = models.CharField(db_column='Note5_Desc', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     note5_name = models.CharField(db_column='Note5_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     note6_desc = models.CharField(db_column='Note6_Desc', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     note6_name = models.CharField(db_column='Note6_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     partlyhiddenservices = models.CharField(db_column='PartlyHiddenServices', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     partlyhiddenservices_quotes = models.CharField(db_column='PartlyHiddenServices_Quotes', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     prefobjrepid = models.CharField(db_column='PrefObjRepID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     projnum_digits = models.CharField(db_column='ProjNum_Digits', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     systemname = models.CharField(db_column='SystemName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     versionchangehistory = models.CharField(db_column='VersionChangeHistory', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     workflowchangehistory = models.CharField(db_column='WorkflowChangeHistory', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     workflowrevisionnumber = models.CharField(db_column='WorkflowRevisionNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     digit_count = models.CharField(db_column='DIGIT_COUNT', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editprojstatus = models.CharField(db_column='EditProjStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     locationinfo = models.CharField(db_column='LocationInfo', max_length=50, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         db_table = 'quoteinvoicearch'


# class Sample(models.Model):
#     samplognum = models.CharField(db_column='SampLogNum', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     projectnumber = models.CharField(db_column='ProjectNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     projid = models.CharField(db_column='ProjID', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     actionlog = models.TextField(db_column='ActionLog', blank=True, null=True)  # Field name made lowercase.
#     actionloghdg = models.TextField(db_column='ActionLogHdg', blank=True, null=True)  # Field name made lowercase.
#     actionnotes = models.TextField(db_column='ActionNotes', blank=True, null=True)  # Field name made lowercase.
#     authordate = models.TextField(db_column='AuthorDate', blank=True, null=True)  # Field name made lowercase.
#     authorname = models.TextField(db_column='AuthorName', blank=True, null=True)  # Field name made lowercase.
#     authors = models.TextField(db_column='Authors', blank=True, null=True)  # Field name made lowercase.
#     companyname = models.TextField(db_column='CompanyName', blank=True, null=True)  # Field name made lowercase.
#     created = models.TextField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
#     dangerousgoods = models.TextField(db_column='DangerousGoods', blank=True, null=True)  # Field name made lowercase.
#     datedue = models.TextField(db_column='DateDue', blank=True, null=True)  # Field name made lowercase.
#     datereceived = models.TextField(db_column='DateReceived', blank=True, null=True)  # Field name made lowercase.
#     deaschedule = models.TextField(db_column='DEASchedule', blank=True, null=True)  # Field name made lowercase.
#     docid = models.TextField(db_column='DocID', blank=True, null=True)  # Field name made lowercase.
#     editauthors = models.TextField(db_column='EditAuthors', blank=True, null=True)  # Field name made lowercase.
#     editdatename = models.TextField(db_column='EditDateName', blank=True, null=True)  # Field name made lowercase.
#     editdates = models.TextField(db_column='EditDates', blank=True, null=True)  # Field name made lowercase.
#     edited = models.TextField(db_column='Edited', blank=True, null=True)  # Field name made lowercase.
#     editprojstatus = models.TextField(db_column='EditProjStatus', blank=True, null=True)  # Field name made lowercase.
#     embeddedobjects = models.TextField(db_column='EmbeddedObjects', blank=True, null=True)  # Field name made lowercase.
#     familyid = models.TextField(db_column='FamilyID', blank=True, null=True)  # Field name made lowercase.
#     familyname = models.TextField(db_column='FamilyName', blank=True, null=True)  # Field name made lowercase.
#     ghs00 = models.TextField(db_column='GHS00', blank=True, null=True)  # Field name made lowercase.
#     ghs01 = models.TextField(db_column='GHS01', blank=True, null=True)  # Field name made lowercase.
#     ghs02 = models.TextField(db_column='GHS02', blank=True, null=True)  # Field name made lowercase.
#     ghs03 = models.TextField(db_column='GHS03', blank=True, null=True)  # Field name made lowercase.
#     ghs04 = models.TextField(db_column='GHS04', blank=True, null=True)  # Field name made lowercase.
#     ghs05 = models.TextField(db_column='GHS05', blank=True, null=True)  # Field name made lowercase.
#     ghs06 = models.TextField(db_column='GHS06', blank=True, null=True)  # Field name made lowercase.
#     ghs07 = models.TextField(db_column='GHS07', blank=True, null=True)  # Field name made lowercase.
#     ghs08 = models.TextField(db_column='GHS08', blank=True, null=True)  # Field name made lowercase.
#     ghs09 = models.TextField(db_column='GHS09', blank=True, null=True)  # Field name made lowercase.
#     lastaccessed = models.TextField(db_column='LastAccessed', blank=True, null=True)  # Field name made lowercase.
#     lastmodified = models.TextField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.
#     lightsensitive = models.TextField(db_column='LightSensitive', blank=True, null=True)  # Field name made lowercase.
#     locationid = models.TextField(db_column='LocationID', blank=True, null=True)  # Field name made lowercase.
#     noticesent = models.TextField(db_column='NoticeSent', blank=True, null=True)  # Field name made lowercase.
#     prefobjrepid = models.TextField(db_column='PrefObjRepID', blank=True, null=True)  # Field name made lowercase.
#     projstatus = models.TextField(db_column='ProjStatus', blank=True, null=True)  # Field name made lowercase.
#     sampanlreq = models.TextField(db_column='SampAnlReq', blank=True, null=True)  # Field name made lowercase.
#     sampbsl = models.TextField(db_column='SampBSL', blank=True, null=True)  # Field name made lowercase.
#     sampclass = models.TextField(db_column='SampClass', blank=True, null=True)  # Field name made lowercase.
#     sampclassatf = models.TextField(db_column='SampClassATF', blank=True, null=True)  # Field name made lowercase.
#     sampclassdea = models.TextField(db_column='SampClassDEA', blank=True, null=True)  # Field name made lowercase.
#     samphazards = models.TextField(db_column='SampHazards', blank=True, null=True)  # Field name made lowercase.
#     samphazflame = models.TextField(db_column='SampHazFlame', blank=True, null=True)  # Field name made lowercase.
#     samphazhealth = models.TextField(db_column='SampHazHealth', blank=True, null=True)  # Field name made lowercase.
#     samphazppe = models.TextField(db_column='SampHazPPE', blank=True, null=True)  # Field name made lowercase.
#     samphazreact = models.TextField(db_column='SampHazReact', blank=True, null=True)  # Field name made lowercase.
#     sampid = models.TextField(db_column='SampID', blank=True, null=True)  # Field name made lowercase.
#     samponewordlist = models.TextField(db_column='SampOneWordList', blank=True, null=True)  # Field name made lowercase.
#     sampphraselist = models.TextField(db_column='SampPhraseList', blank=True, null=True)  # Field name made lowercase.
#     sampqty = models.TextField(db_column='SampQty', blank=True, null=True)  # Field name made lowercase.
#     sampstorg = models.TextField(db_column='SampStorg', blank=True, null=True)  # Field name made lowercase.
#     samptwowordlist = models.TextField(db_column='SampTwoWordList', blank=True, null=True)  # Field name made lowercase.
#     samptype = models.TextField(db_column='SampType', blank=True, null=True)  # Field name made lowercase.
#     signalword = models.TextField(db_column='SignalWord', blank=True, null=True)  # Field name made lowercase.
#     smplsrchwrdcnt = models.TextField(db_column='SmplSrchWrdCnt', blank=True, null=True)  # Field name made lowercase.
#     universalid = models.TextField(db_column='UniversalID', blank=True, null=True)  # Field name made lowercase.
#     unnumber = models.TextField(db_column='UNnumber', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         db_table = 'sample'


# class Samplearch(models.Model):
#     samplognum = models.CharField(db_column='SampLogNum', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     projectnumber = models.CharField(db_column='ProjectNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     projid = models.CharField(db_column='ProjID', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     actionlog = models.TextField(db_column='ActionLog', blank=True, null=True)  # Field name made lowercase.
#     actionloghdg = models.TextField(db_column='ActionLogHdg', blank=True, null=True)  # Field name made lowercase.
#     actionnotes = models.TextField(db_column='ActionNotes', blank=True, null=True)  # Field name made lowercase.
#     authordate = models.TextField(db_column='AuthorDate', blank=True, null=True)  # Field name made lowercase.
#     authorname = models.TextField(db_column='AuthorName', blank=True, null=True)  # Field name made lowercase.
#     authors = models.TextField(db_column='Authors', blank=True, null=True)  # Field name made lowercase.
#     companyname = models.TextField(db_column='CompanyName', blank=True, null=True)  # Field name made lowercase.
#     created = models.TextField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
#     dangerousgoods = models.TextField(db_column='DangerousGoods', blank=True, null=True)  # Field name made lowercase.
#     datedue = models.TextField(db_column='DateDue', blank=True, null=True)  # Field name made lowercase.
#     datereceived = models.TextField(db_column='DateReceived', blank=True, null=True)  # Field name made lowercase.
#     deaschedule = models.TextField(db_column='DEASchedule', blank=True, null=True)  # Field name made lowercase.
#     docid = models.TextField(db_column='DocID', blank=True, null=True)  # Field name made lowercase.
#     editauthors = models.TextField(db_column='EditAuthors', blank=True, null=True)  # Field name made lowercase.
#     editdatename = models.TextField(db_column='EditDateName', blank=True, null=True)  # Field name made lowercase.
#     editdates = models.TextField(db_column='EditDates', blank=True, null=True)  # Field name made lowercase.
#     edited = models.TextField(db_column='Edited', blank=True, null=True)  # Field name made lowercase.
#     editprojstatus = models.TextField(db_column='EditProjStatus', blank=True, null=True)  # Field name made lowercase.
#     embeddedobjects = models.TextField(db_column='EmbeddedObjects', blank=True, null=True)  # Field name made lowercase.
#     familyid = models.TextField(db_column='FamilyID', blank=True, null=True)  # Field name made lowercase.
#     familyname = models.TextField(db_column='FamilyName', blank=True, null=True)  # Field name made lowercase.
#     ghs00 = models.TextField(db_column='GHS00', blank=True, null=True)  # Field name made lowercase.
#     ghs01 = models.TextField(db_column='GHS01', blank=True, null=True)  # Field name made lowercase.
#     ghs02 = models.TextField(db_column='GHS02', blank=True, null=True)  # Field name made lowercase.
#     ghs03 = models.TextField(db_column='GHS03', blank=True, null=True)  # Field name made lowercase.
#     ghs04 = models.TextField(db_column='GHS04', blank=True, null=True)  # Field name made lowercase.
#     ghs05 = models.TextField(db_column='GHS05', blank=True, null=True)  # Field name made lowercase.
#     ghs06 = models.TextField(db_column='GHS06', blank=True, null=True)  # Field name made lowercase.
#     ghs07 = models.TextField(db_column='GHS07', blank=True, null=True)  # Field name made lowercase.
#     ghs08 = models.TextField(db_column='GHS08', blank=True, null=True)  # Field name made lowercase.
#     ghs09 = models.TextField(db_column='GHS09', blank=True, null=True)  # Field name made lowercase.
#     lastaccessed = models.TextField(db_column='LastAccessed', blank=True, null=True)  # Field name made lowercase.
#     lastmodified = models.TextField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.
#     lightsensitive = models.TextField(db_column='LightSensitive', blank=True, null=True)  # Field name made lowercase.
#     locationid = models.TextField(db_column='LocationID', blank=True, null=True)  # Field name made lowercase.
#     noticesent = models.TextField(db_column='NoticeSent', blank=True, null=True)  # Field name made lowercase.
#     prefobjrepid = models.TextField(db_column='PrefObjRepID', blank=True, null=True)  # Field name made lowercase.
#     projstatus = models.TextField(db_column='ProjStatus', blank=True, null=True)  # Field name made lowercase.
#     sampanlreq = models.TextField(db_column='SampAnlReq', blank=True, null=True)  # Field name made lowercase.
#     sampbsl = models.TextField(db_column='SampBSL', blank=True, null=True)  # Field name made lowercase.
#     sampclass = models.TextField(db_column='SampClass', blank=True, null=True)  # Field name made lowercase.
#     sampclassatf = models.TextField(db_column='SampClassATF', blank=True, null=True)  # Field name made lowercase.
#     sampclassdea = models.TextField(db_column='SampClassDEA', blank=True, null=True)  # Field name made lowercase.
#     samphazards = models.TextField(db_column='SampHazards', blank=True, null=True)  # Field name made lowercase.
#     samphazflame = models.TextField(db_column='SampHazFlame', blank=True, null=True)  # Field name made lowercase.
#     samphazhealth = models.TextField(db_column='SampHazHealth', blank=True, null=True)  # Field name made lowercase.
#     samphazppe = models.TextField(db_column='SampHazPPE', blank=True, null=True)  # Field name made lowercase.
#     samphazreact = models.TextField(db_column='SampHazReact', blank=True, null=True)  # Field name made lowercase.
#     sampid = models.TextField(db_column='SampID', blank=True, null=True)  # Field name made lowercase.
#     samponewordlist = models.TextField(db_column='SampOneWordList', blank=True, null=True)  # Field name made lowercase.
#     sampphraselist = models.TextField(db_column='SampPhraseList', blank=True, null=True)  # Field name made lowercase.
#     sampqty = models.TextField(db_column='SampQty', blank=True, null=True)  # Field name made lowercase.
#     sampstorg = models.TextField(db_column='SampStorg', blank=True, null=True)  # Field name made lowercase.
#     samptwowordlist = models.TextField(db_column='SampTwoWordList', blank=True, null=True)  # Field name made lowercase.
#     samptype = models.TextField(db_column='SampType', blank=True, null=True)  # Field name made lowercase.
#     signalword = models.TextField(db_column='SignalWord', blank=True, null=True)  # Field name made lowercase.
#     smplsrchwrdcnt = models.TextField(db_column='SmplSrchWrdCnt', blank=True, null=True)  # Field name made lowercase.
#     universalid = models.TextField(db_column='UniversalID', blank=True, null=True)  # Field name made lowercase.
#     unnumber = models.TextField(db_column='UNnumber', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         db_table = 'samplearch'


# class Samplen1(models.Model):
#     samplognum = models.CharField(db_column='SampLogNum', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     projectnumber = models.CharField(db_column='ProjectNumber', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     docid = models.CharField(db_column='DocID', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     familyid = models.CharField(db_column='FamilyID', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     locationid = models.CharField(db_column='LocationID', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     projid = models.CharField(db_column='ProjID', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     sampid = models.CharField(db_column='SampID', max_length=176, blank=True, null=True)  # Field name made lowercase.
#     actionlog = models.TextField(db_column='ActionLog', blank=True, null=True)  # Field name made lowercase.
#     authordate = models.CharField(db_column='AuthorDate', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     authorname = models.CharField(db_column='AuthorName', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     companyname = models.CharField(db_column='CompanyName', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     dangerousgoods = models.CharField(db_column='DangerousGoods', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     datedue = models.CharField(db_column='DateDue', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     datereceived = models.CharField(db_column='DateReceived', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     deaschedule = models.CharField(db_column='DEASchedule', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     familyname = models.CharField(db_column='FamilyName', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     ghs00 = models.CharField(db_column='GHS00', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     ghs01 = models.CharField(db_column='GHS01', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     ghs02 = models.CharField(db_column='GHS02', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     ghs03 = models.CharField(db_column='GHS03', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     ghs04 = models.CharField(db_column='GHS04', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     ghs05 = models.CharField(db_column='GHS05', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     ghs06 = models.CharField(db_column='GHS06', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     ghs07 = models.CharField(db_column='GHS07', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     ghs08 = models.CharField(db_column='GHS08', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     ghs09 = models.CharField(db_column='GHS09', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     noticesent = models.CharField(db_column='NoticeSent', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     projstatus = models.CharField(db_column='ProjStatus', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     sampanlreq = models.CharField(db_column='SampAnlReq', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     sampbsl = models.CharField(db_column='SampBSL', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     sampclass = models.CharField(db_column='SampClass', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     sampclassatf = models.CharField(db_column='SampClassATF', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     sampclassdea = models.CharField(db_column='SampClassDEA', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     samphazards = models.CharField(db_column='SampHazards', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     samphazflame = models.CharField(db_column='SampHazFlame', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     samphazhealth = models.CharField(db_column='SampHazHealth', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     samphazppe = models.CharField(db_column='SampHazPPE', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     samphazreact = models.CharField(db_column='SampHazReact', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     samponewordlist = models.CharField(db_column='SampOneWordList', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     sampphraselist = models.CharField(db_column='SampPhraseList', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     sampqty = models.CharField(db_column='SampQty', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     sampstorg = models.CharField(db_column='SampStorg', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     samptwowordlist = models.CharField(db_column='SampTwoWordList', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     samptype = models.TextField(db_column='SampType', blank=True, null=True)  # Field name made lowercase.
#     signalword = models.CharField(db_column='SignalWord', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     smplsrchwrdcnt = models.CharField(db_column='SmplSrchWrdCnt', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     universalid = models.CharField(db_column='UniversalID', max_length=35, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         db_table = 'samplen1'


# class Sampletable(models.Model):
#     analysisqty = models.IntegerField(db_column='AnalysisQty', blank=True, null=True)  # Field name made lowercase.
#     analysistypes = models.CharField(db_column='AnalysisTypes', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appsaleknow = models.CharField(db_column='AppSaleKnow', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     autoprint = models.CharField(db_column='AutoPrint', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     body = models.CharField(db_column='Body', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     companyname = models.CharField(db_column='CompanyName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     created = models.DateTimeField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
#     embeddedobjects = models.TextField(db_column='EmbeddedObjects', blank=True, null=True)  # Field name made lowercase.
#     form = models.CharField(db_column='Form', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     lastaccessed = models.DateTimeField(db_column='LastAccessed', blank=True, null=True)  # Field name made lowercase.
#     lastmodified = models.DateTimeField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.
#     noteid = models.CharField(db_column='NoteID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     projectnumber = models.CharField(db_column='ProjectNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     projid = models.CharField(db_column='ProjID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     ptlversion = models.CharField(db_column='PTLVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     sampleqty = models.IntegerField(db_column='SampleQty', blank=True, null=True)  # Field name made lowercase.
#     sampletypes = models.CharField(db_column='SampleTypes', primary_key=True, max_length=50)  # Field name made lowercase.
#     universalid = models.CharField(db_column='UniversalID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     affiliates1 = models.CharField(db_column='Affiliates1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     affiliates2 = models.CharField(db_column='Affiliates2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     affiliatessummaryinfo1 = models.CharField(db_column='AffiliatesSummaryInfo1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     affiliatessummaryinfo2 = models.CharField(db_column='AffiliatesSummaryInfo2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appactivity = models.CharField(db_column='AppActivity', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appanalytics = models.CharField(db_column='AppAnalytics', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appbidproc = models.CharField(db_column='AppBidProc', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appcontact = models.CharField(db_column='AppContact', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appdeareg = models.CharField(db_column='AppDEAReg', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appdir = models.CharField(db_column='AppDir', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appdir2 = models.CharField(db_column='AppDir2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appprojectwkfl = models.CharField(db_column='AppProjectWkfl', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appsaleopp = models.CharField(db_column='AppSaleOpp', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appsalesmkt = models.CharField(db_column='AppSalesMkt', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appserver = models.CharField(db_column='AppServer', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appservices = models.CharField(db_column='AppServices', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appsyspref = models.CharField(db_column='AppSysPref', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     apptestmethods = models.CharField(db_column='AppTestMethods', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     appthisdb = models.CharField(db_column='AppThisDB', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     authordate = models.DateTimeField(db_column='AuthorDate', blank=True, null=True)  # Field name made lowercase.
#     authorname = models.CharField(db_column='AuthorName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     colorcoding = models.CharField(db_column='ColorCoding', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     digit_count = models.CharField(db_column='DIGIT_COUNT', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editauthors = models.CharField(db_column='EditAuthors', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdatename = models.CharField(db_column='EditDateName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editdates = models.DateTimeField(db_column='EditDates', blank=True, null=True)  # Field name made lowercase.
#     edited = models.CharField(db_column='Edited', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     editprojstatus = models.CharField(db_column='EditProjStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     formulachecker = models.CharField(db_column='FormulaChecker', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     hiddenservices = models.CharField(db_column='HiddenServices', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     hiddenservices_quotes = models.CharField(db_column='HiddenServices_Quotes', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     locationinfo = models.CharField(db_column='LocationInfo', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     note1_desc = models.CharField(db_column='Note1_Desc', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     note1_name = models.CharField(db_column='Note1_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     note2_desc = models.CharField(db_column='Note2_Desc', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     note2_name = models.CharField(db_column='Note2_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     note3_desc = models.CharField(db_column='Note3_Desc', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     note3_name = models.CharField(db_column='Note3_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     note4_desc = models.CharField(db_column='Note4_Desc', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     note4_name = models.CharField(db_column='Note4_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     note5_desc = models.CharField(db_column='Note5_Desc', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     note5_name = models.CharField(db_column='Note5_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     note6_desc = models.CharField(db_column='Note6_Desc', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     note6_name = models.CharField(db_column='Note6_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     partlyhiddenservices = models.CharField(db_column='PartlyHiddenServices', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     partlyhiddenservices_quotes = models.CharField(db_column='PartlyHiddenServices_Quotes', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     prefobjrepid = models.CharField(db_column='PrefObjRepID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     projnum_digits = models.CharField(db_column='ProjNum_Digits', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     systemname = models.CharField(db_column='SystemName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     versionchangehistory = models.CharField(db_column='VersionChangeHistory', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     workflowchangehistory = models.CharField(db_column='WorkflowChangeHistory', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     workflowrevisionnumber = models.CharField(db_column='WorkflowRevisionNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         db_table = 'sampletable'


# class Service(models.Model):
#     serviceid = models.CharField(db_column='ServiceID', primary_key=True, max_length=35)  # Field name made lowercase.
#     department = models.TextField(db_column='Department', blank=True, null=True)  # Field name made lowercase.
#     technique = models.TextField(db_column='Technique', blank=True, null=True)  # Field name made lowercase.
#     instrument = models.TextField(db_column='Instrument', blank=True, null=True)  # Field name made lowercase.
#     test = models.TextField(db_column='Test', blank=True, null=True)  # Field name made lowercase.
#     serviceprice = models.TextField(db_column='ServicePrice', blank=True, null=True)  # Field name made lowercase.
#     prevprice = models.TextField(db_column='PrevPrice', blank=True, null=True)  # Field name made lowercase.
#     pricedate = models.TextField(db_column='PriceDate', blank=True, null=True)  # Field name made lowercase.
#     nameslist = models.TextField(db_column='NamesList', blank=True, null=True)  # Field name made lowercase.
#     intraining = models.TextField(db_column='InTraining', blank=True, null=True)  # Field name made lowercase.
#     servicelocation = models.TextField(db_column='ServiceLocation', blank=True, null=True)  # Field name made lowercase.
#     servicecategories = models.TextField(db_column='ServiceCategories', blank=True, null=True)  # Field name made lowercase.
#     methodservicetype = models.TextField(db_column='MethodServiceType', blank=True, null=True)  # Field name made lowercase.
#     description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
#     specialbilling = models.TextField(db_column='SpecialBilling', blank=True, null=True)  # Field name made lowercase.
#     servicenotes = models.TextField(db_column='Servicenotes', blank=True, null=True)  # Field name made lowercase.
#     authordate = models.TextField(db_column='AuthorDate', blank=True, null=True)  # Field name made lowercase.
#     authorname = models.TextField(db_column='AuthorName', blank=True, null=True)  # Field name made lowercase.
#     edited = models.TextField(db_column='Edited', blank=True, null=True)  # Field name made lowercase.
#     editdatename = models.TextField(db_column='EditDateName', blank=True, null=True)  # Field name made lowercase.
#     oldprice = models.TextField(db_column='OldPrice', blank=True, null=True)  # Field name made lowercase.
#     oldpricedate = models.TextField(db_column='OldPriceDate', blank=True, null=True)  # Field name made lowercase.
#     type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
#     universalid = models.CharField(db_column='UniversalID', max_length=35, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         db_table = 'service'


# class Servicen1(models.Model):
#     serviceid = models.CharField(db_column='ServiceID', primary_key=True, max_length=35)  # Field name made lowercase.
#     department = models.CharField(db_column='Department', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     technique = models.CharField(db_column='Technique', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     instrument = models.CharField(db_column='Instrument', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     test = models.CharField(db_column='Test', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     serviceprice = models.CharField(db_column='ServicePrice', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     prevprice = models.CharField(db_column='PrevPrice', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     pricedate = models.CharField(db_column='PriceDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     nameslist = models.TextField(db_column='NamesList', blank=True, null=True)  # Field name made lowercase.
#     intraining = models.CharField(db_column='InTraining', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     servicelocation = models.CharField(db_column='ServiceLocation', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     servicecategories = models.CharField(db_column='ServiceCategories', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     methodservicetype = models.CharField(db_column='MethodServiceType', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=105, blank=True, null=True)  # Field name made lowercase.
#     specialbilling = models.CharField(db_column='SpecialBilling', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     servicenotes = models.TextField(db_column='Servicenotes', blank=True, null=True)  # Field name made lowercase.
#     authordate = models.CharField(db_column='AuthorDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     authorname = models.CharField(db_column='AuthorName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     oldprice = models.CharField(db_column='OldPrice', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     oldpricedate = models.CharField(db_column='OldPriceDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     type = models.CharField(db_column='Type', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     universalid = models.CharField(db_column='UniversalID', max_length=35, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         db_table = 'servicen1'
