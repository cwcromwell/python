
# Analzye user logs (format: "sender_user_id recipient_user_id amount_of_transation") and identify users with more than a threshold number of transactions

logs=["88 99 200", "88 99 300", "99 32 100", "12 12 15", "88 99 200", "88 99 300", "99 32 100", "12 12 15", "88 99 200", "88 99 300", "99 32 100", "12 12 15"]

def processLogs(logs, threshold):
    user_transactions={}  # The dict that identifies users with the number of transactions
    final_summary = {}
    for item in logs:
        x=item.split()
        if len(item)<2: 
          continue
        sender_user_id = x[0]
        recipient_user_id = x[1]
        amount_of_transaction = x[2]
        if user_transactions.get(sender_user_id, None) != None:
          user_transactions[sender_user_id] = user_transactions[sender_user_id] +1
        else: 
          user_transactions.update({sender_user_id:1 })
        
    user_transactions = sorted(user_transactions.items())
  #  user_transactions = sorted(user_transactions)
    #print(user_transactions)
    heading1 = "Users" 
    heading2 = "Transactions"
    print(f"{heading1:<10}{heading2:<10}")
    for entry in user_transactions: 
      if entry[1] >= threshold: 
         print(f"{entry[0]:<10}{entry[1]:<10}")
         
    




if __name__ == '__main__':
   processLogs(logs, 2)