from django.shortcuts import render


def about(request):
    return render(request,
                  template_name="pages/about.html",
                  context={"title": "О проекте"}
                  )


def rules(request):
    return render(request,
                  template_name="pages/rules.html",
                  context={"title": "Наши правила"}
                  )
