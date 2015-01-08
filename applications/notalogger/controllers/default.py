'''
NotaLogger: Notarization Code Generator and Logging Service

Date created: 4th August 2013
Created by: Maurice Ling <mauriceling@acm.org>
License: General Public License version 3
'''
import time
import random

import ntplib

from gluon.tools import Service
service = Service(globals())
def call(): return service()

@service.xmlrpc
@service.jsonrpc
def new_notarization(name, pidentifier, email, usage, comments, length=20):
    '''
    XMLRPC or JSONRPC based generation of notarization code.
    
    Example for XMLRPC:
    >>> from xmlrpclib import ServerProxy
    >>> s = ServerProxy('http://ml-lab.bioinformatics.org/init/plugin_notalogger/call/xmlrpc')
    >>> notarizecode = s.new_notarization('xmlrpc test', 'xmlrpc test', 'xmlrpc test', 
                                          'xmlrpc test', 'xmlrpc test', 20)
    '''
    notarizecode = generate_code(length)
    comments = 'RPC notarization | ' + comments
    notalogger_db.logger.insert(notarizecode=notarizecode,
                                name=name,
                                pidentifier=pidentifier,
                                email=email,
                                usage=usage,
                                comments=comments,
                                datetimeserver='Local server',
                                seconds_since_epoch=str(time.time()))
    notalogger_db.commit()
    return notarizecode


def generate_code(length=20):
    '''
    Generate notarization code of specific length.
    '''
    mapping = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A',
               'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
               'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'd', 'e', 'g',
               'h', 'q', 'r', '=', '#', '$', '%', '&', '@']
    code = [random.choice(mapping) for i in range(length)]
    return ''.join(code)


def index():
    '''
    Creates a form for generating a new notarization code, and insert a record
    into database.
    Calls notarization_output function to show notarization code.
    '''
    form = FORM(TABLE(
                TR('Name(*):', INPUT(_type='text', _name='name', _size=80,
                                  requires=IS_NOT_EMPTY())),
                TR('Personal Identifier:', INPUT(_type='text', _name='pid', _size=80)),
                TR('Email Address:', INPUT(_type='text', _name='email', _size=80)),
                TR('Code Length(*):', INPUT(_type='text', _name='clength', _size=10,
                                         requires=IS_NOT_EMPTY())),
                TR('Usage(*):', TEXTAREA(_type='text', _name='usage', 
                                      requires=IS_NOT_EMPTY())),
                TR('Other Comments:', TEXTAREA(_type='text', _name='comments')),
                TR('', INPUT(_type='submit', _name='submit'))))
    form.vars.clength = 20
    if form.accepts(request.vars, session):
        if int(form.vars.clength) < 5: form.vars.clength = 5
        session.notacode = generate_code(int(form.vars.clength))
        session.epoch = str(time.time())
        session.name = form.vars.name
        session.pidentifier = form.vars.pid
        session.clength = form.vars.clength
        session.email = form.vars.email
        session.usage = form.vars.usage
        session.comments = form.vars.comments
        notalogger_db.logger.insert(notarizecode=session.notacode,
                                    name=session.name,
                                    pidentifier=session.pidentifier,
                                    email=session.email,
                                    usage=session.usage,
                                    comments=session.comments,
                                    datetimeserver='Local server',
                                    seconds_since_epoch=session.epoch)
        redirect(URL(r=request, f='notarization_output'))
    return dict(form=form)


def notarization_output():
    '''
    Called by index function to display newly generated notarization code, 
    and other details.
    '''
    return dict(results=session)


def search():
    '''
    Creates a form for users to search for details pertaining to an existing 
    notarization code. 
    Using this search function will trigger ntp_logging function to insert 
    a NIST Internet Time Server timestamp record into the database. In addition,
    the search will be logged as a record.
    '''
    form = FORM(TABLE(
                TR('Notarization Code(*):', 
                    INPUT(_type='text', _name='code', _size=60, 
                          requires=IS_LENGTH(minsize=5))),
                TR('Purpose of Search(*):',
                    TEXTAREA(_type='text', _name='usage', requires=IS_NOT_EMPTY()),
                    INPUT(_type='submit', _name='submit'))))
    if form.accepts(request.vars, session):
        try: ntp_logging()
        except: pass
        session.code = form.vars.code
        session.result = [x 
                          for x in notalogger_db(
                              notalogger_db.logger.notarizecode.like('%' + \
                              form.vars.code + '%')).select()]
        session.count = len(session.result)
        results = ['Number of codes found: ' + str(session.count)] + \
                  [str(x.notarizecode) for x in session.result]
        results = ' | '.join(results)
        usage = 'Search form usage | Purpose: ' + form.vars.usage
        notalogger_db.logger.insert(notarizecode='',
                                    name='',
                                    pidentifier='',
                                    email='',
                                    usage=usage,
                                    comments=results,
                                    datetimeserver='Local server',
                                    seconds_since_epoch=str(time.time()))
        redirect(URL(r=request, f='search_output'))
    return dict(form=form)
    
  
def search_output():
    '''
    Called by search function to display details pertaining to an existing 
    notarization code. 
    '''
    #if len(session.count) > 50:
    #    session.result = session.result[:50]
    return dict(results=session)
    

@service.xmlrpc
@service.jsonrpc    
def ntp_logging():
    '''
    Compute a timestamp using NIST Internet Time Servers as an additional 
    level of assurance for database. This function is called by search 
    function or can be called via XML or JSON remote procedure calls.
    
    Example for XMLRPC:
    >>> from xmlrpclib import ServerProxy
    >>> s = ServerProxy('http://ml-lab.bioinformatics.org/init/plugin_notalogger/call/xmlrpc')
    >>> s.ntp_logging()
    '''
    ntp_pool = ['asia.pool.ntp.org',
                'europe.pool.ntp.org',
                'oceania.pool.ntp.org',
                'north-america.pool.ntp.org',
                'south-america.pool.ntp.org',
                'africa.pool.ntp.org']
    client = ntplib.NTPClient()
    server = random.choice(ntp_pool)
    response = client.request(server, version=3)
    try:
        results = ['Network time server: ' + server,
                   'Offset : %f' % response.offset,
                   'Stratum : %s (%d)' % (ntplib.stratum_to_text(response.stratum),
                                          response.stratum),
                   'Precision : %d' % response.precision,
                   'Root delay : %f ' % response.root_delay,
                   'Root dispersion : %f' % response.root_dispersion,
                   'Delay : %f' % response.delay,
                   'Leap indicator : %s (%d)' % (ntplib.leap_to_text(response.leap),
                                                 response.leap),
                   'Poll : %d' % response.poll,
                   'Mode : %s (%d)' % (ntplib.mode_to_text(response.mode),
                                       response.mode),
                   'Reference clock identifier : ' + \
                                        ntplib.ref_id_to_text(response.ref_id,
                                        response.stratum),
                   'Original timestamp : ' + time.ctime(response.orig_time),
                   'Receive timestamp : ' + time.ctime(response.recv_time),
                   'Transmit timestamp : ' + time.ctime(response.tx_time),
                   'Destination timestamp : ' + time.ctime(response.dest_time)]
        results = ' | '.join(results)
    except:
        results = 'Failure to connect to network time server or there is \
        an internet error. Please try again later.'
    notalogger_db.logger.insert(notarizecode='',
                                name='',
                                pidentifier='',
                                email='',
                                usage='NTP pool server time check',
                                comments=results,
                                datetimeserver=str(server),
                                seconds_since_epoch=str(time.time()))
    notalogger_db.commit()
