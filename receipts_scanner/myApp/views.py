from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, status
from .models import UserProfile, Group, Expense, Debt
from .serializers import UserProfileSerializer, GroupSerializer, DebtSerializer, ExpenseSerializer
from rest_framework.response import Response
from django.http import QueryDict

# Create your views here.

class UserView(APIView):
    #queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def post(self, request) -> Response:
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #name = serializer.validated_data.get('first_name')
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request) -> Response:
        users = UserProfile.objects.all()
        emails = [user.email for user in users]
        if emails == []:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(emails, status=status.HTTP_201_CREATED)
    
class CreateGroupView(APIView):
    serializer_class = GroupSerializer
    def post(self, request) -> Response:
        
        all_users = []
        for user_email in request.data.get('members', []):
            all_users.append(UserProfile.objects.get(email=user_email))
        request.data['members'] = all_users
        
     
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    '''
    def get(self,request) -> Response:
        groups = Group.objects.all()
        names = [group.group_name for group in groups]
        if names == []:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(names, status=status.HTTP_201_CREATED)
    '''
    def get(self,request) -> Response:
        if request.GET.get('group') == None:
            groups = Group.objects.all()
            names = [group.group_name for group in groups]
            if names == []:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return Response(names, status=status.HTTP_201_CREATED)

        group = request.GET.get('group')
        
        if not Group.objects.get(group_name=group):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        members = self.serializer_class.get_members(self,Group.objects.get(group_name=group))

     
        
        return Response(members, status=status.HTTP_201_CREATED)
    

    
class CreateDebtView(APIView):
    serializer_class = DebtSerializer

    def post(self, request) -> Response:
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #name = serializer.validated_data.get('first_name')
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CreateExpenseView(APIView):
    serializer_class = ExpenseSerializer

    def post(self, request) -> Response:
        

            
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #name = serializer.validated_data.get('first_name')
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request) -> Response:
        users = Expense.objects.all()
        name = [user.expense_name for user in users]
        return Response(name, status=status.HTTP_201_CREATED)
    
    def delete(self, request):
        # Custom delete logic
        # Perform any additional operations before deleting the expense
        
        # Call the base delete method to delete the expense from the database
        users = Expense.objects.all()
        users.delete()
    
        return Response(status=status.HTTP_200_OK)
    
class GetExpenseView(APIView):
    serializer_class = DebtSerializer
    def get(self,request) -> Response: 
        group = request.GET.get('group')
        expenses = Expense.objects.all()
        group_expenses = [expense for expense in expenses if expense.selectedGroup.group_name == group ]
       
        balance = {}
        for expense in group_expenses:
            if expense.paidBy.email in balance:
                balance[expense.paidBy.email] += expense.amount

            else:
               balance[expense.paidBy.email] = expense.amount 

            owers =  expense.splitbtw.all()
            count = expense.splitbtw.count()
            for person in owers:
                balance[person.email] = balance.get(person.email,0) - expense.amount/count
        Group.objects.get(group_name=group).debts.all().delete()
        self.helper_balance(balance, group)
        debts = []   
        debts_all = Group.objects.get(group_name=group).debts.all()
        for debt in debts_all:
            debts.append([debt.borrower.get_full_name(), debt.reciever.get_full_name(), debt.amount])
        return Response(debts, status=status.HTTP_201_CREATED)



    def helper_balance(self, balance, group):
        max_credit = max(balance.values())
        max_debit = min(balance.values())
        pc = max(balance, key=balance.get)
        pd = min(balance, key=balance.get)

         # Compute the minimum of maxDebit and maxCredit
        x = min(abs(max_debit), max_credit)
        
        # Debit 'x' from pd and credit this amount to pc
        balance[pd] += x
        balance[pc] -= x
        # Retrieve the instance of the Group model
        req_group = Group.objects.get(group_name=group)

        # Create a Debt instance and set the borrower, receiver, and amount fields
        debt = Debt.objects.create(borrower=UserProfile.objects.get(email=pd), reciever=UserProfile.objects.get(email=pc), amount=x)

        # Add the Debt instance to the debts field of the Group instance
        req_group.debts.add(debt)

        # Save the Group instance to persist the changes
        req_group.save()
        # Remove pc if x is equal to maxCredit, otherwise remove pd
        if abs(max_debit) == max_credit:
            
            balance.pop(pc)
            balance.pop(pd)
        elif x == max_credit:
            
            balance.pop(pc)
        else:
            balance.pop(pd)
        
       
        # Recursive call for remaining persons
        if len(balance) > 1:
            self.helper_balance(balance, group)

        return 
    


        
        











    
    
        

     