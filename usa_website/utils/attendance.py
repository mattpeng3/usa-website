# -*- coding: utf-8 -*-
#Get authentication to use google API
import httplib2
import os
from googleapiclient.discovery import build

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

#from multiprocessing import Pool
from cachetools import cached, TTLCache
cacheHeaders = TTLCache(maxsize=9, ttl=172800)
cacheSIDs = TTLCache(maxsize=150, ttl=172800)

#Full code takes about 6 seconds TODO: See if we can lower that

try:
    import argparse
    flags = tools.argparser.parse_args([])
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
#change bleow to /usa_website/utils/client_secret.json when testing
CLIENT_SECRET_LOC = '/home/u/ug/ugradsa/usa-website/src/usa_website/utils/client_secret.json'
APPLICATION_NAME = 'SusaClient'
REDIRECT_URI = 'https://susa.berkeley.edu/attendance.html'
#You wouldn't steal a car would you? So please don't steal our credentials! Thanks!

def get_credentials():
    #change following line to /usa_website/utils when testing
    HOME_DIR = '/home/u/ug/ugradsa/usa-website/src/usa_website/utils/'
    #HOME_DIR = './usa_website/utils'
    credential_dir = os.path.join(HOME_DIR, '.credentials')
    http = httplib2.Http(cache=".cache")
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'credentials.json')
    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_LOC, SCOPES)
        flow.params['access_type'] = 'offline'
        flow.params['approval_prompt'] = 'force'
        flow.params['redirect_uri'] = REDIRECT_URI
        print(flow.params['access_type'])
        if flags:
            credentials = tools.run_flow(flow, store, flags)
    return credentials

@cached(cacheHeaders)
def GetAttendanceHeader(SID):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = build('sheets', 'v4', http)
    SPREADSHEET_ID = '1dnLK86wVXIvtJ5sOPUgPKkDRap6IG11q8ZqUXvixmAE'
    range='A1:I1'
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=range).execute()
    values=result.get('values', [])
    flat_values = [item for sublist in values for item in sublist]
    return(flat_values)

@cached(cacheSIDs)
def LookupSIDs():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = build('sheets', 'v4', http)
    SPREADSHEET_ID = '1dnLK86wVXIvtJ5sOPUgPKkDRap6IG11q8ZqUXvixmAE'
    range='C2:C148'
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=range).execute()
    values=result.get('values', [])
    print("lookup called")
    return values

def GetAttendanceDetails(SID, values):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = build('sheets', 'v4', http)
    SPREADSHEET_ID = '1dnLK86wVXIvtJ5sOPUgPKkDRap6IG11q8ZqUXvixmAE'
    icounter = 0
    flat_values = [item for sublist in values for item in sublist]
    for i,val in enumerate(flat_values):
        if SID == val:
            icounter = i + 2 #account for python index starting at 0 and SIDs starting at row 2
    if icounter <= 1:
        return(1)
    else:
        new_range='A'+ str(icounter) + ':I' + str(icounter)
        print(new_range)
        new_result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=new_range).execute()
        new_values=new_result.get('values', [])
        alph = ['A','B','C','D','E','F','G','H','I']
        new_flat_values = [item for sublist in new_values for item in sublist]
        final_values = [x or '0' for x in new_flat_values]
        i = len(alph) - len(final_values)
        while i > 0:
            final_values.append(0)
            i=i-1
        print(final_values)
        print(new_range)
        print(new_result)
        return(final_values)
