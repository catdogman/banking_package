from com.bca.openapi.client.services.AccountStatementService import AccountStatementService
from com.bca.openapi.client.services.AccountBalanceService import AccountBalanceService
from com.bca.openapi.client.services.GenerateQRISService import GenerateQRISService
from com.bca.openapi.client.services.InquiryQRISService import InquiryQRISService
from com.bca.openapi.client.services.SettlementQRISService import SettlementQRISService
from com.bca.openapi.client.services.OneklikAccountBindingService import OneklikAccountBindingService
from com.bca.openapi.client.services.OneklikAccountBindingInquiryService import OneklikAccountBindingInquiryService
from com.bca.openapi.client.services.OneklikAccountUnbindingService import OneklikAccountUnbindingService
from com.bca.openapi.client.services.OneklikPaymentService import OneklikPaymentService
from com.bca.openapi.client.services.OneklikInquiryPaymentStatusService import OneklikInquiryPaymentStatusService
from com.bca.openapi.client.services.OneklikInquiryPhoneNumberOTPService import OneklikInquiryPhoneNumberOTPService
from com.bca.openapi.client.services.OneklikGeneratePaymentOTPService import OneklikGeneratePaymentOTPService
from com.bca.openapi.client.services.TransferIntraBankService import TransferIntraBankService
from com.bca.openapi.client.services.TransferStatusService import TransferStatusService
from com.bca.openapi.client.services.TransferInterBankONLService import TransferInterBankONLService
from com.bca.openapi.client.services.TransferInterBankRTGSService import TransferInterBankRTGSService
from com.bca.openapi.client.services.TransferInterBankSKNService import TransferInterBankSKNService
from com.bca.openapi.client.services.ExternalAccountInquiryService import ExternalAccountInquiryService
from com.bca.openapi.client.services.VAPaymentStatusService import VAPaymentStatusService
from com.bca.openapi.client.services.VAPaymentService import VAPaymentService
from com.bca.openapi.client.services.VABillPresentmentService import VABillPresentmentService
from com.bca.openapi.client.services.InternalAccountInquiryService import InternalAccountInquiryService
from com.bca.openapi.client.services.SharedBillerService import SharedBillerService
from com.bca.openapi.client.entity.accountstatementrequest.AccountStatementRequest import AccountStatementRequest
from com.bca.openapi.client.entity.accountbalancerequest.AccountBalanceRequest import AccountBalanceRequest
from com.bca.openapi.client.entity.generateqrisrequest.GenerateQRISRequest import GenerateQRISRequest
from com.bca.openapi.client.entity.inquiryqrisrequest.InquiryQRISRequest import InquiryQRISRequest
from com.bca.openapi.client.entity.settlementqrisrequest.SettlementQRISRequest import SettlementQRISRequest
from com.bca.openapi.client.entity.oneklikaccountbindingrequest.OneklikAccountBindingRequest import OneklikAccountBindingRequest,AdditionalData, AdditionalInfo
from com.bca.openapi.client.entity.oneklikaccountbindinginquiryrequest.OneklikAccountBindingInquiryRequest import OneklikAccountBindingInquiryRequest
from com.bca.openapi.client.entity.oneklikaccountunbindingrequest.OneklikAccountUnbindingRequest import OneklikAccountUnbindingRequest
from com.bca.openapi.client.entity.oneklikpaymentrequest.OneklikPaymentRequest import OneklikPaymentRequest,AdditionalInfo, PayOptionDetails, FeeAmount, BillDetails, TransAmount
from com.bca.openapi.client.entity.oneklikinquirypaymentstatusrequest.OneklikInquiryPaymentStatusRequest import OneklikInquiryPaymentStatusRequest
from com.bca.openapi.client.entity.oneklikinquiryphonenumberotprequest.OneklikInquiryPhoneNumberOTPRequest import OneklikInquiryPhoneNumberOTPRequest
from com.bca.openapi.client.entity.oneklikgeneratepaymentotprequest.OneklikGeneratePaymentOTPRequest import OneklikGeneratePaymentOTPRequest,AdditionalInfo, TransAmount 
from com.bca.openapi.client.entity.transferintrabankrequest.TransferIntraBankRequest import TransferIntraBankRequest,AdditionalInfo, Amount
from com.bca.openapi.client.entity.transferstatusrequest.TransferStatusRequest import TransferStatusRequest
from com.bca.openapi.client.entity.transferinterbankonlrequest.TransferInterBankONLRequest import TransferInterBankONLRequest
from com.bca.openapi.client.entity.transferinterbankrtgsrequest.TransferInterBankRTGSRequest import TransferInterBankRTGSRequest
from com.bca.openapi.client.entity.transferinterbanksknrequest.TransferInterBankSKNRequest import TransferInterBankSKNRequest
from com.bca.openapi.client.entity.externalaccountinquiryrequest.ExternalAccountInquiryRequest import ExternalAccountInquiryRequest
from com.bca.openapi.client.entity.vapaymentstatusrequest.VAPaymentStatusRequest import VAPaymentStatusRequest
from com.bca.openapi.client.entity.vabillpresentmentrequest.VABillPresentmentRequest import VABillPresentmentRequest
from com.bca.openapi.client.entity.vapaymentrequest.VAPaymentRequest import VAPaymentRequest, PaidAmount, TotalAmount, CumulativePaymentAmount, BillDetails, BillDescription, FreeTexts, FeeAmount, BillAmount
from com.bca.openapi.client.entity.internalaccountinquiryrequest.InternalAccountInquiryRequest import InternalAccountInquiryRequest
from com.bca.openapi.client.entity.sharedbillerinquirypaymentstatusrequest.SharedBillerRequest import SharedBillerRequest
from com.bca.openapi.client.entity.sharedbillerbillpresentmentrequest.SharedBillerRequest import SharedBillerRequest
from com.bca.openapi.client.entity.sharedbillerpaymentflagrequest.SharedBillerRequest import SharedBillerRequest, PaidAmount
import com.banking_info