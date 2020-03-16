from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Risk
from .serializers import RiskSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import statistics

# Create your views here.

def risk_list(request):

    user_answer = request.GET.get('response', None)
    context_data = {'response': user_answer}
    if user_answer is None:
        return JsonResponse(data=context_data)

    #assume response given is questinnaire(11 responses) followed by counter
    #sample input = "a,a,a,a,a,a,a,a,a,a,a,50"
    response = "a,a,a,a,a,a,a,a,a,a,a,50"
    full_input = response.upper().split(",")
    counter_raw_data = [69, 92, 48, 47, 120, 60, 100, 88, 88, 100, 55, 30, 35, 90, 99, 120, 30, 69, 88, 101, 95, 90, 66,
                        67, 67, 43, 108, 150, 100, 70]

    limit = 0
    user_input = []
    for inputs in full_input:
        user_input.append(inputs)
        limit += 1
        if limit == 11:
            break

    counter_input = None
    count_limit = 0
    for inputs in full_input:
        count_limit += 1
        if count_limit > 11:
            counter_input = int(inputs)

    score = 0
    user_profile = ""

    for response in user_input:
        if response == "A":
            score += 1
        elif response == "B":
            score += 3
        elif response == "C":
            score += 5

    sd = statistics.stdev(counter_raw_data) * 2
    mean = statistics.mean(counter_raw_data)

    if counter_input <= mean - sd:
        score += 15
    elif counter_input > mean - sd and counter_input <= mean:
        deviate = int((abs(counter_input - mean) / sd * 6))
        score += 9 + deviate
    elif counter_input > mean and counter_input <= mean + sd:
        deviate = int((abs(counter_input - mean) / sd * 6))
        score += 9 - deviate
    elif counter_input > mean + sd:
        score += 3
    print(score)

    if score <= 21:
        user_profile = "Aggressive"

    elif score > 21 and score <= 34:
        user_profile = "Moderate Balance"

    elif score > 35 and score <= 47:
        user_profile = "Growth Bance"

    elif score > 48:
        user_profile = "Conservative"

    context = {
        'user profile': user_profile
    }
    return JsonResponse(data=context)

