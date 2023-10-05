from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.postgres.search import SearchVector
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from taggit.models import Tag

from .models import Articles
from .forms import ArticlesForm, CommentForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request, tag_slug=None):
    news = Articles.objects.order_by('-date')

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        news = news.filter(tags__in=[tag])

    paginator = Paginator(news, 3)
    page = request.GET.get('page')
    news = paginator.get_page(page)
    return render(request, 'news/news_home.html', {'news': news, 'paginator': paginator, 'tag': tag})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

    def form_valid(self, form):
        form.instance.updated = timezone.now()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class NewsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author or self.request.user.is_superuser


class NewsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news_delete.html'

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author or self.request.user.is_superuser


@login_required
def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()

            return redirect('news_home')
        else:
            error = 'Форма была неверной'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)


@login_required
def new_comment(request, pk):
    article = get_object_or_404(Articles, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.new = article
            comment.author = request.user
            comment.save()

    else:
        form = CommentForm()

    return redirect('news-detail', pk=pk)