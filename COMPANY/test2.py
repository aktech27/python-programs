from supports.inner import test,numtowords


B=test.Beneficiary()    
B.getbenf()

fileobj=open('web.html','r')
web2=fileobj.read()
fileobj.close()


#<--- Filling party's details --->#

before=web2.find('<b>TO:</b><br>COMPANY NAME,<br>ADDRESS LINE1,<br>ADDRESS LINE2,<br>ADDRESS LINE3,<br>PHONE')
length=len('<b>TO:</b><br>COMPANY NAME,<br>ADDRESS LINE1,<br>ADDRESS LINE2,<br>ADDRESS LINE3,<br>PHONE')
after='<b>TO:</b><br>'+B.Company_name+',<br>'+B.Company_ad1+',<br>'+B.Company_ad2+',<br>'+B.Company_ad3+',<br>'+str(B.Company_phone)
web2=web2.replace(web2[before:before+length],after)

#<--- Filling GST no --->#

before=web2.find('''<td colspan="100%"><p id="gstno">Party's GSTIN No. 33AHXPR7557F1ZM</p></td>''')
length=len('''<td colspan="100%"><p id="gstno">Party's GSTIN No. 33AHXPR7557F1ZM</p></td>''')
after=('''<td colspan="100%"><p id="gstno">Party's GSTIN No. '''+B.Company_GST+'''</p></td>''')
web2=web2.replace(web2[before:before+length],after)

#<--- Filling Date and Lorry no --->#

before=web2.find('''<tr><td id="subdetails" colspan="45%">DATE:<b>00/00/0000</b></td></tr>
               <tr><td id="subdetails" colspan="45%">LORRY NO:<b>TN00AB0000</b></td></tr>''')
length=len('''<tr><td id="subdetails" colspan="45%">DATE:<b>00/00/0000</b></td></tr>
               <tr><td id="subdetails" colspan="45%">LORRY NO:<b>TN00AB0000</b></td></tr>''')
after=('''<tr><td id="subdetails" colspan="45%">DATE:<b>'''+B.Date+'''</b></td></tr>
               <tr><td id="subdetails" colspan="45%">LORRY NO:<b>'''+B.Lorryno+'''</b></td></tr>''')
web2=web2.replace(web2[before:before+length],after)

#<--- Modifying Empty Space --->#

before=web2.find('<tr id="emptyspace" height="245px">')
length=len('<tr id="emptyspace" height="245px">')

# NOTE: one empty space is 35px in height.Thus default is seven empty space (35 x 7 = 245px).
# NOTE: for every new item starting from second deduct one empty space(35px)
newheight=245-((len(B.Products)-1)*35)
after=('<tr id="emptyspace" height="'+str(newheight)+'px">')
web2=web2.replace(web2[before:before+length],after)


#<--- Filling Particulars --->#

before=web2.find('''<tr id="goods">
                     <td colspan="5%" id="item_Sno">1</td>
                     <td colspan="45%" id="item_Particular">T.B. CHANNEL</td>
                     <td colspan="10%" id="item_HSN">8538</td>
                     <td colspan="10%" id="item_Quantity">1000</td>
                     <td colspan="10%" id="item_Rate">28</td>
                     <td colspan="5%" id="item_Ratep">00</td>
                     <td colspan="10%" id="item_Amount">28000</td>
                     <td colspan="5%" id="item_Amountp">00</td>
               </tr>''')
length=len('''<tr id="goods">
                     <td colspan="5%" id="item_Sno">1</td>
                     <td colspan="45%" id="item_Particular">T.B. CHANNEL</td>
                     <td colspan="10%" id="item_HSN">8538</td>
                     <td colspan="10%" id="item_Quantity">1000</td>
                     <td colspan="10%" id="item_Rate">28</td>
                     <td colspan="5%" id="item_Ratep">00</td>
                     <td colspan="10%" id="item_Amount">28000</td>
                     <td colspan="5%" id="item_Amountp">00</td>
               </tr>''')
after=('''<tr id="goods">
                     <td colspan="5%" id="item_Sno">1</td>
                     <td colspan="45%" id="item_Particular">'''+B.Products[0]+'''</td>
                     <td colspan="10%" id="item_HSN">'''+B.HSNs[0]+'''</td>
                     <td colspan="10%" id="item_Quantity">'''+B.Quantities[0]+'''</td>
                     <td colspan="10%" id="item_Rate">'''+B.Raters[0]+'''</td>
                     <td colspan="5%" id="item_Ratep">'''+B.Rateps[0]+'''</td>
                     <td colspan="10%" id="item_Amount">'''+B.Amountrs[0]+'''</td>
                     <td colspan="5%" id="item_Amountp">'''+B.Amountps[0]+'''</td>
               </tr>''')
web2=web2.replace(web2[before:before+length],after)

for i in range(1,(len(B.Products))):
    before=web2.find('<tr id="emptyspace"')
    length=len('<tr id="emptyspace"')
    inserters=('''<tr id="goods">
                     <td colspan="5%" id="item_Sno">'''+str(i+1)+'''</td>
                     <td colspan="45%" id="item_Particular">'''+B.Products[i]+'''</td>
                     <td colspan="10%" id="item_HSN">'''+B.HSNs[i]+'''</td>
                     <td colspan="10%" id="item_Quantity">'''+B.Quantities[i]+'''</td>
                     <td colspan="10%" id="item_Rate">'''+B.Raters[i]+'''</td>
                     <td colspan="5%" id="item_Ratep">'''+B.Rateps[i]+'''</td>
                     <td colspan="10%" id="item_Amount">'''+B.Amountrs[i]+'''</td>
                     <td colspan="5%" id="item_Amountp">'''+B.Amountps[i]+'''</td>
               </tr>
               ''')
    web2=web2.replace(web2[before:before+length],(inserters+'<tr id="emptyspace"'))


#<--- Filling Total --->#
before=web2.find('''<td colspan="15%" id="cols3"><b>TOTAL</td>
                    <td colspan="10%" width="13%" id="totalrup">28000</td>
                    <td colspan="5%" width="4%"id="totalp">00</td>''')
length=len('''<td colspan="15%" id="cols3"><b>TOTAL</td>
                    <td colspan="10%" width="13%" id="totalrup">28000</td>
                    <td colspan="5%" width="4%"id="totalp">00</td>''')
rs,ps=B.Total.split('.')
after=('''<td colspan="15%" id="cols3"><b>TOTAL</td>
                    <td colspan="10%" width="13%" id="totalrup">'''+rs+'''</td>
                    <td colspan="5%" width="4%"id="totalp">'''+ps+'''</td>''')
web2=web2.replace(web2[before:before+length],after)

#<--- Filling CGST --->#
before=web2.find('''<td colspan="15%" id="cols3"><b id="perc_cgst">CGST 0%</td>
                    <td colspan="10%" id="cgstrup">0000</td>
                    <td colspan="5%" id="cgstp" width="4%">00</td>''')
length=len('''<td colspan="15%" id="cols3"><b id="perc_cgst">CGST 0%</td>
                    <td colspan="10%" id="cgstrup">0000</td>
                    <td colspan="5%" id="cgstp" width="4%">00</td>''')
rs,ps=B.cgstamt.split('.')
after=('''<td colspan="15%" id="cols3"><b id="perc_cgst">CGST '''+B.CGST[0]+'''%</td>
                    <td colspan="10%" id="cgstrup">'''+rs+'''</td>
                    <td colspan="5%" id="cgstp" width="4%">'''+ps+'''</td>''')
web2=web2.replace(web2[before:before+length],after)


#<--- Filling SGST --->#
before=web2.find('''<td colspan="15%" id="cols3"><b id="perc_sgst">SGST 0%</td>
                    <td colspan="10%" id="sgstrup">0000</td>
                    <td colspan="5%" id="sgstp" width="4%">00</td>''')
length=len('''<td colspan="15%" id="cols3"><b id="perc_sgst">SGST 0%</td>
                    <td colspan="10%" id="sgstrup">0000</td>
                    <td colspan="5%" id="sgstp" width="4%">00</td>''')
rs,ps=B.sgstamt.split('.')
after=('''<td colspan="15%" id="cols3"><b id="perc_sgst">SGST '''+B.SGST[0]+'''%</td>
                    <td colspan="10%" id="sgstrup">'''+rs+'''</td>
                    <td colspan="5%" id="sgstp" width="4%">'''+ps+'''</td>''')
web2=web2.replace(web2[before:before+length],after)
    

#<--- Filling IGST --->#
before=web2.find('''<td colspan="15%" id="cols3"><b id="perc_igst">IGST 0%</td>
                    <td colspan="10%" id="igstrup">0</td>
                    <td colspan="5%" id="igstp" width="4%">00</td>''')
length=len('''<td colspan="15%" id="cols3"><b id="perc_igst">IGST 0%</td>
                    <td colspan="10%" id="igstrup">0</td>
                    <td colspan="5%" id="igstp" width="4%">00</td>''')
rs,ps=B.igstamt.split('.')
after=('''<td colspan="15%" id="cols3"><b id="perc_igst">IGST '''+B.IGST[0]+'''%</td>
                    <td colspan="10%" id="igstrup">'''+rs+'''</td>
                    <td colspan="5%" id="igstp" width="4%">'''+ps+'''</td>''')
web2=web2.replace(web2[before:before+length],after)


#<--- Filling Grand Total --->#
before=web2.find('''<td colspan="15%" id="cols3"><b>GRAND TOTAL</td>
                    <td colspan="10%" id="grandrup">00000</td>
                    <td colspan="5%" id="grandp" width="4%">00</td>''')
length=len('''<td colspan="15%" id="cols3"><b>GRAND TOTAL</td>
                    <td colspan="10%" id="grandrup">00000</td>
                    <td colspan="5%" id="grandp" width="4%">00</td>''')
rs,ps=B.GrandTotal.split('.')
after=('''<td colspan="15%" id="cols3"><b>GRAND TOTAL</td>
                    <td colspan="10%" id="grandrup">'''+rs+'''</td>
                    <td colspan="5%" id="grandp" width="4%">'''+ps+'''</td>''')
web2=web2.replace(web2[before:before+length],after)

#<--- Filling GST Details --->#
before=web2.find('''<td colspan="5%" id="t4hsn">8538</td>
                    <td colspan="15%" id="t4amt"></td>
                    <td colspan="7%" id="t4perc_cgst">9%</td>
                    <td colspan="13%" id="t4sgst"></td>
                    <td colspan="7%" id="t4perc_sgst">9%</td>
                    <td colspan="13%" id="t4cgst"></td>
                    <td colspan="7%" id="t4perc_igst">0%</td>
                    <td colspan="13%" id="t4igst"></td>
                    <td colspan="20%" id="t4tot"></td>''')
length=len('''<td colspan="5%" id="t4hsn">8538</td>
                    <td colspan="15%" id="t4amt"></td>
                    <td colspan="7%" id="t4perc_cgst">9%</td>
                    <td colspan="13%" id="t4sgst"></td>
                    <td colspan="7%" id="t4perc_sgst">9%</td>
                    <td colspan="13%" id="t4cgst"></td>
                    <td colspan="7%" id="t4perc_igst">0%</td>
                    <td colspan="13%" id="t4igst"></td>
                    <td colspan="20%" id="t4tot"></td>''')
after=('''<td colspan="5%" id="t4hsn">'''+B.HSNs[0]+'''</td>
                    <td colspan="15%" id="t4amt">'''+B.Total+'''</td>
                    <td colspan="7%" id="t4perc_cgst">9%</td>
                    <td colspan="13%" id="t4sgst">'''+B.cgstamt+'''</td>
                    <td colspan="7%" id="t4perc_sgst">9%</td>
                    <td colspan="13%" id="t4cgst">'''+B.sgstamt+'''</td>
                    <td colspan="7%" id="t4perc_igst">0%</td>
                    <td colspan="13%" id="t4igst">'''+B.igstamt+'''</td>
                    <td colspan="20%" id="t4tot">'''+B.GSTTotal+'''</td>''')
web2=web2.replace(web2[before:before+length],after)


before=web2.find('''<td colspan="5%" align="right">Total</td>
                    <td colspan="15%" id="t4amt1" align="right"></td>
                    <td colspan="7%" align="right"></td>
                    <td colspan="13%" id="t4sgst1" align="right"></td>
                    <td colspan="7%" align="right"></td>
                    <td colspan="13%" id="t4cgst1" align="right"></td>
                    <td colspan="7%" align="right"></td>
                    <td colspan="13%" id="t4igst1"align="right"></td>
                    <td colspan="20%" id="t4tot1" align="right"></td>''')
length=len('''<td colspan="5%" align="right">Total</td>
                    <td colspan="15%" id="t4amt1" align="right"></td>
                    <td colspan="7%" align="right"></td>
                    <td colspan="13%" id="t4sgst1" align="right"></td>
                    <td colspan="7%" align="right"></td>
                    <td colspan="13%" id="t4cgst1" align="right"></td>
                    <td colspan="7%" align="right"></td>
                    <td colspan="13%" id="t4igst1"align="right"></td>
                    <td colspan="20%" id="t4tot1" align="right"></td>''')
after=('''<td colspan="5%" align="right">Total</td>
                    <td colspan="15%" id="t4amt1" align="right"></td>
                    <td colspan="7%" align="right"></td>
                    <td colspan="13%" id="t4sgst1" align="right">'''+B.cgstamt+'''</td>
                    <td colspan="7%" align="right"></td>
                    <td colspan="13%" id="t4cgst1" align="right">'''+B.sgstamt+'''</td>
                    <td colspan="7%" align="right"></td>
                    <td colspan="13%" id="t4igst1"align="right">'''+B.igstamt+'''</td>
                    <td colspan="20%" id="t4tot1" align="right">'''+B.GSTTotal+'''</td>''')
web2=web2.replace(web2[before:before+length],after)

#<--- Filling Amount in words --->#

before=web2.find('''<tr>
                    <td id="t4words" colspan="100%">TAX AMOUNT(in words):</td>
               </tr>
               <tr>
                    <td id="inwords" colspan="70%">Rupees:</td>''')
length=len('''<tr>
                    <td id="t4words" colspan="100%">TAX AMOUNT(in words):</td>
               </tr>
               <tr>
                    <td id="inwords" colspan="70%">Rupees:</td>''')
after=('''<tr>
                    <td id="t4words" colspan="100%">TAX AMOUNT(in words): '''+numtowords.convert(B.GSTTotal)+'''</td>
               </tr>
               <tr>
                    <td id="inwords" colspan="70%">Rupees: '''+numtowords.convert(B.GrandTotal)+'''</td>''')
web2=web2.replace(web2[before:before+length],after)









