from Connection import cur

# SPECIFIQUE ETUDE :

def Tables (premier_id, tab) :
	if premier_id == 0 :
		cur.execute('''
			DROP TABLE IF EXISTS ''' + tab + ''';
			CREATE TABLE IF NOT EXISTS ''' + tab + ''' (
				I_d             BIGINT NOT NULL PRIMARY KEY UNIQUE,
				IdStudy         INTEGER,
				GfKCountry      TEXT,
				Category        TEXT,
				Language        TEXT,
				StudyType       TEXT,
				FieldworkStart  DATE,
				FieldworkEnd    DATE,
				ID              BIGINT,
				IdBrand         TEXT,
				IdCBR           TEXT,
				CBR3            TEXT,
				FieldWeek       INTEGER,
				FieldYear       INTEGER,
				Date            DATE,
				Gender          TEXT,
				AgeScale        INTEGER,
				MaritalStatus   TEXT,
				Weight          REAL,
				ChildrenScale   TEXT,
				ChildrenRecoded TEXT,
				Country         TEXT,
				Age18_24_55_65  TEXT,
				Age0_19_46P     TEXT,
				AgeR00_17_65P   TEXT,
				Age0_21_66P     TEXT,
				AgeR25_30_56P   TEXT,
				AgeR18_24_55Pv2 TEXT,
				AgeR14_17_75P   TEXT,
				AgeR0_17_75     TEXT,
				AgeR16_17_65p   TEXT,
				AgeR15_16_70p   TEXT,
				AgeR0_17_85p    TEXT,
				AgeR20_35_36_45 TEXT,
				AgeR0_19_65p    TEXT,
				AgeR25_29_45_50 TEXT,
				AgeR14_15_65p   INTEGER,
				Industry        TEXT,
				Year            INTEGER,
				TrakerFreq      TEXT,
				Region          TEXT,
				GlobalRegion    TEXT,
				RegionGFK       TEXT,
				CBR             INTEGER,
				MultiDirectCBR  TEXT
			)''')

def Variables (premier_identifiant, tab, line) :
	i_d = premier_identifiant
	cur.execute( 'INSERT INTO ' + tab + '\
		(I_d,IdStudy,GfKCountry,Category,Language,StudyType,FieldworkStart,FieldworkEnd,ID,IdBrand,IdCBR,CBR3,FieldWeek,FieldYear,Date,Gender,AgeScale,MaritalStatus,Weight,ChildrenScale,ChildrenRecoded,Country,Age18_24_55_65,Age0_19_46P,AgeR00_17_65P,Age0_21_66P,AgeR25_30_56P,AgeR18_24_55Pv2,AgeR14_17_75P,AgeR0_17_75,AgeR16_17_65p,AgeR15_16_70p,AgeR0_17_85p,AgeR20_35_36_45,AgeR0_19_65p,AgeR25_29_45_50,AgeR14_15_65p,Industry,Year,TrakerFreq,Region,GlobalRegion,RegionGFK,CBR,MultiDirectCBR) \
		VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', \
		(i_d,line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],line[16],line[17],line[18],line[19],line[20],line[21],line[22],line[23],line[24],line[25],line[26],line[27],line[28],line[29],line[30],line[31],line[32],line[33],line[34],line[35],line[36],line[37],line[38],line[39],line[40],line[41],line[42],line[43]) )

# line[0]  IdStudy
# line[1]  GfKCountry
# line[2]  Category
# line[3]  Language
# line[4]  StudyType
# line[5]  FieldworkStart
# line[6]  FieldworkEnd
# line[7]  ID
# line[8]  IdBrand
# line[9]  IdCBR
# line[10] CBR3
# line[11] FieldWeek
# line[12] FieldYear
# line[13] Date
# line[14] Gender
# line[15] AgeScale
# line[16] MaritalStatus
# line[17] Weight
# line[18] ChildrenScale
# line[19] ChildrenRecoded
# line[20] Country
# line[21] Age18_24_55_65
# line[22] Age0_19_46P
# line[23] AgeR00_17_65P
# line[24] Age0_21_66P
# line[25] AgeR25_30_56P
# line[26] AgeR18_24_55Pv2
# line[27] AgeR14_17_75P
# line[28] AgeR0_17_75
# line[29] AgeR16_17_65p
# line[30] AgeR15_16_70p
# line[31] AgeR0_17_85p
# line[32] AgeR20_35_36_45
# line[33] AgeR0_19_65p
# line[34] AgeR25_29_45_50
# line[35] AgeR14_15_65p
# line[36] Industry
# line[37] Year
# line[38] TrakerFreq
# line[39] Region
# line[40] GlobalRegion
# line[41] RegionGFK
# line[42] CBR
# line[43] MultiDirectCBR
