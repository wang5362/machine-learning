# from bs4 import BeautifulSoup
#
#
# def xsdparse(filename):
# #sauce = open ('/Users/sweeney/PycharmProjects/CTI/eis_ABS_AutoLeaseAssetData.xsd')
#     sauce = open (filename)
#     soup = BeautifulSoup (sauce, 'lxml')
#     sequence = soup.find('xs:sequence')
#     children = sequence.findChildren ()
#     name = ()
#     for child in children:
#         name+=(child.attrs['name'].lower(),)
#     return name
#
# autolease_name = xsdparse('/Users/sweeney/PycharmProjects/CTI/eis_ABS_AutoLeaseAssetData.xsd')
# autoloan_name = xsdparse('/Users/sweeney/PycharmProjects/CTI/eis_ABS_AutoLoanAssetData.xsd')
# print(autolease_name)
# print(autoloan_name)

lease_name = ('assettypenumber', 'assetnumber', 'reportingperiodbegindate', 'reportingperiodenddate', 'originatorname',
              'originationdate', 'acquisitioncost', 'originalleasetermnumber', 'scheduledterminationdate',
              'originalfirstpaymentdate', 'underwritingindicator', 'graceperiod', 'paymenttypecode', 'subvented',
              'vehiclemanufacturername', 'vehiclemodelname', 'vehiclenewusedcode', 'vehiclemodelyear',
              'vehicletypecode', 'vehiclevalueamount', 'vehiclevaluesourcecode', 'baseresidualvalue',
              'baseresidualsourcecode', 'contractresidualvalue', 'lesseecreditscoretype',
              'lesseecreditscore', 'lesseeincomeverificationlevelcode', 'lesseeemploymentverificationcode',
              'colesseepresentindicator', 'paymenttoincomepercentage', 'lesseegeographiclocation', 'assetaddedindicator',
              'remainingtermnumber', 'reportingperiodmodificationindicator', 'servicingadvancemethodcode',
              'reportingperiodsecuritizationvalueamount', 'securitizationdiscountrate', 'nextreportingperiodpaymentamountdue',
              'servicingfeepercentage', 'servicingflatfeeamount', 'otherleaselevelservicingfeesretainedamount',
              'otherassesseduncollectedservicerfeeamount', 'reportingperiodendingactualbalanceamount', 'reportingperiodscheduledpaymentamount',
              'totalactualamountpaid', 'actualothercollectedamount', 'reportingperiodendactualsecuritizationamount',
              'serviceradvancedamount', 'paidthroughdate', 'zerobalanceeffectivedate', 'zerobalancecode', 'currentdelinquencystatus',
              'primaryleaseservicername', 'mostrecentservicingtransferreceiveddate', 'assetsubjectdemandindicator',
              'assetsubjectdemandstatuscode', 'repurchaseamount', 'demandresolutiondate', 'repurchasername',
              'repurchaseorreplacementreasoncode', 'chargedoffamount', 'modificationtypecode', 'leaseextended',
              'terminationindicator', 'excessfeeamount', 'liquidationproceedsamount')

loan_name = ('assettypenumber', 'assetnumber', 'reportingperiodbeginningdate', 'reportingperiodendingdate', 'originatorname', 'originationdate', 'originalloanamount', 'originalloanterm', 'loanmaturitydate', 'originalinterestratepercentage', 'interestcalculationtypecode', 'originalinterestratetypecode', 'originalinterestonlytermnumber', 'originalfirstpaymentdate', 'underwritingindicator', 'graceperiodnumber', 'paymenttypecode', 'subvented', 'vehiclemanufacturername', 'vehiclemodelname', 'vehiclenewusedcode', 'vehiclemodelyear', 'vehicletypecode', 'vehiclevalueamount', 'vehiclevaluesourcecode', 'obligorcreditscoretype', 'obligorcreditscore', 'obligorincomeverificationlevelcode', 'obligoremploymentverificationcode', 'coobligorindicator', 'paymenttoincomepercentage', 'obligorgeographiclocation', 'assetaddedindicator', 'remainingtermtomaturitynumber', 'reportingperiodmodificationindicator', 'servicingadvancemethodcode', 'reportingperiodbeginningloanbalanceamount', 'nextreportingperiodpaymentamountdue', 'reportingperiodinterestratepercentage', 'nextinterestratepercentage', 'servicingfeepercentage', 'servicingflatfeeamount', 'otherservicerfeeretainedbyservicer', 'otherassesseduncollectedservicerfeeamount', 'scheduledinterestamount', 'scheduledprincipalamount', 'otherprincipaladjustmentamount', 'reportingperiodactualendbalanceamount', 'reportingperiodscheduledpaymentamount', 'totalactualamountpaid', 'actualinterestcollectedamount', 'actualprincipalcollectedamount', 'actualothercollectedamount', 'serviceradvancedamount', 'interestpaidthroughdate', 'zerobalanceeffectivedate', 'zerobalancecode', 'currentdelinquencystatus', 'primaryloanservicername', 'mostrecentservicingtransferreceiveddate', 'assetsubjectdemandindicator', 'assetsubjectdemandstatuscode', 'repurchaseamount', 'demandresolutiondate', 'repurchasername', 'repurchasereplacementreasoncode', 'chargedoffprincipalamount', 'recoveredamount', 'modificationtypecode', 'paymentextendednumber', 'repossessedindicator', 'repossessedproceedsamount')