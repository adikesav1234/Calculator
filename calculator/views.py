from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads 

# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class AdditionView(View):
    def post(self,request):
        request_body=request.body    #type of request_body is json ==> python native -dictionary

        #\r\n    "num1":15,\r\n    "num":10\r\n
        #num1:15 , num2:10

        form_data=loads(request_body) #converting json to python native
        n1=form_data.get("num1")
        n2=form_data.get("num2")
        result=n1+n2
        print(request_body)
        data={
            "Sum":result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name='dispatch')
class SubstractionView(View):
    
    def post(self,request):
        request_body=request.body
    
        form_data=loads(request_body)
    
        n1=form_data.get("num1")
        n2=form_data.get("num2")
    
        result=n1-n2

        data={
            "Difference":result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class MultiplicationView(View):

    def post(self, request):
        request_body = request.body

        form_data = loads(request_body)

        n1 = form_data.get("num1")
        n2 = form_data.get("num2")

        result = n1 * n2

        data = {
            "Multiplication": result
        }

        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class DivisionView(View):

    def post(self, request):
        request_body = request.body

        form_data = loads(request_body)

        n1 = form_data.get("num1")
        n2 = form_data.get("num2")

        result = n1 / n2

        data = {
            "Division": result
        }

        return JsonResponse(data)

@method_decorator(csrf_exempt,name='dispatch')
class ModulusView(View):
    def post(self,request):
        request_body=request.body
        
        form_data=loads(request_body)
        
        n1=form_data.get("num1")
        n2=form_data.get("num2")
        
        result=n1%n2
        
        data={
            "Modulus":result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name='dispatch')
class BmiView(View):
    def post(self,request):
        
        request_body=request.body
        form_data=loads(request_body)

        height=form_data.get("height")
        weight=form_data.get("weight")

        height=height/100
        bmi=weight/(height**2)

        data = {
            "height": height,
            "weight": weight,
            "BMI": bmi
        }

        return JsonResponse(data)

@method_decorator(csrf_exempt,name='dispatch')
class AgeView(View):
    def post(self,request):

        request_body=request.body
        form_data=loads(request_body)

        birth_year=form_data.get("birth_year")
        current_year=form_data.get("current_year")

        age=current_year-birth_year

        data={
            "Age":age
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name='dispatch')
class PercentageView(View):
    def post(self,request):

        request_body=request.body
        form_data=loads(request_body)

        obtained=form_data.get("obtained_marks")
        total=form_data.get("total_marks")

        result=(obtained / total) * 100

        data={
            "Percentage":result
        }
        return JsonResponse(data)
