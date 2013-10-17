#!/usr/bin/python
NEW_OBJECT_TYPES = [
    ('com.bricsnet.core.dal.addressinfo.LegacyAddressInfoDTO', 'OBJECT_TYPE_LEGACY_ADDRESS_INFO'),
    ('com.bricsnet.core.dal.adhoc.AdhocReportCriteriaDTO', 'OBJECT_TYPE_ADHOC_REPORT_CRITERIA'),
    ('com.bricsnet.core.dal.adhoc.AdhocReportDTO', 'OBJECT_TYPE_ADHOC_REPORT'),
    ('com.bricsnet.core.dal.atstructure.LegacyAssetTypeStructureDTO', 'OBJECT_TYPE_LEGACY_ASSET_TYPE_STRUCTURE'),
    ('com.bricsnet.core.dal.attribute.LegacyAttributeDTO', 'OBJECT_TYPE_LEGACY_ATTRIBUTE'),
    ('com.bricsnet.core.dal.attributevalue.LegacyAttributeValueDTO', 'OBJECT_TYPE_LEGACY_ATTRIBUTE_VALUE'),
    ('com.bricsnet.core.dal.businessrole.LegacyBusinessRoleDTO', 'OBJECT_TYPE_LEGACY_BUSINESS_ROLE'),
    ('com.bricsnet.core.dal.ccstructure.LegacyCostCenterStructureDTO', 'OBJECT_TYPE_LEGACY_COST_CENTER_STRUCTURE'),
    ('com.bricsnet.core.dal.classification.ClassTeamDTO', 'OBJECT_TYPE_CLASS_TEAM'),
    ('com.bricsnet.core.dal.classification.ClassTreeDTO', 'OBJECT_TYPE_CLASS_TREE'),
    ('com.bricsnet.core.dal.classification.ObjectClassDTO', 'OBJECT_TYPE_OBJECT_CLASS'),
    ('com.bricsnet.core.dal.costcenter.LegacyCostCenterDTO', 'OBJECT_TYPE_LEGACY_COST_CENTER'),
    ('com.bricsnet.core.dal.costcenterindex.LegacyCostCenterIndexDTO', 'OBJECT_TYPE_LEGACY_COST_CENTER_INDEX'),
    ('com.bricsnet.core.dal.currency.LegacyCurrencyDTO', 'OBJECT_TYPE_LEGACY_CURRENCY'),
    ('com.bricsnet.core.dal.dashboard.DashboardDTO', 'OBJECT_TYPE_DASHBOARD'),
    ('com.bricsnet.core.dal.dashboard.DashboardSettingDTO', 'OBJECT_TYPE_DASHBOARD_SETTING'),
    ('com.bricsnet.core.dal.document.LegacyDocumentBlobDTO', 'OBJECT_TYPE_LEGACY_DOCUMENT_BLOB'),
    ('com.bricsnet.core.dal.document.LegacyDocumentDTO', 'OBJECT_TYPE_LEGACY_DOCUMENT'),
    ('com.bricsnet.core.dal.document.LegacyDocumentHistoryDTO', 'OBJECT_TYPE_LEGACY_DOCUMENT_HISTORY'),
    ('com.bricsnet.core.dal.document.LegacyDocumentStructureDTO', 'OBJECT_TYPE_LEGACY_DOCUMENT_STRUCTURE'),
    ('com.bricsnet.core.dal.documentextension.LegacyDocumentExtensionDTO', 'OBJECT_TYPE_LEGACY_DOCUMENT_EXTENSION'),
    ('com.bricsnet.core.dal.documentindex.LegacyDocumentIndexDTO', 'OBJECT_TYPE_LEGACY_DOCUMENT_INDEX'),
    ('com.bricsnet.core.dal.kpi.KpiPanelDTO', 'OBJECT_TYPE_KPI_PANEL'),
    ('com.bricsnet.core.dal.locale.LegacyLocaleDTO', 'OBJECT_TYPE_LEGACY_LOCALE'),
    ('com.bricsnet.core.dal.locale.LegacyLocaleDTO', 'OBJECT_TYPE_LEGACY_LOCALE'),
    ('com.bricsnet.core.dal.note.NoteDTO', 'OBJECT_TYPE_NOTE'),
    ('com.bricsnet.core.dal.objectsecurity.LegacyObjectSecurityDTO', 'OBJECT_TYPE_LEGACY_OBJECT_SECURITY'),
    ('com.bricsnet.core.dal.objectsecurity.LegacyObjectSecurityDTO', 'OBJECT_TYPE_LEGACY_OBJECT_SECURITY'),
    ('com.bricsnet.core.dal.organization.LegacyOrganizationDTO', 'OBJECT_TYPE_LEGACY_ORGANIZATION'),
    ('com.bricsnet.core.dal.orgperson.LegacyOrgPersonDTO', 'OBJECT_TYPE_LEGACY_ORG_PERSON'),
    ('com.bricsnet.core.dal.orgstructure.LegacyOrgStructureDTO', 'OBJECT_TYPE_LEGACY_ORG_STRUCTURE'),
    ('com.bricsnet.core.dal.password.ResetRequestDTO', 'OBJECT_TYPE_RESET_REQUEST'),
    ('com.bricsnet.core.dal.procedure.LegacyCycleDTO', 'OBJECT_TYPE_LEGACY_CYCLE'),
    ('com.bricsnet.core.dal.procedure.LegacyCycleDTO', 'OBJECT_TYPE_LEGACY_CYCLE'),
    ('com.bricsnet.core.dal.procedure.LegacyProcedureCycleDTO', 'OBJECT_TYPE_LEGACY_PROCEDURE_CYCLE'),
    ('com.bricsnet.core.dal.procedure.LegacyProcedureDTO', 'OBJECT_TYPE_LEGACY_PROCEDURE'),
    ('com.bricsnet.core.dal.procedure.LegacyProcedureStepDTO', 'OBJECT_TYPE_LEGACY_PROCEDURE_STEP'),
    ('com.bricsnet.core.dal.procedure.LegacyProcedureStepDTO', 'OBJECT_TYPE_LEGACY_PROCEDURE_STEP'),
    ('com.bricsnet.core.dal.product.LegacyProductDTO', 'OBJECT_TYPE_LEGACY_PRODUCT'),
    ('com.bricsnet.core.dal.product.LegacyProductDTO', 'OBJECT_TYPE_LEGACY_PRODUCT'),
    ('com.bricsnet.core.dal.report.LegacyReportBatchKeyDTO', 'OBJECT_TYPE_LEGACY_REPORT_BATCH_KEY'),
    ('com.bricsnet.core.dal.report.LegacyReportBatchKeyDTO', 'OBJECT_TYPE_LEGACY_REPORT_BATCH_KEY'),
    ('com.bricsnet.core.dal.report.LegacyReportDTO', 'OBJECT_TYPE_LEGACY_REPORT'),
    ('com.bricsnet.core.dal.report.LegacyReportDTO', 'OBJECT_TYPE_LEGACY_REPORT'),
    ('com.bricsnet.core.dal.tax.TaxRateUseDTO', 'OBJECT_TYPE_TAX_RATE_USE'),
    ('com.bricsnet.core.dal.tax.TaxRateUseDTO', 'OBJECT_TYPE_TAX_RATE_USE'),
    ('com.bricsnet.core.dal.userlog.UserLogDTO', 'OBJECT_TYPE_USER_LOG'),
    ('com.bricsnet.core.dal.workpriority.LegacyWorkPriorityDTO', 'OBJECT_TYPE_LEGACY_WORK_PRIORITY'),
    ('com.bricsnet.docmanager.dal.documenthistory.DocumentHistoryDTO', 'OBJECT_TYPE_DOCUMENT_HISTORY'),
    ('com.bricsnet.docmanager.dal.documentmarkup.DocumentMarkupDTO', 'OBJECT_TYPE_DOCUMENT_MARKUP'),
    ('com.bricsnet.docmanager.dal.documentpermission.DocumentPermissionDTO', 'OBJECT_TYPE_DOCUMENT_PERMISSION'),
    ('com.bricsnet.docmanager.dal.documentsubscriber.DocumentSubscriberDTO', 'OBJECT_TYPE_DOCUMENT_SUBSCRIBER'),
    ('com.bricsnet.docmanager.dal.documentversion.DocumentVersionDTO', 'OBJECT_TYPE_DOCUMENT_VERSION'),
    ('com.bricsnet.lease.dal.project.LeaseProjectDTO', 'OBJECT_TYPE_LEASE_PROJECT'),
    ('com.bricsnet.lease.dal.tx.LeaseTxDTO', 'OBJECT_TYPE_LEASE_TX'),
    ('com.bricsnet.lease.dal.worktype.LeaseWorkTypeDTO', 'OBJECT_TYPE_LEASE_WORK_TYPE'),
    ('com.bricsnet.project.dal.bid.BidDTO', 'OBJECT_TYPE_BID'),
    ('com.bricsnet.project.dal.biditem.BidItemDTO', 'OBJECT_TYPE_BID_ITEM'),
    ('com.bricsnet.project.dal.budget.BudgetDTO', 'OBJECT_TYPE_BUDGET'),
    ('com.bricsnet.project.dal.budgetitem.BudgetItemDTO', 'OBJECT_TYPE_BUDGET_ITEM'),
    ('com.bricsnet.project.dal.commitment.CommitmentDTO', 'OBJECT_TYPE_COMMITMENT'),
    ('com.bricsnet.project.dal.commitmentitem.CommitmentItemDTO', 'OBJECT_TYPE_COMMITMENT_ITEM'),
    ('com.bricsnet.project.dal.fundingaccount.FundingAccountDTO', 'OBJECT_TYPE_FUNDING_ACCOUNT'),
    ('com.bricsnet.project.dal.fundingvalue.FundingValueDTO', 'OBJECT_TYPE_FUNDING_VALUE'),
    ('com.bricsnet.project.dal.invoice.InvoiceDTO', 'OBJECT_TYPE_INVOICE'),
    ('com.bricsnet.project.dal.invoiceitem.InvoiceItemDTO', 'OBJECT_TYPE_INVOICE_ITEM'),
    ('com.bricsnet.project.dal.payment.PaymentDTO', 'OBJECT_TYPE_PAYMENT'),
    ('com.bricsnet.project.dal.rfp.RfpDTO', 'OBJECT_TYPE_RFP'),
    ('com.bricsnet.project.dal.spendyear.SpendYearDTO', 'OBJECT_TYPE_SPEND_YEAR'),
    ('com.bricsnet.property.dal.pwo.PropertyPaymentWorkOrderDTO', 'OBJECT_TYPE_PROPERTY_PAYMENT_WORK_ORDER')
    ]
def main():
	global NEW_OBJECT_TYPES
	module = set()
	subModule = set()
	subSubModule = set()
	xxx = []
	for dtoName, constant in NEW_OBJECT_TYPES:
		s = dtoName.split('.')
		module.add(s[2])
		
		if s[3]!='dal':
			i=3
		else:
			i=4
		subModule.add(s[i])
		xxx.append([s[2],s[i],s[i+1]])
	for i, x in enumerate(xxx):
		print i, x
	m = list(module)
	m.sort()
	sm = list(subModule)
	sm.sort()
	for mod in m:
		
	
	dm = dict(zip(m,range(len(m))))
	dsm = dict(zip(sm,range(len(sm))))
	
	for dtoName, constant in NEW_OBJECT_TYPES:
		s = dtoName.split('.')
		number = ""
		number = str(dm[s[2]])+"-"
		i=0
		if s[3]!='dal':
			i=3
		else:
			i=4
		number+=doZeros(dsm[s[i]])+"-"
		print number, dtoName
def count(rist, index):
	if len(rist)==1:
		return 0
	for l in rist[1:]
		count(l,)
		
	
	count(rist[1:])
	names = set()
	for x in xxx:
		if x[index]==moduleName:
			names.add(x)
	lNames = list(names)
	lNames.sort()
	 return dict(zip(lNames,len(names)))
	 
# writes leading zero	
def doZeros(num):
	
	if num<10:
		return "0"+str(num)
	else:
		return str(num)
	print m
	#print subModule
	#print subSubModule
	
		
main()