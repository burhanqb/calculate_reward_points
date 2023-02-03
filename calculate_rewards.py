import math
import json
import sys

# Loading a JSON file.
if len(sys.argv) < 2:
    print("Input File Missing")
    sys.exit()

with open(sys.argv[1]) as json_data:
    transactions = json.load(json_data)
    
#Calculating the total amount spent at each merchant by using the merchant code
def calculate_rewards(transactions):
    merchant_spend = {}
    for trans in transactions.values():
        merchant = trans['merchant_code']
        amount = trans['amount_cents']
        if merchant not in merchant_spend:
            merchant_spend[merchant] = amount
        else:
            merchant_spend[merchant] += amount
    return get_rewards(merchant_spend)

#Calculating the max points that can be achieved
def get_rewards(merchant_spend):
    reward_points = 0
    
    #RULE 1
    if (merchant_spend.get('sportcheck', 0) >= 7500 and merchant_spend.get("tim_hortons", 0) >=2500 and merchant_spend.get("subway", 0) >= 2500): 
        numPromo = min(math.floor(merchant_spend.get("sportcheck")/7500), math.floor(merchant_spend.get("tim_hortons")/2500), math.floor(merchant_spend.get("subway")/2500))
        reward_points += 500 * numPromo
        merchant_spend['sportcheck'] -= 7500*numPromo
        merchant_spend['tim_hortons'] -= 2500*numPromo
        merchant_spend['subway'] -= 2500*numPromo

    #RULE 2
    if (merchant_spend.get('sportcheck', 0) >= 7500 and merchant_spend.get("tim_hortons", 0) >=2500): 
        numPromo = min(math.floor(merchant_spend.get("sportcheck")/7500), math.floor(merchant_spend.get("tim_hortons")/2500))
        reward_points += 300 * numPromo
        merchant_spend['sportcheck'] -= 7500*numPromo
        merchant_spend['tim_hortons'] -= 2500*numPromo
    
    #RULE 3 NEVER RUNS AS THE OTHER RULES OVERRIDE THIS RULE
    
    #RULE 4
    if (merchant_spend.get('sportcheck', 0) >= 2500 and merchant_spend.get("tim_hortons", 0) >=1000 and merchant_spend.get("subway", 0) >=1000): 
        numPromo = min(math.floor(merchant_spend.get("sportcheck")/2500), math.floor(merchant_spend.get("tim_hortons")/1000), math.floor(merchant_spend.get("subway")/1000))
        reward_points += 150 * numPromo
        merchant_spend['sportcheck'] -= 2500*numPromo
        merchant_spend['tim_hortons'] -= 1000*numPromo
        merchant_spend['subway'] -= 1000*numPromo
    
    #RULE 5 NEVER RUNS AS THE OTHER RULES OVERRIDE THIS RULE
    
    #RULE 6
    if (merchant_spend.get('sportcheck', 0) >= 2000): 
        numPromo = math.floor(merchant_spend.get("sportcheck")/2000)
        reward_points += 75 * numPromo
        merchant_spend['sportcheck'] -= 2000*numPromo
    
    #RULE 7
    for key,amount in merchant_spend.items(): #RULE 7
        numPromo = math.floor(amount/100)
        reward_points += 1 * numPromo
        merchant_spend[key] -= 100*numPromo

    return reward_points

#Prints maximum number of points achieved
monthly_rewards = calculate_rewards(transactions)
print("Total monthly reward points earned:", monthly_rewards)


