from django.shortcuts import render

import requests
from django.http import JsonResponse
from .models import MiclatData, MiclatLog
from .miclat import get_data


def verify_nin(nin):
    try:
        response = get_data(nin)

        #  Cas status ==  -1
        if response == -1:
            MiclatLog.objects.create(
                nin=nin,
                status="FAILED",
                message="API returned -1"
            )
            return False

        #  Cas status != 200
        if response.status_code != 200:
            try:
                error_data = response.json()
                message = error_data.get("message") or error_data.get("error")
            except Exception:
                error_data = response.text
                message = response.text[:200]

            MiclatLog.objects.create(
                nin=nin,
                status="FAILED",
                response_code=response.status_code,
                message=message,
                response_data=error_data
            )
            return False

        #  Cas status == 200
        json_data = response.json()
        identite = json_data.get("identite")

        if identite:
            
            MiclatData.objects.update_or_create(
                nin=nin,
                defaults={
                    "sexe": identite.get("sexe"),
                    "acteN": identite.get("acteN"),
                    "annee": identite.get("annee"),
                    "nom_a": identite.get("nom_a"),
                    "nom_f": identite.get("nom_f"),
                    "d_nais": identite.get("d_nais"),
                    "h_nais": identite.get("h_nais"),
                    "pren_a": identite.get("pren_a"),
                    "pren_f": identite.get("pren_f"),
                    "presume": identite.get("presume"),
                    "codecomm": identite.get("codecomm"),
                    "nom_mere": identite.get("nom_mere"),
                    "lieu_nais": identite.get("lieu_nais"),
                    "pren_mere": identite.get("pren_mere"),
                    "pren_pere": identite.get("pren_pere"),
                    "decesMentions": identite.get("decesMentions"),
                    "divorceMentions": identite.get("divorceMentions"),
                    "mariageMentions": identite.get("mariageMentions"),
                    "data": json_data
                }
            )

            MiclatLog.objects.create(
                nin=nin,
                status="SUCCESS",
                response_code=200,
                response_data=json_data
            )

            return True

        # Cas identite vide status == 200
        MiclatLog.objects.create(
            nin=nin,
            status="FAILED",
            response_code=200,
            message="Identite not found",
            response_data=json_data
        )

        return False

    except Exception as e:
        MiclatLog.objects.create(
            nin=nin,
            status="ERROR",
            message=str(e)
        )
        return False
    

def get_miclate_data(request, nin):

    result = verify_nin(nin)

    if result:
        return JsonResponse({"message": "JSON sauvegardé avec succès"})
    else:
        return JsonResponse({"error": "Identité non trouvée"}, status=400)    