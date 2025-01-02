import calendar
from datetime import date, datetime

from dateutil.relativedelta import relativedelta

from newAutomationFrameWorkPytest.pages.navigation import Navigation
from newAutomationFrameWorkPytest.utility.TestingUtil import TestingUtil


class PageObjectsUI(object):
    def __init__(self, driver):
        self.navigation = Navigation(driver)
        self.testingUtil = TestingUtil()
        # Date stuff
        today = date.today()
        NEXT_MONTH = (datetime.today() + relativedelta(months=1))
        NEXT_TWO_MONTH = (datetime.today() + relativedelta(months=2))
        LAST_MONTH = (datetime.today() + relativedelta(months=-1))

        self.year = today.year
        self.month = today.month
        self.nextMonth = NEXT_MONTH.strftime("%m")
        self.nextTwoMonth = NEXT_TWO_MONTH.strftime("%m")
        self.lastMonth = LAST_MONTH.strftime("%m")
        self.monthShort = today.strftime("%b")
        self.nextMonthShort = NEXT_MONTH.strftime("%b")
        self.nextTwoMonthShort = NEXT_TWO_MONTH.strftime("%b")
        self.lastMonthShort = LAST_MONTH.strftime("%b")
        self.monthLong = today.strftime("%B")
        self.nextMonthLong = NEXT_MONTH.strftime("%B")
        self.nextTwoMonthLong = NEXT_TWO_MONTH.strftime("%B")
        self.lastMonthLong = LAST_MONTH.strftime("%B")
        self.endOfMonth = calendar.monthrange(self.year, int(self.month))[1]
        self.endOfNextMonth = calendar.monthrange(self.year, int(self.nextMonth))[1]
        self.endOfNextTwoMonth = calendar.monthrange(self.year, int(self.nextTwoMonth))[1]
        self.endOfLastMonth = calendar.monthrange(self.year, int(self.lastMonth))[1]

        # the year of the next month; not simply year + 1
        # July --> Aug the nextMonthYear should be equal to self.year but Dec --> Jan nextMonthYear should be "self.year + 1"
        self.nextMonthsYear = NEXT_MONTH.year
        self.nextTwoMonthsYear = NEXT_TWO_MONTH.year