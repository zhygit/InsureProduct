#-*- coding:utf-8 -*-


prodTypeCodeOne =['ProdTypeCode_00','ProdTypeCode_01','ProdTypeCode_02','ProdTypeCode_03','ProdTypeCode_04']
prodTypeCodeTwo= ['ProdTypeCode_00_00','ProdTypeCode_00_01','ProdTypeCode_00_02']


#人寿保险-定期寿险
tag1={
 "type1":"人寿保险",
 "type2":"定期寿险",
 "type3":"",
 "type4":""
}
pageCount="10"
cnt=5000
param1 ={
"pageNo": "1",
"pageCount": pageCount,
"prodTermsShow.prodName": "",
"prodTermsShow.insComName": "",
"prodTermsShow.insItemCode": "",
"prodTermsShow.saleStatus": "",
"prodTermsShow.specialAttri": "",
"prodTermsShow.insType": "",
"prodTermsShow.insPerdType":"",
"prodTypeCodeOne": "ProdTypeCode_00",
"prodTypeCodeTwo": "ProdTypeCode_00_00",
# "prodTypeCodeThree" :"ProdTypeCode_02_01_01",
# "prodTypeCodeFour":"ProdTypeCode_02_01_01_00",
"prodTermsShow.prodTypeCode": "ProdTypeCode_00_00",
"prodTermsShow.prodDesiCode": "",
"pageSize": cnt,
"goToPage": ""
}


#人寿保险-终身寿险
tag2={
 "type1":"人寿保险",
 "type2":"终身寿险",
 "type3":"",
 "type4":""
}

param2 ={
"pageNo": "1",
"pageCount": pageCount,
"prodTermsShow.prodName": "",
"prodTermsShow.insComName": "",
"prodTermsShow.insItemCode": "",
"prodTermsShow.saleStatus": "",
"prodTermsShow.specialAttri": "",
"prodTermsShow.insType": "",
"prodTermsShow.insPerdType":"",
"prodTypeCodeOne": "ProdTypeCode_00",
"prodTypeCodeTwo": "ProdTypeCode_00_01",
# "prodTypeCodeThree" :"ProdTypeCode_02_01_01",
# "prodTypeCodeFour":"ProdTypeCode_02_01_01_00",
"prodTermsShow.prodTypeCode": "ProdTypeCode_00_01",
"prodTermsShow.prodDesiCode": "",
"pageSize": cnt,
"goToPage": ""
}

#人寿保险-两全保险
tag3={
 "type1":"人寿保险",
 "type2":"两全保险",
 "type3":"",
 "type4":""
}
param3 ={
"pageNo": "1",
"pageCount": pageCount,
"prodTermsShow.prodName": "",
"prodTermsShow.insComName": "",
"prodTermsShow.insItemCode": "",
"prodTermsShow.saleStatus": "",
"prodTermsShow.specialAttri": "",
"prodTermsShow.insType": "",
"prodTermsShow.insPerdType":"",
"prodTypeCodeOne": "ProdTypeCode_00",
"prodTypeCodeTwo": "ProdTypeCode_00_02",
# "prodTypeCodeThree" :"ProdTypeCode_02_01_01",
# "prodTypeCodeFour":"ProdTypeCode_02_01_01_00",
"prodTermsShow.prodTypeCode": "ProdTypeCode_00_02",
"prodTermsShow.prodDesiCode": "",
"pageSize": cnt,
"goToPage": ""
}

#养老保险-养老年金保险
tag4={
 "type1":"年金保险",
 "type2":"养老年金保险",
 "type3":"",
 "type4":""
}
pageCount = 374
param4 ={
"pageNo": "1",
"pageCount": pageCount,
"prodTermsShow.prodName": "",
"prodTermsShow.insComName": "",
"prodTermsShow.insItemCode": "",
"prodTermsShow.saleStatus": "",
"prodTermsShow.specialAttri": "",
"prodTermsShow.insType": "",
"prodTermsShow.insPerdType":"",
"prodTypeCodeOne": "ProdTypeCode_01",
"prodTypeCodeTwo": "ProdTypeCode_01_00",
# "prodTypeCodeThree" :"ProdTypeCode_02_01_01",
# "prodTypeCodeFour":"ProdTypeCode_02_01_01_00",
"prodTermsShow.prodTypeCode": "ProdTypeCode_01_00",
"prodTermsShow.prodDesiCode": "",
"pageSize": cnt,
"goToPage": ""
}

#养老保险-非养老年金保险
tag5={
 "type1":"年金保险",
 "type2":"非养老年金保险",
 "type3":"",
 "type4":""
}
pageCount = 207
param5 ={
"pageNo": "1",
"pageCount": pageCount,
"prodTermsShow.prodName": "",
"prodTermsShow.insComName": "",
"prodTermsShow.insItemCode": "",
"prodTermsShow.saleStatus": "",
"prodTermsShow.specialAttri": "",
"prodTermsShow.insType": "",
"prodTermsShow.insPerdType":"",
"prodTypeCodeOne": "ProdTypeCode_01",
"prodTypeCodeTwo": "ProdTypeCode_01_01",
# "prodTypeCodeThree" :"ProdTypeCode_02_01_01",
# "prodTypeCodeFour":"ProdTypeCode_02_01_01_00",
"prodTermsShow.prodTypeCode": "ProdTypeCode_01_01",
"prodTermsShow.prodDesiCode": "",
"pageSize": cnt,
"goToPage": ""
}

#健康保险--个人税收优惠型健康险
tag6={
 "type1":"健康保险",
 "type2":"个人税收优惠型健康险",
 "type3":"",
 "type4":""
}
pageCount = 207
param6 ={
"pageNo": "1",
"pageCount": pageCount,
"prodTermsShow.prodName": "",
"prodTermsShow.insComName": "",
"prodTermsShow.insItemCode": "",
"prodTermsShow.saleStatus": "",
"prodTermsShow.specialAttri": "",
"prodTermsShow.insType": "",
"prodTermsShow.insPerdType":"",
"prodTypeCodeOne": "ProdTypeCode_02",
"prodTypeCodeTwo": "ProdTypeCode_02_00",
# "prodTypeCodeThree" :"ProdTypeCode_02_01_01",
# "prodTypeCodeFour":"ProdTypeCode_02_01_01_00",
"prodTermsShow.prodTypeCode": "ProdTypeCode_02_00",
"prodTermsShow.prodDesiCode": "",
"pageSize": cnt,
"goToPage": ""
}

#健康保险--非个人税收优惠型健康险-疾病保险-重大疾病保险
tag7={
 "type1":"健康保险",
 "type2":"非个人税收优惠型健康险",
 "type3":"疾病保险",
 "type4":"重大疾病保险"
}
pageCount = 269
param7 ={
"pageNo": "1",
"pageCount": pageCount,
"prodTermsShow.prodName": "",
"prodTermsShow.insComName": "",
"prodTermsShow.insItemCode": "",
"prodTermsShow.saleStatus": "",
"prodTermsShow.specialAttri": "",
"prodTermsShow.insType": "",
"prodTermsShow.insPerdType":"",
"prodTypeCodeOne": "ProdTypeCode_02",
"prodTypeCodeTwo": "ProdTypeCode_02_01",
"prodTypeCodeThree" :"ProdTypeCode_02_01_00",
"prodTypeCodeFour":"ProdTypeCode_02_01_00_00",
"prodTermsShow.prodTypeCode": "ProdTypeCode_02_01_00_00",
"prodTermsShow.prodDesiCode": "",
"pageSize": cnt,
"goToPage": ""
}


#健康保险--非个人税收优惠型健康险-疾病保险-防癌保险
tag8={
 "type1":"健康保险",
 "type2":"非个人税收优惠型健康险",
 "type3":"疾病保险",
 "type4":"防癌保险"
}
pageCount = 244
param8 ={
"pageNo": "1",
"pageCount": pageCount,
"prodTermsShow.prodName": "",
"prodTermsShow.insComName": "",
"prodTermsShow.insItemCode": "",
"prodTermsShow.saleStatus": "",
"prodTermsShow.specialAttri": "",
"prodTermsShow.insType": "",
"prodTermsShow.insPerdType":"",
"prodTypeCodeOne": "ProdTypeCode_02",
"prodTypeCodeTwo": "ProdTypeCode_02_01",
"prodTypeCodeThree" :"ProdTypeCode_02_01_00",
"prodTypeCodeFour":"ProdTypeCode_02_01_00_01",
"prodTermsShow.prodTypeCode": "ProdTypeCode_02_01_00_01",
"prodTermsShow.prodDesiCode": "",
"pageSize": cnt,
"goToPage": ""
}

#健康保险--非个人税收优惠型健康险-疾病保险-其他保险
tag9={
 "type1":"健康保险",
 "type2":"非个人税收优惠型健康险",
 "type3":"疾病保险",
 "type4":"其他保险"
}
pageCount = 42
param9 ={
"pageNo": "1",
"pageCount": pageCount,
"prodTermsShow.prodName": "",
"prodTermsShow.insComName": "",
"prodTermsShow.insItemCode": "",
"prodTermsShow.saleStatus": "",
"prodTermsShow.specialAttri": "",
"prodTermsShow.insType": "",
"prodTermsShow.insPerdType":"",
"prodTypeCodeOne": "ProdTypeCode_02",
"prodTypeCodeTwo": "ProdTypeCode_02_01",
"prodTypeCodeThree" :"ProdTypeCode_02_01_00",
"prodTypeCodeFour":"ProdTypeCode_02_01_00_02",
"prodTermsShow.prodTypeCode": "ProdTypeCode_02_01_00_02",
"prodTermsShow.prodDesiCode": "",
"pageSize": cnt,
"goToPage": ""
}


#健康保险--非个人税收优惠型健康险-医疗保险-费用补偿型医疗保险
tag10={
 "type1":"健康保险",
 "type2":"非个人税收优惠型健康险",
 "type3":"医疗保险",
 "type4":"费用补偿型医疗保险"
}
pageCount = 269
param10 ={
"pageNo": "1",
"pageCount": pageCount,
"prodTermsShow.prodName": "",
"prodTermsShow.insComName": "",
"prodTermsShow.insItemCode": "",
"prodTermsShow.saleStatus": "",
"prodTermsShow.specialAttri": "",
"prodTermsShow.insType": "",
"prodTermsShow.insPerdType":"",
"prodTypeCodeOne": "ProdTypeCode_02",
"prodTypeCodeTwo": "ProdTypeCode_02_01",
"prodTypeCodeThree" :"ProdTypeCode_02_01_01",
"prodTypeCodeFour":"ProdTypeCode_02_01_01_00",
"prodTermsShow.prodTypeCode": "ProdTypeCode_02_01_01_00",
"prodTermsShow.prodDesiCode": "",
"pageSize": cnt,
"goToPage": ""
}

#健康保险--非个人税收优惠型健康险-医疗保险-定额给付型医疗保险
tag11={
 "type1":"健康保险",
 "type2":"非个人税收优惠型健康险",
 "type3":"医疗保险",
 "type4":"定额给付型医疗保险"
}
pageCount = 269
param11 ={
"pageNo": "1",
"pageCount": pageCount,
"prodTermsShow.prodName": "",
"prodTermsShow.insComName": "",
"prodTermsShow.insItemCode": "",
"prodTermsShow.saleStatus": "",
"prodTermsShow.specialAttri": "",
"prodTermsShow.insType": "",
"prodTermsShow.insPerdType":"",
"prodTypeCodeOne": "ProdTypeCode_02",
"prodTypeCodeTwo": "ProdTypeCode_02_01",
"prodTypeCodeThree" :"ProdTypeCode_02_01_01",
"prodTypeCodeFour":"ProdTypeCode_02_01_01_01",
"prodTermsShow.prodTypeCode": "ProdTypeCode_02_01_01_01",
"prodTermsShow.prodDesiCode": "",
"pageSize": cnt,
"goToPage": ""
}

#健康保险--非个人税收优惠型健康险-失能收入损失保险
tag12={
 "type1":"健康保险",
 "type2":"非个人税收优惠型健康险",
 "type3":"失能收入损失保险",
 "type4":""
}
pageCount = 113
param12 ={
"pageNo": "1",
"pageCount": pageCount,
"prodTermsShow.prodName": "",
"prodTermsShow.insComName": "",
"prodTermsShow.insItemCode": "",
"prodTermsShow.saleStatus": "",
"prodTermsShow.specialAttri": "",
"prodTermsShow.insType": "",
"prodTermsShow.insPerdType":"",
"prodTypeCodeOne": "ProdTypeCode_02",
"prodTypeCodeTwo": "ProdTypeCode_02_01",
"prodTypeCodeThree" :"ProdTypeCode_02_01_02",
# "prodTypeCodeFour":"ProdTypeCode_02_01_02_00",
"prodTermsShow.prodTypeCode": "ProdTypeCode_02_01_02",
"prodTermsShow.prodDesiCode": "",
"pageSize": cnt,
"goToPage": ""
}

#健康保险--非个人税收优惠型健康险-护理保险
tag13={
 "type1":"健康保险",
 "type2":"非个人税收优惠型健康险",
 "type3":"护理保险",
 "type4":""
}
pageCount = 20
param13 ={
"pageNo": "1",
"pageCount": pageCount,
"prodTermsShow.prodName": "",
"prodTermsShow.insComName": "",
"prodTermsShow.insItemCode": "",
"prodTermsShow.saleStatus": "",
"prodTermsShow.specialAttri": "",
"prodTermsShow.insType": "",
"prodTermsShow.insPerdType":"",
"prodTypeCodeOne": "ProdTypeCode_02",
"prodTypeCodeTwo": "ProdTypeCode_02_01",
"prodTypeCodeThree" :"ProdTypeCode_02_01_03",
# "prodTypeCodeFour":"ProdTypeCode_02_01_02_00",
"prodTermsShow.prodTypeCode": "ProdTypeCode_02_01_03",
"prodTermsShow.prodDesiCode": "",
"pageSize": cnt,
"goToPage": ""
}

#意外伤害保险
tag14={
 "type1":"意外伤害保险",
 "type2":"",
 "type3":"",
 "type4":""
}
pageCount = 20
param14 ={
"pageNo": "1",
"pageCount": pageCount,
"prodTermsShow.prodName": "",
"prodTermsShow.insComName": "",
"prodTermsShow.insItemCode": "",
"prodTermsShow.saleStatus": "",
"prodTermsShow.specialAttri": "",
"prodTermsShow.insType": "",
"prodTermsShow.insPerdType":"",
"prodTypeCodeOne": "ProdTypeCode_03",
# "prodTypeCodeTwo": "ProdTypeCode_02_01",
# "prodTypeCodeThree" :"ProdTypeCode_02_01_03",
# "prodTypeCodeFour":"ProdTypeCode_02_01_02_00",
"prodTermsShow.prodTypeCode": "ProdTypeCode_03",
"prodTermsShow.prodDesiCode": "",
"pageSize": cnt,
"goToPage": ""
}


#委托管理业务-- 健康保障委托管理
tag15={
 "type1":"委托管理业务",
 "type2":"健康保障委托管理",
 "type3":"",
 "type4":""
}
pageCount = 5
param15 ={
"pageNo": "1",
"pageCount": pageCount,
"prodTermsShow.prodName": "",
"prodTermsShow.insComName": "",
"prodTermsShow.insItemCode": "",
"prodTermsShow.saleStatus": "",
"prodTermsShow.specialAttri": "",
"prodTermsShow.insType": "",
"prodTermsShow.insPerdType":"",
"prodTypeCodeOne": "ProdTypeCode_04",
"prodTypeCodeTwo": "ProdTypeCode_04_00",
# "prodTypeCodeThree" :"ProdTypeCode_02_01_03",
# "prodTypeCodeFour":"ProdTypeCode_02_01_02_00",
"prodTermsShow.prodTypeCode": "ProdTypeCode_04_00",
"prodTermsShow.prodDesiCode": "",
"pageSize": cnt,
"goToPage": ""
}

#委托管理业务-- 健康保障委托管理
tag16={
 "type1":"委托管理业务",
 "type2":"养老保障委托管理",
 "type3":"",
 "type4":""
}
pageCount = 5
param16 ={
"pageNo": "1",
"pageCount": pageCount,
"prodTermsShow.prodName": "",
"prodTermsShow.insComName": "",
"prodTermsShow.insItemCode": "",
"prodTermsShow.saleStatus": "",
"prodTermsShow.specialAttri": "",
"prodTermsShow.insType": "",
"prodTermsShow.insPerdType":"",
"prodTypeCodeOne": "ProdTypeCode_04",
"prodTypeCodeTwo": "ProdTypeCode_04_01",
# "prodTypeCodeThree" :"ProdTypeCode_02_01_03",
# "prodTypeCodeFour":"ProdTypeCode_02_01_02_00",
"prodTermsShow.prodTypeCode": "ProdTypeCode_04_01",
"prodTermsShow.prodDesiCode": "",
"pageSize": cnt,
"goToPage": ""
}

plist = [param1,
 param2,
 param3,
 param4,
 param5,
 param6,
 param7,
 param8,
 param9,
 param10,
 param11,
 param12,
 param13,
 param14,
 param15,
 param16]

tlist=[tag1,
 tag2,
 tag3,
 tag4,
 tag5,
 tag6,
 tag7,
 tag8,
 tag9,
 tag10,
 tag11,
 tag12,
 tag13,
 tag14,
 tag15,
 tag16]

print tlist

# print  plist



px ={
"pageNo": "1",
"pageCount": "123",
"prodTermsShow.prodName": "",
"prodTermsShow.insComName": "",
"prodTermsShow.insItemCode": "",
"prodTermsShow.saleStatus": "",
"prodTermsShow.specialAttri": "",
"prodTermsShow.insType": "",
"prodTermsShow.insPerdType":"",
"prodTypeCodeOne": "ProdTypeCode_00",
"prodTypeCodeTwo": "ProdTypeCode_00_00",
# "prodTypeCodeThree" :"ProdTypeCode_02_01_01",
# "prodTypeCodeFour":"ProdTypeCode_02_01_01_00",
"prodTermsShow.prodTypeCode": "ProdTypeCode_00_00",
"prodTermsShow.prodDesiCode": "",
"pageSize": 120,
"goToPage": ""
}