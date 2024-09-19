from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from posts_app.models import Posts
from posts_app.forms import PostsForms
from django.http import HttpResponseRedirect
# Create your views here.

def post_list(request):
    template_path = 'posts_app\pages\post-list.html' # nome do templates
    posts = Posts.objects.all() # query com todos as Postagens
    context = {
        'posts' : posts
    }

    return render(request, template_path, context) # renderiza o template 

# view para visualizar os detalhes do post 
def post_details(request, id):
    template_path = 'posts_app\pages\post-detail.html' 
    post = Posts.objects.get(id = id) # metodo get vai retornar o post que tem o id correto
    print(post)
    context = { # criando o contexto para chamr o template
        'post': post
    }

    return render(request, template_path, context)


# view para criar um post 
def post_create(request):
    if request.method == 'POST': # se for o metodo POST
        form = PostsForms(request.POST, request.FILES) # pegando as informações do formulario
        if form.is_valid(): # se as informações do formulario forem validas
            form = form.save(commit=False)
            form.save()

            # mensagem de criação
            return redirect('post-list')
    form = PostsForms() # senão carregada o formulario
    return render(request, 'posts_app\pages\post-create.html', {"form":form}) # nesse template

# view para atualização de dados de um post
def post_update(request, id):
    post = get_object_or_404(Posts, id=id) # id do post
    form = PostsForms(request.POST or None, request.FILES or None, instance=post)
    context = {
        'form':form
    }
    if form.is_valid():
        form.save()

        return HttpResponseRedirect(reverse('detalhes', args=[post.id]))
    return render(request, "posts_app/pages/post-create.html", context)