from dataProcessing import *
from podioUpdating import *

LC_CODE = 0

result_OGX_APDs, result_OGX_REs , result_OGX_FIs, result_ICX_APDs, result_ICX_REs, result_ICX_FIs = extract_data()

podioUpdateREs(26298855,result_ICX_REs)

#checkDuplications(26298855,result_ICX_APDs)

#podioUpdateREs(result_ICX_REs)

# print(result_OGX_APDs)
# print(result_OGX_REs)
# print(result_OGX_FIs)
#print(result_ICX_APDs)
# print(result_ICX_REs)
# print(result_ICX_FIs)
