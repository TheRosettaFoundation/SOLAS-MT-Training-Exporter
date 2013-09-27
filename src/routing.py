#!/usr/bin/python

from bottle import route, run, template, request, response
from database import baseXDB 

def createHeaders ():
  response.set_header('Access-Control-Allow-Origin', '*')
  response.set_header('Access-Control-Allow-Headers', 'Content-Type')
  response.set_header('Access-Control-Allow-Methods' ,'GET, POST, PUT, DELETE')

## Returns all databases names
@route('/dbs/', method='GET')
def showDatabases():
    createHeaders ()
    dataStore = baseXDB()
    return dataStore.queryDB("""xquery let $list :=db:list-details()
                            return <dbs>
                                {
                                    for $x in $list
                                    return <db id='{data($x)}'/>
                                }
                            </dbs>""")
    ##return dataStore.queryDB("list")

## Returns all document id's in a specific database
@route('/dbs/<dbName>/', method='GET')
def showDocumentIds(dbName):
    createHeaders ()
    dataStore = baseXDB()
    dataStore.setDatabase(dbName)
    return dataStore.queryDB("""xquery let $x :=1
                                return <dbs>
                                        <db id = '%(dbname)s'>
                                            <docs>
                                            {
                                                for $idStr in collection()/document-uri()
                                                    return 
                                                        <doc id = '{substring-after(data($idStr), '/')}'>
                                                        
                                                        </doc>
                                            }
                                            </docs>
                                        </db>
                                    </dbs>""" % {"dbname":dbName})

## Returns all documents in a specific database
@route('/dbs/<dbName>/docs/', method='GET')
def showDocumentsInDatabase(dbName):
    createHeaders ()
    response.content_type = "application/x-xliff"
    dataStore = baseXDB()
    dataStore.setDatabase(dbName)
    return dataStore.queryDB("""xquery let $x :=1
                            return <dbs>
                                    <db id = '%(dbname)s'>
                                        <docs>
                                        {
                                            for $idStr in collection()/document-uri()
                                            let $doc := collection( $idStr)
                                            return
                                            <doc id = '{substring-after(data($idStr), '/')}'>
                                                {$doc}
                                            </doc>
                                        }
                                        </docs>
                                    </db>
                                </dbs>""" % {"dbname":dbName})

## Sends document to the db
@route('/dbs/<dbName>/docs/', method='POST')
def createDoc(dbName):
    createHeaders ()
    document = request.body
    dataStore = baseXDB()
    dataStore.setDatabase(dbName)
    return dataStore.insert(document)
    #return document

## Returns specified document
@route('/dbs/<dbName>/docs/<idStr>/', method='GET')
def retrieveElement(dbName, idStr):
    createHeaders ()
    dataStore = baseXDB()
    dataStore.setDatabase(dbName)
    return dataStore.queryDB("""xquery let $x :=1
                                return 
                                <dbs>
                                    <db id = '%(dbname)s'>
                                        <docs>
                                        {
                                            let $doc := collection('%(dbname)s/%(docID)s')
                                            return
                                            <doc id = '%(docID)s'>
                                                {$doc}
                                            </doc>
                                        }
                                        </docs>
                                    </db>
                                </dbs>""" % {"dbname":dbName, "docID":idStr})

## Returns all domains in a specified document
@route('/dbs/<dbName>/docs/<idStr>/domains/', method='GET')
def retrieveDomainsInDocument(dbName,idStr):
    createHeaders ()
    dataStore = baseXDB()
    dataStore.setDatabase(dbName)
    return dataStore.queryDB("""xquery let $x :=
                                                (
                                                        for $domain in collection('%(dbname)s/%(docID)s')//*[@*:domains]
                                                            let $value := tokenize(($domain/@*:domains), ',')
                                                                for $endValue in $value
                                                                    return
                                                                        normalize-space($endValue) 
                                                )
                                return <dbs>
                                        <db id = '%(dbname)s'>
                                            <docs>
                                                <doc id='%(docID)s'/>
                                                <domains>
                                                {
                                                    for $y in distinct-values($x)
                                                        return
                                                            <domain id = '{$y}'/>
                                                }
                                                </domains>
                                            </docs>
                                        </db>
                                    </dbs>""" % {"dbname":dbName, "docID":idStr})
  
## Returns all domains in a database
@route('/dbs/<dbName>/domains/', method='GET')
def retrieveDomains(dbName):
    createHeaders ()
    dataStore = baseXDB()
    dataStore.setDatabase(dbName)
    return dataStore.queryDB("""xquery let $x := 
                                                (
                                                    let $list := //@*:domains
                                                        for $domain in distinct-values($list)
                                                            let $value := tokenize($domain, ',')
                                                                for $endValue in $value
                                                                    return
                                                                        normalize-space($endValue) 
                                                )
                                                return 
                                                    <dbs>
                                                        <db id = '%(dbname)s'>
                                                            <domains>
                                                            {
                                                                for $y in distinct-values($x)
                                                                    return
                                                                        <domain id = '{$y}'/>
                                                            }
                                                            </domains>
                                                        </db>
                                                    </dbs>""" % {"dbname":dbName})
    ##return dataStore.queryDB("xquery for $domain at $i in //*[@*:domains]  return <domain>{data($domain/@*:domains)}</domain>")
    ##return dataStore.queryDB("xquery //*[local-name()='trans-unit' and @*:domains='{0}']".format(domain))

## Returns document id's with a specified domain
@route('/dbs/<dbName>/domains/<domain>/', method='GET')
def retrieveDocsByDomain(dbName, domain):
    createHeaders ()
    dataStore = baseXDB()
    dataStore.setDatabase(dbName)
    return dataStore.queryDB("""xquery let $x :=1
                                return <dbs>
                                        <db id = '%(dbname)s'>
                                            <docs>
                                            {
                                                for $idStr in collection()[.//*[@*:domains='%(domain)s']]/document-uri()
                                                    return 
                                                        <doc id = '{substring-after(data($idStr), '/')}'>
                                                        
                                                        </doc>
                                            }
                                            </docs>
                                        </db>
                                    </dbs>"""  % {"dbname":dbName, "domain":domain})

## Returns all documents with a specified domain
@route('/dbs/<dbName>/domains/<domain>/docs/', method='GET')
def retrieveDocumentsInDomains(dbName, domain):
    createHeaders ()
    response.content_type = "application/x-xliff";
    dataStore = baseXDB()
    dataStore.setDatabase(dbName)
    return dataStore.queryDB("""xquery let $x :=1
                                return <dbs>
                                        <db id = '%(dbname)s'>
                                            <docs>
                                            {
                                                for $idStr in collection()[.//*[@*:domains='%(domain)s']]/document-uri()                                                
                                                let $doc := collection($idStr)
                                                    return 
                                                        <doc id = '{substring-after(data($idStr), '/')}'>
                                                        {$doc}
                                                        </doc>
                                            }
                                            </docs>
                                        </db>
                                    </dbs>"""  % {"dbname":dbName, "domain":domain})

## Returns transunits which contain specified domains from a specified db 
@route('/dbs/<dbName>/domains/<domain>/trans-units/', method='GET')
def retrieveTransUnitsDataBase(dbName, domain):
    createHeaders ()
    response.content_type = "application/x-xliff"
    dataStore = baseXDB()
    dataStore.setDatabase(dbName)
    return dataStore.queryDB("""xquery let $x :=1
                                return <dbs>
                                        <db id = '%(dbname)s'>
                                            <docs>
                                            {
                                                                                                
                                                let $list := collection()//*[local-name()='trans-unit' and @*:domains='%(domain)s']
                                                    return 
                                                    <doc id = '1' domains="%(domain)s">
                                                        <xliff xmlns="urn:oasis:names:tc:xliff:document:1.2" xmlns:itsx="http://www.ul.ie/its/x-its" version="1.2" xmlns:its="http://www.w3.org/2005/11/its">
                                                            <file datatype="plaintext" source-language="en-us" >
                                                                <header/>
                                                                <body>
                                                                {
                                                                for $trans at $i in $list
                                                                return 
                                                                    <trans-unit id='{$i}'>
                                                                        {$trans/*}
                                                                    </trans-unit>
                                                                }
                                                                </body>
                                                            </file>
                                                        </xliff>
                                                    </doc>
                                                    
                                            }
                                            <domains>
                                                <domain id='%(domain)s'/>
                                            </domains>
                                            </docs>
                                        </db>
                                    </dbs>"""  % {"dbname":dbName, "domain":domain})
    ##return dataStore.queryDB("xquery //*[local-name()='trans-unit' and @*:domains='{0}']".format(domain))

## Delete a specified document
@route('/dbs/<dbName>/docs/<idStr>/', method='DELETE')
def updateElement(dbName, idStr):
    createHeaders ()
    dataStore = baseXDB()
    dataStore.setDatabase(dbName)
    return dataStore.queryDB("delete {0}".format(idStr))

## Drops the specified database
@route('/dbs/<dbName>/', method='DELETE')
def dropDatabase(dbName):
    createHeaders ()
    dataStore = baseXDB()
    dataStore.dropDatabase(dbName)
    
# ## Returns transunits which contain specified domains
# @route('/dbs/<dbName>/trans-units/<domain>/', method='GET')
# def retrieveTransUnitsDB(dbName, domain):
#     createHeaders ()
#     dataStore = baseXDB()
#     dataStore.setDatabase(dbName)
#     return dataStore.queryDB("""xquery let $x :=1 """  % {"dbname":dbName, "domain":domain})

# ## Returns transunits which contain specified domains from a specified document
# @route('/dbs/<dbName>/docs/<idStr>/trans-units/<domain>/', method='GET')
# def retrieveTransUnits(dbName, idStr, domain):
#     createHeaders ()
#     dataStore = baseXDB()
#     dataStore.setDatabase(dbName)
#     return dataStore.queryDB("xquery collection('{0}/{1}')//*[local-name()='trans-unit' and @*:domains='{2}']".format(dbName, idStr, domain))    
    
# ## Returns all documents on a specified db
# @route('/dbs/<dbName>/docs', method='GET')
# def displayDocs(dbName):
#     createHeaders ()
#     dataStore = baseXDB()
#     dataStore.setDatabase(dbName)
#     return dataStore.queryDB("xquery /")

# ## Add a specified document
# @route('/databases/<databaseName>/docs/<idStr>', method='PUT')
# def addElement(databaseName, idStr):
#     dataStore = baseXDB()
#     dataStore.setDatabase(databaseName)
#     return dataStore.queryDB("add {0}".format(idStr))

#/database/<databaseName>/document/:id?query=//group[domain=helth]/transunit[id<20 and id>023]&

 
run(host='0.0.0.0', port=8080, debug=True)


