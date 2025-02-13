'''
@Created by yuhsiang
@Date : 2019/5/20
'''

# 個人中心
class Member(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def RewardRecord(self, data):
        # API Name =>個人
        # body--
        path = 'RewardRecord'
        self.response_data = self.__http.sendRequest('GET', path, data)

# 会员等级管理
class MemberLevelSetting(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def list(self, data):
        # API Name =>会员等级管理-取得頁面
        # body--
        path = '/MemberLevelSetting/List'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getList(self, data):
        # API Name =>会员等级管理-取得列表清單
        # body--
        path = '/MemberLevelSetting/GetList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getMemberCount(self, data):
        # API Name =>会员等级管理-取得各等級的會員數
        # body--
        path = '/MemberLevelSetting/GetMemberCount'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getEventList(self, data):
        #  取得各等級的參加活動數量
        path = '/MemberLevelSetting/GetEventList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def create(self, data):
        # API Name =>会员等级管理-新增等級頁面
        # body--
        path = '/MemberLevelSetting/Create'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def createSubmit(self, data):
        # API Name =>会员等级管理-新增等級
        # body--/{createParams}
        path = '/MemberLevelSetting/CreateSubmit'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def delete(self, data):
        # API Name =>会员等级管理-刪除等級
        # body--/{id}
        path = '/MemberLevelSetting/Delete'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def modify(self, data):
        # API Name =>会员等级管理-取得修改頁面
        # body--
        path = '/MemberLevelSetting/Modify'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getDetail(self, data):
        # API Name =>会员等级管理-取得詳細資料
        # body--/{id}
        path = '/MemberLevelSetting/GetDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getDetailMemberCount(self, data):
        # API Name =>会员等级管理-取得該等級會員數
        # body--/{id}
        path = '/MemberLevelSetting/GetDetailMemberCount'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def update(self, data):
        # API Name =>会员等级管理-修改等級(更新)
        # body--/{updateParams}
        path = '/MemberLevelSetting/Update'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def detail(self, data):
        # API Name =>会员等级管理-取得設定詳細資料頁面
        # body--
        path = '/MemberLevelSetting/Detail'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def updateIsDangerous(self, data):
        # API Name =>会员等级管理-更改危險等級設定
        # body--/{id}/{isDangerous}
        path = '/MemberLevelSetting/UpdateIsDangerous'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 公司入款帐户
class GroupAccount(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def list(self, data):
        # API Name =>公司入款帐户管理-取得頁面
        # body--
        path = '/GroupAccount/List'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def create(self, data):
        # API Name =>公司入款帐户管理-取得新增頁面
        # body--
        path = '/GroupAccount/Create'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def detail(self, data):
        # API Name =>公司入款帐户管理-取得詳細頁面
        # body--
        path = '/GroupAccount/Detail'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def modify(self, data):
        # API Name =>公司入款帐户管理-取得修改頁面
        # body--
        path = '/GroupAccount/Modify'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def createSubmit(self, data):
        # API Name =>公司入款帐户管理-新增
        # body--/{createAccountParams}
        path = '/GroupAccount/CreateSubmit'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getDetail(self, data):
        # API Name =>公司入款帐户管理-取得公司入款帳戶詳細資料
        # body--/{id}
        path = '/GroupAccount/GetDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateSubmit(self, data):
        # API Name =>公司入款帐户管理-修改
        # body--/{updateAccountParams}
        path = '/GroupAccount/UpdateSubmit'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def delete(self, data):
        # API Name =>公司入款帐户管理-刪除
        # body--/{id}
        path = '/GroupAccount/Delete'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getList(self, data):
        # API Name =>公司入款帐户管理-取得公司入款帳戶列表
        # body--
        path = '/GroupAccount/GetList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def disable(self, data):
        # API Name =>公司入款帐户管理-停用
        # body--/{id}
        path = '/GroupAccount/Disable'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def active(self, data):
        # API Name =>公司入款帐户管理-啟用
        # body--/{id}
        path = '/GroupAccount/Active'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def adjustSum(self, data):
        # API Name =>公司入款帐户管理-變更目前累積(調整)(歸零)
        # body--/{id}/{targetNumber}
        path = '/GroupAccount/AdjustSum'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def broadcastSumInfoUpdated(self, data):
        # API Name =>公司入款帐户管理-廣播更新
        # body--/{id}
        path = '/GroupAccount/BroadcastSumInfoUpdated'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getAllGroupAccountType(self, data):
        # API Name =>公司入款帐户管理-取得所有公司入款帳戶類型
        # body--
        path = '/GroupAccount/GetAllGroupAccountType'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def confirmAllCdnQrCodeImage(self, data):
        # API Name =>公司入款帐户管理-確認 CDN 上 QRCode 圖片
        # body--
        path = '/GroupAccount/ConfirmAllCdnQrCodeImage'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateAvailableMinutes(self, data):
        # API Name =>公司入款帐户管理-更新有效分鐘數
        # body--/{id}/{args}
        path = '/GroupAccount/UpdateAvailableMinutes'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateImage(self, data):
        # API Name =>公司入款帐户管理-更新圖片
        # body--/{qrCodefile}
        path = '/GroupAccount/UpdateImage'
        self.response_data = self.__http.sendRequestForUploadFile(path, data)
        return self.response_data


# 线上支付商户
class GroupThirdParty(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def list(self, data):
        # API Name =>线上支付商户管理-取得列表頁面
        # body--
        path = '/GroupThirdParty/List'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def get_list(self, data):
        # API Name =>线上支付商户管理-取得線上支付商戶列表
        # body--
        path = '/GroupThirdParty/GetList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def create(self, data):
        # API Name =>线上支付商户管理-取得新增頁面
        # body--
        path = '/GroupThirdParty/Create'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def get_types(self, data):
        # API Name =>线上支付商户管理-取得線上商戶類型
        # body--
        path = '/GroupThirdParty/GetTypes'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_third_party_type_list(self, data):
        # API Name =>线上支付商户管理-取得目前支付種類
        # body--
        path = '/GroupThirdParty/GetThirdPartyTypeList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    # def detail(self, data):
    #     # API Name =>线上支付商户管理-取得明細頁面
    #     # body--
    #     path = '/GroupThirdParty/Detail'
    #     self.response_data = self.__http.sendRequest('GET', path, data)
    #     return self.response_data

    def modify(self, data):
        # API Name =>线上支付商户管理-取得修改頁面
        # body--
        path = '/GroupThirdParty/Modify'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def create_dtpp_submit(self, data):
        # API Name =>线上支付商户管理-新增金流公司商戶資料
        # body--/{createDTPPSettingParams}
        path = '/GroupThirdParty/CreateDTPPSubmit'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def get_dtpp_detail(self, data):
        # API Name =>线上支付商户管理-取得新版金流公司商戶資料
        # body--/{id}
        path = '/GroupThirdParty/GetDTPPDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def dtpp_disable(self, data):
        # API Name =>线上支付商户管理-停用金流公司商戶資料
        # body--/{id}
        path = '/GroupThirdParty/DTPPDisable'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def dtpp_active(self, data):
        # API Name =>线上支付商户管理-啟用金流公司商戶資料
        # body--/{id}
        path = '/GroupThirdParty/DTPPActive'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def dtpp_reset(self, data):
        # API Name =>线上支付商户管理-歸零目前商戶累計金額
        # body--/{id}
        path = '/GroupThirdParty/DTPPReset'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def update_dtpp_name(self, data):
        # API Name =>线上支付商户管理-更新名稱
        # body--/{id}/{args}
        path = '/GroupThirdParty/UpdateDTPPName'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def broad_cast_dtpp_sum_info_updated(self, data):
        # API Name =>线上支付商户管理-廣播累計資訊更新
        # body--/{id}
        path = '/GroupThirdParty/BroadcastDTPPSumInfoUpdated'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateDTPPMerchantData(self, data):
        # API Name =>线上支付商户管理-更新商戶資料
        # body--/{id}/{args}/{isNew}
        path = '/GroupThirdParty/UpdateDTPPMerchantData'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateDTPPRange(self, data):
        # API Name =>线上支付商户管理-更新單次存款限額
        # body--/{id}/{args}
        path = '/GroupThirdParty/UpdateDTPPRange'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateDTPPLimit(self, data):
        # API Name =>线上支付商户管理-更新總存款限額
        # body--/{id}/{args}
        path = '/GroupThirdParty/UpdateDTPPLimit'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateDTPPLevelSettingIds(self, data):
        # API Name =>线上支付商户管理-更新可用之會員等級
        # body--/{id}/{args}
        path = '/GroupThirdParty/UpdateDTPPLevelSettingIds'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateDTPPMemo(self, data):
        # API Name =>线上支付商户管理-更新備註
        # body--/{id}/{args}
        path = '/GroupThirdParty/UpdateDTPPMemo'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateDTPPAvailableMinutes(self, data):
        # API Name =>线上支付商户管理-更新有效分鐘數
        # body--/{id}/{args}
        path = '/GroupThirdParty/UpdateDTPPAvailableMinutes'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def dTPPDelete(self, data):
        # API Name =>线上支付商户管理-刪除金流公司商戶資料
        # body--/{id}
        path = '/GroupThirdParty/DTPPDelete'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getDepositLimitsCn(self, data):
        # API Name =>线上支付商户管理-
        # body--/{id}
        path = '/GroupThirdParty/GetDepositLimitsCn'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateDTPPDepositLimitsCn(self, data):
        # API Name =>线上支付商户管理-
        # body--/{id}/{args}
        path = '/GroupThirdParty/UpdateDTPPDepositLimitsCn'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def updateDTPPRecommendationMemo(self, data):
        # API Name =>线上支付商户管理-
        # body--/{id}/{args}
        path = '/GroupThirdParty/UpdateDTPPRecommendationMemo'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateDTPPAmountLock(self, data):
        # API Name =>线上支付商户管理-
        # body--/{id}/{args}
        path = '/GroupThirdParty/UpdateDTPPAmountLock'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateDTPPRecommendationAmountSettings(self, data):
        # API Name =>线上支付商户管理-
        # body--/{id}/{args}
        path = '/GroupThirdParty/UpdateDTPPRecommendationAmountSettings'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateThirdPartySettingSort(self, data):
        # API Name =>线上支付商户管理-
        # body--/{SettingId}/{PreviousSort}/{NextSort}
        path = '/GroupThirdParty/UpdateThirdPartySettingSort'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def getDTPPTypeList(self, data):
        # 新增商戶取得支付商戶列表
        path = '/GroupThirdParty/GetDTPPTypeList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getSettingDetail(self, data):
        # 取得商戶詳細設定資料
        path = '/GroupThirdParty/GetSettingDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getValidDTPP(self, data):
        # 新增商戶取得支付商戶
        path = '/GroupThirdParty/GetValidDTPP'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def SetDtppSortingMode(self, data):
        # API Name =>线上支付看板-自訂排序
        # body--/{query}/{maxId}
        path = '/GroupThirdParty/SetDtppSortingMode'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def UpdateDTPPIsShowCustomMerchant(self, data):
        # API Name =>线上支付看板-自訂商戶開關
        # body--/{maxId}/{isShow}
        path = '/GroupThirdParty/UpdateDTPPIsShowCustomMerchant'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def GetList(self, data):
        # API Name =>线上支付看板-取得商户使用占比与成功率列表
        # body--/{maxId}/{isShow}
        path = '/ThirdPartyPaymentStatistics/GetList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 會員流失預測
class retentionListUsers(object):

    def __init__(self, http):
        self.__http = http
        self.response = {}

    def GetComputeTime(self, data):
        # API Name =>會員流失預測 - 獲取計算時間
        # body--/{}
        path = '/RetentionListUsers/GetComputeTime'
        self.response = self.__http.sendRequest('POST', path, data)
        return self.response

    def GetList(self, data):
        # API Name =>會員流失預測 - 取得列表
        # body--/{pageIndex}/{pageSize}
        path = '/RetentionListUsers/GetList'
        self.response = self.__http.sendRequest('POST', path, data)
        return self.response

    def GetDetail(self, data):
        # API Name =>會員流失預測 - 取得詳細列表
        # body--/{memberId}
        path = '/RetentionListUsers/GetDetail'
        self.response = self.__http.sendRequest('POST', path, data)
        return self.response

    def Export(self, data):
        # API Name =>會員流失預測 - 匯出檔案
        # body--/{}
        path = '/RetentionListUsers/Export'
        self.response = self.__http.sendRequest('POST', path, data)
        return self.response


# 簡訊商戶管理
class SmsMerchantManagement(object):
    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def GetList(self):
        # API Name =>簡訊商戶管理 - 取得商戶列表
        # body--/{}
        data = {}
        path = '/SmsNotificationMgmt/GetList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def AddSmsMerchant(self, data):
        # API Name =>簡訊商戶管理 - 新增商戶
        # body--/{request}
        path = '/SmsNotificationMgmt/AddSmsMerchant'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def GetDetail(self, data):
        # API Name =>簡訊商戶管理 - 取得商戶詳細資料
        # body--/{id}
        path = '/SmsNotificationMgmt/GetDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def UpdateSecret(self, data):
        # API Name =>簡訊商戶管理 - 修改商戶資料
        # body--//{id}/{newValue}
        path = '/SmsNotificationMgmt/UpdateSecret'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def UpdateTemplateId(self, data):
        # API Name =>簡訊商戶管理 - 修改模板ID
        # body--//{id}/{newValue}
        path = '/SmsNotificationMgmt/UpdateTemplateId'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def UpdateState(self, data):
        # API Name =>簡訊商戶管理 - 變更狀態
        # body--//{id}/{newValue}
        path = '/SmsNotificationMgmt/UpdateState'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def UpdateLevelSettingIds(self, data):
        # API Name =>簡訊商戶管理 - 變更可使用會員等級
        # body--//{id}/{levelSettingIds}
        path = '/SmsNotificationMgmt/UpdateLevelSettingIds'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def UpdateMemo(self, data):
        # API Name =>簡訊商戶管理 - 變更備註
        # body--//{id}/{newValue}
        path = '/SmsNotificationMgmt/UpdateMemo'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def UpdateName(self, data):
        # API Name =>簡訊商戶管理 - 變更名稱
        # body--//{id}/{newValue}
        path = '/SmsNotificationMgmt/UpdateName'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def DeleteSmsMerchant(self, data):
        # API Name =>簡訊商戶管理 - 刪除商戶
        # body--//{id}
        path = '/SmsNotificationMgmt/DeleteSmsMerchant'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# GPK活動管理
class JackPotActivity(object):
    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def GetList(self, data):
        # API Name =>GPK活動管理 - 取得列表
        # body--/{}
        path = '/JackPotActivity/GetList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def GetJoinList(self, data):
        # API Name =>GPK活動管理 - 獲取加入列表
        # body--/{}
        path = '/JackPotActivity/GetJoinList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def GetJoinListTotalInfo(self, data):
        # API Name =>GPK活動管理 - 獲取加入列表以獲取全部信息
        # body--/{}
        path = '/JackPotActivity/GetJoinListTotalInfo'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def GetJoinListActivityInfo(self, data):
        # API Name =>GPK活動管理 - 獲取加入列表活動信息
        # body--/{}
        path = '/JackPotActivity/GetJoinListActivityInfo'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def GetJoinDetail(self, data):
        # API Name =>GPK活動管理 - 獲取加入詳細信息
        # body--/{}
        path = '/JackPotActivity/GetJoinDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def JoinListExport(self, data):
        # API Name =>GPK活動管理 - 列表匯出
        # body--/{}
        path = '/JackPotActivity/JoinListExport'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def Search(self, data):
        # API Name =>GPK活動管理 - GPK活动钱包额度转移记录搜尋
        # body--/{}
        path = '/ActivityWalletTransferRecord/Search'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def GetTotalInfo(self, data):
        # API Name =>GPK活動管理 - 獲取總信息
        # body--/{}
        path = '/ActivityWalletTransferRecord/Search'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 代付商戶管理
class PayoutMerchantManagement(object):
    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def GetList(self):
        # API Name =>代付商戶管理 - 取得代付商戶列表
        # body--/{}
        data = {}
        path = '/ThirdPartyPayout/GetList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def GetDetail(self, data):
        # API Name =>代付商戶管理 - 取得代付商戶詳細資料
        # body--/{id}
        path = '/ThirdPartyPayout/GetDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def GetApiList(self):
        # API Name =>代付商戶管理 - 取得代付商戶API列表
        # body--/{}
        data = {}
        path = '/ThirdPartyPayout/GetApiList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def UpdateMerchantName(self, data):
        # API Name =>代付商戶管理 - 修改代付商戶名稱資料
        # body--//{id}/{name}
        path = '/ThirdPartyPayout/UpdateMerchantName'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def UpdateMerchantTotalLimit(self, data):
        # API Name =>代付商戶管理 - 修改代付商戶出款金額
        # body--///{id}/{totalPayoutLimit}
        path = '/ThirdPartyPayout/UpdateMerchantTotalLimit'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def UpdateStatus(self, data):
        # API Name =>代付商戶管理 - 修改代付商戶狀態
        # body--//{id}/{name}
        path = '/ThirdPartyPayout/UpdateStatus'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def UpdateAvailableMinutes(self, data):
        # API Name =>代付商戶管理 - 修改代付商戶有效分鐘數
        # body--//{id}/{name}
        path = '/ThirdPartyPayout/UpdateAvailableMinutes'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def Create(self, data):
        # API Name =>代付商戶管理 - 新增代付商戶
        # body--//{id}/{name}
        path = '/ThirdPartyPayout/Create'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def Delete(self, data):
        # API Name =>代付商戶管理 - 刪除代付商戶
        # body--//{id}
        path = '/ThirdPartyPayout/Delete'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def UpdateCondition(self, data):
        # API Name =>代付商戶管理 - 修改代付商戶禁止使用狀態
        # body--//{id}/{updateCondition}
        path = '/ThirdPartyPayout/UpdateCondition'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def UpdateMerchantData(self, data):
        # API Name =>代付商戶管理 - 修改代付商戶資料
        # body--///{id}/{updateMerchantData}
        path = '/ThirdPartyPayout/UpdateMerchantData'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def UpdateCurrentSumToZero(self, data):
        # API Name =>代付商戶管理 - 代付商戶目前累計歸0
        # body--///{id}
        path = '/ThirdPartyPayout/UpdateCurrentSumToZero'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def UpdateMemberLevelSetting(self, data):
        # API Name =>代付商戶管理 - 代付商戶會員等級
        # body--////{id}/{memberLevelSettings}
        path = '/ThirdPartyPayout/UpdateMemberLevelSetting'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def UpdateDispensingBankSetting(self, data):
        # API Name =>代付商戶管理 - 代付商戶出款銀行
        # body--////{id}/{memberbank}
        path = '/ThirdPartyPayout/UpdateDispensingBankSetting'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def UpdateMerchantLimitRange(self, data):
        # API Name =>代付商戶管理 - 代付商戶出款限額
        # body--///{id}/{payoutLimitStart}/{payoutLimitEnd}
        path = '/ThirdPartyPayout/UpdateMerchantLimitRange'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def UpdateMemo(self, data):
        # API Name =>代付商戶管理 - 代付商戶備註
        # body--///{id}/{memo}
        path = '/ThirdPartyPayout/UpdateMemo'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def UpdateAutoPayoutSwitch(self, data):
        # API Name =>代付商戶管理 - 代付商戶自动出款设置
        # body--///{id}/{isOpen}
        path = '/ThirdPartyPayout/UpdateAutoPayoutSwitch'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


class GPKRewardRecords(object):
    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def getExcel(self, data):
        # 取得GPK2打賞匯出Excel
        path = '/BetRecord/ExportGtiRewardRecord'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 郵件商戶管理
class EmailNotificationMgmt(object):
    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def getList(self, data):
        # 取得郵件商戶列表
        path = '/EmailNotificationMgmt/GetList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getServiceZone(self, data):
        # 取得服務區
        path = '/EmailNotificationMgmt/GetServiceZone'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getDetail(self, data):
        # 取得詳細資料
        path = '/EmailNotificationMgmt/GetDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateName(self, data):
        # 更新商戶名字
        path = '/EmailNotificationMgmt/UpdateName'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateSecret(self, data):
        # 更新AccessKeySecret
        path = '/EmailNotificationMgmt/UpdateSecret'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateState(self, data):
        # 更新狀態
        path = '/EmailNotificationMgmt/UpdateState'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateLevelSettingIds(self, data):
        # 更新會員等級
        path = '/EmailNotificationMgmt/UpdateLevelSettingIds'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateMemo(self, data):
        # 更新備註
        path = '/EmailNotificationMgmt/UpdateMemo'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def addEmailMerchant(self, data):
        # 新增郵件商戶
        path = '/EmailNotificationMgmt/AddEmailMerchant'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def deleteEmailMerchant(self, data):
        # 刪除郵件商戶
        path = '/EmailNotificationMgmt/DeleteEmailMerchant'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 余额宝管理
class Yuebao(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def create(self, data):
        # API Name =>余额宝管理-
        # body--/{dto}
        path = '/Yuebao/Create'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def setEnableTime(self, data):
        # API Name =>余额宝管理-
        # body--/{dto}
        path = '/Yuebao/SetEnableTime'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def setMemberLevelSetting(self, data):
        # API Name =>余额宝管理-
        # body--/{dto}
        path = '/Yuebao/SetMemberLevelSetting'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def sort(self, data):
        # API Name =>余额宝管理-
        # body--/{dto}
        path = '/Yuebao/Sort'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def withdraw(self, data):
        # API Name =>余额宝管理-
        # body--/{dto}
        path = '/Yuebao/Withdraw'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def query(self, data):
        # API Name =>余额宝管理-
        # body--/{dto}
        path = '/Yuebao/Query'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def list(self, data):
        # API Name =>余额宝管理-
        # body--/{dto}
        path = '/Yuebao/List'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def detail(self, data):
        # API Name =>余额宝管理-
        # body--/{dto}
        path = '/Yuebao/Detail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def orderUserDetail(self, data):
        # API Name =>余额宝管理-
        # body--/{dto}
        path = '/Yuebao/OrderUserDetail'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def history(self, data):
        # API Name =>余额宝管理-
        # body--/{id}/{pageSize}/{pageIndex}
        path = '/Yuebao/History'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getMemberLevelSetting(self, data):
        # API Name =>余额宝管理-
        # body--
        path = '/Yuebao/GetMemberLevelSetting'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data


# 会员端设定
class PortalSetting(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def list(self, data):
        # API Name =>会员端设定-取得會員端設定列表頁面
        # body--
        path = '/PortalSetting/List'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def create(self, data):
        # API Name =>会员端设定-取得新增頁面
        # body--
        path = '/PortalSetting/Create'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def detail(self, data):
        # API Name =>会员端设定-取得詳細資料頁面
        # body--
        path = '/PortalSetting/Detail'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getList(self, data):
        # API Name =>会员端设定-取得會員端設定列表
        # body--
        path = '/PortalSetting/GetList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def createSubmit(self, data):
        # API Name =>会员端设定-會員端設定-新增成功
        # body--/{args}
        path = '/PortalSetting/CreateSubmit'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getDetail(self, data):
        # API Name =>会员端设定-取得會員端設定詳細資料
        # body--/{id}
        path = '/PortalSetting/GetDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateName(self, data):
        # API Name =>会员端设定-取得會員端設定-修改設定名稱
        # body--/{id}/{args}
        path = '/PortalSetting/UpdateName'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateRegisterSetting(self, data):
        # API Name =>会员端设定-會員注冊設定更新
        # body--/{id}/{args}
        path = '/PortalSetting/UpdateRegisterSetting'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateAgentRegisterSetting(self, data):
        # API Name =>会员端设定-代理注冊設定更新
        # body--/{id}/{args}
        path = '/PortalSetting/UpdateAgentRegisterSetting'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateMemo(self, data):
        # API Name =>会员端设定-備註更新
        # body--/{id}/{args}
        path = '/PortalSetting/UpdateMemo'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def delete(self, data):
        # API Name =>会员端设定-刪除
        # body--/{id}/{args}
        path = '/PortalSetting/Delete'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateCompanyDepositToggle(self, data):
        # API Name =>会员端设定-關閉公司入款(false)
        # body--/{id}/{status}
        path = '/PortalSetting/UpdateCompanyDepositToggle'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateCompanyDepositMessage(self, data):
        # API Name =>会员端设定-公司入款修改內容更新
        # body--/{id}/{args}
        path = '/PortalSetting/UpdateCompanyDepositMessage'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateWithdrawToggle(self, data):
        # API Name =>会员端设定-關閉取款申請(false)
        # body--/{id}/{status}
        path = '/PortalSetting/UpdateWithdrawToggle'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateWithdrawMessage(self, data):
        # API Name =>会员端设定-取款申請修改內容更新
        # body--/{id}/{args}
        path = '/PortalSetting/UpdateWithdrawMessage'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateWalletDepositToggle(self, data):
        # API Name =>会员端设定-
        # body--/{id}/{status}
        path = '/PortalSetting/UpdateWalletDepositToggle'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def updateWalletDepositMessage(self, data):
        # API Name =>会员端设定-
        # body--/{id}/{args}
        path = '/PortalSetting/UpdateWalletDepositMessage'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def updateWalletWithdrawToggle(self, data):
        # API Name =>会员端设定-
        # body--/{id}/{status}
        path = '/PortalSetting/UpdateWalletWithdrawToggle'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def updateWalletWithdrawMessage(self, data):
        # API Name =>会员端设定-
        # body--/{id}/{args}
        path = '/PortalSetting/UpdateWalletWithdrawMessage'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def updateWalletRemittancePortalToggle(self, data):
        # API Name =>会员端设定-
        # body--/{id}/{status}
        path = '/PortalSetting/UpdateWalletRemittancePortalToggle'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def updateIsYuebaoToggle(self, data):
        # API Name =>会员端设定-
        # body--/{id}/{status}
        path = '/PortalSetting/UpdateIsYuebaoToggle'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 返水设定
class AnyTimeDiscountSetting(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def list(self, data):
        # API Name =>时时返水-取得返水設定列表頁面
        # body--
        path = '/AnyTimeDiscount/List'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def createForBatch(self, data):
        # API Name =>时时返水-
        # body--
        path = '/AnyTimeDiscount/CreateForBatch'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def detail(self, data):
        # API Name =>时时返水-
        # body--
        path = '/AnyTimeDiscount/Detail'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def modifyForBatch(self, data):
        # API Name =>时时返水-
        # body--
        path = '/AnyTimeDiscount/ModifyForBatch'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def modifyForATD(self, data):
        # API Name =>时时返水-
        # body--
        path = '/AnyTimeDiscount/ModifyForATD'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def activeDialog(self, data):
        # API Name =>时时返水-
        # body--
        path = '/AnyTimeDiscount/ActiveDialog'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def resetDialog(self, data):
        # API Name =>时时返水-
        # body--
        path = '/AnyTimeDiscount/ResetDialog'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def detailDialog(self, data):
        # API Name =>时时返水-
        # body--
        path = '/AnyTimeDiscount/DetailDialog'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def getList(self, data):
        # API Name =>时时返水-
        # body--
        path = '/AnyTimeDiscount/GetList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def createSubmit(self, data):
        # API Name =>时时返水-
        # body--/{createParams}/{setting}/{detail}
        path = '/AnyTimeDiscount/CreateSubmit'

        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def verifyParams(self, data):
        # API Name =>时时返水-
        # body--/{createParams}
        path = '/AnyTimeDiscount/VerifyParams'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getDetail(self, data):
        # API Name =>时时返水-
        # body--/{id}
        path = '/AnyTimeDiscount/GetDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def delete(self, data):
        # API Name =>时时返水-
        # body--/{id}
        path = '/AnyTimeDiscount/Delete'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateHasDiscount(self, data):
        # API Name =>时时返水-
        # body--/{id}/{isDiscount}
        path = '/AnyTimeDiscount/UpdateHasDiscount'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateMemo(self, data):
        # API Name =>时时返水-
        # body--/{id}/{memo}
        path = '/AnyTimeDiscount/UpdateMemo'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateName(self, data):
        # API Name =>时时返水-
        # body--/{id}/{name}
        path = '/AnyTimeDiscount/UpdateName'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateDetails(self, data):
        # API Name =>时时返水-
        # body--/{id}/{details}
        path = '/AnyTimeDiscount/UpdateDetails'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def notifyResetFinish(self, data):
        # API Name =>时时返水-
        # body--
        path = '/AnyTimeDiscount/NotifyResetFinish'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def getATDSetting(self, data):
        # API Name =>时时返水-
        # body--/{discountSettingId}
        path = '/AnyTimeDiscount/GetATDSetting'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getATDSettingDetail(self, data):
        # API Name =>时时返水-
        # body--/{discountSettingId}
        path = '/AnyTimeDiscount/GetATDSettingDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getATDSupplierDetail(self, data):
        # API Name =>时时返水-
        # body--
        path = '/AnyTimeDiscount/GetATDSupplierDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def alterATDSetting(self, data):
        # API Name =>时时返水-
        # body--/{setting}/{detail}
        path = '/AnyTimeDiscount/AlterATDSetting'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def alterATDLimit(self, data):
        # API Name =>时时返水-
        # body--/{discountSettingId}/{limit}
        path = '/AnyTimeDiscount/AlterATDLimit'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def alterATDMaxAmountLimit(self, data):
        # API Name =>时时返水-
        # body--/{discountSettingId}/{Maxlimint}
        path = '/AnyTimeDiscount/AlterATDMaxAmountLimit'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def alterATDAppointment(self, data):
        # API Name =>时时返水-
        # body--/{discountSettingId}/{EnableAppointment}/{DisableAppointment}
        path = '/AnyTimeDiscount/AlterATDAppointment'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def alterATDAudit(self, data):
        # API Name =>时时返水-
        # body--/{discountSettingId}/{audit}
        path = '/AnyTimeDiscount/AlterATDAudit'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def alterATDReceiveSwitch(self, data):
        # API Name =>时时返水-
        # body--/{discountSettingId}/{receiveSwitch}
        path = '/AnyTimeDiscount/AlterATDReceiveSwitch'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def alterATDPercentages(self, data):
        # API Name =>时时返水-
        # body--/{discountSettingId}/{viewModel}
        path = '/AnyTimeDiscount/AlterATDPercentages'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def alterATDResetByDiscountSetting(self, data):
        # API Name =>时时返水-
        # body--/{password}/{discountSettingId}
        path = '/AnyTimeDiscount/AlterATDResetByDiscountSetting'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def alterATDResetByOneMember(self, data):
        # API Name =>时时返水-
        # body--/{password}/{id}
        path = '/AnyTimeDiscount/AlterATDResetByOneMember'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def getMemberDiscountTotalAmount(self, data):
        # API Name =>时时返水-
        # body--/{memberId}/{isClearCache}
        path = '/AnyTimeDiscount/GetMemberDiscountTotalAmount'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def getMemberDiscountDetail(self, data):
        # API Name =>时时返水-
        # body--/{memberId}
        path = '/AnyTimeDiscount/GetMemberDiscountDetail'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def getSettingRecords(self, data):
        # API Name =>时时返水-
        # body--/{discountSettingId}
        path = '/AnyTimeDiscount/GetSettingRecords'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def getIsATDResetRunning(self, data):
        # API Name =>时时返水-
        # body--
        path = '/AnyTimeDiscount/GetIsATDResetRunning'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getGPKReceivSwitchStatus(self, data):
        # API Name =>时时返水-
        # body--
        path = '/AnyTimeDiscount/GetGPKReceivSwitchStatus'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def refreshMemberDiscountDetail(self, data):
        # API Name =>时时返水-
        # body--/{memberId}
        path = '/AnyTimeDiscount/RefreshMemberDiscountDetail'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def getATDResetByDiscountSettingRecord(self, data):
        # 時返歸零歷程記錄 -2019/12/20
        path = '/AnyTimeDiscount/GetATDResetByDiscountSettingRecord'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getATDWithdrawSwitchLog(self, data):
        # 時返歸零歷程記錄 -2019/12/20
        path = '/AnyTimeDiscount/GetATDWithdrawSwitchLog'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 佣金设定
class CommissionSetting(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def list(self, data):
        # API Name =>佣金设定-取得列表頁面
        # body--
        path = '/CommissionSetting/List'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def create(self, data):
        # API Name =>佣金设定-取得設定頁面
        # body--
        path = '/CommissionSetting/Create'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def detail(self, data):
        # API Name =>佣金设定-取得詳細資料頁面
        # body--
        path = '/CommissionSetting/Detail'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def modify(self, data):
        # API Name =>佣金设定-取得修改頁面
        # body--
        path = '/CommissionSetting/Modify'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getList(self, data):
        # API Name =>佣金设定-取得設定列表
        # body--
        path = '/CommissionSetting/GetList'

        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getDetail(self, data):
        # API Name =>佣金设定-取得列表詳細資料
        # body--/{id}
        path = '/CommissionSetting/GetDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def changeState(self, data):
        # API Name =>佣金设定-佣金設定更改狀態
        # body--/{id}
        path = '/CommissionSetting/ChangeState'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def delete(self, data):
        # API Name =>佣金设定-刪除佣金設定
        # body--/{id}
        path = '/CommissionSetting/Delete'

        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def update(self, data):
        # API Name =>佣金设定-更新佣金設定
        # body--/{commissionSetting}
        path = '/CommissionSetting/Update'

        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def createSubmit(self, data):
        # API Name =>佣金设定-新增佣金設定
        # body--/{commissionSetting}
        path = '/CommissionSetting/CreateSubmit'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 娱乐城管理
class GameHallManagement(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def list(self, data):
        # API Name =>娱乐城管理-取得娛樂城管理頁面
        # body--
        path = '/GameHallManagement/List'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def detail(self, data):
        # API Name =>娱乐城管理-取得娛樂城管理詳細資料頁面
        # body--
        path = '/GameHallManagement/Detail'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def history(self, data):
        # API Name =>娱乐城管理-取得娛樂城管理歷史紀錄頁面
        # body--
        path = '/GameHallManagement/History'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getGameHallList(self, data):
        # API Name =>娱乐城管理-取得娛樂城管理列表
        # body--
        path = '/GameHallManagement/GetGameHallList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getGameHallListInfo(self, data):
        # API Name =>娱乐城管理-取得娛樂城管理列表資訊
        # body--
        path = '/GameHallManagement/GetGameHallListInfo'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getGameCategoryTypes(self, data):
        # API Name =>娱乐城管理-取得娛樂城所有遊戲類型
        # body--/{gameSupplierType}
        path = '/GameHallManagement/GetGameCategoryTypes'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getGameHallDetail(self, data):
        # API Name =>娱乐城管理-取得娛樂城詳細
        # body--/{gameHallUrlText}/{jaguar}
        path = '/GameHallManagement/GetGameHallDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getGameHallStatus(self, data):
        # API Name =>娱乐城管理-取得指定娛樂城狀態
        # body--/{gameHallUrlText}/{jaguar}
        path = '/GameHallManagement/GetGameHallStatus'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getBackofficeUrl(self, data):
        # API Name =>娱乐城管理-取得娛樂城後台連結 Url
        # body--/{gameSupplierType}
        path = '/GameHallManagement/GetBackofficeUrl'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def loadHistory(self, data):
        # API Name =>娱乐城管理-載入指定娛樂城歷史紀錄
        # body--/{gameHallUrlText}/{take}/{skip}/{query}
        path = '/GameHallManagement/LoadHistory'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def transferGameHallUrlText(self, data):
        # API Name =>娱乐城管理-把url的Text改成要顯示的Text
        # body--/{gameHallUrlText}/{jaguar}
        path = '/GameHallManagement/TransferGameHallUrlText'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def modifyGameHallStatus(self, data):
        # API Name =>娱乐城管理-變更指定娛樂城狀態
        # body--/{gameSupplierType}/{isEnterable}
        path = '/GameHallManagement/ModifyGameHallStatus'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def exitGameHall(self, data):
        # API Name =>娱乐城管理-踢出指定娛樂城所有會員
        # body--/{gameSupplierType}
        path = '/GameHallManagement/ExitGameHall'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def transferMoneyBack(self, data):
        # API Name =>娱乐城管理-轉回指定娛樂城所有錢包
        # body--/{gameSupplierType}
        path = '/GameHallManagement/TransferMoneyBack'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateAllWallet(self, data):
        # API Name =>娱乐城管理-更新指定娛樂城所有錢包
        # body--/{gameSupplierType}
        path = '/GameHallManagement/UpdateAllWallet'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def calculateValidBet(self, data):
        # API Name =>娱乐城管理-娛樂城計算有效投注
        # body--/{searchParam}
        path = '/GameHallManagement/CalculateValidBet'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 站内信
class SiteMail(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def list(self, data):
        # API Name =>站内信-取得列表頁面
        # body--
        path = '/SiteMail/List'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def send(self, data):
        # API Name =>站内信-取得發送信件頁面
        # body--
        path = '/SiteMail/Send'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getInboxList(self, data):
        # API Name =>站内信-取得收件匣的信件列表
        # body--/{input}
        path = '/SiteMail/GetInboxList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getUnreadCount(self, data):
        # API Name =>站内信-取得未讀信件總數
        # body--
        path = '/SiteMail/GetUnreadCount'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getSentboxList(self, data):
        # API Name =>站内信-取得寄件匣的信件列表
        # body--/{input}
        path = '/SiteMail/GetSentboxList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getSearchMailDateList(self, data):
        # API Name =>站内信-取得搜尋日期用的列表
        # body--
        path = '/SiteMail/GetSearchMailDateList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def deleteInboxMails(self, data):
        # API Name =>站内信-刪除收件匣的信件
        # body--/{inboxMailIds}
        path = '/SiteMail/DeleteInboxMails'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def deleteSentboxMails(self, data):
        # API Name =>站内信-刪除寄件匣的信件
        # body--/{sentboxMailIds}
        path = '/SiteMail/DeleteSentboxMails'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def setInboxMailsAsReadOrUnread(self, data):
        # API Name =>站内信-設定收件匣信件已讀未讀
        # body--/{inboxMailIds}/{isRead}
        path = '/SiteMail/SetInboxMailsAsReadOrUnread'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getMailDetail(self, data):
        # API Name =>站内信-取得信件詳細內容
        # body--/{mailId}
        path = '/SiteMail/GetMailDetail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getMailReceiverList(self, data):
        # API Name =>站内信-取得收件人清單
        # body--/{input}
        path = '/SiteMail/GetMailReceiverList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getAllSiteMemberCount(self, data):
        # API Name =>站内信-取得全站會員數量
        # body--
        path = '/SiteMail/GetAllSiteMemberCount'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def sendMail(self, data):
        # API Name =>站内信-發送信件
        # body--/{input}
        path = '/SiteMail/SendMail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getMemberSiteMailInfo(self, data):
        # API Name =>站内信-取得管端收件匣中，會員寄送的信件總數以及未讀的信件總數 (For 會員詳細頁)
        # body--/{memberId}
        path = '/SiteMail/GetMemberSiteMailInfo'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def notifyNewInboxMail(self, data):
        # API Name =>站内信-通知管端Client收件匣有新的信件 (供Portal/Mobile使用)
        # body--/{input}
        path = '/SiteMail/NotifyNewInboxMail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def uploadCustomExcel(self, data):
        # API Name =>站内信-
        # body--/{excelFile}
        path = '/SiteMail/UploadCustomExcel'
        self.response_data = self.__http.sendRequestForUploadFile(path, data)
        return self.response_data

    def downloadCustomExcelValidateResult(self, data):
        # API Name =>站内信-
        # body--/{excelPath}
        path = '/SiteMail/DownloadCustomExcelValidateResult'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def downloadSampleExcel(self, data):
        # API Name =>站内信-下載匯入發信範本
        # body--
        path = '/SiteMail/DownloadSampleExcel'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def downloadSiteMailExcelContent(self, data):
        # API Name =>站内信-
        # body--/{siteMailId}
        path = '/SiteMail/DownloadSiteMailExcelContent'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def announcement_GetList(self, data):
        # 站內信 - 促銷匣列表
        path = '/AnnouncementSiteMail/GetList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def announcement_SendMail(self, data):
        path = '/AnnouncementSiteMail/SendMail'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def announcement_Delete(self, data):
        path = '/AnnouncementSiteMail/Delete'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 前台网站管理
class PortalManagement(object):
    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def getWebsiteList(self, data):
        # 前台网站管理 - 取得前台網站管理列表
        path = '/PortalManagement/GetWebsiteList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getPortalSettings(self, data):
        # 前台网站管理 - 取得會員端設定
        path = '/WebsiteSetting/GetPortalSettings'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateWebsite(self, data):
        # 前台网站管理 - 更新站台
        path = '/PortalManagement/UpdateWebsite'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    # 公告管理
    class AnnouncementManagement:
        def __init__(self, http):
            self.__http = http
            self.response_data = {}

        def getAnnouncementList(self, data):
            # 公告管理-取得公告列表
            path = '/PortalManagement/GetAnnouncementList'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def checkTutorialNeedWatch(self, data):
            # 公告管理-
            path = '/PortalManagement/CheckTutorialNeedWatch'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def getAnnouncementSetting(self, data):
            # 公告管理 - 取得公告管理設定
            path = '/PortalManagement/GetAnnouncementSetting'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def updateAnnouncementSetting(self, data):
            # 公告管理 - 更新公告管理設定
            path = '/PortalManagement/UpdateAnnouncementSetting'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def addAnnouncement(self, data):
            # 公告管理 - 新增公告
            path = '/PortalManagement/AddAnnouncement'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def getAnnouncementDetail(self, data):
            # 公告管理 - 公告詳細資料
            path = '/PortalManagement/GetAnnouncementDetail'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def modifyAnnouncement(self, data):
            # 公告管理 - 修改公告
            path = '/PortalManagement/ModifyAnnouncement'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def modifyAnnouncementEnable(self, data):
            # 公告管理 - 更新是否啟用
            path = '/PortalManagement/ModifyAnnouncementEnable'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def moveAnnouncementToDevice(self, data):
            # 公告管理 - 移動到手機板
            path = '/PortalManagement/MoveAnnouncementToDevice'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def moveAnnouncementToWebsite(self, data):
            # 公告管理 - 移動到其他站台
            path = '/PortalManagement/MoveAnnouncementToWebsite'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def copyAnnouncementToDevice(self, data):
            # 公告管理 - 複製到手機板
            path = '/PortalManagement/CopyAnnouncementToDevice'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def copyAnnouncementToWebsite(self, data):
            # 公告管理 - 複製到其他站台
            path = '/PortalManagement/CopyAnnouncementToWebsite'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def deleteAnnouncement(self, data):
            # 公告管理 - 刪除公告
            path = '/PortalManagement/DeleteAnnouncement'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def modifyAnnouncementSort(self, data):
            # 公告管理 - 修改公告順序
            path = '/PortalManagement/ModifyAnnouncementSort'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def getAnnouncementPreviewList(self, data):
            # 公告管理 - 預覽公告列表
            path = '/PortalManagement/GetAnnouncementPreviewList'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def getMarqueeContent(self, data):
            # 公告管理 - 取得跑馬燈內容
            path = '/PortalManagement/GetMarqueeContent'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def updateMarqueeContent(self, data):
            # 公告管理 - 取得跑馬燈內容
            path = '/PortalManagement/UpdateMarqueeContent'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

    # 大圖輪播
    class SlideShow:
        def __init__(self, http):
            self.__http = http
            self.response_data = {}

        def GetSlideShowInfo(self, data):
            # 取得大圖輪播資訊
            path = '/PortalManagement/GetSlideShowInfo'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def UploadSlideShowImageV2(self, data):
            # 上傳圖片
            path = '/PortalManagement/UploadSlideShowImageV2'
            self.response_data = self.__http.sendRequestForUploadFile(path, data)
            return self.response_data

        def SaveSlideShowChangesV2(self, data):
            # 儲存圖片
            path = '/PortalManagement/SaveSlideShowChangesV2'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

    # 會員註冊
    class RegisterCopywriting:
        def __init__(self, http):
            self.__http = http
            self.response_data = {}

        def GetRegisterCopywriting(self, data):
            # 會員註冊 - 取得文案
            path = '/PortalManagement/GetRegisterCopywriting'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def ModifyRegisterCopywriting(self, data):
            # 會員註冊 - 修改文案
            path = '/PortalManagement/ModifyRegisterCopywriting'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def CopyRegisterCopywriting(self, data):
            # 會員註冊 - 複製其他網站
            path = '/PortalManagement/CopyRegisterCopywriting'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

    # 聯絡資訊
    class SiteParameter:
        def __init__(self, http):
            self.__http = http
            self.response_data = {}

        def GetSiteParameter(self, data):
            # 聯絡資訊 - 取得聯絡資訊
            path = '/PortalManagement/GetSiteParameter'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def UpdateSiteParameter(self, data):
            # 聯絡資訊 - 更新聯絡資訊
            path = '/PortalManagement/UpdateSiteParameter'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

    # 財務中心
    class FinanceCenter:
        def __init__(self, http):
            self.__http = http
            self.response_data = {}

        def GetFinanceCenterSubCategory(self, data):
            # 財務中心 取得分類列表狀態
            path = '/FinanceCenter/GetFinanceCenterSubCategory'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def GetOnlinePaymentDirectSetting(self, data):
            # 財務中心 取得裝置種類狀態
            path = '/FinanceCenter/GetOnlinePaymentDirectSetting'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def GetFinanceCenterDetailSetting(self, data):
            # 財務中心 取得詳細資料列表狀態
            path = '/FinanceCenter/GetFinanceCenterDetailSetting'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def UpdateFinanceCenterSubCategory(self, data):
            # 財務中心 修改推廣圖標文字狀態
            path = '/FinanceCenter/UpdateFinanceCenterSubCategory'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

    # 選單管理
    class MobileMenu:
        def __init__(self, http):
            self.__http = http
            self.response_data = {}

        def GetList(self, data):
            # 選單管理 取得登入前列表狀態
            path = '/MobileMenuManagement/GetList'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def GetDefaultList(self, data):
            # 選單管理 取得登入前列表狀態
            path = '/MobileMenuManagement/GetDefaultList'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def UpdateList(self, data):
            # 選單管理 新增項目功能
            path = '/MobileMenuManagement/UpdateList'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def CopyMenu(self, data):
            # 選單管理 複制功能
            path = '/MobileMenuManagement/CopyMenu'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

    # 優惠管理
    class PromotionManage:
        def __init__(self, http):
            self.__http = http
            self.response_data = {}

        def GetPromotions(self, data):
            # 優惠管理 取得列表狀態、複制子子分類
            path = '/PromotionManagement/GetPromotions'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def Submit(self, data):
            # 優惠管理 新增/移除：大分類、子分類、子子分類功能
            path = '/PromotionManagement/Submit'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

    # 主題設置
    class MobileTheme:
        def __init__(self, http):
            self.__http = http
            self.response_data = {}

        def GetMobileThemeDomain(self, data):
            # 主題設置 - 取得手機主題域
            path = '/MobileThemeManagement/GetMobileThemeDomain'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def GetMobileTheme(self, data):
            # 主題設置 - 取得手機主題
            path = '/MobileThemeManagement/GetMobileTheme'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def AddColor(self, data):
            # 主題設置 - 另存色系主題名稱
            path = '/MobileThemeManagement/AddColor'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def UpdateColorName(self, data):
            # 主題設置 - 修改色系主題名稱
            path = '/MobileThemeManagement/UpdateColorName'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def SaveMobileTheme(self, data):
            # 主題設置 - 修改值向手機預設版本
            path = '/MobileThemeManagement/SaveMobileTheme'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def DeleteColor(self, data):
            # 主題設置 - 刪除色系Tag名稱
            path = '/MobileThemeManagement/DeleteColor'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

    # 網站版面
    class PortalManagement:
        def __init__(self, http):
            self.__http = http
            self.response_data = {}

        def GetProductSetting(self, data):
            # 網站版面 - 獲取產品設置
            path = '/PortalManagement/GetProductSetting'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def SaveProductSetting(self, data):
            path = '/PortalManagement/SaveProductSetting'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data


# 子帐号管理


# 站台系统值设置
class SystemInfo(object):
    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def index(self, data):
        # API Name =>站台系统值设置-取得站台系統值設置頁面
        # body--
        path = '/SystemInfo/Index'
        self.response_data = self.__http.sendRequest('GET', path, data)
        return self.response_data

    def getMemberStates(self, data):
        # API Name =>站台系统值设置-取得會員狀態
        # body--
        path = '/SystemInfo/GetMemberStates'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getAll(self, data):
        # API Name =>站台系统值设置-取得站台系統值設置
        # body--
        path = '/SystemInfo/GetAll'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateAgentCustomerService(self, data):
        # API Name =>站台系统值设置-代理管端系统客服
        # body--
        path = '/SystemInfo/UpdateAgentCustomerService'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateCaptchaTypeLogin(self, data):
        # API Name =>站台系统值设置-更新會員登入驗證碼類型
        # body--
        path = '/SystemInfo/UpdateCaptchaTypeLogin'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updatePortalLoginFailTimesLimit(self, data):
        # API Name =>站台系统值设置-更新密碼錯誤次數
        # body--
        path = '/SystemInfo/UpdatePortalLoginFailTimesLimit'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateLoginRegionValidationEnable(self, data):
        # API Name =>站台系统值设置-更新區域驗證
        # body--
        path = '/SystemInfo/UpdateLoginRegionValidationEnable'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateLockOtherRegion(self, data):
        # API Name =>站台系统值设置-更新跨區驗證鎖頭
        # body--
        path = '/SystemInfo/UpdateLockOtherRegion'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateLoginSmsValidationEnable(self, data):
        # API Name =>站台系统值设置-更新簡訊驗證
        # body--
        path = '/SystemInfo/UpdateLoginSmsValidationEnable'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateLoginGoogleAuthenticatorEnable(self, data):
        # API Name =>站台系统值设置-更新二次驗證
        # body--
        path = '/SystemInfo/UpdateLoginGoogleAuthenticatorEnable'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updatePortalNeedNeCaptcha(self, data):
        # API Name =>站台系统值设置-更新會員登入圖片驗證
        # body--
        path = '/SystemInfo/UpdatePortalNeedNeCaptcha'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateCaptchaTypeRegister(self, data):
        # API Name =>站台系统值设置-更新會員註冊驗證碼類型
        # body--
        path = '/SystemInfo/UpdateCaptchaTypeRegister'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateRobotQuestionRegister(self, data):
        # API Name =>站台系统值设置-更新問答驗證
        # body--
        path = '/SystemInfo/UpdateRobotQuestionRegister'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updatePortalNeedNeCaptchaForRegister(self, data):
        # API Name =>站台系统值设置-更新會員註冊圖片驗證
        # body--
        path = '/SystemInfo/UpdatePortalNeedNeCaptchaForRegister'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateMemberNoBetEnable(self, data):
        # API Name =>站台系统值设置 - 更新未投注會員管理
        # body--
        path = '/SystemInfo/UpdateMemberNoBetEnable'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateMemberNoBetDayAndStatus(self, data):
        # API Name =>站台系统值设置 - 更新未投注會員管理設定條件
        # body--
        path = '/SystemInfo/UpdateMemberNoBetDayAndStatus'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateLoginEmailValidationEnable(self, data):
        # API Name =>站台系统值设置 - 更新郵件驗證
        # body--
        path = '/SystemInfo/UpdateLoginEmailValidationEnable'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateGpkAuthenticator(self, data):
        # API Name =>站台系统值设置 - 更新裝置驗證
        # body--
        path = '/SystemInfo/UpdateGpkAuthenticator'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# 活动管理
class ActivityManagement(object):
    # 红包派送
    class RedEnvelopeManagement:

        def __init__(self, http):
            self.__http = http
            self.response_data = {}

        def getList(self, data):
            # API Name =>红包派送-取得列表資料
            # body--
            path = '/RedEnvelopeManagement/GetList'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def getAllStatus(self, data):
            # 取得紅包狀態
            path = '/RedEnvelopeManagement/GetAllStatus'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def get_detail(self, data):
            # API Name =>红包派送-詳細資料
            # body--
            path = '/RedEnvelopeManagement/GetDetail'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def addRedEnvelope(self, data):
            # 紅包匯入 - 1205
            path = '/RedEnvelopeManagement/AddRedEnvelope'
            self.response_data = self.__http.sendRequestForUploadFile(path, data)
            return self.response_data

        def updateMemo(self, data):
            # 更新備註
            path = '/RedEnvelopeManagement/UpdateMemo'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def suspendActivity(self, data):
            # 立即中止紅包
            path = '/RedEnvelopeManagement/SuspendActivity'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def revoke(self, data):
            # 紅包沖銷
            path = '/RedEnvelopeManagement/Revoke'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

    # 限时优惠
    class TimeLimitedEvent:

        def __init__(self, http):
            self.__http = http
            self.response_data = {}

        def loadNew(self, data):
            # API Name =>限时优惠-取得列表資料
            # body--
            path = '/TimeLimitedEvent/LoadNew'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def getDetail(self, data):
            # API Name =>限时优惠-詳細資料
            # body--
            path = '/TimeLimitedEvent/GetDetail'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def getEventName(self, data):
            # API Name =>限时优惠-取得活動名稱
            # body--
            path = '/TimeLimitedEvent/GetEventName'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def memberJoinListLoadNew(self, data):
            # API Name =>限时优惠-會員參與名單
            # body--
            path = '/TimeLimitedEvent/MemberJoinListLoadNew'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def Create(self, data):
            # API Name =>限时优惠-新增活動
            # body--
            path = '/TimeLimitedEvent/Create'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def eventOff(self, data):
            # 立刻下架
            path = '/TimeLimitedEvent/EventOff'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

    # 幸运转盘
    class LuckyWheelManagement:

        def __init__(self, http):
            self.__http = http
            self.response_data = {}

        def index(self, data):
            # API Name =>活动管理-取得列表頁面
            # body--
            path = '/LuckyWheelManagement/Index'
            self.response_data = self.__http.sendRequest('GET', path, data)
            return self.response_data

        def detail(self, data):
            # API Name =>活动管理-
            # body--
            path = '/LuckyWheelManagement/Detail'
            self.response_data = self.__http.sendRequest('GET', path, data)
            return self.response_data

        def getImage(self, data):
            # 取得入口圖片
            path = '/ActivityManagement/GetImage'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def createAndModify(self, data):
            # API Name =>活动管理-
            # body--
            path = '/LuckyWheelManagement/CreateAndModify'
            self.response_data = self.__http.sendRequest('GET', path, data)
            return self.response_data

        def getEventTimeList(self, data):
            path = '/LuckyWheelManagement/GetEventTimeList'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def preview(self, data):
            # API Name =>活动管理-
            # body--
            path = '/LuckyWheelManagement/Preview'
            self.response_data = self.__http.sendRequest('', path, data)
            return self.response_data

        def rewardRecord(self, data):
            # API Name =>活动管理-
            # body--
            path = '/LuckyWheelManagement/RewardRecord'
            self.response_data = self.__http.sendRequest('GET', path, data)
            return self.response_data

        def serialNumber(self, data):
            # API Name =>活动管理-
            # body--
            path = '/LuckyWheelManagement/SerialNumber'
            self.response_data = self.__http.sendRequest('GET', path, data)
            return self.response_data

        def getEventList(self, data):
            # API Name =>活动管理- 取得幸運輪盤活動列表
            # body--/{filters}
            path = '/LuckyWheelManagement/GetEventList'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def uploadRewardImage(self, data):
            # API Name =>活动管理- 上傳幸運輪盤獎項圖片
            # body--/{imageFile}
            path = '/LuckyWheelManagement/UploadRewardImage'
            self.response_data = self.__http.sendRequestForUploadFile(path, data)
            return self.response_data

        def createNewEvent(self, data):
            # API Name =>活动管理-
            # body--/{request}
            path = '/LuckyWheelManagement/CreateNewEvent'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def getEventDetail(self, data):
            # API Name =>活动管理-
            # body--/{eventID}
            path = '/LuckyWheelManagement/GetEventDetail'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def deleteEvent(self, data):
            # API Name =>活动管理-
            # body--/{eventID}
            path = '/LuckyWheelManagement/DeleteEvent'
            self.response_data = self.__http.sendRequest('', path, data)
            return self.response_data

        def updateEvent(self, data):
            # API Name =>活动管理-
            # body--/{request}
            path = '/LuckyWheelManagement/UpdateEvent'
            self.response_data = self.__http.sendRequest('', path, data)
            return self.response_data

        def getRewardRecord(self, data):
            # API Name =>活动管理-
            # body--/{request}
            path = '/LuckyWheelManagement/GetRewardRecord'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def getRewardStatistics(self, data):
            # API Name =>活动管理-
            # body--/{eventID}
            path = '/LuckyWheelManagement/GetRewardStatistics'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def createSerialNumber(self, data):
            # API Name =>活动管理-
            # body--/{request}
            path = '/LuckyWheelManagement/CreateSerialNumber'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def getSerialNumberList(self, data):
            # API Name =>活动管理-
            # body--/{eventID}
            path = '/LuckyWheelManagement/GetSerialNumberList'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def sendRewards(self, data):
            # API Name =>活动管理-
            # body--/{eventID}/{recordIDs}
            path = '/LuckyWheelManagement/SendRewards'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def getEventTypeList(self, data):
            # API Name =>活动管理-
            # body--
            path = '/LuckyWheelManagement/GetEventTypeList'
            self.response_data = self.__http.sendRequest('', path, data)
            return self.response_data

        def getRewardTypeList(self, data):
            # API Name =>活动管理-
            # body--
            path = '/LuckyWheelManagement/GetRewardTypeList'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def getRuleTypeList(self, data):
            # API Name =>活动管理-
            # body--
            path = '/LuckyWheelManagement/GetRuleTypeList'
            self.response_data = self.__http.sendRequest('', path, data)
            return self.response_data

        def getPortalUrl(self, data):
            # API Name =>活动管理-
            # body--
            path = '/LuckyWheelManagement/GetPortalUrl'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def checkEventDateTimeDuplicated(self, data):
            # API Name =>活动管理-
            # body--/{request}
            path = '/LuckyWheelManagement/CheckEventDateTimeDuplicated'
            self.response_data = self.__http.sendRequest('', path, data)
            return self.response_data

        def exportExcel(self, data):
            # 匯出序號管理名單
            path = '/LuckyWheelManagement/ExportExcel'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def eventOff(self, data):
            # 立即下架
            path = '/LuckyWheelManagement/EventOff'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

    # 签到奖励
    class CheckInEvent:

        def __init__(self, http):
            self.__http = http
            self.response_data = {}

        def loadNew(self, data):
            # API Name =>签到奖励-取得列表資料
            # body--{take}/{skip}/{query}/{connectionId}
            path = '/CheckInOffer/LoadNew'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def Create(self, data):
            # API Name =>签到奖励-取得列表資料
            # body--
            path = '/CheckInOffer/Create'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def GetEventTimeList(self, data):
            # API Name =>签到奖励-取得活動列表時間
            # body--{}
            path = '/CheckInOffer/GetEventTimeList'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def EventOff(self, data):
            # API Name =>签到奖励-活動下架
            # body--{}
            path = '/CheckinOffer/EventOff'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def UploadImage(self, data):
            # API Name =>签到奖励-活動圖片
            # body--{}
            path = '/CheckInOffer/UploadImage'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def AllAvailableMemberLevelSetting(self, data):
            # API Name =>签到奖励-取得所有可用的會員級別設置
            # body--{}
            path = '/CheckInOffer/AllAvailableMemberLevelSetting'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def GetDetail(self, data):
            # API Name =>签到奖励-取得所有可用的會員級別設置
            # body--/{ID}
            path = '/CheckInOffer/GetDetail'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def Update(self, data):
            # API Name =>签到奖励-修改未開始活動
            # body--/{ID}
            path = '/CheckInOffer/Update'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

    # 任务挑战
    class MissionReward:

        def __init__(self, http):
            self.__http = http
            self.response_data = {}

        def getList(self, data):
            # API Name =>任务挑战-取得列表資料
            # body--
            path = '/MissionReward/GetList'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def getConditionType(self, data):
            # API Name =>任务挑战-任務類型
            # body--
            path = '/MissionReward/GetConditionType'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def uploadImage(self, data):
            # API Name =>任务挑战-上傳圖片
            # body--
            path = '/MissionReward/UploadImage'
            self.response_data = self.__http.sendRequestForUploadFile(path, data)
            return self.response_data

        def create(self, data):
            # API Name =>任务挑战-新增任務挑戰
            # body--
            path = '/MissionReward/Create'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def getDetail(self, data):
            # API Name =>任务挑战-任務挑戰詳細
            # body--
            path = '/MissionReward/GetDetail'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def updateReceiveBonusLimitTime(self, data):
            # API Name =>任务挑战-更新領獎時間
            # body--
            path = '/MissionReward/UpdateReceiveBonusLimitTime'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def getEventName(self, data):
            # API Name =>任务挑战- 取得活動名稱
            # body--
            path = '/MissionReward/GetEventName'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def getJoinList(self, data):
            # API Name =>任务挑战-取得參與名單
            # body--
            path = '/MissionReward/GetJoinList'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def eventOff(self, data):
            # API Name =>任务挑战-立即下架
            # body--
            path = '/MissionReward/EventOff'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

    # 时来运转
    class NewLuckyWheel:

        def __init__(self, http):
            self.__http = http
            self.response_data = {}

        def getList(self, data):
            # API Name =>时来运转-取得列表資料
            # body--
            path = '/NewLuckyWheel/GetList'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def getImage(self, data):
            # 取得入口圖片
            path = '/ActivityManagement/GetImage'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def uploadImages(self, data):
            # 更新入口圖片
            path = '/ActivityManagement/UploadImage'
            self.response_data = self.__http.sendRequestForUploadFile(path, data)
            return self.response_data

        def updateEntranceImage(self, data):
            # 更新活動入口設定
            path = '/ActivityManagement/UpdateEntranceImage'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def getPortalUrl(self, data):
            # 預覽Portal
            path = '/LuckyWheelManagement/GetPortalUrl'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def getAllLuckyWheelTimeList(self, data):
            # 取得全時來運轉時間列表
            path = '/NewLuckyWheel/GetAllLuckyWheelTimeList'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def getRewardTypeList(self, data):
            # 取得獎勵列表
            path = '/NewLuckyWheel/GetRewardTypeList'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def uploadRewardImage(self, data):
            # 上傳獎項圖片
            path = 'NewLuckyWheel/UploadRewardImage'
            self.response_data = self.__http.sendRequestForUploadFile(path, data)
            return self.response_data

        def create(self, data):
            # 新增時來運轉
            path = '/NewLuckyWheel/Create'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def getDetail(self, data):
            # 取得時來運轉詳細資料
            path = '/NewLuckyWheel/GetDetail'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def modifyLuckyWheelInfo(self, data):
            # 修改時來運轉資料
            path = '/NewLuckyWheel/ModifyLuckyWheelInfo'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def luckyWheelOff(self, data):
            # 立即下架
            path = '/NewLuckyWheel/LuckyWheelOff'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def joinMemberDetailList(self, data):
            # 剩餘抽獎次數名單
            path = '/NewLuckyWheel/JoinMemberDetailList'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def exportMemberLuckyDrawCount(self, data):
            # 匯出剩餘抽獎次數名單
            path = '/NewLuckyWheel/ExportMemberLuckyDrawCount'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def getNewLuckyWheelName(self, data):
            # 取得時來運轉的名字
            path = '/NewLuckyWheel/GetNewLuckyWheelName'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def get_RewardTypeList(self, data):
            # 取得時來運轉得獎狀態
            path = '/NewLuckyWheel/GetRewardTypeList'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def getRewardRecords(self, data):
            # 取得時來運轉得獎名單
            path = '/NewLuckyWheel/GetRewardRecords'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def getCalculationCount(self, data):
            # 取得時來運轉得獎總計
            path = '/NewLuckyWheel/GetCalculationCount'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def getRewardStatistics(self, data):
            # 取得時來運轉得獎統計
            path = '/NewLuckyWheel/GetRewardStatistics'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def sendRewards(self, data):
            #  派發獎品
            path = '/NewLuckyWheel/SendRewards'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def manualSupply(self, data):
            # 添加次數
            path = '/NewLuckyWheel/ManualSupply'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data

        def modifyShowRewardRecord(self, data):
            # 中獎人名單開關
            path = '/NewLuckyWheel/ModifyShowRewardRecord'
            self.response_data = self.__http.sendRequest('POST', path, data)
            return self.response_data


# 封锁名单管理

class BlockListManagement(object):
    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def bankAccountGetList(self, data):
        # 封鎖名單管理-取得銀行帳戶列表
        path = '/BankAccountBlockManagement/GetList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def bankAccountGetGroupBank(self, data):
        # 封鎖名單管理-取得銀行列表
        path = '/BankAccountBlockManagement/GetGroupBank'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def bankAccountExportExcel(self, data):
        # 封鎖名單管理-匯出銀行封鎖名單Excel
        path = '/BankAccountBlockManagement/ExportExcel'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def bankAccountAddBankAccountBlockInfo(self, data):
        # 封鎖名單管理-新增銀行帳戶封鎖名單
        path = '/BankAccountBlockManagement/AddBankAccountBlockInfo'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def bankAccountDeleteBankBlocks(self, data):
        # 封鎖名單管理-刪除銀行帳戶封鎖名單
        path = '/BankAccountBlockManagement/DeleteBankBlocks'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def bankAccountDownloadSampleExcel(self, data):
        # 封鎖名單管理-下載銀行帳戶匯入範本
        path = '/BankAccountBlockManagement/DownloadSampleExcel'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def bankAccountCheckImportExcel(self, data):
        # 封鎖名單管理-檢查銀行帳戶匯入範本上傳
        path = '/BankAccountBlockManagement/CheckImportExcel'
        self.response_data = self.__http.sendRequestForUploadFile(path, data)
        return self.response_data

    def bankAccountImportExcel(self, data):
        # 封鎖名單管理-銀行帳戶匯入範本上傳
        path = '/BankAccountBlockManagement/ImportExcel'
        self.response_data = self.__http.sendRequestForUploadFile(path, data)
        return self.response_data

    def ipGetList(self, data):
        # 封鎖名單管理-取得IP列表
        path = '/IPBlockManagement/GetList'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def ipExportExcel(self, data):
        # 封鎖名單管理-匯出IP封鎖名單Excel
        path = '/IPBlockManagement/ExportExcel'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def ipAddIPBlockInfo(self, data):
        # 封鎖名單管理-新增IP封鎖名單
        path = '/IPBlockManagement/AddIPBlockInfo'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def ipDeleteIPBlocks(self, data):
        # 封鎖名單管理-刪除IP封鎖名單
        path = '/IPBlockManagement/DeleteIPBlocks'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def ipCheckImportExcel(self, data):
        # 封鎖名單管理-檢查IP匯入範本上傳
        path = '/IPBlockManagement/CheckImportExcel'
        self.response_data = self.__http.sendRequestForUploadFile(path, data)
        return self.response_data

    def ipImportExcel(self, data):
        # 封鎖名單管理-IP匯入範本上傳
        path = '/IPBlockManagement/ImportExcel'
        self.response_data = self.__http.sendRequestForUploadFile(path, data)
        return self.response_data

    def getCountrySetting(self, data):
        # 封鎖名單管理-取得國別阻擋名單
        path = '/CountryBlockManagement/GetCountrySetting'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def getWhiteListSetting(self, data):
        # 封鎖名單管理-取得白名單IP名單
        path = '/CountryBlockManagement/GetWhiteListSetting'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateCountryBlockSetting(self, data):
        # 封鎖名單管理-更新國別阻擋名單
        path = '/CountryBlockManagement/UpdateCountryBlockSetting'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def checkWhiteIpWhenAdd(self, data):
        # 封鎖名單管理-檢查新增白名單IP
        path = '/CountryBlockManagement/CheckWhiteIpWhenAdd'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data

    def updateWhiteListSetting(self, data):
        # 封鎖名單管理-更新白名單IP
        path = '/CountryBlockManagement/UpdateWhiteListSetting'
        self.response_data = self.__http.sendRequest('POST', path, data)
        return self.response_data


# MyMine 金流设置
class MyMine(object):

    def __init__(self, http):
        self.__http = http
        self.response_data = {}

    def getOrderInfos(self, data):
        # API Name =>MyMine 金流设置 -
        # body--
        path = '/MyMine/GetOrderInfos'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def getMonthOrderInfo(self, data):
        # API Name =>MyMine 金流设置 -
        # body--/{input}
        path = '/MyMine/GetMonthOrderInfo'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def getDayOrderInfo(self, data):
        # API Name =>MyMine 金流设置 -
        # body--/{input}
        path = '/MyMine/GetDayOrderInfo'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def getLastSixMonthOrderInfo(self, data):
        # API Name =>MyMine 金流设置 -
        # body--/{input}
        path = '/MyMine/GetLastSixMonthOrderInfo'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def getGpkMerchant(self, data):
        # API Name =>MyMine 金流设置 -
        # body--/{input}
        path = '/MyMine/GetGpkMerchant'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data

    def uploadDocument(self, data):
        # API Name =>MyMine 金流设置 -
        # body--/{file}
        path = '/MyMine/UploadDocument'
        self.response_data = self.__http.sendRequest('', path, data)
        return self.response_data
