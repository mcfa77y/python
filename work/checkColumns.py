#!/cygdrive/c/Python30/python
# -*- coding: utf-8 -*-
#!/usr/bin/python
import sys, re, os, SearchReplace, pickle
hDicPickleFN = 'hDTOs.pkl'
tDicPickleFN = 'tDTOs.pkl'
#DTOs = ["addressinfo.LegacyAddressInfoDTO.class"]

DTOs = ["addressinfo.LegacyAddressInfoDTO.class",\
"adhoc.AdhocReportCriteriaDTO.class",\
"adhoc.AdhocReportDTO.class",\
"attribute.LegacyAttributeDTO.class",\
"attributevalue.LegacyAttributeValueDTO.class",\
"benchmark.BenchmarkDTO.class",\
"benchmark.BenchmarkVectorDTO.class",\
"benchmark.BenchmarkVectorValueDTO.class",\
"businessrole.LegacyBusinessRoleDTO.class",\
"ccalloc.CostCenterAllocationDTO.class",\
"ccstructure.CostCenterStructureDTO.class",\
"chargetype.ChargeTypeDTO.class",\
"classification.ClassTeamDTO.class",\
"classification.ClassTreeDTO.class",\
"classification.ObjectClassDTO.class",\
"costcenterindex.CostCenterIndexDTO.class",\
"dashboard.DashboardDTO.class",\
"dashboard.DashboardSettingDTO.class",\
"document.LegacyDocumentBlobDTO.class",\
"document.LegacyDocumentDTO.class",\
"document.LegacyDocumentHistoryDTO.class",\
"document.LegacyDocumentStructureDTO.class",\
"documentextension.LegacyDocumentExtensionDTO.class",\
"documentindex.LegacyDocumentIndexDTO.class",\
"emaillog.EmailLogDTO.class",\
"kpi.KpiPanelDTO.class",\
"kpi.KpiSettingDTO.class",\
"locale.LegacyLocaleDTO.class",\
"note.NoteDTO.class",\
"notification.NotificationDTO.class",\
"objectsecurity.LegacyObjectSecurityDTO.class",\
"organization.LegacyOrganizationDTO.class",\
"orgperson.LegacyOrgPersonDTO.class",\
"orgstructure.LegacyOrgStructureDTO.class",\
"password.ResetRequestDTO.class",\
"paymentschedule.PaymentScheduleDTO.class",\
"paymentschedule.PaymentScheduleDateDTO.class",\
"person.DirectoryEntryDTO.class",\
"procedure.LegacyCycleDTO.class",\
"procedure.LegacyProcedureCycleDTO.class",\
"procedure.LegacyProcedureDTO.class",\
"procedure.LegacyProcedureStepDTO.class",\
"product.LegacyProductDTO.class",\
"report.LegacyReportBatchKeyDTO.class",\
"report.LegacyReportDTO.class",\
"tax.TaxChargeTypeDTO.class",\
"tax.TaxDTO.class",\
"tax.TaxGroupDTO.class",\
"tax.TaxRateDTO.class",\
"tax.TaxRateUseDTO.class",\
"userlog.UserLogDTO.class",\
"workpriority.LegacyWorkPriorityDTO.class",\

"document.DocumentDTO.class",\
"documenthistory.DocumentHistoryDTO.class",\
"documentmarkup.DocumentMarkupDTO.class",\
"documentpermission.DocumentPermissionDTO.class",\
"documentrepository.DocumentRepositoryDTO.class",\
"documentsubscriber.DocumentSubscriberDTO.class",\
"documentversion.DocumentVersionDTO.class",\

"amendment.LeaseAmendmentDTO.class",\
"assettype.LeaseAssetTypeDTO.class",\
"clause.LeaseClauseDTO.class",\
"improvement.LeaseImprovementDTO.class",\
"improvementtx.LeaseImprovementTxDTO.class",\
"index.LeaseIndexDTO.class",\
"indexyear.LeaseIndexYearDTO.class",\
"insurance.LeaseInsuranceDTO.class",\
"lease.LeaseDTO.class",\
"lease.LeaseExtendedDTO.class",\
"project.LeaseProjectDTO.class",\
"rent.LeaseRentDTO.class",\
"rent.LeaseRentExtendedDTO.class",\
"rentallocation.LeaseRentAllocationDTO.class",\
"rentcomponent.LeaseRentComponentDTO.class",\
"rentpayment.LeaseRentPaymentDTO.class",\
"responsibility.LeaseResponsibilityDTO.class",\
"securitydeposit.LeaseSecurityDepositDTO.class",\
"tx.LeaseTxDTO.class",\
"worktype.LeaseWorkTypeDTO.class",\

"account.AccountDTO.class",\
"bid.BidDTO.class",\
"biditem.BidItemDTO.class",\
"budget.BudgetDTO.class",\
"budgetitem.BudgetItemDTO.class",\
"chartofaccounts.ChartOfAccountsDTO.class",\
"commitment.CommitmentDTO.class",\
"commitmentitem.CommitmentItemDTO.class",\
"contract.ContractDTO.class",\
"fundingaccount.FundingAccountDTO.class",\
"fundingcategory.FundingCategoryDTO.class",\
"fundingvalue.FundingValueDTO.class",\
"invoice.InvoiceDTO.class",\
"invoiceitem.InvoiceItemDTO.class",\
"payment.PaymentDTO.class",\
"project.ProjectDTO.class",\
"relatedaccount.RelatedAccountDTO.class",\
"relatedproperty.RelatedPropertyDTO.class",\
"rfp.RfpDTO.class",\
"spendyear.SpendYearDTO.class",\
"type.ProjectTypeDTO.class",\

"charge.PropertyChargeDTO.class",\
"payment.PropertyPaymentDTO.class",\
"pwo.PropertyPaymentWorkOrderDTO.class"
]


def arrayToString(a):
        s=""
        for v in a:
                s+=v
        return s
def main():
	global hDic,tDic
	#makeDTODict()
	loadDTODict()
	f = open("output.txt",'w') 
	for dtoName in DTOs:
		
		#colNamesSr = SearchReplace.SearchReplace("C:/home/sofeng/python/input/columnNames.txt")
		dtoFN = dtoName.split('.')[1]+".java"			
		dtoSr = SearchReplace.SearchReplace(hDic[dtoFN])
		transient = "@Transient"
		print(dtoFN)
		list = dtoSr.findFindGet("@Transient","public .+ get\w+",3)
		print(list)
		if len(list)>0:
			f.writeTo(dtoFN+"\n")
		for l in list:
			if l.find("Map")<0 and l.find('getObjectType')<0 and l.find('getHistoryProperties')<0 :
				f.writeTo("\t"+l+"\n")
		'''
		for tKey in colNamesSr.listFile:
			#capitalize
			tKey = tKey[0].capitalize()+tKey[1:]
			getter = "get"+tKey+"\(\)"
			isDBnTrans = dtoSr.findFindExist(getter,transient,-2)
			if isDBnTrans:
				f.writeTo(getter+"\n")
				print(getter)
		'''
	f.close()

		
	
def loadDTODict():
	global hDic,tDic
	output = open(hDicPickleFN,'rb')
	hDic = pickle.load(output)
	output.close()
	
	output = open(tDicPickleFN,'rb')
	tDic = pickle.load(output)
	output.close()

def makeDTODict():
	#fn = sys.argv[1]
	global hDic,tDic
	#fn = "C:/projects/HibernateMigration/bc/"
	fn = "C:/home/sofeng/python/input"
	print("Making Dictionaries")
	for root, dirs, files in os.walk(fn):
		for name in files:
			if name.find('DTO.java')>0 and name.find('.svn')<1:
				#print(("hibernate:\n\t"+name))
				hDic[name]=root+"/"+name
	output = open(hDicPickleFN,'wb')
	pickle.dump(hDic,output)
	output.close()
	print("\tcreated hibernate dictionary")
	#fn = "C:/projects/trunk/bc/"
	fn = "C:/home/sofeng/python/input2"
	for root, dirs, files in os.walk(fn):
		for name in files:
			if name.find('DTO.java')>0 and name.find('.svn')<1:
				#print(("trunk:\n\t"+name))
				tDic[name]=root+'/'+name
	output = open(tDicPickleFN,'wb')
	pickle.dump(tDic,output)
	output.close()
	print("\tcreated trunk dictionary")			
maxKeyLength=0
hDic = dict()
tDic = dict()
main()
