from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView
from django import forms
from .models import DiscussionThread, Comment

# A simple ModelForm for creating a Comment.
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # We only ask for content (parent can be None for top‐level comments)
        fields = ['content', 'parent']
        widgets = {
            # Optionally hide the parent field in the form if you want to
            # restrict it to replying in the detail view
            'parent': forms.HiddenInput(),
        }

class DiscussionThreadListView(ListView):
    """List all discussion threads."""
    model = DiscussionThread
    template_name = "konnected/community/thread_list.html"  # create this template
    context_object_name = "threads"
    paginate_by = 10  # adjust as needed

class DiscussionThreadDetailView(DetailView):
    """Show a single discussion thread and its comments."""
    model = DiscussionThread
    template_name = "konnected/community/thread_detail.html"  # create this template
    context_object_name = "thread"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get top-level comments (those with no parent)
        context["comments"] = self.object.comments.filter(parent__isnull=True)
        # Provide an empty comment form for adding a comment to this thread.
        context["comment_form"] = CommentForm(initial={"parent": None})
        return context

class DiscussionThreadCreateView(CreateView):
    """Allow a user to create a new discussion thread."""
    model = DiscussionThread
    template_name = "konnected/community/thread_form.html"  # create this template
    fields = ["title", "content"]
    success_url = reverse_lazy("community:thread_list")

    def form_valid(self, form):
        # Set the current user as the author
        form.instance.author = self.request.user
        return super().form_valid(form)

class CommentCreateView(CreateView):
    """Allow a user to add a comment to a thread."""
    model = Comment
    form_class = CommentForm
    template_name = "konnected/community/comment_form.html"  # create this template

    def form_valid(self, form):
        # Set the current user as the author and assign the thread.
        form.instance.author = self.request.user
        # We assume the URL includes a thread_pk parameter.
        thread_pk = self.kwargs.get("thread_pk")
        form.instance.thread = DiscussionThread.objects.get(pk=thread_pk)
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect back to the thread detail page.
        return reverse("community:thread_detail", kwargs={"pk": self.kwargs.get("thread_pk")})
