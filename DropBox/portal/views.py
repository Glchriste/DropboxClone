#from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

from forms import UploadFileForm
from models import UploadFile


# Create your views here.
#@login_required
# def portal_main_page(request):
#     """
#     If users are authenticated, direct them to the main page. Otherwise, take
#     them to the login page.
#     """
#     return render_to_response('portal/index.html')
@login_required
def portal_main_page(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = UploadFile(file = request.FILES['file'])
            new_file.owner = request.user #set owner
            new_file.save()
            #messages.success(self.request, 'File uploaded!')
            return HttpResponseRedirect(reverse('portal:portal_main_page'))
            #return render_to_response('portal/index.html')
    else:
        form = UploadFileForm()
 
    data = {'form': form}
    return render_to_response('portal/index.html', data, context_instance=RequestContext(request))