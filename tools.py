import os

token = 'a76f0775767abe47317a149d1657c14ab954b2a967c0429daeaf7d0d601a809a'


base_url='https://futuresappapi.coin-up.pro'
os.environ['NO_PROXY'] = 'futuresappapi.coin-up.pro/position/get_assets_list'

headers ={
"exchange-token":token,
"Content-Type":"application/json;charset=UTF-8"
}
# headers ={"Build-CU":"100061",
# "exChainupBundleVersion":"4550",
# "timezone":"Asia/Shanghai",
# "exchange-client":"app",
# "language":"el_GR",
# "X-Access-Token":token,
# "device-id":"64a2f5285b0a4c10811d7391d673f8d6",
# "platform":"android",
# "clientType":"android",
# "osVersion":"10",
# "SysVersion-CU":"10",
# "Network-CU":"wifi",
# "exchange-token":token,
# "Platform-CU":"android",
# "os":"android",
# "osVersion":"10",
# "appAcceptLanguage":"zh_CN",
# "exchange-language":"zh_CN",
# "osName":"android",
# "appChannel":"google play",
# "device":"85990eef6e053220",
# "Mobile-Model-CU":"ELS-AN00",
# "Content-Type":"application/json;charset=UTF-8",
# "Host":"futuresappapi.coin-up.pro",
# "Connection":"keep-alive",
# "appNetwork":"WIFI",
# "Accept-Encoding":"gzip",
# "User-Agent":"okhttp/4.9.0",
# }