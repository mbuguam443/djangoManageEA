from django.shortcuts import render
from .supabase_client import supabase
from django.shortcuts import redirect

def ea_settings_list(request):
    response = supabase.table("ea_settings").select("*").execute()
    data = response.data
    return render(request, "ea_settings_list.html", {"settings": data})

def ea_settings_create(request):
    if request.method == "POST":
        data = {
            "account_no": int(request.POST["account_no"]),
            "magic_number": int(request.POST["magic_number"]),
            "tp": int(request.POST["tp"]),
            "sl": int(request.POST["sl"]),
            "risk_percent": int(request.POST["risk_percent"]),
            "enable_ea": request.POST["enable_ea"].lower() == "true"
        }
        supabase.table("ea_settings").insert(data).execute()
        return redirect("ea_settings_list")

    return render(request, "ea_settings_create.html")


def ea_settings_edit(request, id):
    if request.method == "POST":
        data = {
            "account_no": int(request.POST["account_no"]),
            "magic_number": int(request.POST["magic_number"]),
            "tp": int(request.POST["tp"]),
            "sl": int(request.POST["sl"]),
            "risk_percent": int(request.POST["risk_percent"]),
            "enable_ea": request.POST["enable_ea"].lower() == "true"
        }
        supabase.table("ea_settings").update(data).eq("id", id).execute()
        return redirect("ea_settings_list")

    record = supabase.table("ea_settings").select("*").eq("id", id).single().execute().data
    return render(request, "ea_settings_edit.html", {"record": record})


def ea_settings_delete(request, id):
    supabase.table("ea_settings").delete().eq("id", id).execute()
    return redirect("ea_settings_list")