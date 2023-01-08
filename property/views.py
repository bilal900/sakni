from django.shortcuts import redirect, render
from django.views.generic.edit import FormMixin
from .forms import ProbertyBookForm
from .filters import PropertyFilter 
from django_filters.views import FilterView # FilterView inheretance from baseview بشان هيك بدلت بين filter view & list view


# Create your views here.
from django.views.generic import ListView , DetailView   #make list,base class view
from .models import Property
class PropertyList(FilterView): #filter
     model=Property 
     paginate_by=1
     filterset_class=PropertyFilter #الكلاس يلي لح فلتر فيه
     template_name='property/property_list.html'# حددت اسم التيمبلت بدال ما اعمل صفحة جديدة
class PropertyDetail(FormMixin , DetailView): #book
     model=Property
     form_class=ProbertyBookForm
     
     def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context["related"] = Property.objects.filter(category=self.get_object().category)[:2]
         return context
     def post(self,request,*args,**kwargs):
          form=self.get_form()
          if form.is_valid():
               myform = form.save(commit=False)
               myform.property=self.get_object()
               myform.user=request.user
               myform.save()
               return redirect('/')
          else:
               return "ca"   
                 




         
     




   


