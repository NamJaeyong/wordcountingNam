from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    text = request.GET['fulltext']
    splited_text = text.split()
    words = "".join(splited_text)
    wordcount2 = len(splited_text)
    wordcount = {}
    for word in splited_text:
          if word in wordcount:
              wordcount[word] += 1
          else:
                wordcount[word] = 1 
    return render(request, 'result.html',{
        'text' :text,
        'wordcount' :wordcount.items(),
        'wordcount2' :wordcount2,
    })

