#### ---- VARIABLE SETUP ---- ####
android = 500
iphone = 600
other = 400
base_plan = 10
unlimited_data = 15
unlimited_talk_text = 10
monthly_fee = 0
#### ---- CALCULATIONS ---- ####

## -- Phone cost -- ##
phone = input("Enter the type of phone you would like, Android ($500), iPhone ($600) or other ($400): ")

if phone == "Android":
    phone = android
if phone == "iPhone":
    phone = iphone
if phone == "other":
    phone = other
    
## -- Finance plan -- ##
print("To use your new phone, you will be automatically enrolled in a basic monthly phone plan for $10 per month. ")
monthly_fee += 10
    
finance_plan = input("Would you like to pay for this phone a) upfront or b) finance it monthly for 12 months? (a/b): ")

if finance_plan == "b":
    phone /= 12
    
## -- Talk text and data -- ##
talk_text = input("Would you like to add unlimited talk/text ($10/month) to your phone plan? (y/n): ")

if talk_text == "y":
    monthly_fee += 10
if talk_text == "n":
    finance_plan = finance_plan
data = input("Would you like to add unlimited data ($15/month) to your phone plan? (y/n): ")

if data == "y":
    monthly_fee += 15
    
#### ---- FINAL OUTPUT ---- ####
print("YOUR PHONE PLAN")
print("---------------------")
print("Your phone will cost $" + str(phone) + " upfront, and $" + str(monthly_fee) + " every month for 12 months")

