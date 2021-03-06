
import pymongo
from QUANTAXIS.QAUtil import (DATABASE, QA_util_getBetweenQuarter, QA_util_log_info, QA_util_add_months,
                              QA_util_to_json_from_pandas, QA_util_today_str,QA_util_get_pre_trade_date,
                              QA_util_datetime_to_strdate)
from QUANTTOOLS.QAStockETL.QAFetch import QA_fetch_get_stock_indicator
from QUANTAXIS.QAFetch.QAQuery_Advance import QA_fetch_stock_list_adv

def QA_SU_save_stock_technical_index_day(START_DATE=None,END_DATE=None,client=DATABASE, ui_log = None, ui_progress = None):
    '''
     save stock_day
    计算技术指标
    历史全部数据
    :return:
    '''
    if START_DATE == None:
        if END_DATE == None:
            END_DATE = QA_util_today_str()
            START_DATE = QA_util_get_pre_trade_date(QA_util_today_str(),3)
        else:
            START_DATE = QA_util_get_pre_trade_date(END_DATE,3)
    else:
        START_DATE = QA_util_get_pre_trade_date(START_DATE,3)
        if END_DATE == None:
            END_DATE = QA_util_today_str()
    codes = list(QA_fetch_stock_list_adv()['code'])

    stock_technical_index = client.stock_technical_index
    stock_technical_index.create_index([("code", pymongo.ASCENDING),("date_stamp", pymongo.ASCENDING)], unique=True)
    err = []

    def __saving_work(code,START_DATE,END_DATE, stock_technical_index):
        try:
            QA_util_log_info(
                '##JOB01 Now Saving stock_technical_index from {START_DATE} to {END_DATE} ==== {code}'.format(code=str(code),START_DATE=START_DATE,END_DATE=END_DATE), ui_log)
            data = QA_fetch_get_stock_indicator(code, START_DATE, END_DATE,'day').set_index(['date','code']).dropna(how='all').reset_index()
            stock_technical_index.insert_many(QA_util_to_json_from_pandas(
                data), ordered=False)
        except Exception as error0:
            print(error0)
            err.append(str(code))

    for item in codes:

        QA_util_log_info('The {} of Total {}'.format
                         ((codes.index(item) +1), len(codes)))

        strProgressToLog = 'DOWNLOAD PROGRESS {}'.format(str(float((codes.index(item) +1) / len(codes) * 100))[0:4] + '%', ui_log)
        intProgressToLog = int(float((codes.index(item) +1) / len(codes) * 100))
        QA_util_log_info(strProgressToLog, ui_log= ui_log, ui_progress= ui_progress, ui_progress_int_value= intProgressToLog)

        __saving_work( item,START_DATE,END_DATE, stock_technical_index)

    if len(err) < 1:
        QA_util_log_info('SUCCESS save stock_technical_index ^_^',  ui_log)
    else:
        QA_util_log_info(' ERROR CODE \n ',  ui_log)
        QA_util_log_info(err, ui_log)


def QA_SU_save_stock_technical_index_his(START_DATE=None,END_DATE=None,client=DATABASE, ui_log = None, ui_progress = None):

    '''
     save stock_day
    计算技术指标
    历史全部数据
    :return:
    '''
    if START_DATE == None:
        if END_DATE == None:
            END_DATE = QA_util_today_str()
            START_DATE = "2006-01-01"
        else:
            START_DATE = QA_util_get_pre_trade_date(END_DATE,3)
    else:
        START_DATE = QA_util_get_pre_trade_date(START_DATE,3)
        if END_DATE == None:
            END_DATE = QA_util_today_str()

    codes = list(QA_fetch_stock_list_adv()['code'])

    stock_technical_index = client.stock_technical_index
    stock_technical_index.create_index([("code", pymongo.ASCENDING),("date_stamp", pymongo.ASCENDING)], unique=True)
    err = []

    def __saving_work(code,START_DATE,END_DATE, stock_technical_index):
        try:
            QA_util_log_info(
                '##JOB01 Now Saving stock_technical_index from {START_DATE} to {END_DATE} ==== {code}'.format(code=str(code),START_DATE=START_DATE,END_DATE=END_DATE), ui_log)
            data = QA_fetch_get_stock_indicator(code, START_DATE, END_DATE).set_index(['date','code']).dropna(how='all').reset_index()
            stock_technical_index.insert_many(QA_util_to_json_from_pandas(
                data), ordered=False)
        except Exception as error0:
            print(error0)
            err.append(str(code))

    for item in codes:

        QA_util_log_info('The {} of Total {}'.format
                         ((codes.index(item) +1), len(codes)))

        strProgressToLog = 'DOWNLOAD PROGRESS {}'.format(str(float((codes.index(item) +1) / len(codes) * 100))[0:4] + '%', ui_log)
        intProgressToLog = int(float((codes.index(item) +1) / len(codes) * 100))
        QA_util_log_info(strProgressToLog, ui_log= ui_log, ui_progress= ui_progress, ui_progress_int_value= intProgressToLog)

        __saving_work( item,START_DATE,END_DATE, stock_technical_index)

    if len(err) < 1:
        QA_util_log_info('SUCCESS save stock_technical_index ^_^',  ui_log)
    else:
        QA_util_log_info(' ERROR CODE \n ',  ui_log)
        QA_util_log_info(err, ui_log)

def QA_SU_save_stock_technical_week_day(START_DATE=None,END_DATE=None,client=DATABASE, ui_log = None, ui_progress = None):
    '''
     save stock_day
    计算技术指标
    历史全部数据
    :return:
    '''
    if START_DATE == None:
        if END_DATE == None:
            END_DATE = QA_util_today_str()
            START_DATE = QA_util_get_pre_trade_date(QA_util_today_str(),3)
        else:
            START_DATE = QA_util_get_pre_trade_date(END_DATE,3)
    else:
        START_DATE = QA_util_get_pre_trade_date(START_DATE,3)
        if END_DATE == None:
            END_DATE = QA_util_today_str()
    codes = list(QA_fetch_stock_list_adv()['code'])

    stock_technical_week = client.stock_technical_week
    stock_technical_week.create_index([("code", pymongo.ASCENDING),("date_stamp", pymongo.ASCENDING)], unique=True)
    err = []

    def __saving_work(code,START_DATE,END_DATE, stock_technical_week):
        try:
            QA_util_log_info(
                '##JOB01 Now Saving stock_technical_week from {START_DATE} to {END_DATE} ==== {code}'.format(code=str(code),START_DATE=START_DATE,END_DATE=END_DATE), ui_log)
            data = QA_fetch_get_stock_indicator(code, START_DATE, END_DATE, type='week').set_index(['date','code']).dropna(how='all').reset_index()
            stock_technical_week.insert_many(QA_util_to_json_from_pandas(
                data), ordered=False)
        except Exception as error0:
            print(error0)
            err.append(str(code))

    for item in codes:

        QA_util_log_info('The {} of Total {}'.format
                         ((codes.index(item) +1), len(codes)))

        strProgressToLog = 'DOWNLOAD PROGRESS {}'.format(str(float((codes.index(item) +1) / len(codes) * 100))[0:4] + '%', ui_log)
        intProgressToLog = int(float((codes.index(item) +1) / len(codes) * 100))
        QA_util_log_info(strProgressToLog, ui_log= ui_log, ui_progress= ui_progress, ui_progress_int_value= intProgressToLog)

        __saving_work( item,START_DATE,END_DATE, stock_technical_week)

    if len(err) < 1:
        QA_util_log_info('SUCCESS save stock_technical_week ^_^',  ui_log)
    else:
        QA_util_log_info(' ERROR CODE \n ',  ui_log)
        QA_util_log_info(err, ui_log)


def QA_SU_save_stock_technical_week_his(START_DATE=None,END_DATE=None,client=DATABASE, ui_log = None, ui_progress = None):

    '''
     save stock_day
    计算技术指标
    历史全部数据
    :return:
    '''
    if START_DATE == None:
        if END_DATE == None:
            END_DATE = QA_util_today_str()
            START_DATE = "2006-01-01"
        else:
            START_DATE = QA_util_get_pre_trade_date(END_DATE,3)
    else:
        START_DATE = QA_util_get_pre_trade_date(START_DATE,3)
        if END_DATE == None:
            END_DATE = QA_util_today_str()

    codes = list(QA_fetch_stock_list_adv()['code'])

    stock_technical_week = client.stock_technical_week
    stock_technical_week.create_index([("code", pymongo.ASCENDING),("date_stamp", pymongo.ASCENDING)], unique=True)
    err = []

    def __saving_work(code,START_DATE,END_DATE, stock_technical_week):
        try:
            QA_util_log_info(
                '##JOB01 Now Saving stock_technical_week from {START_DATE} to {END_DATE} ==== {code}'.format(code=str(code),START_DATE=START_DATE,END_DATE=END_DATE), ui_log)
            data = QA_fetch_get_stock_indicator(code, START_DATE, END_DATE, type='week').set_index(['date','code']).dropna(how='all').reset_index()
            stock_technical_week.insert_many(QA_util_to_json_from_pandas(
                data), ordered=False)
        except Exception as error0:
            print(error0)
            err.append(str(code))

    for item in codes:

        QA_util_log_info('The {} of Total {}'.format
                         ((codes.index(item) +1), len(codes)))

        strProgressToLog = 'DOWNLOAD PROGRESS {}'.format(str(float((codes.index(item) +1) / len(codes) * 100))[0:4] + '%', ui_log)
        intProgressToLog = int(float((codes.index(item) +1) / len(codes) * 100))
        QA_util_log_info(strProgressToLog, ui_log= ui_log, ui_progress= ui_progress, ui_progress_int_value= intProgressToLog)

        __saving_work( item,START_DATE,END_DATE, stock_technical_week)

    if len(err) < 1:
        QA_util_log_info('SUCCESS save stock_technical_week ^_^',  ui_log)
    else:
        QA_util_log_info(' ERROR CODE \n ',  ui_log)
        QA_util_log_info(err, ui_log)

def QA_SU_save_stock_technical_month_day(START_DATE=None,END_DATE=None,client=DATABASE, ui_log = None, ui_progress = None):
    '''
     save stock_day
    计算技术指标
    历史全部数据
    :return:
    '''
    if START_DATE == None:
        if END_DATE == None:
            END_DATE = QA_util_today_str()
            START_DATE = QA_util_get_pre_trade_date(QA_util_today_str(),3)
        else:
            START_DATE = QA_util_get_pre_trade_date(END_DATE,3)
    else:
        START_DATE = QA_util_get_pre_trade_date(START_DATE,3)
        if END_DATE == None:
            END_DATE = QA_util_today_str()
    codes = list(QA_fetch_stock_list_adv()['code'])

    stock_technical_month = client.stock_technical_month
    stock_technical_month.create_index([("code", pymongo.ASCENDING),("date_stamp", pymongo.ASCENDING)], unique=True)
    err = []

    def __saving_work(code,START_DATE,END_DATE, stock_technical_month):
        try:
            QA_util_log_info(
                '##JOB01 Now Saving stock_technical_month from {START_DATE} to {END_DATE} ==== {code}'.format(code=str(code),START_DATE=START_DATE,END_DATE=END_DATE), ui_log)
            data = QA_fetch_get_stock_indicator(code, START_DATE, END_DATE, type='month').set_index(['date','code']).dropna(how='all').reset_index()
            stock_technical_month.insert_many(QA_util_to_json_from_pandas(
                data), ordered=False)
        except Exception as error0:
            print(error0)
            err.append(str(code))

    for item in codes:

        QA_util_log_info('The {} of Total {}'.format
                         ((codes.index(item) +1), len(codes)))

        strProgressToLog = 'DOWNLOAD PROGRESS {}'.format(str(float((codes.index(item) +1) / len(codes) * 100))[0:4] + '%', ui_log)
        intProgressToLog = int(float((codes.index(item) +1) / len(codes) * 100))
        QA_util_log_info(strProgressToLog, ui_log= ui_log, ui_progress= ui_progress, ui_progress_int_value= intProgressToLog)

        __saving_work( item,START_DATE,END_DATE, stock_technical_month)

    if len(err) < 1:
        QA_util_log_info('SUCCESS save stock_technical_month ^_^',  ui_log)
    else:
        QA_util_log_info(' ERROR CODE \n ',  ui_log)
        QA_util_log_info(err, ui_log)


def QA_SU_save_stock_technical_month_his(START_DATE=None,END_DATE=None,client=DATABASE, ui_log = None, ui_progress = None):

    '''
     save stock_day
    计算技术指标
    历史全部数据
    :return:
    '''
    if START_DATE == None:
        if END_DATE == None:
            END_DATE = QA_util_today_str()
            START_DATE = "2006-01-01"
        else:
            START_DATE = QA_util_get_pre_trade_date(END_DATE,3)
    else:
        START_DATE = QA_util_get_pre_trade_date(START_DATE,3)
        if END_DATE == None:
            END_DATE = QA_util_today_str()

    codes = list(QA_fetch_stock_list_adv()['code'])

    stock_technical_month = client.stock_technical_month
    stock_technical_month.create_index([("code", pymongo.ASCENDING),("date_stamp", pymongo.ASCENDING)], unique=True)
    err = []

    def __saving_work(code,START_DATE,END_DATE, stock_technical_month):
        try:
            QA_util_log_info(
                '##JOB01 Now Saving stock_technical_month from {START_DATE} to {END_DATE} ==== {code}'.format(code=str(code),START_DATE=START_DATE,END_DATE=END_DATE), ui_log)
            data = QA_fetch_get_stock_indicator(code, START_DATE, END_DATE, type='month').set_index(['date','code']).dropna(how='all').reset_index()
            stock_technical_month.insert_many(QA_util_to_json_from_pandas(
                data), ordered=False)
        except Exception as error0:
            print(error0)
            err.append(str(code))

    for item in codes:

        QA_util_log_info('The {} of Total {}'.format
                         ((codes.index(item) +1), len(codes)))

        strProgressToLog = 'DOWNLOAD PROGRESS {}'.format(str(float((codes.index(item) +1) / len(codes) * 100))[0:4] + '%', ui_log)
        intProgressToLog = int(float((codes.index(item) +1) / len(codes) * 100))
        QA_util_log_info(strProgressToLog, ui_log= ui_log, ui_progress= ui_progress, ui_progress_int_value= intProgressToLog)

        __saving_work( item,START_DATE,END_DATE, stock_technical_month)

    if len(err) < 1:
        QA_util_log_info('SUCCESS save stock_technical_month ^_^',  ui_log)
    else:
        QA_util_log_info(' ERROR CODE \n ',  ui_log)
        QA_util_log_info(err, ui_log)