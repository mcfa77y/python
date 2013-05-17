#!/cygdrive/c/Python30/python
# -*- coding: utf-8 -*-
a="id=23 alphaId=Rent-0000001 startDate=2001-01-01 00:00:00.0 endDate=2001-12-31 00:00:00.0 contractualDueDate=2001-01-01 00:00:00.0 amount=1000.0 isUsingIndex=false isProcessed=true isInArrears=false comments=null paymentFrequencyMonths=1 typeId=1 proRata=2 payDaysBeforeDue=1 payRecordDaysBeforeDue=1 camAdminFee=null additionalPayment=null annualCap=null minimumCap=null baseYear=null baseYearAmount=null costCenterId=null generalLedgerCodeId=67 organizationId=5000 leaseId=14 amendmentId=null addressId=null indexId=null previousIndex=null previousIndexYear=null previousIndexPeriod=null currentIndex=null currentIndexYear=null currentIndexPeriod=null hasNote=false lastUpdatedBy=10000 lastUpdatedOn=2011-08-08 17:33:54.83 version=2 status=2 scheduleId=null deleteStatus=0 lateFee=null obligation=12000.0 obligationWithTax=12000.0 baseUnit=null baseUnitAmount=null escalationAmount=null escalationType=null escalateEveryNumberOfPayments=null escalationAmountCap=null escalationAmountFloor=null isForecast=0\
".split(' ')
b="id=23 alphaId=Rent-0000001 startDate=2001-01-01 00:00:00.0 endDate=2001-12-31 00:00:00.0 contractualDueDate=2001-01-01 00:00:00.0 amount=2000.0 isUsingIndex=false isProcessed=true isInArrears=false comments=null paymentFrequencyMonths=1 typeId=1 proRata=2 payDaysBeforeDue=1 payRecordDaysBeforeDue=1 camAdminFee=null additionalPayment=null annualCap=null minimumCap=null baseYear=null baseYearAmount=null costCenterId=null generalLedgerCodeId=67 organizationId=5000 leaseId=14 amendmentId=null addressId=null indexId=null previousIndex=null previousIndexYear=null previousIndexPeriod=null currentIndex=null currentIndexYear=null currentIndexPeriod=null hasNote=false lastUpdatedBy=10000 lastUpdatedOn=2011-08-08 17:34:41.112 version=3 status=2 scheduleId=null deleteStatus=0 lateFee=null obligation=24000.0 obligationWithTax=24000.0 baseUnit=null baseUnitAmount=null escalationAmount=null escalationType=null escalateEveryNumberOfPayments=null escalationAmountCap=null escalationAmountFloor=null isForecast=0\
".split(' ')
def main():
    aa={}
    for x in a:
        xx = x.split('=')
        if len(xx)>=2:
            aa[xx[0]]=xx[1]
        else:
            print(xx)

    bb={}
    for x in b:
        xx = x.split('=')
        if len(xx)>=2:
            bb[xx[0]]=xx[1]
        else:
            print(xx)
    match=[]
    unmatch=[]
    for k, v in aa.items():
        vv = bb[k]
        if v==vv:
            match.append((k,v))
        else:
            unmatch.append((k,v,vv))
    print('match',match)
    print('unmatched',unmatch)
main()
		
