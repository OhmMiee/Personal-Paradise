def LOGIN(usn, pwd):
    u = input('Please enter your Username: ')
    p = input('Please enter your Password: ')
    if u == usn and p == pwd:
        return True
    else :
        print('Username or password is wrong')
        return False

def HOME(usn):
    print ('''
Hello''', usn)
    print ('''
------------------------------ Welcome to the Personal Paradise ------------------------------------

            ร้านของเราเป็นร้านที่รวบรวมสมุนไพรต่างๆมากมาย มาไว้ที่นี่ เพื่อให้ท่านได้เลือกซื้ออย่างสะดวก จบได้ในที่เดียว
            
                                      _ _ _ _ _ _ _ _ _ _
                                     |                   |
                                     |        MENU       |
                                     |_ _ _ _ _ _ _ _ _ _|
                                     
                                     ''')
    
def MENU():
    print ('''
******************************************Chinese herbs************************************************

 [1] กุยช่าย        |   [2] ถั่งเช่า          |   [3] แปะก๊วย       |   [4] ลูกเดือย       |   [5] โสม
     ฿90-150/1kg          ฿100-170/1kg          ฿70-120/1kg         ฿80-130/1kg         ฿150-250/1kg
       
*******************************************************************************************************       
       ''')
    print ('''
*****************************************Thailand herbs************************************************

 [6] กระเทียม       |   [7] กะเพรา        |   [8] ตะไคร้         |   [9] บัวบก        |   [10] ฟ้าทะลายโจร
     ฿20-45/1kg           ฿25-50/1kg           ฿40-90/1kg            ฿35-60/1kg           ฿50-120/1kg
       
*******************************************************************************************************       
       ''')

    print ('''
•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°Special herbs°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•

                                        [11] Ganja (สด/อบแห้ง)
                                             ฿1000-10,000/kg
        
•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•

        #หากซื้อครบ 666 บาท รับส่วนลด 100 บาท ทันที!
        
        ''')

def GRADE(herbs):
    if herbs == 1:
        print("กุยช่าย คุณภาพระดับ Premium ราคา 150 บาท / กิโลกรัม")
        print("กุยช่าย คุณภาพระดับ A ราคา 135 บาท / กิโลกรัม")
        print("กุยช่าย คุณภาพระดับ B ราคา 120 บาท / กิโลกรัม")
        print("กุยช่าย คุณภาพระดับ C ราคา 110 บาท / กิโลกรัม")
        print("กุยช่าย คุณภาพระดับ D ราคา 90 บาท / กิโลกรัม")
        
    elif herbs == 2:
        print("ถั่งเช่า คุณภาพระดับ Premium ราคา 170 บาท / กิโลกรัม")
        print("ถั่งเช่า คุณภาพระดับ A ราคา 160 บาท / กิโลกรัม")
        print("ถั่งเช่า คุณภาพระดับ B ราคา 135 บาท / กิโลกรัม")
        print("ถั่งเช่า คุณภาพระดับ C ราคา 120 บาท / กิโลกรัม")
        print("ถั่งเช่า คุณภาพระดับ D ราคา 100 บาท / กิโลกรัม")
        
    elif herbs == 3:
        print("แปะก๊วย คุณภาพระดับ Premium ราคา 120 บาท / กิโลกรัม")
        print("แปะก๊วย คุณภาพระดับ A ราคา 105 บาท / กิโลกรัม")
        print("แปะก๊วย คุณภาพระดับ B ราคา 90 บาท / กิโลกรัม")
        print("แปะก๊วย คุณภาพระดับ C ราคา 80 บาท / กิโลกรัม")
        print("แปะก๊วย คุณภาพระดับ D ราคา 70 บาท / กิโลกรัม")
    
    elif herbs == 4:
        print("ลูกเดือย คุณภาพระดับ Premium ราคา 130 บาท / กิโลกรัม")
        print("ลูกเดือย คุณภาพระดับ A ราคา 110 บาท / กิโลกรัม5")
        print("ลูกเดือย คุณภาพระดับ B ราคา 100 บาท / กิโลกรัม")
        print("ลูกเดือย คุณภาพระดับ C ราคา 90 บาท / กิโลกรัม")
        print("ลูกเดือย คุณภาพระดับ D ราคา 80 บาท / กิโลกรัม")
    
    elif herbs == 5:
        print("โสม คุณภาพระดับ Premium ราคา 250 บาท / กิโลกรัม")
        print("โสม คุณภาพระดับ A ราคา 220 บาท / กิโลกรัม")
        print("โสม คุณภาพระดับ B ราคา 195 บาท / กิโลกรัม")
        print("โสม คุณภาพระดับ C ราคา 170 บาท / กิโลกรัม")
        print("โสม คุณภาพระดับ D ราคา 150 บาท / กิโลกรัม")
        
    elif herbs == 6:
        print("กระเทียม คุณภาพระดับ Premium ราคา 45 บาท / กิโลกรัม")
        print("กระเทียม คุณภาพระดับ A ราคา 35 บาท / กิโลกรัม")
        print("กระเทียม คุณภาพระดับ B ราคา 30 บาท / กิโลกรัม")
        print("กระเทียม คุณภาพระดับ C ราคา 25 บาท / กิโลกรัม")
        print("กระเทียม คุณภาพระดับ D ราคา 20 บาท / กิโลกรัม")
        
    elif herbs == 7:
        print("กะเพรา คุณภาพระดับ Premium ราคา 50 บาท / กิโลกรัม")
        print("กะเพรา คุณภาพระดับ A ราคา 40 บาท / กิโลกรัม")
        print("กะเพรา คุณภาพระดับ B ราคา 35 บาท / กิโลกรัม")
        print("กะเพรา คุณภาพระดับ C ราคา 30 บาท / กิโลกรัม")
        print("กะเพรา คุณภาพระดับ D ราคา 25 บาท / กิโลกรัม")
        
    elif herbs == 8:
        print("ตะไคร้ คุณภาพระดับ Premium ราคา 90 บาท / กิโลกรัม")
        print("ตะไคร้ คุณภาพระดับ A ราคา 75 บาท / กิโลกรัม")
        print("ตะไคร้ คุณภาพระดับ B ราคา 60 บาท / กิโลกรัม")
        print("ตะไคร้ คุณภาพระดับ C ราคา 50 บาท / กิโลกรัม")
        print("ตะไคร้ คุณภาพระดับ D ราคา 40 บาท / กิโลกรัม")
        
    elif herbs == 9:
        print("บัวบก คุณภาพระดับ Premium ราคา 60 บาท / กิโลกรัม")
        print("บัวบก คุณภาพระดับ A ราคา 50 บาท / กิโลกรัม")
        print("บัวบก คุณภาพระดับ B ราคา 45 บาท / กิโลกรัม")
        print("บัวบก คุณภาพระดับ C ราคา 40 บาท / กิโลกรัม")
        print("บัวบก คุณภาพระดับ D ราคา 35 บาท / กิโลกรัม")
        
    elif herbs == 10:
        print("ฟ้าทะลายโจร คุณภาพระดับ Premium ราคา 120 บาท / กิโลกรัม")
        print("ฟ้าทะลายโจร คุณภาพระดับ A ราคา 100 บาท / กิโลกรัม")
        print("ฟ้าทะลายโจร คุณภาพระดับ B ราคา 80 บาท / กิโลกรัม")
        print("ฟ้าทะลายโจร คุณภาพระดับ C ราคา 60 บาท / กิโลกรัม")
        print("ฟ้าทะลายโจร คุณภาพระดับ D ราคา 50 บาท / กิโลกรัม")
        
    elif herbs == 11:
        print("Ganja(สด) คุณภาพระดับ Premium ราคา 9,000 บาท / กิโลกรัม")
        print("Ganja(สด) คุณภาพระดับ A ราคา 8,888 บาท / กิโลกรัม")
        print("Ganja(สด) คุณภาพระดับ B ราคา 5,555 บาท / กิโลกรัม")
        print("Ganja(สด) คุณภาพระดับ C ราคา 2,000 บาท / กิโลกรัม")
        print("Ganja(สด) คุณภาพระดับ D ราคา 666 บาท / กิโลกรัม\n")
        print("Ganja(อบแห้ง) คุณภาพระดับ Premium ราคา 10,000 บาท / กิโลกรัม")
        print("Ganja(อบแห้ง) คุณภาพระดับ A ราคา 9,999 บาท / กิโลกรัม")
        print("Ganja(อบแห้ง) คุณภาพระดับ B ราคา 8,666 บาท / กิโลกรัม")
        print("Ganja(อบแห้ง) คุณภาพระดับ C ราคา 5,555 บาท / กิโลกรัม")
        print("Ganja(อบแห้ง) คุณภาพระดับ D ราคา 3,000 บาท / กิโลกรัม")
        
def MIAN_herbs(herbs,texture,grade): #สูตรคำนวณราคาสมุนไพร
    while True:
        try:
            kg = float(input("ท่านต้องการซื้อกี่กิโลกรัม : "))
            break
        except ValueError:
            print("กรุณาพิมพ์ตัวเลขใหม่ให้ถูกต้องอีกครั้ง")
            
    kilo.append(kg)
    if herbs == 1:
        if grade == "P":
            cost = 150
        elif grade == "A":
            cost = 135
        elif grade == "B":
            cost = 120
        elif grade == "C":
            cost = 110
        elif grade == "D":
            cost = 90
        total = cost*kg
        price.appenกะเพราd(total)
        herbs_type.append("กุยช่าย")
        print("\nกุยช่าย เกรด"+grade,kg,"กิโลกรัม เป็นเงิน",total,"บาท")
        
    elif herbs == 2:
        if grade == "P":
            cost = 170
        elif grade == "A":
            cost = 160
        elif grade == "B":
            cost = 135
        elif grade == "C":
            cost = 120
        elif grade == "D":
            cost = 100
        total = cost*kg
        price.append(total)
        herbs_type.append("ถั่งเช่า")
        print("\nถั่งเช่า เกรด"+grade,kg,"กิโลกรัม เป็นเงิน",total,"บาท")
        
    elif herbs == 3:
        if grade == "P":
            cost = 120
        elif grade == "A":
            cost = 105
        elif grade == "B":
            cost = 90
        elif grade == "C":
            cost = 80
        elif grade == "D":
            cost = 70
        total = cost*kg
        price.append(total)
        herbs_type.append("แปะก๊วย")
        print("\nแปะก๊วย เกรด"+grade,kg,"กิโลกรัม เป็นเงิน",total,"บาท")
        
    elif herbs == 4:
        if grade == "P":
            cost = 130
        elif grade == "A":
            cost = 110
        elif grade == "B":
            cost = 100
        elif grade == "C":
            cost = 90
        elif grade == "D":
            cost = 80
        total = cost*kg
        price.append(total)
        herbs_type.append("ลูกเดือย")
        print("\nลูกเดือย เกรด"+grade,kg,"กิโลกรัม เป็นเงิน",total,"บาท")
    
    elif herbs == 5:
        if grade == "P":
            cost = 250
        elif grade == "A":
            cost = 220
        elif grade == "B":
            cost = 195
        elif grade == "C":
            cost = 170
        elif grade == "D":
            cost = 150
        total = cost*kg
        price.append(total)
        herbs_type.append("โสม")
        print("\nโสม เกรด"+grade,kg,"กิโลกรัม เป็นเงิน",total,"บาท")
        
    elif herbs == 6:
        if grade == "P":
            cost = 45
        elif grade == "A":
            cost = 35
        elif grade == "B":
            cost = 30
        elif grade == "C":
            cost = 25
        elif grade == "D":
            cost = 20
        total = cost*kg
        price.append(total)
        herbs_type.append("กระเทียม")
        print("\nกระเทียม เกรด"+grade,kg,"กิโลกรัม เป็นเงิน",total,"บาท")
        
    elif herbs == 7:
        if grade == "P":
            cost = 50
        elif grade == "A":
            cost = 40
        elif grade == "B":
            cost = 35
        elif grade == "C":
            cost = 30
        elif grade == "D":
            cost = 25
        total = cost*kg
        price.append(total)
        herbs_type.append("กะเพรา")
        print("\nกะเพรา เกรด"+grade,kg,"กิโลกรัม เป็นเงิน",total,"บาท")
        
    elif herbs == 8:
        if grade == "P":
            cost = 90
        elif grade == "A":
            cost = 75
        elif grade == "B":
            cost = 60
        elif grade == "C":
            cost = 50
        elif grade == "D":
            cost = 40
        total = cost*kg
        price.append(total)
        herbs_type.append("ตะไคร้")
        print("\nตะไคร้ เกรด"+grade,kg,"กิโลกรัม เป็นเงิน",total,"บาท")
    
    elif herbs == 9:
        if grade == "P":
            cost = 60
        elif grade == "A":
            cost = 50
        elif grade == "B":
            cost = 45
        elif grade == "C":
            cost = 40
        elif grade == "D":
            cost = 35
        total = cost*kg
        price.append(total)
        herbs_type.append("บัวบก")
        print("\nบัวบก เกรด"+grade,kg,"กิโลกรัม เป็นเงิน",total,"บาท")
        
    elif herbs == 10:
        if grade == "P":
            cost = 120
        elif grade == "A":
            cost = 100
        elif grade == "B":
            cost = 80
        elif grade == "C":
            cost = 60
        elif grade == "D":
            cost = 50
        total = cost*kg
        price.append(total)
        herbs_type.append("ฟ้าทะลายโจร")
        print("\nฟ้าทะลายโจร เกรด"+grade,kg,"กิโลกรัม เป็นเงิน",total,"บาท")

    elif herbs == 11 and texture == 1:
        if grade == "P":
            cost = 9000
        elif grade == "A":
            cost = 8888
        elif grade == "B":
            cost = 5555
        elif grade == "C":
            cost = 2000
        elif grade == "D":
            cost = 666
        total = cost*kg
        price.append(total)
        herbs_type.append("Ganja(สด)")
        print("\nGanja(สด) เกรด"+grade,kg,"กิโลกรัม เป็นเงิน",total,"บาท")
        
    elif herbs == 11 and texture == 2:
        if grade == "P":
            cost = 10000
        elif grade == "A":
            cost = 9999
        elif grade == "B":
            cost = 8666
        elif grade == "C":
            cost = 5555
        elif grade == "D":
            cost = 3000
        total = cost*kg
        price.append(total)
        herbs_type.append("Ganja(อบแห้ง)")
        print("\nGanja(อบแห้ง) เกรด"+grade,kg,"กิโลกรัม เป็นเงิน",total,"บาท")
        
kilo = []
price = []
herbs_tybe = []
quality = []

#ทำรายการซํ้า
while True:
    while True:
        while True:
            MENU() 
            while True: #ลูป h ถ้ากรอกผิด
                try:
                    h = int(input("เลือกสินค้าที่ท่านสนใจ (1-11): "))
                    if h in {1,2,3,4,5,6,7,8,9,10,11}:
                        break
                    print("[กรุณาพิมพ์ตัวเลขใหม่ให้ถูกต้องอีกครั้ง (พิมพ์เลข 1-11)]")
                except ValueError:
                    print("[กรุณาพิมพ์ตัวเลขใหม่ให้ถูกต้องอีกครั้ง (พิมพ์เลข 1-11)]")
            print("\nรายละเอียดสินค้า หมายเลข ["+str(h)+"]")
            grade(h)
            if h in {11}:
                print("ท่านต้องการ Ganja แบบไหน 1 แบบสด หรือ 2 แบบอบแห้ง")
            #ลูป t ถ้ากรอกผิด
                while True:
                    try:
                        t = int(input())
                        if t in {1,2}:
                            break
                        print("กรุณาเลือก 1 เพื่อเลือก Ganja แบบสด หรือ 2 เพื่อเลือก Ganja แบบอบแห้ง")
                    except ValueError:
                        print("กรุณาเลือก 1 เพื่อเลือก Ganja แบบสด หรือ 2 เพื่อเลือก Ganja แบบอบแห้ง")
                        
            else:
                t = 0
                
            g = input("กรุณาเลือกคุณภาพของสมุนไพร (P,A,B,C,D) : ")
            #ลูป g ถ้ากรอกผิด
            while g not in {"P","A","B","C","D","a","b","c","d"}:
                print("กรุณาใส่ตัวอักษรให้ถูกต้องอีกครั้ง (P,A,B,C,D) : ")
            if g == "p":
                quality.append("P")
                gr = "P"
            elif g == "a":
                quality.append("A")
                gr = "A"
            elif g == "b":
                quality.append("B")
                gr = "B"
            elif g == "c":
                quality.append("C")
                gr = "C"
            elif g == "d":
                quality.append("D")
                gr = "D"
            else:
                quality.append("g")
                gr = g
                
            MAIN_herbs(h,t,gr)
            
            print("ท่านต้องการทำรายการต่อหรือไม่?\n กด 1 เพื่อเลือกสินค้าอื่น\n กด 2 หากไม่ต้องการเลือกซื้อสินค้าชิ้นอื่นแล้ว\n กด 3 ยกเลิกรายการล่าสุด")
            #loop LBC ถ้ากรอกผิด
            while True:
                try:
                   leave_back_cancel = int(input())
                   if leave_back_cancel in {1,2,3}:
                       break
                    print("กรุณาใส่ตัวเลข 1 เพื่อเลือกสินค้าอื่น หรือ 2 หากไม่ต้องการเลือกซื้อสินค้าชิ้นอื่นแล้ว หรือ 3 ยกเลิกรายการล่าสุด")
                except ValueError:
                    print("กรุณาใส่ตัวเลข 1 เพื่อเลือกสินค้าอื่น หรือ 2 หากไม่ต้องการเลือกซื้อสินค้าชิ้นอื่นแล้ว หรือ 3 ยกเลิกรายการล่าสุด")   
            if leave_back_cancel == 1:
                continue
            elif leave_back_cancel == 2:
                break
            elif leave_back_cancel == 3:
                del price[-1]
                del herbs_type[-1]
                del quality[-1]
                del kilo[-1]
                if len(herbs_type) == 0:
                    print("\n[รายการล่าสุดถูกยกเลิกแล้ว กรุณาเลือกสินค้าใหม่]")
                    continue
                print("\n[รายการล่าสุดถูกยกเลิกแล้ว]")
                
                print("ท่านต้องการทำรายการต่อหรือไม่?\n กด 1 เพื่อเลือกสินค้าอื่น\n กด 2 หากไม่ต้องการเลือกซื้อสินค้าชิ้นอื่นแล้ว")
                #loop LB ถ้ากรอกผิด
                while True:
                    try:
                        leave_back = int(input())
                        if leave_back in {1,2}:
                            break
                        print("[กรุณาใส่ตัวเลข 1 เพื่อเลือกสินค้าอื่น หรือ 2 หากไม่ต้องการเลือกซื้อสินค้าชิ้นอื่นแล้ว]")
                    except ValueError:
                        print("[กรุณาใส่ตัวเลข 1 เพื่อเลือกสินค้าอื่น หรือ 2 หากไม่ต้องการเลือกซื้อสินค้าชิ้นอื่นแล้ว]")
                if leave_back == 2:
                    break
        
        #รายการรวม
        n = 0
        number = 1
        print("\nรายการสั่งซื้อทั้งหมดที่ท่านเลือก")
        for i in herbs_type:
            print(str(number) +"."+ i ,"เกรด",quality[n],kilo[n],"กิโลกรัม","=",price[n],"บาท")
            n = n+1
            number = number+1
        print("ยืนยันรายการสั้งซื้อของท่านหรือไม่? \n กด [1] เพื่อยืนยันการสั่งซื้อ \n กด [2] เพื่อยกเลิกรายการทั้งหมด")
        #loop LC ถ้ากดผิด
        while True:
            try:
                leave_cancel = int(input())
                if leave_cancel in {1,2}:
                    break
                print("[กรุณาใส่ตัวเลข 1 เพื่อยืนยันการสั่งซื้อ หรือ 2 เพื่อยกเลิกรายการทั้งหมด]")
            except ValueError:
                print("[กรุณาใส่ตัวเลข 1 เพื่อยืนยันการสั่งซื้อ หรือ 2 เพื่อยกเลิกรายการทั้งหมด]")
        if leave_cancel == 1:
            break
        elif leave_cancel ==2:
            del price[:]
            del herbs_type[:]
            del quality[:]
            del kilo[:]
            print("\n[รายการทั้งหมดถูกยกเลิกแล้ว กรุณาเลือกสินค้าใหม่]")

    import math
    #คิดราคา
    if sum(price) >= 666:
        amount = math.ceil(sum(price) - ((sum(price) // 666)) * 100)
        print("รวมเป็นเงินทั้งสิ้น",math.ceil(sum(price)),"บาท ท่านได้รับส่วนลด",(sum(price) // 666) * 100,"บาท เหลือทั้งหมด",amount,"บาท")
    else:
        amount = math.ceil(sum(price))
        print("รวมเป็นเงินทั้งสิ้น",amount,"บาท")
    #loop (pay or cancel) ถ้าลูกค้าใส่จำนวนเงินผิด หรือ อยากยกเลิก
    while True:
        try:
            pay = float(input("กรุณาใส่จำนวนเงินของท่าน(฿) : ")) // 1
            
username = 'uSer'
password = 'pAss'

if LOGIN(username, password) == True:
    HOME(username)
    MENU(username)
    GRADE(username)
    MIAN_herbs(username)
    
else:
    print('ลาก่อย..')
