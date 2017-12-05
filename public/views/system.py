def redirect_page_not_found(request):
  return render_to_response('template/404.html', {}, context_instance=RequestContext(request));

def redirect_500_error(request):
  return render_to_response('template/500.html', {}, context_instance=RequestContext(request));
