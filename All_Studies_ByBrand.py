from Connection import cur

# SPECIFIQUE ETUDE :

def Tables (premier_id, tab) :
	if premier_id == 0 :
		cur.execute('''
			DROP TABLE IF EXISTS ''' + tab + ''';
			CREATE TABLE IF NOT EXISTS ''' + tab + ''' (
				I_d                             BIGINT NOT NULL PRIMARY KEY UNIQUE,
				IdStudy                         INTEGER,
				GfKCountry                      TEXT,
				Category                        TEXT,
				Language                        TEXT,
				StudyType                       TEXT,
				FieldworkStart                  DATE,
				FieldworkEnd                    DATE,
				ID                              BIGINT,
				IdBrand                         TEXT,
				AttributionBrandRecommendation  TEXT,
				Weight                          REAL,
				AttributionAidedBrandAwareness  INTEGER,
				AttributionBrandpurchase        INTEGER,
				Gender                          TEXT,
				AgeScale                        INTEGER,
				Country                         TEXT,
				Funnel                          TEXT,
				BrandUsage                      TEXT,
				SW3                             TEXT,
				SW3_Min                         TEXT,
				SW3_Max                         TEXT,
				CBRCLU                          TEXT,
				RBX_X                           INTEGER,
				RBX_Y                           INTEGER,
				CBR3_1                          TEXT,
				CBR3_2                          TEXT,
				CBR3_3                          TEXT,
				CBR3_4                          TEXT,
				CBR3_5                          TEXT,
				CBR3_6                          TEXT,
				CBR3_7                          TEXT,
				CBR3_8                          TEXT,
				CBR3_9                          TEXT,
				CBR3_10                         TEXT,
				CBR3_11                         TEXT,
				CBR3_12                         TEXT,
				CBR3_13                         TEXT,
				CBR3_14                         TEXT,
				CBR3_15                         TEXT,
				CBR3_16                         TEXT,
				CBR3_17                         TEXT,
				CBR3_18                         TEXT,
				CBR3_19                         TEXT,
				CBR3_20                         TEXT,
				CBR3_21                         TEXT,
				CBR3_22                         TEXT,
				CBR3_23                         TEXT,
				CBR3_24                         TEXT,
				CBR3_25                         TEXT,
				CBR3_26                         TEXT,
				CBR3_27                         TEXT,
				CBR4                            TEXT,
				FieldWeek                       INTEGER,
				FieldYear                       INTEGER,
				Date                            DATE,
				MaritalStatus                   TEXT,
				AttributionConsideration        TEXT,
				AAAW                            TEXT,
				AAAW_Min                        TEXT,
				AAAW_Max                        TEXT,
				AttributionBrandPreference      TEXT,
				ChildrenScale                   TEXT,
				ChildrenRecoded                 TEXT,
				FAM                             TEXT,
				FAM_Min                         TEXT,
				FAM_Max                         TEXT,
				USE                             TEXT,
				USE_Min                         TEXT,
				USE_Max                         TEXT,
				DirectCBR4                      TEXT,
				CBR_Flag                        TEXT,
				Industry                        TEXT,
				TempCountry                     INTEGER,
				Year                            INTEGER,
				Region                          TEXT,
				GlobalRegion                    TEXT,
				RegionGFK                       TEXT,
				STIC1                           TEXT,
				STIC1_Min                       TEXT,
				STIC1_Max                       TEXT,
				STIC2                           TEXT,
				STIC2_Min                       TEXT,
				STIC2_Max                       TEXT,
				STIC3                           TEXT,
				STIC3_Min                       TEXT,
				STIC3_Max                       TEXT,
				PULL1                           TEXT,
				PULL1_Min                       TEXT,
				PULL1_Max                       TEXT,
				PULL2                           TEXT,
				PULL2_Min                       TEXT,
				PULL2_Max                       TEXT,
				AttributionBrandMostOften       TEXT,
				NoteBrandRecommandation         TEXT,
				NoteBrandRecommandationMin      TEXT,
				NoteBrandRecommandationMax      TEXT,
				SAAW                            TEXT,
				SAAW_Min                        TEXT,
				SAAW_Max                        TEXT)
		''')

def Variables (premier_identifiant, tab, line) :
	i_d = premier_identifiant
	cur.execute( 'INSERT INTO ' + tab + '\
		(I_d,IdStudy,GfKCountry,Category,Language,StudyType,FieldworkStart,FieldworkEnd,ID,IdBrand,AttributionBrandRecommendation,Weight,AttributionAidedBrandAwareness,AttributionBrandpurchase,Gender,AgeScale,Country,Funnel,BrandUsage,SW3,SW3_Min,SW3_Max,CBRCLU,RBX_X,RBX_Y,CBR3_1,CBR3_2,CBR3_3,CBR3_4,CBR3_5,CBR3_6,CBR3_7,CBR3_8,CBR3_9,CBR3_10,CBR3_11,CBR3_12,CBR3_13,CBR3_14,CBR3_15,CBR3_16,CBR3_17,CBR3_18,CBR3_19,CBR3_20,CBR3_21,CBR3_22,CBR3_23,CBR3_24,CBR3_25,CBR3_26,CBR3_27,CBR4,FieldWeek,FieldYear,Date,MaritalStatus,AttributionConsideration,AAAW,AAAW_Min,AAAW_Max,AttributionBrandPreference,ChildrenScale,ChildrenRecoded,FAM,FAM_Min,FAM_Max,USE,USE_Min,USE_Max,DirectCBR4,CBR_Flag,Industry,TempCountry,Year,Region,GlobalRegion,RegionGFK,STIC1,STIC1_Min,STIC1_Max,STIC2,STIC2_Min,STIC2_Max,STIC3,STIC3_Min,STIC3_Max,PULL1,PULL1_Min,PULL1_Max,PULL2,PULL2_Min,PULL2_Max,AttributionBrandMostOften,NoteBrandRecommandation,NoteBrandRecommandationMin,NoteBrandRecommandationMax,SAAW,SAAW_Min,SAAW_Max) \
		VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', \
		(i_d,line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],line[16],line[17],line[18],line[19],line[20],line[21],line[22],line[23],line[24],line[25],line[26],line[27],line[28],line[29],line[30],line[31],line[32],line[33],line[34],line[35],line[36],line[37],line[38],line[39],line[40],line[41],line[42],line[43],line[44],line[45],line[46],line[47],line[48],line[49],line[50],line[51],line[52],line[53],line[54],line[55],line[56],line[57],line[58],line[59],line[60],line[61],line[62],line[63],line[64],line[65],line[66],line[67],line[68],line[69],line[70],line[71],line[72],line[73],line[74],line[75],line[76],line[77],line[78],line[79],line[80],line[81],line[82],line[83],line[84],line[85],line[86],line[87],line[88],line[89],line[90],line[91],line[92],line[93],line[94],line[95],line[96],line[97],line[98]) )

# line[0]  IdStudy
# line[1]  GfKCountry
# line[2]  Category
# line[3]  Language
# line[4]  StudyType
# line[5]  FieldworkStart
# line[6]  FieldworkEnd
# line[7]  ID
# line[8]  IdBrand
# line[9]  AttributionBrandRecommendation
# line[10] Weight
# line[11] AttributionAidedBrandAwareness
# line[12] AttributionBrandpurchase
# line[13] Gender
# line[14] AgeScale
# line[15] Country
# line[16] Funnel
# line[17] BrandUsage
# line[18] SW3
# line[19] SW3_Min
# line[20] SW3_Max
# line[21] CBRCLU
# line[22] RBX_X
# line[23] RBX_Y
# line[24] CBR3_1
# line[25] CBR3_2
# line[26] CBR3_3
# line[27] CBR3_4
# line[28] CBR3_5
# line[29] CBR3_6
# line[30] CBR3_7
# line[31] CBR3_8
# line[32] CBR3_9
# line[33] CBR3_10
# line[34] CBR3_11
# line[35] CBR3_12
# line[36] CBR3_13
# line[37] CBR3_14
# line[38] CBR3_15
# line[39] CBR3_16
# line[40] CBR3_17
# line[41] CBR3_18
# line[42] CBR3_19
# line[43] CBR3_20
# line[44] CBR3_21
# line[45] CBR3_22
# line[46] CBR3_23
# line[47] CBR3_24
# line[48] CBR3_25
# line[49] CBR3_26
# line[50] CBR3_27
# line[51] CBR4
# line[52] FieldWeek
# line[53] FieldYear
# line[54] Date
# line[55] MaritalStatus
# line[56] AttributionConsideration
# line[57] AAAW
# line[58] AAAW_Min
# line[59] AAAW_Max
# line[60] AttributionBrandPreference
# line[61] ChildrenScale
# line[62] ChildrenRecoded
# line[63] FAM
# line[64] FAM_Min
# line[65] FAM_Max
# line[66] USE
# line[67] USE_Min
# line[68] USE_Max
# line[69] DirectCBR4
# line[70] CBR_Flag
# line[71] Industry
# line[72] TempCountry
# line[73] Year
# line[74] Region
# line[75] GlobalRegion
# line[76] RegionGFK
# line[77] STIC1
# line[78] STIC1_Min
# line[79] STIC1_Max
# line[80] STIC2
# line[81] STIC2_Min
# line[82] STIC2_Max
# line[83] STIC3
# line[84] STIC3_Min
# line[85] STIC3_Max
# line[86] PULL1
# line[87] PULL1_Min
# line[88] PULL1_Max
# line[89] PULL2
# line[90] PULL2_Min
# line[91] PULL2_Max
# line[92] AttributionBrandMostOften
# line[93] NoteBrandRecommandation
# line[94] NoteBrandRecommandationMin
# line[95] NoteBrandRecommandationMax
# line[96] SAAW
# line[97] SAAW_Min
# line[98] SAAW_Max
