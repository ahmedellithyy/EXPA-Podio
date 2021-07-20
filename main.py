from dataProcessing import *
from podioUpdating import *


# 0 index -> EXPA LC Code
# 1 index -> ICX App ID
# 2 index -> OGX App ID
# if -1 in App ID -> it means LC doesn't have app in this area
lc_codes = {
"6th October":	[2820,-1,23945004],
"AAST-Alex":	[1788,23200755,23200752],
"AAST-Cairo":	[1322,23056932,23057023],
"Ain Shams":	[1789,23200779,23200776],
"Alexandria":	[899,-1,23200746],
"AUC":	[1489,23200725,23200722],
"Beni Suef": [2126,-1,23200770],
"Cairo University":	[1064,23200719,23200716],
"Damietta":	[109,23200701,23200698],
"GUC":	[257,23200761,23200758],
"Helwan":	[2124,25183181,23200710],
"KSU":	[2524,-1,23328153],
"Luxor":	[2114,26031821,23200794],
"Mansoura":	[171,23200791,23200788],
"Menofia":	[1727,23200731,23200728],
"MIU":	[2125,23200785,23200782],
"MSA":	[2817,-1,23945012],
"MUST":	[2818,-1,23944991],
"Suez":	[15,23200707,23200704],
"Tanta": [1725,23200767,23200764],
"Zagazig":[1114,23200737,23200734]
}
#write the date in this format dd/MM/yyyy
date = "01/07/2021"

lc_codes_values = lc_codes.values()
resultSum = 0
for lc in lc_codes_values:
    expa_code = lc[0]
    icx_app_id = lc[1]
    ogx_app_id = lc[2]
    result_OGX_APDs, result_OGX_REs , result_OGX_FIs, result_ICX_APDs, result_ICX_REs, result_ICX_FIs = extract_data(expa_code,date)
    resultSum = resultSum + len(result_OGX_APDs)+len(result_OGX_REs)+len(result_OGX_FIs)+len(result_ICX_APDs)+len(result_ICX_REs)+len(result_ICX_FIs)
    if icx_app_id != -1:
        podioUpdateAPDs(result_ICX_APDs,26298855)
        podioUpdateREs(result_ICX_REs,26298855)
        podioUpdateFIs(result_ICX_FIs,26298855)
    podioUpdateAPDs(result_OGX_APDs, 26298855)
    podioUpdateREs(result_OGX_REs, 26298855)
    podioUpdateFIs(result_OGX_FIs, 26298855)
    print(expa_code)
    print(resultSum)
