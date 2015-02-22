import MySQLdb as mdb
import sys

class DB:
    def __init__(self, dbUrl, dbName, user, password, query, queryWindow, tableName):
        self.tableName = tableName
        # query must have id and path in the select statement
        self.query = query
        self.queryWindow = queryWindow
        try:
            self.connection = mdb.connect(dbUrl, user, password, dbName)
        except mdb.Error, e:
            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)

    def getImagePaths(self, i):
      idToPath = {}
      with self.connection:
        cur = self.connection.cursor()
        query = self.query + self.__getLimit(i)
        i+=1
        print "Query: ", query
        cur.execute(query)
        # iterate window getting id and path info
        for j in range(cur.rowcount):
          row = cur.fetchone()
          imageId = str(row[0])
          imagePath = str(row[1])
          # print imageId, imagePath
          # skip empty paths
          if len(imagePath) <= 0:
            writeErrorLog("null or no path for image: " +imageId)
            continue
          idToPath[imageId] = imagePath
      return idToPath
      print("paths finished")

    # mark a row as successfully put into aws
    def markSuccess(self, idNumber):
      query = "UPDATE " + self.tableName + "\
              SET status = 1\
              WHERE id = " + idNumber + ";"
      with self.connection:
        cur = self.connection.cursor()
        cur.execute(query)
    
    def markFail(self, idNumber):
      query = "UPDATE " + self.tableName + "\
              SET status = null\
              WHERE id = " + idNumber + ";"
      with self.connection:
        cur = self.connection.cursor()
        cur.execute(query)

    def __getLimit(self, i):
      return  " LIMIT " + str(i * self.queryWindow) +", " + str(self.queryWindow)