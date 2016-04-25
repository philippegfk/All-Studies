from Connection import cur

# SPECIFIQUE ETUDE :

def Tables (premier_id, tab) :
	if premier_id == 0 :
		cur.execute('''
			DROP TABLE IF EXISTS ''' + tab + ''';
			CREATE TABLE IF NOT EXISTS ''' + tab + ''' (
				I_d             BIGINT NOT NULL PRIMARY KEY UNIQUE,
				IdStudy         TEXT,
				GfKCountry      TEXT,
				Category        TEXT,
				Language        TEXT,
				StudyType       TEXT,
				FieldworkStart  DATE,
				FieldworkEnd    DATE,
				ID              BIGINT,
				IdXP            TEXT,
				IndiceXP        TEXT,
				xp              TEXT,
				xp3X            INTEGER,
				xp3Y            INTEGER,
				IdBrand         INTEGER,
				XPWeight        REAL,
				Weight          REAL,
				FieldWeek       INTEGER,
				FieldYear       INTEGER,
				Date            DATE,
				Gender          TEXT,
				AgeScale        INTEGER,
				MaritalStatus   TEXT,
				Country         TEXT,
				ChildrenScale   TEXT,
				ChildrenRecoded TEXT,
				Wave            TEXT,
				Age20_24_60P    TEXT,
				Industry        TEXT,
				Year            INTEGER,
				TrakerFreq      TEXT,
				FieldWork       TEXT,
				Region          TEXT,
				GlobalRegion    TEXT,
				RegionGFK       TEXT
			)''')

def Variables (premier_identifiant, tab, line) :
	i_d = premier_identifiant
	cur.execute( 'INSERT INTO ' + tab + '\
		(I_d,IdStudy,GfKCountry,Category,Language,StudyType,FieldworkStart,FieldworkEnd,ID,IdXP,IndiceXP,xp,xp3X,xp3Y,IdBrand,XPWeight,Weight,FieldWeek,FieldYear,Date,Gender,AgeScale,MaritalStatus,Country,ChildrenScale,ChildrenRecoded,Wave,Age20_24_60P,Industry,Year,TrakerFreq,FieldWork,Region,GlobalRegion,RegionGFK) \
		VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', \
		(i_d,line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],line[16],line[17],line[18],line[19],line[20],line[21],line[22],line[23],line[24],line[25],line[26],line[27],line[28],line[29],line[30],line[31],line[32],line[33]) )

# line [0]  IdStudy
# line [1]  GfKCountry
# line [2]  Category
# line [3]  Language
# line [4]  StudyType
# line [5]  FieldworkStart
# line [6]  FieldworkEnd
# line [7]  ID
# line [8]  IdXP
# line [9]  IndiceXP
# line [10] xp
# line [11] xp3X
# line [12] xp3Y
# line [13] IdBrand
# line [14] XPWeight
# line [15] Weight
# line [16] FieldWeek
# line [17] FieldYear
# line [18] Date
# line [19] Gender
# line [20] AgeScale
# line [21] MaritalStatus
# line [22] Country
# line [23] ChildrenScale
# line [24] ChildrenRecoded
# line [25] Wave
# line [26] Age20_24_60P
# line [27] Industry
# line [28] Year
# line [29] TrakerFreq
# line [30] FieldWork
# line [31] Region
# line [32] GlobalRegion
# line [33] RegionGFK
