# Lab9 Replication and Sharding
Distributed Systems Course at Innopolis University, Fall 2019

## Before dropping a primary node

### Screenshot of web app

![alt text](https://user-images.githubusercontent.com/20341995/68052759-6f8ccc80-fcfb-11e9-9cf4-aac459869d62.png "Screenshot 1")

### rs.status()

```javascript
{
  "set" : "rs0",
  "date" : ISODate("2019-11-01T19:22:35.444Z"),
  "myState" : 2,
  "term" : NumberLong(1),
  "syncingTo" : "server-2:27017",
  "syncSourceHost" : "server-2:27017",
  "syncSourceId" : 0,
  "heartbeatIntervalMillis" : NumberLong(2000),
  "majorityVoteCount" : 2,
  "writeMajorityCount" : 2,
  "optimes" : {
    "lastCommittedOpTime" : {
      "ts" : Timestamp(1572636150, 1),
      "t" : NumberLong(1)
    },
    "lastCommittedWallTime" : ISODate("2019-11-01T19:22:30.463Z"),
    "readConcernMajorityOpTime" : {
      "ts" : Timestamp(1572636150, 1),
      "t" : NumberLong(1)
    },
    "readConcernMajorityWallTime" : ISODate("2019-11-01T19:22:30.463Z"),
    "appliedOpTime" : {
      "ts" : Timestamp(1572636150, 1),
      "t" : NumberLong(1)
    },
    "durableOpTime" : {
      "ts" : Timestamp(1572636150, 1),
      "t" : NumberLong(1)
    },
    "lastAppliedWallTime" : ISODate("2019-11-01T19:22:30.463Z"),
    "lastDurableWallTime" : ISODate("2019-11-01T19:22:30.463Z")
  },
  "lastStableRecoveryTimestamp" : Timestamp(1572636120, 1),
  "lastStableCheckpointTimestamp" : Timestamp(1572636120, 1),
  "members" : [
    {
      "_id" : 0,
      "name" : "server-2:27017",
      "ip" : "172.31.2.251",
      "health" : 1,
      "state" : 1,
      "stateStr" : "PRIMARY",
      "uptime" : 5792,
      "optime" : {
        "ts" : Timestamp(1572636150, 1),
        "t" : NumberLong(1)
      },
      "optimeDurable" : {
        "ts" : Timestamp(1572636150, 1),
        "t" : NumberLong(1)
      },
      "optimeDate" : ISODate("2019-11-01T19:22:30Z"),
      "optimeDurableDate" : ISODate("2019-11-01T19:22:30Z"),
      "lastHeartbeat" : ISODate("2019-11-01T19:22:33.812Z"),
      "lastHeartbeatRecv" : ISODate("2019-11-01T19:22:34.117Z"),
      "pingMs" : NumberLong(0),
      "lastHeartbeatMessage" : "",
      "syncingTo" : "",
      "syncSourceHost" : "",
      "syncSourceId" : -1,
      "infoMessage" : "",
      "electionTime" : Timestamp(1572630239, 2),
      "electionDate" : ISODate("2019-11-01T17:43:59Z"),
      "configVersion" : 3
    },
    {
      "_id" : 1,
      "name" : "server-1:27017",
      "ip" : "172.31.9.57",
      "health" : 1,
      "state" : 2,
      "stateStr" : "SECONDARY",
      "uptime" : 5976,
      "optime" : {
        "ts" : Timestamp(1572636150, 1),
        "t" : NumberLong(1)
      },
      "optimeDate" : ISODate("2019-11-01T19:22:30Z"),
      "syncingTo" : "server-2:27017",
      "syncSourceHost" : "server-2:27017",
      "syncSourceId" : 0,
      "infoMessage" : "",
      "configVersion" : 3,
      "self" : true,
      "lastHeartbeatMessage" : ""
    },
    {
      "_id" : 2,
      "name" : "server-3:27017",
      "ip" : "172.31.13.245",
      "health" : 1,
      "state" : 2,
      "stateStr" : "SECONDARY",
      "uptime" : 5780,
      "optime" : {
        "ts" : Timestamp(1572636150, 1),
        "t" : NumberLong(1)
      },
      "optimeDurable" : {
        "ts" : Timestamp(1572636150, 1),
        "t" : NumberLong(1)
      },
      "optimeDate" : ISODate("2019-11-01T19:22:30Z"),
      "optimeDurableDate" : ISODate("2019-11-01T19:22:30Z"),
      "lastHeartbeat" : ISODate("2019-11-01T19:22:33.812Z"),
      "lastHeartbeatRecv" : ISODate("2019-11-01T19:22:34.795Z"),
      "pingMs" : NumberLong(0),
      "lastHeartbeatMessage" : "",
      "syncingTo" : "server-1:27017",
      "syncSourceHost" : "server-1:27017",
      "syncSourceId" : 1,
      "infoMessage" : "",
      "configVersion" : 3
    }
  ],
  "ok" : 1,
  "$clusterTime" : {
    "clusterTime" : Timestamp(1572636150, 1),
    "signature" : {
      "hash" : BinData(0,"oTw/mMmu94+O+baKHNae4zvxheI="),
      "keyId" : NumberLong("6754395449500631042")
    }
  },
  "operationTime" : Timestamp(1572636150, 1)
}
```

### rs.config()

```javascript
{
  "_id" : "rs0",
  "version" : 3,
  "protocolVersion" : NumberLong(1),
  "writeConcernMajorityJournalDefault" : true,
  "members" : [
    {
      "_id" : 0,
      "host" : "server-2:27017",
      "arbiterOnly" : false,
      "buildIndexes" : true,
      "hidden" : false,
      "priority" : 1,
      "tags" : {
        
      },
      "slaveDelay" : NumberLong(0),
      "votes" : 1
    },
    {
      "_id" : 1,
      "host" : "server-1:27017",
      "arbiterOnly" : false,
      "buildIndexes" : true,
      "hidden" : false,
      "priority" : 1,
      "tags" : {
        
      },
      "slaveDelay" : NumberLong(0),
      "votes" : 1
    },
    {
      "_id" : 2,
      "host" : "server-3:27017",
      "arbiterOnly" : false,
      "buildIndexes" : true,
      "hidden" : false,
      "priority" : 1,
      "tags" : {
        
      },
      "slaveDelay" : NumberLong(0),
      "votes" : 1
    }
  ],
  "settings" : {
    "chainingAllowed" : true,
    "heartbeatIntervalMillis" : 2000,
    "heartbeatTimeoutSecs" : 10,
    "electionTimeoutMillis" : 10000,
    "catchUpTimeoutMillis" : -1,
    "catchUpTakeoverDelayMillis" : 30000,
    "getLastErrorModes" : {
      
    },
    "getLastErrorDefaults" : {
      "w" : 1,
      "wtimeout" : 0
    },
    "replicaSetId" : ObjectId("5dbc6edf38e70b41a9c993ad")
  }
}
```

## After dropping a primary node

### Screenshot of web app

![alt text](https://user-images.githubusercontent.com/20341995/68052993-ee820500-fcfb-11e9-8472-d558daab4f6c.png "Screenshot 2")

### rs.status()

```javascript
{
  "set" : "rs0",
  "date" : ISODate("2019-11-01T19:42:56.581Z"),
  "myState" : 2,
  "term" : NumberLong(2),
  "syncingTo" : "server-1:27017",
  "syncSourceHost" : "server-1:27017",
  "syncSourceId" : 1,
  "heartbeatIntervalMillis" : NumberLong(2000),
  "majorityVoteCount" : 2,
  "writeMajorityCount" : 2,
  "optimes" : {
    "lastCommittedOpTime" : {
      "ts" : Timestamp(1572637371, 1),
      "t" : NumberLong(2)
    },
    "lastCommittedWallTime" : ISODate("2019-11-01T19:42:51.798Z"),
    "readConcernMajorityOpTime" : {
      "ts" : Timestamp(1572637371, 1),
      "t" : NumberLong(2)
    },
    "readConcernMajorityWallTime" : ISODate("2019-11-01T19:42:51.798Z"),
    "appliedOpTime" : {
      "ts" : Timestamp(1572637371, 1),
      "t" : NumberLong(2)
    },
    "durableOpTime" : {
      "ts" : Timestamp(1572637371, 1),
      "t" : NumberLong(2)
    },
    "lastAppliedWallTime" : ISODate("2019-11-01T19:42:51.798Z"),
    "lastDurableWallTime" : ISODate("2019-11-01T19:42:51.798Z")
  },
  "lastStableRecoveryTimestamp" : Timestamp(1572637340, 1),
  "lastStableCheckpointTimestamp" : Timestamp(1572637340, 1),
  "members" : [
    {
      "_id" : 0,
      "name" : "server-2:27017",
      "ip" : "172.31.2.251",
      "health" : 0,
      "state" : 8,
      "stateStr" : "(not reachable/healthy)",
      "uptime" : 0,
      "optime" : {
        "ts" : Timestamp(0, 0),
        "t" : NumberLong(-1)
      },
      "optimeDurable" : {
        "ts" : Timestamp(0, 0),
        "t" : NumberLong(-1)
      },
      "optimeDate" : ISODate("1970-01-01T00:00:00Z"),
      "optimeDurableDate" : ISODate("1970-01-01T00:00:00Z"),
      "lastHeartbeat" : ISODate("2019-11-01T19:42:53.033Z"),
      "lastHeartbeatRecv" : ISODate("2019-11-01T19:41:20.330Z"),
      "pingMs" : NumberLong(0),
      "lastHeartbeatMessage" : "Error connecting to server-2:27017 (172.31.2.251:27017) :: caused by :: No route to host",
      "syncingTo" : "",
      "syncSourceHost" : "",
      "syncSourceId" : -1,
      "infoMessage" : "",
      "configVersion" : -1
    },
    {
      "_id" : 1,
      "name" : "server-1:27017",
      "ip" : "172.31.9.57",
      "health" : 1,
      "state" : 1,
      "stateStr" : "PRIMARY",
      "uptime" : 7001,
      "optime" : {
        "ts" : Timestamp(1572637371, 1),
        "t" : NumberLong(2)
      },
      "optimeDurable" : {
        "ts" : Timestamp(1572637371, 1),
        "t" : NumberLong(2)
      },
      "optimeDate" : ISODate("2019-11-01T19:42:51Z"),
      "optimeDurableDate" : ISODate("2019-11-01T19:42:51Z"),
      "lastHeartbeat" : ISODate("2019-11-01T19:42:55.002Z"),
      "lastHeartbeatRecv" : ISODate("2019-11-01T19:42:56.153Z"),
      "pingMs" : NumberLong(0),
      "lastHeartbeatMessage" : "",
      "syncingTo" : "",
      "syncSourceHost" : "",
      "syncSourceId" : -1,
      "infoMessage" : "",
      "electionTime" : Timestamp(1572637280, 1),
      "electionDate" : ISODate("2019-11-01T19:41:20Z"),
      "configVersion" : 3
    },
    {
      "_id" : 2,
      "name" : "server-3:27017",
      "ip" : "172.31.13.245",
      "health" : 1,
      "state" : 2,
      "stateStr" : "SECONDARY",
      "uptime" : 7206,
      "optime" : {
        "ts" : Timestamp(1572637371, 1),
        "t" : NumberLong(2)
      },
      "optimeDate" : ISODate("2019-11-01T19:42:51Z"),
      "syncingTo" : "server-1:27017",
      "syncSourceHost" : "server-1:27017",
      "syncSourceId" : 1,
      "infoMessage" : "",
      "configVersion" : 3,
      "self" : true,
      "lastHeartbeatMessage" : ""
    }
  ],
  "ok" : 1,
  "$clusterTime" : {
    "clusterTime" : Timestamp(1572637371, 1),
    "signature" : {
      "hash" : BinData(0,"UFz7SpzTRCTzLOveVWpjqBqmhh0="),
      "keyId" : NumberLong("6754395449500631042")
    }
  },
  "operationTime" : Timestamp(1572637371, 1)
}
```

### rs.config()

```javascript
{
  "_id" : "rs0",
  "version" : 3,
  "protocolVersion" : NumberLong(1),
  "writeConcernMajorityJournalDefault" : true,
  "members" : [
    {
      "_id" : 0,
      "host" : "server-2:27017",
      "arbiterOnly" : false,
      "buildIndexes" : true,
      "hidden" : false,
      "priority" : 1,
      "tags" : {
        
      },
      "slaveDelay" : NumberLong(0),
      "votes" : 1
    },
    {
      "_id" : 1,
      "host" : "server-1:27017",
      "arbiterOnly" : false,
      "buildIndexes" : true,
      "hidden" : false,
      "priority" : 1,
      "tags" : {
        
      },
      "slaveDelay" : NumberLong(0),
      "votes" : 1
    },
    {
      "_id" : 2,
      "host" : "server-3:27017",
      "arbiterOnly" : false,
      "buildIndexes" : true,
      "hidden" : false,
      "priority" : 1,
      "tags" : {
        
      },
      "slaveDelay" : NumberLong(0),
      "votes" : 1
    }
  ],
  "settings" : {
    "chainingAllowed" : true,
    "heartbeatIntervalMillis" : 2000,
    "heartbeatTimeoutSecs" : 10,
    "electionTimeoutMillis" : 10000,
    "catchUpTimeoutMillis" : -1,
    "catchUpTakeoverDelayMillis" : 30000,
    "getLastErrorModes" : {
      
    },
    "getLastErrorDefaults" : {
      "w" : 1,
      "wtimeout" : 0
    },
    "replicaSetId" : ObjectId("5dbc6edf38e70b41a9c993ad")
  }
}
```

