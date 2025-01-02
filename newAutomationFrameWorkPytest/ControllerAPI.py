import calendar
from datetime import date
from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta

from newAutomationFrameWorkPytest.apiModules.API_Mock import APIMock
from newAutomationFrameWorkPytest.apiModules.client import ApiClient
from newAutomationFrameWorkPytest.utility.TestingUtil import TestingUtil


class ControllerAPI(object):
    def __init__(self, api_client: ApiClient):
        self.client = api_client
        self.testUtil = TestingUtil()
        self.apiMock = APIMock(api_client)

        NEXT_MONTH = (datetime.today() + relativedelta(months=1))
        NEXT_TWO_MONTH = (datetime.today() + relativedelta(months=2))
        LAST_MONTH = (datetime.today() + relativedelta(months=-1))
        LAST_TWO_MONTH = (datetime.today() + relativedelta(months=-2))

        # Date stuff
        self.today = date.today()
        self.utcnowPreviousDay = (datetime.utcnow() + relativedelta(days=-1)).strftime("%Y-%m-%dT%H:%M:%SZ")
        self.utcnow = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        self.utcnowEndDate = (datetime.utcnow() + relativedelta(days=2)).strftime("%Y-%m-%dT%H:%M:%SZ")
        self.year = self.today.year
        self.lastYear = self.year - 1
        self.lastTwoYears = self.year - 2
        self.month = self.today.strftime("%m")
        self.day = self.today.strftime("%d")
        self.nextMonth = NEXT_MONTH.strftime("%m")
        self.nextMonthYear = NEXT_MONTH.strftime("%m%Y")
        self.nextTwoMonth = NEXT_TWO_MONTH.strftime("%m")
        self.lastMonth = LAST_MONTH.strftime("%m")
        self.lastMonthName = LAST_MONTH.strftime("%B")
        self.lastTwoMonth = LAST_TWO_MONTH.strftime("%m")
        self.lastTwoMonthName = LAST_TWO_MONTH.strftime("%B")
        self.lastMonthYear = LAST_MONTH.strftime("%m%Y")
        self.lastMonthYearOnly = LAST_MONTH.strftime("%Y")
        self.monthShort = self.today.strftime("%b")
        self.nextMonthShort = NEXT_MONTH.strftime("%b")
        self.nextTwoMonthShort = NEXT_TWO_MONTH.strftime("%b")
        self.lastMonthShort = LAST_MONTH.strftime("%b")
        self.monthLong = self.today.strftime("%B")
        self.nextMonthLong = NEXT_MONTH.strftime("%B")
        self.nextTwoMonthLong = NEXT_TWO_MONTH.strftime("%B")
        self.lastMonthLong = LAST_MONTH.strftime("%B")
        self.lastTwoMonthLong = LAST_TWO_MONTH.strftime("%B")
        self.endOfMonth = calendar.monthrange(self.year, int(self.month))[1]
        self.endOfNextMonth = calendar.monthrange(self.year, int(self.nextMonth))[1]
        self.endOfNextTwoMonth = calendar.monthrange(self.year, int(self.nextTwoMonth))[1]
        self.endOfLastMonth = calendar.monthrange(self.year, int(self.lastMonth))[1]
        self.utcLastMonth = (datetime.utcnow() + relativedelta(months=-1)).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
        self.activateDate = (datetime.utcnow() + relativedelta(months=-1)).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]
        self.activateDateTwoMonths = (datetime.utcnow() + relativedelta(months=-2)).strftime("%Y-%m-%dT%H:%M:%S.%f")[
                                     :-3]
        self.activateDateThreeMonthsBack = (datetime.utcnow() + relativedelta(months=-3)).strftime(
            "%Y-%m-%dT%H:%M:%S.%f")[:-3]
        self.activateDateOneYearBack = (datetime.utcnow() + relativedelta(months=-12)).strftime(
            "%Y-%m-%dT%H:%M:%S.%f")[:-3]
        self.activateDateTwoYearsBack = (datetime.utcnow() + relativedelta(months=-24)).strftime(
            "%Y-%m-%dT%H:%M:%S.%f")[:-3]
        self.lastMonthLastYear = (str(self.lastMonth) + str(self.lastYear))  # ex. format is 082023
        self.lastMonthTextCurrentYear = str(
            (self.today - relativedelta(months=1)).strftime("%B %Y"))  # ex. format is August 2023
        self.twoMonthsPast = self.today - relativedelta(months=2)
        self.threeMonthsPast = self.today - relativedelta(months=3)
        self.twoMonthsPastMonthYear = self.twoMonthsPast.strftime("%m%Y")
        self.threeMonthsPastMonthYear = self.threeMonthsPast.strftime("%m%Y")
        self.oneMonthPast = self.today - relativedelta(months=1)
        self.oneMonthPastMonthYear = self.oneMonthPast.strftime("%m%Y")
        self.currentMonthYear = self.today.strftime("%B - %Y")
        self.currentMonthYearMMYYYY = self.today.strftime("%m%Y")
        self.currentMonthName = self.today.strftime("%B")
        self.firstMonthCurrentYearMMYYYY = ("01" + str(self.year))
        self.lastMonthCurrentYearMMYYYY = ("12" + str(self.year))
        self.firstMonthLastYearMMYYYY = ("01" + str(self.lastYear))
        self.lastMonthLastYearMMYYYY = ("12" + str(self.lastYear))

        # the year of the next month; not simply year + 1
        # July --> Aug the nextMonthYear should be equal to self.year but Dec --> Jan nextMonthYear should be "self.year + 1"
        self.nextMonthsYear = NEXT_MONTH.year
        self.nextTwoMonthsYear = NEXT_TWO_MONTH.year
        self.get_last_month = date.today() + relativedelta(months=-1)
        self.start_date = datetime.strptime('2022-01-01', '%Y-%m-%d').date()
