from django.shortcuts import render, redirect
from .forms import PostForm, ContributionForm
from .models import Post, Contribution
import pandas
# Create your views here.

# CRUD operations for the Post objects

def home(request):


    return render (request, 'blog/home.html')


# create post view 

def createPost_view(request):

    if request.method == 'POST': # request.POST = {'title':'', 'content':'', '':''}
        
        # 1.PostForm was used to create an object of type Post in our template
        # 2.PostForm enables us  too  to create an object that we can use to add it in the database

        obj = PostForm(request.POST) # create an object 
        if obj.is_valid(): # controll the validity of the object
            obj.save()     # save the object in the database after validation

    return render(request,'blog/create_post.html',{'form': PostForm()})


# retrieve all posts view : fetch all data from database

def retrievePosts_view(request):

    return render(request,'blog/list_posts.html',{'posts':Post.objects.all()})


# Show more text from the post ==> fetch one element from the database using its post_pk parameter

def detail_view(request, post_pk):



    return render(request, 'blog/detail_post.html',{'post': Post.objects.get(id = post_pk)})


# update a given post : fetch data from database and use ModelForm to update it

def updatePost_view(request, post_pk):
    post = Post.objects.get(id = post_pk)
    if request.method == 'POST':
        
        obj = PostForm(request.POST, instance= post)

        if obj.is_valid():
            obj.save()



    return render(request,'blog/update_post.html',{'form' : PostForm(instance = post),'post':post })


# delete a given post
def deletePost_view(request, post_pk):

    if request.method == 'POST':
        obj = Post.objects.get(id = post_pk)
        obj.delete()
        return redirect('retrievePosts_view-path')

    return render(request, 'blog/delete_post.html',{'post' : Post.objects.get(id = post_pk)})



######################CRUD for PostContributions manipulation #####################

# Create a Contribution view

def creatContribution_view(request, post_pk):

    if request.method == 'POST':
        obj = ContributionForm(request.POST)
        if obj.is_valid():
            post = Post.objects.get(id = post_pk)
            contrib = obj.save(False)
            contrib.post = post
            contrib.save()
            return redirect('retrievePostContributions_View-path',post_pk)

    return render (request, 'blog/create_contribution.html',{'form' : ContributionForm()})

# Retrieve contributions of a given post

def retrievePostContributions_View(request, post_pk):

    post = Post.objects.get(id = post_pk)
    contribs = Contribution.objects.filter(post = post)

    return render (request,'blog/retrieve_post_contributions.html',{'contribs' : contribs})

# Update a contribution  of a Post

def updatePostContributions_view(request, contrib_pk):
    contrib = Contribution.objects.get(id = contrib_pk)
    if request.method == 'POST':
        obj = ContributionForm(request.POST, instance= contrib)
        if obj.is_valid():
            obj.save()
            post_pk = contrib.post.pk
            return redirect('retrievePostContributions_View-path',post_pk)

    return render (request, 'blog/update_post_Contribution.html',{'form': ContributionForm(instance= contrib)})

# Delete a Post contribution
def deletePostContribution_view(request, contrib_pk):

    obj = Contribution.objects.get(id = contrib_pk)
    post_pk = obj.post.pk
    if request.method == 'POST':
        obj.delete()
        return redirect('retrievePostContributions_View-path',post_pk)

    return render(request,'blog/delete_post_contribution.html',{'post': obj.post})
