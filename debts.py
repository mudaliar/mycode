debts = ['A B 2','B A 2', 'C A 5', 'B C 7', 'A B 4', 'A C 4']

members_their_debts = {}
print("This is the start")
for i in range(len(debts)):
    member1 = debts[i].split(" ")[0]
    member2 = debts[i].split(" ")[1]
    debtamt = debts[i].split(" ")[2]
    debtamt = int(debtamt)
    print('this is lender',member2,'this is borrower',member1,'this is the type',type(debtamt))
    if member1 in members_their_debts.keys():
        print("This is member1",members_their_debts[member1])
        tmp = members_their_debts[member1]
        tmp -= debtamt
        members_their_debts[member1] = tmp
    else:
        members_their_debts.update({member1:debtamt})
        print("This is members added to the debts list", members_their_debts)
        
    if member2 in members_their_debts.keys():
        tmp = members_their_debts[member2]
        tmp -= debtamt

        members_their_debts[member2] = tmp
    else:
        members_their_debts.update({member2:debtamt})
    print ("This the dict",members_their_debts)

    print("This is answer",min(members_their_debts, key=members_their_debts.get))
